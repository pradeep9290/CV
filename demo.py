"""Minimal demo running a 2-orbit simulation producing 120 frames."""

from SpaceSim.dynamics import DynamicsModel
from SpaceSim.control import ZeroControl
from SpaceSim.navigation import Navigator
from SpaceSim.rendering import Renderer
from SpaceSim.data_logging import DataLogger
from SpaceSim.simulation import Simulation


def main():
    dynamics = DynamicsModel()
    navigator = Navigator(use_ground_truth=True)
    controller = ZeroControl()
    renderer = Renderer(output_dir="renders")
    logger = DataLogger("simulation_log.csv")

    sim = Simulation(dynamics, navigator, controller, renderer, logger)
    sim.run()


if __name__ == "__main__":
    main()
