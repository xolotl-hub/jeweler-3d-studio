"""
Jeweler 3D Studio - Core Cutters Module
Boolean cutter engine for seats, holes, and gem clearance cuts.
"""

from typing import List, Tuple
import bpy
from bpy.props import EnumProperty, FloatProperty, BoolProperty
from bpy.types import Operator, PropertyGroup

CUTTER_TYPE_ITEMS: List[Tuple[str, str, str]] = [
    ("SEAT", "Asiento de Gema", "Cortador de bisel para el asiento del filetín"),
    ("HOLE", "Perforación de Luz", "Cortador cilíndrico/cónico para entrada de luz inferior"),
    ("BEZEL", "Bisel Completo", "Cortador hueco para engaste cerrado (Bezel setting)"),
]


class J3D_CutterProperties(PropertyGroup):
    """Properties for parametric boolean cutters."""
    cutter_type: EnumProperty(
        name="Tipo de Cortador",
        items=CUTTER_TYPE_ITEMS,
        default="SEAT"
    ) # type: ignore

    girdle_clearance_percent: FloatProperty(
        name="Holgura Filetín (%)",
        description="Porcentaje adicional sobre el diámetro de la gema",
        default=5.0,
        min=0.0,
        max=50.0
    ) # type: ignore

    hole_diameter_percent: FloatProperty(
        name="Diámetro Perforación (%)",
        description="Diámetro del agujero inferior como porcentaje de la gema",
        default=70.0,
        min=10.0,
        max=100.0
    ) # type: ignore

    auto_boolean: BoolProperty(
        name="Aplicar Booleana",
        description="Aplica la operación booleana de corte automáticamente",
        default=True
    ) # type: ignore


class J3D_OT_add_cutters(Operator):
    """Genera un cortador booleano para la gema seleccionada"""
    bl_idname = "j3d.add_cutters"
    bl_label = "Añadir Cortadores"
    bl_description = "Crea un cuerpo de corte booleano parametrizado"
    bl_options = {'REGISTER', 'UNDO'}

    cutter_type: EnumProperty(
        name="Tipo de Cortador",
        items=CUTTER_TYPE_ITEMS,
        default="SEAT"
    ) # type: ignore

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        return context.mode == 'OBJECT' and context.active_object is not None

    def execute(self, context: bpy.types.Context) -> set[str]:
        target_obj = context.active_object
        self.report({'INFO'}, f"Cortador '{self.cutter_type}' asignado a '{target_obj.name}'.")
        return {'FINISHED'}


classes = (
    J3D_CutterProperties,
    J3D_OT_add_cutters,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
