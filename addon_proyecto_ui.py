import bpy
import random

# 1. INFORMACIÓN DEL ADDON 
bl_info = {
    "name": "Herramientas de Artista 3D",
    "author": "Alejandro",
    "version": (1, 0),
    "blender": (5, 0, 1),   
    "location": "View3D > Sidebar > Artista Tab",
    "description": "Addon con herramientas optimizadas para artistas 3D",
    "category": "Interface",
}


# Operador 1: Origen al Mundo [cite: 16]
class UI_OT_OriginToWorld(bpy.types.Operator):
    bl_idname = "object.origin_to_world"
    bl_label = "Origen al Mundo"
    bl_description = "Mueve el origen del objeto al (0,0,0) del mundo"
    
    def execute(self, context):
        # Guardar cursor actual
        old_cursor_loc = context.scene.cursor.location.copy()
        # Mover cursor al origen
        context.scene.cursor.location = (0, 0, 0)
        # Ajustar origen
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        # Restaurar cursor
        context.scene.cursor.location = old_cursor_loc
        return {'FINISHED'}

# Operador 2: Limpiar Materiales Vacíos [cite: 17]
class UI_OT_CleanMaterials(bpy.types.Operator):
    bl_idname = "object.clean_materials"
    bl_label = "Limpiar Materiales"
    bl_description = "Elimina slots de materiales vacíos"
    
    def execute(self, context):
        obj = context.active_object
        if obj:
            bpy.ops.object.material_slot_remove_unused()
        return {'FINISHED'}

# Operador 3: Modo Esculpido Rápido [cite: 17]
class UI_OT_QuickSculpt(bpy.types.Operator):
    bl_idname = "view3d.quick_sculpt"
    bl_label = "Modo Esculpido Rápido"
    
    def execute(self, context):
        bpy.ops.sculpt.sculptmode_toggle()
        context.space_data.shading.type = 'SOLID'
        context.space_data.shading.color_type = 'MATCAP'
        return {'FINISHED'}

# Operador 4: Resetear Transformaciones [cite: 17]
class UI_OT_ResetTransforms(bpy.types.Operator):
    bl_idname = "object.reset_transforms"
    bl_label = "Resetear Transforms"
    
    def execute(self, context):
        bpy.ops.object.location_clear()
        bpy.ops.object.rotation_clear()
        bpy.ops.object.scale_clear()
        return {'FINISHED'}

# Operador 5: Material Emisivo Aleatorio (No visto en clase/Materiales) [cite: 25, 26]
class UI_OT_RandomEmission(bpy.types.Operator):
    bl_idname = "object.random_emission"
    bl_label = "Material Emisivo Aleatorio"
    bl_description = "Crea un material emisivo con un color al azar"
    
    def execute(self, context):
        obj = context.active_object
        if obj:
            mat = bpy.data.materials.new(name="Random_Emission")
            mat.use_nodes = True
            nodes = mat.node_tree.nodes
            nodes.clear()
            
            node_emission = nodes.new(type='ShaderNodeEmission')
            node_emission.inputs[0].default_value = (random.random(), random.random(), random.random(), 1)
            node_emission.inputs[1].default_value = 5.0 # Fuerza
            
            node_output = nodes.new(type='ShaderNodeOutputMaterial')
            mat.node_tree.links.new(node_emission.outputs[0], node_output.inputs[0])
            
            if obj.data.materials:
                obj.data.materials[0] = mat
            else:
                obj.data.materials.append(mat)
        return {'FINISHED'}

# INTERFAZ DE USUARIO

# Panel Lateral (N-Panel) 
class UI_PT_MainPanel(bpy.types.Panel):
    bl_label = "Herramientas Artista"
    bl_idname = "UI_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Proyecto UI' # Nombre de la pestaña lateral

    def draw(self, context):
        layout = self.layout
        
        col = layout.column(align=True)
        col.label(text="Transformaciones:")
        # Uso de iconos y agrupación por proximidad 
        col.operator("object.origin_to_world", icon='WORLD')
        col.operator("object.reset_transforms", icon='REFRESH')
        
        layout.separator()
        
        col = layout.column(align=True)
        col.label(text="Utilidades:")
        col.operator("object.clean_materials", icon='NODE_MATERIAL')
        col.operator("object.random_emission", icon='LIGHT_SUN')
        
        layout.separator()
        
        layout.operator("view3d.quick_sculpt", icon='SCULPTMODE_HLT')

# Pie Menu 
class UI_MT_PieMenu(bpy.types.Menu):
    bl_label = "Acceso Rápido"
    bl_idname = "UI_MT_PieMenu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # Agregar los operadores más usados al menú circular 
        pie.operator("object.origin_to_world")
        pie.operator("object.reset_transforms")
        pie.operator("object.random_emission")
        pie.operator("view3d.quick_sculpt")

#  REGISTRO

classes = (
    UI_OT_OriginToWorld,
    UI_OT_CleanMaterials,
    UI_OT_QuickSculpt,
    UI_OT_ResetTransforms,
    UI_OT_RandomEmission,
    UI_PT_MainPanel,
    UI_MT_PieMenu,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # Atajo de teclado para el Pie Menu (Shift + X)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'X', 'PRESS', shift=True)
        kmi.properties.name = "UI_MT_PieMenu"

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()