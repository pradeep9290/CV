"""Control module providing abstract interface for guidance algorithms."""

from dataclasses import dataclass
import numpy as np

@dataclass
class ControlCommand:
    dv: np.ndarray  # Delta-v command [km/s]

class ControlPolicy:
    """Abstract base class for maneuver generation."""
    def compute_control(self, state_est: np.ndarray, t: float) -> ControlCommand:
        """Compute a delta-v command at time ``t`` given the estimated state."""
        raise NotImplementedError

class ZeroControl(ControlPolicy):
    """Do-nothing controller useful for open-loop propagation."""
    def compute_control(self, state_est: np.ndarray, t: float) -> ControlCommand:
        return ControlCommand(dv=np.zeros(3))
