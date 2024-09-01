"""Main module for 3D Artisan, a feature-rich 3D modeling software."""

import logging
from typing import List, Dict, Any

from .modeling import ModelingTools
from .texturing import TexturingTools
from .animation import AnimationTools
from .rendering import RenderingEngine
from .file_io import FileIO
from .plugin_manager import PluginManager


class Artisan:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.modeling = ModelingTools()
        self.texturing = TexturingTools()
        self.animation = AnimationTools()
        self.rendering = RenderingEngine()
        self.file_io = FileIO()
        self.plugin_manager = PluginManager()

        self.current_project: Dict[str, Any] = {}
        self.scene_objects: List[Any] = []

    def create_new_project(self, name: str) -> None:
        """Create a new 3D modeling project."""
        self.current_project = {"name": name, "objects": []}
        self.scene_objects = []
        self.logger.info(f"New project created: {name}")

    def add_object(self, object_type: str, parameters: Dict[str, Any]) -> None:
        """Add a new object to the scene."""
        new_object = self.modeling.create_object(object_type, parameters)
        self.scene_objects.append(new_object)
        self.logger.info(f"Added new {object_type} to the scene")

    def apply_texture(self, object_id: int, texture_params: Dict[str, Any]) -> None:
        """Apply texture to a specific object in the scene."""
        if 0 <= object_id < len(self.scene_objects):
            self.texturing.apply_texture(self.scene_objects[object_id], texture_params)
            self.logger.info(f"Applied texture to object {object_id}")
        else:
            self.logger.error(f"Invalid object ID: {object_id}")

    def create_animation(
        self, object_id: int, animation_params: Dict[str, Any]
    ) -> None:
        """Create an animation for a specific object in the scene."""
        if 0 <= object_id < len(self.scene_objects):
            self.animation.create_animation(
                self.scene_objects[object_id], animation_params
            )
            self.logger.info(f"Created animation for object {object_id}")
        else:
            self.logger.error(f"Invalid object ID: {object_id}")

    def render_scene(self, render_settings: Dict[str, Any]) -> str:
        """Render the current scene and return the path to the rendered image."""
        rendered_image_path = self.rendering.render(self.scene_objects, render_settings)
        self.logger.info(f"Scene rendered: {rendered_image_path}")
        return rendered_image_path

    def save_project(self, file_path: str) -> None:
        """Save the current project to a file."""
        self.file_io.save_project(self.current_project, self.scene_objects, file_path)
        self.logger.info(f"Project saved to: {file_path}")

    def load_project(self, file_path: str) -> None:
        """Load a project from a file."""
        self.current_project, self.scene_objects = self.file_io.load_project(file_path)
        self.logger.info(f"Project loaded from: {file_path}")

    def install_plugin(self, plugin_path: str) -> None:
        """Install a new plugin."""
        self.plugin_manager.install_plugin(plugin_path)
        self.logger.info(f"Plugin installed: {plugin_path}")


# Additional methods for other functionalities can be added here
