"""
Jeweler 3D Studio - Core Gems Module
Minimal fail-proof gem operators for step-by-step building.
"""

import bpy
import bmesh
from bpy.props import EnumProperty, FloatProperty
from bpy.types import Operator, PropertyGroup

GEM_CUT_ITEMS = [
    ("ROUND", "Redonda (Brillante)", "Talla redonda brillante"),
    ("PRINCESS", "Princesa", "Talla cuadrada brillante"),
    ("OVAL", "Oval", "Talla ovalada brillante"),
    ("EMERALD", "Esmeralda", "Talla rectangular escalonada"),
    ("PEAR", "Pera", "Talla en forma de gota"),
    ("MARQUISE", "Marquesa", "Talla de dos puntas"),
]

STONE_ENUM_ITEMS = [
    ("DIAMOND", "Diamante", "Diamante claro"),
    ("RUBY", "Rubí", "Rubí rojo"),
    ("SAPPHIRE", "Zafiro", "Zafiro azul"),
    ("EMERALD", "Esmeralda", "Esmeralda verde"),
]


class J3D_OT_add_gem(Operator):
    """Añadir Gema"""
    bl_idname = "j3d.add_gem"
    bl_label = "Add Gem"
    bl_description = "Añade una nueva piedra preciosa a la escena"
    bl_options = {'REGISTER', 'UNDO'}

    cut_type: EnumProperty(name="Cut", items=GEM_CUT_ITEMS, default="ROUND") # type: ignore
    stone_type: EnumProperty(name="Stone", items=STONE_ENUM_ITEMS, default="DIAMOND") # type: ignore
    size_mm: FloatProperty(name="Size (mm)", default=6.5, min=0.5, max=50.0) # type: ignore

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        return context.mode == 'OBJECT'

    def execute(self, context: bpy.types.Context) -> set[str]:
        mesh = bpy.data.meshes.new(f"Mesh_Gem_{self.cut_type}")
        bm = bmesh.new()
        bmesh.ops.create_icosphere(bm, subdivisions=2, diameter=self.size_mm / 1000.0)
        bm.to_mesh(mesh)
        bm.free()

        obj = bpy.data.objects.new(f"Gem_{self.stone_type}_{self.cut_type}", mesh)
        context.collection.objects.link(obj)
        obj.location = context.scene.cursor.location

        obj["j3d_type"] = "GEM"
        obj["j3d_cut"] = self.cut_type
        obj["j3d_stone"] = self.stone_type
        obj["j3d_size_mm"] = self.size_mm

        for ob in context.selected_objects:
            ob.select_set(False)
        obj.select_set(True)
        context.view_layer.objects.active = obj

        self.report({'INFO'}, f"Gema {self.cut_type} añadida.")
        return {'FINISHED'}


class J3D_OT_edit_gem(Operator):
    """Editar Gema"""
    bl_idname = "j3d.edit_gem"
    bl_label = "Edit Gem"
    bl_description = "Edita la gema seleccionada"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        obj = context.active_object
        return obj is not None and obj.get("j3d_type") == "GEM"

    def execute(self, context: bpy.types.Context) -> set[str]:
        self.report({'INFO'}, "Gema editada.")
        return {'FINISHED'}


classes = (
    J3D_OT_add_gem,
    J3D_OT_edit_gem,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
