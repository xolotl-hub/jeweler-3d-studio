"""
Jeweler 3D Studio - Core Gems Module
Handles gem shapes, cuts, metadata, and stone placement.
"""

from typing import List, Tuple
import bpy
from bpy.props import EnumProperty, FloatProperty, StringProperty
from bpy.types import Operator, PropertyGroup

GEM_CUT_ITEMS: List[Tuple[str, str, str]] = [
    ("ROUND", "Redonda (Brillante)", "Talla redonda brillante de 57/58 facetas"),
    ("PRINCESS", "Princesa", "Talla cuadrada brillante"),
    ("OVAL", "Oval", "Talla ovalada brillante"),
    ("EMERALD", "Esmeralda", "Talla rectangular en escalón"),
    ("PEAR", "Pera", "Talla en forma de lágrima/pera"),
    ("MARQUISE", "Marquesa", "Talla de dos puntas (Navette)"),
]


class J3D_GemProperties(PropertyGroup):
    """Properties for gem customization and metadata."""
    cut_type: EnumProperty(
        name="Talla de Gema",
        description="Selección del corte/estilo de la piedra preciosa",
        items=GEM_CUT_ITEMS,
        default="ROUND"
    ) # type: ignore

    size_mm: FloatProperty(
        name="Diámetro / Ancho (mm)",
        description="Dimensión principal de la gema en milímetros",
        default=6.5,  # ~1.0 Carat Diamond equivalent
        min=0.5,
        max=50.0,
        unit='LENGTH'
    ) # type: ignore

    carat_weight: FloatProperty(
        name="Peso Estimado (ct)",
        description="Peso aproximado en quilates (ct) para diamante",
        default=1.0,
        min=0.01,
        max=100.0
    ) # type: ignore


class J3D_OT_add_gem(Operator):
    """Añade una gema parametrizada a la escena 3D"""
    bl_idname = "j3d.add_gem"
    bl_label = "Añadir Gema"
    bl_description = "Crea una nueva gema según la talla y dimensiones especificadas"
    bl_options = {'REGISTER', 'UNDO'}

    cut_type: EnumProperty(
        name="Talla",
        items=GEM_CUT_ITEMS,
        default="ROUND"
    ) # type: ignore

    size_mm: FloatProperty(
        name="Tamaño (mm)",
        default=6.5,
        min=0.5,
        max=50.0
    ) # type: ignore

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        return context.mode == 'OBJECT'

    def execute(self, context: bpy.types.Context) -> set[str]:
        # Placeholder mesh generation for gems
        size_m = self.size_mm / 1000.0
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=2,
            radius=size_m / 2.0,
            location=context.scene.cursor.location
        )
        gem_obj = context.active_object
        gem_obj.name = f"Gem_{self.cut_type}_{self.size_mm:.1f}mm"
        gem_obj["j3d_type"] = "GEM"
        gem_obj["j3d_cut"] = self.cut_type
        gem_obj["j3d_size_mm"] = self.size_mm

        self.report({'INFO'}, f"Gema {self.cut_type} ({self.size_mm:.1f}mm) añadida.")
        return {'FINISHED'}


classes = (
    J3D_GemProperties,
    J3D_OT_add_gem,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
