"""
Jeweler 3D Studio - UI Panels Module
Main N-Panel interface located in 3D Viewport under 'Jeweler 3D' tab.
Features collapsible sections for ring creation, gems, cutters, prongs, and metal weight metrics.
"""

from typing import Optional
import bpy
from bpy.props import EnumProperty, BoolProperty
from bpy.types import Panel, Context
from ..core.metrics import METAL_ENUM_ITEMS, calculate_mesh_weight, calculate_mesh_volume_cm3, get_metal_density


class VIEW3D_PT_jeweler_3d_studio(Panel):
    """Panel principal N-Panel de Jeweler 3D Studio en la vista 3D."""
    bl_label = "Jeweler 3D Studio"
    bl_idname = "VIEW3D_PT_jeweler_3d_studio"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        layout = self.layout
        scene = context.scene
        obj = context.active_object

        # -------------------------------------------------------------------
        # SECCIÓN 1: Anillo Base (Collapsible Box)
        # -------------------------------------------------------------------
        box_ring = layout.box()
        row = box_ring.row(align=True)
        icon_ring = 'DOWNARROW_HLT' if scene.j3d_ui_box_ring else 'RIGHTARROW'
        row.prop(scene, "j3d_ui_box_ring", icon=icon_ring, text="Anillo Base (Talla & Perfil)", toggle=True)

        if scene.j3d_ui_box_ring:
            col = box_ring.column(align=True)
            col.operator("j3d.create_ring_shank", icon='MESH_TORUS', text="Generar Cuerpo Anillo")

        # -------------------------------------------------------------------
        # SECCIÓN 2: Gemas y Engastes (Collapsible Box)
        # -------------------------------------------------------------------
        box_gems = layout.box()
        row = box_gems.row(align=True)
        icon_gems = 'DOWNARROW_HLT' if scene.j3d_ui_box_gems else 'RIGHTARROW'
        row.prop(scene, "j3d_ui_box_gems", icon=icon_gems, text="Gemas y Engastes", toggle=True)

        if scene.j3d_ui_box_gems:
            col = box_gems.column(align=True)
            col.operator("j3d.add_gem", icon='LIGHT_PROBE', text="Añadir Gema Individual")
            col.separator()
            col.operator("j3d.create_pave", icon='PARTICLES', text="Distribución Pavé")

        # -------------------------------------------------------------------
        # SECCIÓN 3: Cortadores y Garras (Collapsible Box)
        # -------------------------------------------------------------------
        box_cutters = layout.box()
        row = box_cutters.row(align=True)
        icon_cutters = 'DOWNARROW_HLT' if scene.j3d_ui_box_cutters else 'RIGHTARROW'
        row.prop(scene, "j3d_ui_box_cutters", icon=icon_cutters, text="Cortadores y Garras", toggle=True)

        if scene.j3d_ui_box_cutters:
            col = box_cutters.column(align=True)
            col.operator("j3d.add_prongs", icon='MOD_HOOK', text="Añadir Garras (Prongs)")
            col.operator("j3d.add_cutters", icon='MOD_BOOLEAN', text="Añadir Cortador Booleano")

        # -------------------------------------------------------------------
        # SECCIÓN 4: Métricas y Metales (Collapsible Box)
        # -------------------------------------------------------------------
        box_metrics = layout.box()
        row = box_metrics.row(align=True)
        icon_metrics = 'DOWNARROW_HLT' if scene.j3d_ui_box_metrics else 'RIGHTARROW'
        row.prop(scene, "j3d_ui_box_metrics", icon=icon_metrics, text="Métricas y Metales", toggle=True)

        if scene.j3d_ui_box_metrics:
            col = box_metrics.column(align=True)
            col.prop(scene, "j3d_metal_type", text="Metal")

            metal_key = scene.j3d_metal_type
            density = get_metal_density(metal_key)
            col.label(text=f"Densidad: {density:.2f} g/cm³", icon='INFO')

            if obj and obj.type == 'MESH':
                # Lightweight volume and weight display
                vol_cm3 = calculate_mesh_volume_cm3(obj)
                weight_g = vol_cm3 * density

                box_info = col.box()
                box_info.label(text=f"Objeto: {obj.name}")
                box_info.label(text=f"Volumen Neto: {vol_cm3:.3f} cm³")
                box_info.label(text=f"Peso Metal: {weight_g:.2f} g", icon='PHYSICS')
            else:
                col.label(text="Selecciona una malla activa para pesaje", icon='WARNING')

            col.separator()
            col.operator("j3d.export_report", icon='FILE_TEXT', text="Exportar Ficha Técnica")


classes = (
    VIEW3D_PT_jeweler_3d_studio,
)


def register():
    bpy.types.Scene.j3d_metal_type = EnumProperty(
        name="Tipo de Metal",
        description="Selección de aleación metálica para cálculo de densidad y peso",
        items=METAL_ENUM_ITEMS,
        default="GOLD_18K_YELLOW"
    ) # type: ignore

    bpy.types.Scene.j3d_ui_box_ring = BoolProperty(
        name="Anillo Base",
        default=True
    ) # type: ignore

    bpy.types.Scene.j3d_ui_box_gems = BoolProperty(
        name="Gemas y Engastes",
        default=True
    ) # type: ignore

    bpy.types.Scene.j3d_ui_box_cutters = BoolProperty(
        name="Cortadores y Garras",
        default=True
    ) # type: ignore

    bpy.types.Scene.j3d_ui_box_metrics = BoolProperty(
        name="Métricas y Metales",
        default=True
    ) # type: ignore

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.j3d_metal_type
    del bpy.types.Scene.j3d_ui_box_ring
    del bpy.types.Scene.j3d_ui_box_gems
    del bpy.types.Scene.j3d_ui_box_cutters
    del bpy.types.Scene.j3d_ui_box_metrics
