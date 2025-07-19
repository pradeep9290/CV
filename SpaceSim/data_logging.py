"""Simple CSV-based logging of simulation data per frame."""

import csv
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class LogRecord:
    time: float
    true_pos: list
    est_pos: list
    dv_cmd: list
    rgb: str
    depth: str
    seg: str

class DataLogger:
    def __init__(self, csv_path: str = "log.csv"):
        self.csv_path = Path(csv_path)
        if not self.csv_path.exists():
            with open(self.csv_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=LogRecord.__annotations__.keys())
                writer.writeheader()

    def log(self, record: LogRecord) -> None:
        with open(self.csv_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=LogRecord.__annotations__.keys())
            writer.writerow(asdict(record))
