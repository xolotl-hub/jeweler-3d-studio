"""
Jeweler 3D Studio - Core Gems Module
Provides gem material generation, utility functions, and UI operators.
"""

import math
import bpy
import bmesh
from bpy.types import Operator


# Gem material properties
GEM_TYPES = {
    "DIAMOND":       {"name": "Diamante",   "ior": 2.417, "density": 3.52, "color": (1.0, 1.0, 1.0, 1.0)},
    "RUBY":          {"name": "Rubi",       "ior": 1.770, "density": 4.02, "color": (0.85, 0.02, 0.08, 1.0)},
    "SAPPHIRE":      {"name": "Zafiro",     "ior": 1.770, "density": 4.02, "color": (0.05, 0.15, 0.85, 1.0)},
    "EMERALD":       {"name": "Esmeralda",  "ior": 1.580, "density": 2.76, "color": (0.02, 0.75, 0.25, 1.0)},
    "AQUAMARINE":    {"name": "Aquamarina", "ior": 1.575, "density": 2.72, "color": (0.35, 0.85, 0.95, 1.0)},
    "AMETHYST":      {"name": "Amatista",   "ior": 1.544, "density": 2.65, "color": (0.45, 0.08, 0.65, 1.0)},
    "CUBIC_ZIRCONIA":{"name": "Circonia",   "ior": 2.150, "density": 5.65, "color": (0.95, 0.95, 1.0, 1.0)},
}


def get_or_create_gem_material(gem_type):
    """Crea o reutiliza un material BSDF realista para la gema seleccionada."""
    mat_name = "J3D_Material_" + gem_type
    mat = bpy.data.materials.get(mat_name)
    if mat is not None:
        return mat

    mat = bpy.data.materials.new(name=mat_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out_node = nodes.new('ShaderNodeOutputMaterial')
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    links.new(bsdf.outputs['BSDF'], out_node.inputs['Surface'])

    props = GEM_TYPES.get(gem_type, GEM_TYPES["DIAMOND"])

    if 'Transmission Weight' in bsdf.inputs:
        bsdf.inputs['Transmission Weight'].default_value = 1.0
    elif 'Transmission' in bsdf.inputs:
        bsdf.inputs['Transmission'].default_value = 1.0

    bsdf.inputs['Base Color'].default_value = props["color"]
    bsdf.inputs['Roughness'].default_value = 0.0
    bsdf.inputs['IOR'].default_value = props["ior"]
    return mat


# ── Dummy cube operator (used by all secondary subpanels as placeholder) ──────
class J3D_OT_dummy_cube(Operator):
    """Aniadir Cubo de Prueba 5mm"""
    bl_idname = "j3d.dummy_cube"
    bl_label = "Aniadir Cubo"
    bl_description = "Aniade un cubo de 5mm de referencia a la escena"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        unit_scale = context.scene.unit_settings.scale_length or 1.0
        cube_size = 5.0 / unit_scale
        bpy.ops.mesh.primitive_cube_add(
            size=cube_size,
            location=context.scene.cursor.location
        )
        self.report({'INFO'}, "Cubo de 5 mm creado.")
        return {'FINISHED'}


# ── Gem operator (Visor de Gemas) ─────────────────────────────────────────────
class J3D_OT_add_gem(Operator):
    """Aniadir Diamante 5mm"""
    bl_idname = "j3d.add_gem"
    bl_label = "Aniadir Gema"
    bl_description = "Aniade un diamante redondo de 5mm en la posicion del cursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        unit_scale = context.scene.unit_settings.scale_length or 1.0
        # Diamante: radio 2.5mm, alto 3mm
        r = 2.5 / unit_scale
        h = 3.0 / unit_scale
        loc = context.scene.cursor.location

        bpy.ops.mesh.primitive_cone_add(
            vertices=16,
            radius1=r,
            radius2=0.0,
            depth=h,
            location=(loc.x, loc.y, loc.z)
        )
        obj = context.active_object
        if obj:
            obj.name = "Diamond_5mm"
            mat = get_or_create_gem_material("DIAMOND")
            obj.data.materials.append(mat)

        self.report({'INFO'}, "Diamante 5mm creado.")
        return {'FINISHED'}


classes = (
    J3D_OT_dummy_cube,
    J3D_OT_add_gem,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
