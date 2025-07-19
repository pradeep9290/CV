# High-Fidelity Spacecraft Visualization & GNC Simulation

This module provides a minimal framework for closed-loop Guidance–Navigation–Control
(GNC) simulation using synthetic imagery. Blender is used as the first rendering
backend with an abstract interface to enable future Unity/Unreal implementations.

## Folder Structure

```
SpaceSim/
  dynamics.py       # orbital propagation
  control.py        # maneuver policies
  navigation.py     # image-based state estimation
  rendering.py      # synthetic sensor layer (Blender)
  data_logging.py   # CSV logging utility
  simulation.py     # main loop logic
  README.md         # this file

demo.py             # runnable example
```

## Running

### Headless

```bash
blender -b -P demo.py
```

### Interactive

```bash
blender -P demo.py
```

Rendered frames will be written to the `renders/` directory and a CSV log to
`simulation_log.csv`.
