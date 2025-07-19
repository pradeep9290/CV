# Simulation Architecture

```text
+---------------+       +------------+       +------------+       +--------------+
| DynamicsModel | <-->  | Navigator  | <-->  | Controller | <-->  | Renderer     |
+---------------+       +------------+       +------------+       +--------------+
        ^                      |                   |                     |
        |                      v                   v                     v
        +---------------------------------------------------------------+
        |                         DataLogger                            |
        +---------------------------------------------------------------+
```

1. **DynamicsModel** propagates the spacecraft translational state.
2. **Renderer** produces RGB, depth and segmentation frames.
3. **Navigator** consumes rendered data (or ground truth) to estimate state.
4. **Controller** computes delta-v commands based on the estimated state.
5. **DataLogger** records simulation outputs per frame.
6. **Simulation** orchestrates the loop, calling each module every step.

The abstraction allows swapping the rendering backend (e.g. Blender, Unity) or
control algorithms without changing the outer loop.
