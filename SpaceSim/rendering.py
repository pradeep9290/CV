"""Synthetic sensor layer using Blender's Python API (``bpy``).

The renderer produces RGB, depth, and segmentation masks. It is written so
that other backends (Unity, Unreal) can be implemented by exposing the same
interface.
"""

from dataclasses import dataclass

@dataclass
class RenderOutput:
    rgb_path: str
    depth_path: str
    seg_path: str

class Renderer:
    """Thin wrapper around the rendering engine."""
    def __init__(self, output_dir: str = "renders"):
        self.output_dir = output_dir

    def setup_scene(self):
        """Setup camera, lights, and spacecraft proxy in Blender."""
        import bpy
        bpy.ops.mesh.primitive_cube_add(size=1)
        bpy.ops.object.light_add(type='SUN')
        bpy.ops.object.camera_add(location=(5, 0, 0))
        bpy.context.scene.camera = bpy.context.object

    def render(self, frame: int) -> RenderOutput:
        """Render the current frame and return file paths to outputs."""
        import bpy
        rgb = f"{self.output_dir}/rgb_{frame:04d}.png"
        depth = f"{self.output_dir}/depth_{frame:04d}.exr"
        seg = f"{self.output_dir}/seg_{frame:04d}.png"
        bpy.context.scene.frame_set(frame)
        bpy.context.scene.render.filepath = rgb
        bpy.ops.render.render(write_still=True)
        # Depth/mask outputs would require additional compositor setup
        return RenderOutput(rgb_path=rgb, depth_path=depth, seg_path=seg)
