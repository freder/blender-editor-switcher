import bpy
from .menu import ADDON_MT_Menu, ADDON_OT_set_area_type


bl_info = {
	'name': 'Editor Switcher Pie Menu',
	'description': 'Pie menu to quickly switch to a different editor type',
	'category': 'User Interface',
	'support': 'COMMUNITY',
	'author': 'https://github.com/freder',
	# 'version': (1, 0),
	'blender': (3, 0, 0),
}


class ADDON_OT_call_menu(bpy.types.Operator):
	bl_idname = 'addon.call_menu'
	bl_label = 'Editor Switcher'
	bl_options = {'REGISTER'}

	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name='ADDON_MT_Menu')
		return {'FINISHED'}


addon_keymaps = []


def register():
	bpy.utils.register_class(ADDON_MT_Menu)
	bpy.utils.register_class(ADDON_OT_set_area_type)
	bpy.utils.register_class(ADDON_OT_call_menu)

	wm = bpy.context.window_manager
	km = wm.keyconfigs.addon.keymaps.new(
		name='Window',
		space_type='EMPTY',
		region_type='WINDOW'
	)
	# https://docs.blender.org/api/2.79/bpy.types.KeyMapItems.html#bpy.types.KeyMapItems.new
	kmi = km.keymap_items.new(
		ADDON_OT_call_menu.bl_idname,
		type='ACCENT_GRAVE',
		value='PRESS',
		alt=True
	)
	addon_keymaps.append(km)


def unregister():
	bpy.utils.unregister_class(ADDON_MT_Menu)
	bpy.utils.unregister_class(ADDON_OT_set_area_type)
	bpy.utils.unregister_class(ADDON_OT_call_menu)

	wm = bpy.context.window_manager
	for km in addon_keymaps:
		wm.keyconfigs.addon.keymaps.remove(km)
	del addon_keymaps[:]


if __name__ == '__main__':
	register()
