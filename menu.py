import bpy
from bpy.types import Menu


class ADDON_OT_set_area_type(bpy.types.Operator):
	bl_idname = 'addon.set_area_type'
	bl_label = 'Editor Switcher Pie Menu Options'

	# https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items
	# `(identifier, name, description, icon, number)`
	mode_options = [
		# general
		('VIEW_3D', '3D Viewport', '', 'VIEW3D', 0),
		('IMAGE_EDITOR', 'Image Editor', '', 'IMAGE', 1),
		('UV', 'UV Editor', '', 'UV', 2),
		('CompositorNodeTree', 'Compositor', '', 'NODE_COMPOSITING', 3),
		('SEQUENCE_EDITOR', 'Video Sequencer', '', 'SEQ_SEQUENCER', 4),
		('CLIP_EDITOR', 'Movie Clip Editor', '', 'TRACKER', 5),
		('ShaderNodeTree', 'Shader Node Editor', '', 'NODE_MATERIAL', 6),
		('TextureNodeTree', 'Texture Node Editor', '', 'NODE_TEXTURE', 7),
		('GeometryNodeTree', 'Geometry Node Editor', '', 'GEOMETRY_NODES', 8),

		# animation
		('DOPESHEET', 'Dope Sheet', '', 'ACTION', 9),
		('FCURVES', 'Graph Editor', '', 'GRAPH', 10),
		('NLA_EDITOR', 'Nonlinear Animation', '', 'NLA', 11),
		('TIMELINE', 'Timeline', '', 'TIME', 12),
		('DRIVERS', 'Drivers', '', 'DRIVER', 13),

		# scripting
		('TEXT_EDITOR', 'Text Editor', '', 'TEXT', 14),
		('CONSOLE', 'Python Console', '', 'CONSOLE', 15),
		('INFO', 'Info', '', 'INFO', 16),
		# ('TOPBAR', 'Top Bar', '', 'TEXT', 12),
		# ('STATUSBAR', 'Status Bar', '', 'TEXT', 13),

		# data
		('OUTLINER', 'Outliner', '', 'OUTLINER', 17),
		('PROPERTIES', 'Properties', '', 'PROPERTIES', 18),
		('FILES', 'File Browser', '', 'FILEBROWSER', 19),
		('ASSETS', 'Asset Browser', '', 'ASSET_MANAGER', 20),
		('SPREADSHEET', 'Spreadsheet', '', 'SPREADSHEET', 21),
		('PREFERENCES', 'Preferences', '', 'PREFERENCES', 22),
	]

	selected_mode: bpy.props.EnumProperty(
		items=mode_options,
		default='VIEW_3D'
	)

	def execute(self, context):
		bpy.context.area.ui_type = self.selected_mode
		return {'FINISHED'}


class ADDON_MT_Menu(Menu):
	bl_label = 'Editor type:'

	def draw(self, context):
		layout = self.layout
		pie = layout.menu_pie()
		pie.operator_enum(
			ADDON_OT_set_area_type.bl_idname,
			'selected_mode'
		)
