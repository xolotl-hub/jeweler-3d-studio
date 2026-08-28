"""
Jeweler 3D Studio - Core Ring Shank & Size Module
Provides parametric generation of ring size references (US Sizes with half sizes)
and ring shank geometry (Bezier Curves / Mesh Cylinders).
"""

from typing import Dict, Tuple, List
import math
import bpy
import bmesh
from bpy.props import EnumProperty, FloatProperty, StringProperty
from bpy.types import Operator, PropertyGroup

# Complete US Ring Size Chart (US Size -> Inner Diameter in mm)
US_RING_SIZES: Dict[str, float] = {
    "3.0": 14.05,
    "3.5": 14.45,
    "4.0": 14.86,
    "4.5": 15.27,
    "5.0": 15.70,
    "5.5": 16.10,
    "6.0": 16.51,
    "6.5": 16.92,
    "7.0": 17.32,  # Default
    "7.5": 17.73,
    "8.0": 18.14,
    "8.5": 18.54,
    "9.0": 18.95,
    "9.5": 19.35,
    "10.0": 19.76,
    "10.5": 20.17,
    "11.0": 20.57,
    "11.5": 20.98,
    "12.0": 21.39,
    "12.5": 21.79,
    "13.0": 22.20,
    "13.5": 22.61,
}

US_SIZE_ITEMS: List[Tuple[str, str, str]] = [
    (k, f"US {k} ({v:.2f} mm)", f"Talla US {k} - Diámetro interno {v:.2f} mm")
    for k, v in US_RING_SIZES.items()
]

GEOMETRY_TYPE_ITEMS: List[Tuple[str, str, str, str, int]] = [
    ("CURVE", "Curva Bézier", "Genera una curva circular Bézier 3D para el perfil del anillo", "CURVE_NCIRCLE", 0),
    ("CYLINDER", "Cilindro Malla", "Genera una malla 3D de cilindro como referencia de talla", "MESH_CYLINDER", 1),
]

PROFILE_ITEMS: List[Tuple[str, str, str]] = [
    ("MEDIA_CANA", "Media Caña", "Perfil abombado superior y plano inferior"),
    ("PLANO", "Plano", "Perfil rectangular plano tradicional"),
    ("CONFORT", "Confort", "Perfil abombado suave interior y exterior"),
]


class J3D_OT_create_ring_size(Operator):
    """Genera la geometría base de Talla de Anillo (Curva o Cilindro)"""
    bl_idname = "j3d.create_ring_size"
    bl_label = "Crear Talla de Anillo"
    bl_description = "Crea la referencia de talla de anillo según la talla US seleccionada"
    bl_options = {'REGISTER', 'UNDO'}

    us_size: EnumProperty(
        name="Talla US",
        description="Selección de talla estándar US (incluye medias tallas)",
        items=US_SIZE_ITEMS,
        default="7.0"
    ) # type: ignore

    geometry_type: EnumProperty(
        name="Tipo de Geometría",
        description="Formato del objeto de salida (Curva Bézier o Cilindro 3D)",
        items=GEOMETRY_TYPE_ITEMS,
        default="CURVE"
    ) # type: ignore

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        return context.mode == 'OBJECT'

    def draw(self, context: bpy.types.Context) -> None:
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(self, "us_size", text="Talla US")

        row = layout.row(align=True)
        row.label(text="Tipo de Salida")
        row.prop(self, "geometry_type", expand=True)

    def execute(self, context: bpy.types.Context) -> set[str]:
        inner_dia_mm = US_RING_SIZES.get(self.us_size, 17.32)
        # Diámetro en metros (escena Blender en metros, default)
        diameter_m = inner_dia_mm / 1000.0   # ej: 17.32mm -> 0.01732m
        radius_m   = diameter_m / 2.0        # ej: 0.01732m -> 0.00866m

        loc = context.scene.cursor.location

        if self.geometry_type == 'CURVE':
            # Primitivo nativo Blender: Bezier Circle, radio default 1m
            bpy.ops.curve.primitive_bezier_circle_add(
                radius=1.0,
                enter_editmode=False,
                align='WORLD',
                location=loc
            )
            obj = context.active_object
            # Escalar al diámetro real en metros
            obj.scale = (radius_m, radius_m, radius_m)
            bpy.ops.object.transform_apply(scale=True)

        else:  # CYLINDER
            # Primitivo nativo Blender: Cylinder, radio default 1m
            bpy.ops.mesh.primitive_cylinder_add(
                vertices=64,
                radius=1.0,
                depth=1.0,
                enter_editmode=False,
                align='WORLD',
                location=loc
            )
            obj = context.active_object
            # Escalar: XY al radio real, Z a 3mm de grosor de referencia
            obj.scale = (radius_m, radius_m, 0.003)
            bpy.ops.object.transform_apply(scale=True)

        obj.name = f"RingSize_US_{self.us_size}"
        obj["j3d_type"] = "RING_SIZE"
        obj["j3d_us_size"] = self.us_size
        obj["j3d_inner_dia_mm"] = inner_dia_mm

        self.report({'INFO'}, f"Talla US {self.us_size} ({inner_dia_mm:.2f} mm = {diameter_m*1000:.2f} mm) creada.")
        return {'FINISHED'}


classes = (
    J3D_OT_create_ring_size,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
