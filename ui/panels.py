"""
Jeweler 3D Studio - UI Panels Module
Clean top-level sidebar panels for 3D Viewport ('Jeweler 3D' tab).
"""

import bpy
from bpy.props import EnumProperty
from bpy.types import Panel, Context
from ..core.metrics import METAL_ENUM_ITEMS, calculate_mesh_volume_cm3, get_metal_density


class VIEW3D_PT_j3d_ring(Panel):
    bl_label = "Anillo Base (Talla & Perfil)"
    bl_idname = "VIEW3D_PT_j3d_ring"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        layout = self.layout
        col = layout.column(align=True)
        col.operator("j3d.create_ring_shank", icon='MESH_TORUS', text="Generar Cuerpo Anillo")


class VIEW3D_PT_j3d_gems(Panel):
    bl_label = "Gemas y Engastes"
    bl_idname = "VIEW3D_PT_j3d_gems"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        layout = self.layout
        col = layout.column(align=True)
        col.operator("j3d.add_gem", icon='LIGHT_PROBE', text="Add Gem")
        col.operator("j3d.edit_gem", icon='EDITMODE_HLT', text="Edit Gem")


class VIEW3D_PT_j3d_cutters(Panel):
    bl_label = "Cortadores y Garras"
    bl_idname = "VIEW3D_PT_j3d_cutters"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        layout = self.layout
        col = layout.column(align=True)
        col.operator("j3d.add_prongs", icon='MOD_HOOK', text="Añadir Garras")
        col.operator("j3d.add_cutters", icon='MOD_BOOLEAN', text="Añadir Cortadores")


class VIEW3D_PT_j3d_metrics(Panel):
    bl_label = "Métricas y Metales"
    bl_idname = "VIEW3D_PT_j3d_metrics"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        layout = self.layout
        scene = context.scene

        col = layout.column(align=True)
        col.prop(scene, "j3d_metal_type", text="Metal")

        density = get_metal_density(scene.j3d_metal_type)
        col.label(text=f"Densidad: {density:.2f} g/cm³", icon='INFO')


classes = (
    VIEW3D_PT_j3d_ring,
    VIEW3D_PT_j3d_gems,
    VIEW3D_PT_j3d_cutters,
    VIEW3D_PT_j3d_metrics,
)


def register():
    bpy.types.Scene.j3d_metal_type = EnumProperty(
        name="Tipo de Metal",
        items=METAL_ENUM_ITEMS,
        default="GOLD_18K_YELLOW"
    ) # type: ignore

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.j3d_metal_type
