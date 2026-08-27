"""
Jeweler 3D Studio - Core Ring Shank Module
Provides parametric generation of ring shanks with customizable US/EU sizes and profile sections.
"""

import math
from typing import Dict, Tuple, List
import bpy
from bpy.props import EnumProperty, FloatProperty, StringProperty
from bpy.types import Operator, PropertyGroup

# Ring US Size to Inner Diameter in mm
US_RING_SIZES: Dict[str, float] = {
    "4": 14.86,
    "5": 15.70,
    "6": 16.51,
    "7": 17.32,
    "8": 18.14,
    "9": 18.95,
    "10": 19.76,
    "11": 20.57,
    "12": 21.39,
    "13": 22.20,
}

US_SIZE_ITEMS: List[Tuple[str, str, str]] = [
    (k, f"US {k} ({v:.2f} mm)", f"Talla US {k} con diámetro interno {v:.2f} mm")
    for k, v in US_RING_SIZES.items()
]

PROFILE_ITEMS: List[Tuple[str, str, str]] = [
    ("MEDIA_CANA", "Media Caña", "Perfil abombado superior y plano inferior"),
    ("PLANO", "Plano", "Perfil rectangular plano tradicional"),
    ("CONFORT", "Confort", "Perfil abombado suave interior y exterior"),
]


class J3D_RingProperties(PropertyGroup):
    """Properties for parametric ring shank customization."""
    us_size: EnumProperty(
        name="Talla US",
        description="Talla del anillo según estándares US/Internacionales",
        items=US_SIZE_ITEMS,
        default="7"
    ) # type: ignore

    profile_type: EnumProperty(
        name="Perfil del Metal",
        description="Forma de la sección transversal del anillo",
        items=PROFILE_ITEMS,
        default="MEDIA_CANA"
    ) # type: ignore

    width_top: FloatProperty(
        name="Ancho Superior (mm)",
        description="Ancho del perfil en la parte superior/cabeza del anillo",
        default=4.0,
        min=1.0,
        max=25.0,
        unit='LENGTH'
    ) # type: ignore

    width_bottom: FloatProperty(
        name="Ancho Inferior (mm)",
        description="Ancho del perfil en la base del anillo",
        default=2.5,
        min=1.0,
        max=20.0,
        unit='LENGTH'
    ) # type: ignore

    thickness: FloatProperty(
        name="Grosor (mm)",
        description="Espesor del perfil metálico del anillo",
        default=1.8,
        min=0.8,
        max=10.0,
        unit='LENGTH'
    ) # type: ignore


class J3D_OT_create_ring_shank(Operator):
    """Genera un cuerpo de anillo paramétrico (Ring Shank) según talla y perfil"""
    bl_idname = "j3d.create_ring_shank"
    bl_label = "Crear Anillo Base"
    bl_description = "Genera una nueva geometría de anillo paramétrico según los parámetros configurados"
    bl_options = {'REGISTER', 'UNDO'}

    us_size: EnumProperty(
        name="Talla US",
        items=US_SIZE_ITEMS,
        default="7"
    ) # type: ignore

    profile_type: EnumProperty(
        name="Perfil",
        items=PROFILE_ITEMS,
        default="MEDIA_CANA"
    ) # type: ignore

    width_top: FloatProperty(
        name="Ancho Superior (mm)",
        default=4.0,
        min=1.0,
        max=25.0
    ) # type: ignore

    width_bottom: FloatProperty(
        name="Ancho Inferior (mm)",
        default=2.5,
        min=1.0,
        max=20.0
    ) # type: ignore

    thickness: FloatProperty(
        name="Grosor (mm)",
        default=1.8,
        min=0.8,
        max=10.0
    ) # type: ignore

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        """Solo ejecutable en Object Mode."""
        return context.mode == 'OBJECT'

    def execute(self, context: bpy.types.Context) -> set[str]:
        inner_dia_mm = US_RING_SIZES.get(self.us_size, 17.32)
        inner_radius_m = (inner_dia_mm / 2.0) / 1000.0  # Convert mm to Blender meters
        thickness_m = self.thickness / 1000.0
        width_m = self.width_top / 1000.0

        # Create circle curve for shank path
        curve_data = bpy.data.curves.new(name="J3D_Ring_Path", type='CURVE')
        curve_data.dimensions = '3D'
        curve_data.use_path = True

        spline = curve_data.splines.new('NURBS')
        spline.use_cyclic_u = True

        # Create circle points
        r = inner_radius_m + (thickness_m / 2.0)
        num_points = 8
        spline.points.add(num_points - 1)
        for i in range(num_points):
            angle = (2.0 * math.pi * i) / num_points
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            spline.points[i].co = (x, y, 0.0, 1.0)

        curve_obj = bpy.data.objects.new(name=f"Ring_Shank_US{self.us_size}", object_data=curve_data)
        curve_obj["j3d_type"] = "RING_SHANK"
        curve_obj["j3d_us_size"] = self.us_size
        curve_obj["j3d_profile"] = self.profile_type

        # Link to active collection
        context.collection.objects.link(curve_obj)
        context.view_layer.objects.active = curve_obj
        curve_obj.select_set(True)

        self.report({'INFO'}, f"Anillo Talla US {self.us_size} creado exitosamente.")
        return {'FINISHED'}


classes = (
    J3D_RingProperties,
    J3D_OT_create_ring_shank,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
