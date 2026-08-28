"""
Jeweler 3D Studio - UI Panels Module
Clean panel and subpanel architecture for Viewport N-Panel ('Jeweler 3D' tab).
All subpanels default to closed ('DEFAULT_CLOSED') to keep UI clean, except Gem Visor.
"""

import bpy
from bpy.props import EnumProperty
from bpy.types import Panel, Context
from ..core.ring import US_SIZE_ITEMS, GEOMETRY_TYPE_ITEMS


# ===================================================================
# 1. PANEL 1: Anillo y Talla
# ===================================================================

class VIEW3D_PT_j3d_ring_size(Panel):
    bl_label = "Anillo y Talla"
    bl_idname = "VIEW3D_PT_j3d_ring_size"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        pass


class VIEW3D_PT_j3d_sub_size(Panel):
    bl_label = "Talla"
    bl_idname = "VIEW3D_PT_j3d_sub_size"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_ring_size"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        layout = self.layout
        scene = context.scene
        col = layout.column(align=True)

        col.prop(scene, "j3d_us_size", text="Talla US")

        row = col.row(align=True)
        row.prop(scene, "j3d_geometry_type", expand=True)

        col.separator()
        op = col.operator("j3d.create_ring_size", icon='CURVE_NCIRCLE', text="Crear Talla")
        op.us_size = scene.j3d_us_size
        op.geometry_type = scene.j3d_geometry_type


class VIEW3D_PT_j3d_sub_profile(Panel):
    bl_label = "Perfil del Metal"
    bl_idname = "VIEW3D_PT_j3d_sub_profile"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_ring_size"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Perfil)")


# ===================================================================
# 2. PANEL 2: Gemas
# ===================================================================

class VIEW3D_PT_j3d_gems(Panel):
    bl_label = "Gemas"
    bl_idname = "VIEW3D_PT_j3d_gems"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        pass


class VIEW3D_PT_j3d_sub_gem_visor(Panel):
    bl_label = "Visor de Gemas"
    bl_idname = "VIEW3D_PT_j3d_sub_gem_visor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_gems"
    # Permanece abierto por defecto para acceso rápido

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Visor Gemas)")


class VIEW3D_PT_j3d_sub_gem_map(Panel):
    bl_label = "Mapa de Gemas"
    bl_idname = "VIEW3D_PT_j3d_sub_gem_map"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_gems"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Mapa Gemas)")


# ===================================================================
# 3. PANEL 3: Engastes
# ===================================================================

class VIEW3D_PT_j3d_settings(Panel):
    bl_label = "Engastes"
    bl_idname = "VIEW3D_PT_j3d_settings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        pass


class VIEW3D_PT_j3d_sub_prongs(Panel):
    bl_label = "Garras (Prongs)"
    bl_idname = "VIEW3D_PT_j3d_sub_prongs"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Garras)")


class VIEW3D_PT_j3d_sub_bezel(Panel):
    bl_label = "Bisel (Bezel)"
    bl_idname = "VIEW3D_PT_j3d_sub_bezel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Bisel)")


class VIEW3D_PT_j3d_sub_pave(Panel):
    bl_label = "Pavé"
    bl_idname = "VIEW3D_PT_j3d_sub_pave"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_settings"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Pavé)")


# ===================================================================
# 4. PANEL 4: Cortadores
# ===================================================================

class VIEW3D_PT_j3d_cutters(Panel):
    bl_label = "Cortadores"
    bl_idname = "VIEW3D_PT_j3d_cutters"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        pass


class VIEW3D_PT_j3d_sub_cutter_seat(Panel):
    bl_label = "Asiento y Perforación"
    bl_idname = "VIEW3D_PT_j3d_sub_cutter_seat"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_cutters"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Asiento)")


class VIEW3D_PT_j3d_sub_cutter_v(Panel):
    bl_label = "Cortador en V"
    bl_idname = "VIEW3D_PT_j3d_sub_cutter_v"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_cutters"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Cortador V)")


# ===================================================================
# 5. PANEL 5: Canastas
# ===================================================================

class VIEW3D_PT_j3d_baskets(Panel):
    bl_label = "Canastas"
    bl_idname = "VIEW3D_PT_j3d_baskets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        pass


class VIEW3D_PT_j3d_sub_basket_gallery(Panel):
    bl_label = "Galería Estándar"
    bl_idname = "VIEW3D_PT_j3d_sub_basket_gallery"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_baskets"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Galería)")


class VIEW3D_PT_j3d_sub_basket_supports(Panel):
    bl_label = "Soportes"
    bl_idname = "VIEW3D_PT_j3d_sub_basket_supports"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_baskets"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Soportes)")


# ===================================================================
# 6. PANEL 6: Métricas y Cotizador
# ===================================================================

class VIEW3D_PT_j3d_metrics(Panel):
    bl_label = "Métricas & Cotizador"
    bl_idname = "VIEW3D_PT_j3d_metrics"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'

    def draw(self, context: Context) -> None:
        pass


class VIEW3D_PT_j3d_sub_weights(Panel):
    bl_label = "Pesos y Metales"
    bl_idname = "VIEW3D_PT_j3d_sub_weights"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_metrics"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Pesos)")


class VIEW3D_PT_j3d_sub_quotation(Panel):
    bl_label = "Cotizador & Ficha Técnica"
    bl_idname = "VIEW3D_PT_j3d_sub_quotation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jeweler 3D'
    bl_parent_id = "VIEW3D_PT_j3d_metrics"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context) -> None:
        col = self.layout.column(align=True)
        col.operator("j3d.dummy_cube", icon='CUBE', text="Añadir Cubo (Cotizador)")


# ===================================================================
# REGISTRO DE CLASES
# ===================================================================

classes = (
    VIEW3D_PT_j3d_ring_size,
    VIEW3D_PT_j3d_sub_size,
    VIEW3D_PT_j3d_sub_profile,
    VIEW3D_PT_j3d_gems,
    VIEW3D_PT_j3d_sub_gem_visor,
    VIEW3D_PT_j3d_sub_gem_map,
    VIEW3D_PT_j3d_settings,
    VIEW3D_PT_j3d_sub_prongs,
    VIEW3D_PT_j3d_sub_bezel,
    VIEW3D_PT_j3d_sub_pave,
    VIEW3D_PT_j3d_cutters,
    VIEW3D_PT_j3d_sub_cutter_seat,
    VIEW3D_PT_j3d_sub_cutter_v,
    VIEW3D_PT_j3d_baskets,
    VIEW3D_PT_j3d_sub_basket_gallery,
    VIEW3D_PT_j3d_sub_basket_supports,
    VIEW3D_PT_j3d_metrics,
    VIEW3D_PT_j3d_sub_weights,
    VIEW3D_PT_j3d_sub_quotation,
)


def register():
    bpy.types.Scene.j3d_us_size = EnumProperty(
        name="Talla US",
        description="Selección de talla estándar US (incluye medias tallas)",
        items=US_SIZE_ITEMS,
        default="7.0"
    ) # type: ignore

    bpy.types.Scene.j3d_geometry_type = EnumProperty(
        name="Tipo de Geometría",
        description="Formato de salida de la talla",
        items=GEOMETRY_TYPE_ITEMS,
        default="CURVE"
    ) # type: ignore

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.j3d_us_size
    del bpy.types.Scene.j3d_geometry_type
