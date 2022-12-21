from arm.logicnode.arm_nodes import *

class SetCursorLocationNode(ArmLogicTreeNode):
    """Assigns the mouse cursor location in screen coordinates (pixels)."""
    bl_idname = 'LNSetCursorLocationNode'
    bl_label = 'Set Cursor Location'
    arm_section = 'mouse'
    arm_version = 1

    def arm_init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmIntSocket', 'X')
        self.add_input('ArmIntSocket', 'Y')

        self.add_output('ArmNodeSocketAction', 'Out')
