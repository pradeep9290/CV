"""Dynamics module for simplified CR3BP or two-body propagation.

This module defines a basic integrator that propagates the 6-DOF
state vector ``[x, y, z, vx, vy, vz]``. It is intentionally minimal and
engine-agnostic so that higher fidelity implementations can be swapped in
later (e.g., astrodynamics libraries).
"""

from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    """Spacecraft translational state."""
    position: np.ndarray  # 3-vector [km]
    velocity: np.ndarray  # 3-vector [km/s]

class DynamicsModel:
    """Simplified propagator using two-body dynamics with optional J2."""
    def __init__(self, mu: float = 4902.800066):
        self.mu = mu  # gravitational parameter of the Moon [km^3/s^2]

    def propagate(self, state: State, dt: float) -> State:
        """Propagate state by ``dt`` seconds.

        Parameters
        ----------
        state : State
            Current spacecraft state.
        dt : float
            Time step in seconds.

        Returns
        -------
        State
            New propagated state using a simple Euler method.
        """
        r = state.position
        v = state.velocity
        r_norm = np.linalg.norm(r)
        acc = -self.mu * r / r_norm**3
        new_v = v + acc * dt
        new_r = r + new_v * dt
        return State(position=new_r, velocity=new_v)
