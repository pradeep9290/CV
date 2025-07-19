"""Core simulation loop orchestrating dynamics, navigation, control and rendering."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

import numpy as np

from .dynamics import DynamicsModel, State
from .control import ControlPolicy, ControlCommand
from .navigation import Navigator, NavOutput
from .rendering import Renderer, RenderOutput
from .data_logging import DataLogger, LogRecord

@dataclass
class SimulationConfig:
    dt: float = 10.0
    num_frames: int = 120

class Simulation:
    def __init__(
        self,
        dynamics: DynamicsModel,
        navigator: Navigator,
        controller: ControlPolicy,
        renderer: Renderer,
        logger: Optional[DataLogger] = None,
        cfg: SimulationConfig | None = None,
    ):
        self.dynamics = dynamics
        self.navigator = navigator
        self.controller = controller
        self.renderer = renderer
        self.logger = logger
        self.cfg = cfg or SimulationConfig()
        self.state = State(position=np.array([5000.0, 0.0, 0.0]), velocity=np.array([0.0, 1.0, 0.0]))
        self.t = 0.0

    def step(self, frame: int):
        # Render synthetic image
        render_out: RenderOutput = self.renderer.render(frame)

        # Navigation step (using ground truth here)
        nav_out: NavOutput = self.navigator.estimate_state(render_out, NavOutput(self.state.position, self.state.velocity))

        # Control step
        cmd: ControlCommand = self.controller.compute_control(np.hstack([nav_out.position, nav_out.velocity]), self.t)

        # Simple dynamics update applying impulsive dv
        self.state.velocity += cmd.dv
        self.state = self.dynamics.propagate(self.state, self.cfg.dt)
        self.t += self.cfg.dt

        if self.logger:
            record = LogRecord(
                time=self.t,
                true_pos=self.state.position.tolist(),
                est_pos=nav_out.position.tolist(),
                dv_cmd=cmd.dv.tolist(),
                rgb=render_out.rgb_path,
                depth=render_out.depth_path,
                seg=render_out.seg_path,
            )
            self.logger.log(record)

    def run(self):
        self.renderer.setup_scene()
        for frame in range(self.cfg.num_frames):
            self.step(frame)
