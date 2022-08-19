'''
Copyright (C) cgtinker, cgtinker.com, hello@cgtinker.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from . import abs_rigging
from ...cgt_naming import HAND
from .hand_drivers import FingerDriverContainer
from .rigify_naming import rigify_finger_bone_names


class RigifyHands(abs_rigging.BpyRigging):
    """ Used for mapping values to drivers, holds rigify bone names and custom data names.
        Objects are getting searched by name, then drivers and constraints get applied. """

    def __init__(self, armature, driver_objects):
        super().__init__(armature)
        # driver to rigify cgt_rig transfer name references
        bone_name_provider = rigify_finger_bone_names.RigifyBoneNameProvider()
        bone_name_provider.update()

        self.constraint_limits = [
            [-0.261, 3.14159], [-0.261, 3.1415926], [-0.349, 3.1415926],  # thumb
            [-0.261, 1.22634], [-0.136, 1.3962634], [-0.136, 1.3962634],  # index
            [-0.349, 1.22634], [-0.136, 1.3962634], [-0.136, 1.3962634],  # middle
            [-0.436, 1.22634], [-0.136, 1.3962634], [-0.136, 1.3962634],  # ring
            [-0.698, 1.22634], [-0.136, 1.3962634], [-0.136, 1.3962634],  # pinky
        ]

        self.no_limits = [[-3.142, 3.142]]*15

        self.rigify_bone_refs = {
            HAND.wrist:                    bone_name_provider.wrist,
            HAND.driver_thumb_cmc:         bone_name_provider.thumb_cmc,
            HAND.driver_thumb_mcp:         bone_name_provider.thumb_mcp,
            HAND.driver_thumb_ip:          bone_name_provider.thumb_ip,
            # HAND.driver_thumb_tip:          bone_name_provider.thumb_tip,
            HAND.driver_index_finger_mcp:  bone_name_provider.index_mcp,
            HAND.driver_index_finger_pip:  bone_name_provider.index_pip,
            HAND.driver_index_finger_dip:  bone_name_provider.index_dip,
            # HAND.driver_index_finger_tip:  bone_name_provider.index_tip,
            HAND.driver_middle_finger_mcp: bone_name_provider.middle_mcp,
            HAND.driver_middle_finger_pip: bone_name_provider.middle_pip,
            HAND.driver_middle_finger_dip: bone_name_provider.middle_dip,
            # HAND.driver_middle_finger_tip: bone_name_provider.middle_tip,
            HAND.driver_ring_finger_mcp:   bone_name_provider.ring_mcp,
            HAND.driver_ring_finger_pip:   bone_name_provider.ring_pip,
            HAND.driver_ring_finger_dip:   bone_name_provider.ring_dip,
            # HAND.driver_ring_finger_tip:   bone_name_provider.ring_tip,
            HAND.driver_pinky_mcp:         bone_name_provider.pinky_mcp,
            HAND.driver_pinky_pip:         bone_name_provider.pinky_pip,
            HAND.driver_pinky_dip:         bone_name_provider.pinky_dip,
            # HAND.driver_pinky_tip:         bone_name_provider.pinky_tip,
        }
        self.bone_ref_list = list(self.rigify_bone_refs.keys())

        finger_driver_references = {
            # provider              # target
            HAND.thumb_cmc:         HAND.driver_thumb_cmc,
            HAND.thumb_mcp:         HAND.driver_thumb_mcp,
            HAND.thumb_ip:          HAND.driver_thumb_ip,
            # HAND.thumb_tip:         HAND.driver_thumb_tip,
            HAND.index_finger_mcp:  HAND.driver_index_finger_mcp,
            HAND.index_finger_pip:  HAND.driver_index_finger_pip,
            HAND.index_finger_dip:  HAND.driver_index_finger_dip,
            # HAND.index_finger_tip:  HAND.driver_index_finger_tip,
            HAND.middle_finger_mcp: HAND.driver_middle_finger_mcp,
            HAND.middle_finger_pip: HAND.driver_middle_finger_pip,
            HAND.middle_finger_dip: HAND.driver_middle_finger_dip,
            # HAND.middle_finger_tip: HAND.driver_middle_finger_tip,
            HAND.ring_finger_mcp:   HAND.driver_ring_finger_mcp,
            HAND.ring_finger_pip:   HAND.driver_ring_finger_pip,
            HAND.ring_finger_dip:   HAND.driver_ring_finger_dip,
            # HAND.ring_finger_tip:   HAND.driver_ring_finger_tip,
            HAND.pinky_mcp:         HAND.driver_pinky_mcp,
            HAND.pinky_pip:         HAND.driver_pinky_pip,
            HAND.pinky_dip:         HAND.driver_pinky_dip,
            # HAND.pinky_tip:         HAND.driver_pinky_tip,
        }

        # setting up finger driver names for L/R
        left_finger_provider = [key + ".L" for key in finger_driver_references.keys()]
        right_finger_provider = [key + ".R" for key in finger_driver_references.keys()]
        left_finger_targets = [value + ".L" for value in finger_driver_references.values()]
        right_finger_targets = [value + ".R" for value in finger_driver_references.values()]

        # setting up drivers for fingers
        self.left_finger_angle_drivers = FingerDriverContainer(
            left_finger_targets,
            left_finger_provider,
            "left",
            [self.get_reference_bone(b, ".L")[1] for b in self.bone_ref_list[1:]]
        )

        self.right_finger_angle_drivers = FingerDriverContainer(
            right_finger_targets,
            right_finger_provider,
            "right",
            [self.get_reference_bone(b, ".R")[1] for b in self.bone_ref_list[1:]]
        )

        # storing relations between rigify and driver cgt_rig (left / right hand)
        self.rot_constraint_dict = {}
        self.limit_constraint_dict = {}
        self.custom_bone_props = {}
        self.set_relation_dict(driver_objects)

        self.apply_driver([self.left_finger_angle_drivers, self.right_finger_angle_drivers])
        self.apply_constraints(self.rot_constraint_dict)
        self.apply_constraints(self.limit_constraint_dict)

    def get_reference_bone(self, key, extension):
        """ get reference bone and index by driver empty name. """
        try:
            index = self.bone_ref_list.index(key)
        except ValueError:
            index = -1
            pass

        if "TIP" in key:
            # rigify finger tip haµs .001 extension (why ever..)
            bone_name = self.rigify_bone_refs[key] + extension + ".001"
            return index, bone_name

        bone_name = self.rigify_bone_refs[key] + extension
        return index, bone_name

    def set_relation_dict(self, driver_objects):
        """ sets relation dict containing bone name and reference empty obj. """
        for empty in driver_objects:
            # can be left / right hand
            if ".L" in empty.name:
                extension = ".L"
            else:
                extension = ".R"

            # remove extension from driver name
            name = empty.name.replace(extension, "")
            try:
                index, bone_name = self.get_reference_bone(name, extension)
                self.rot_constraint_dict[empty.name] = [bone_name, "COPY_ROTATION"]
                # self.custom_bone_props[bone_name] = mapping.CustomProperties(bone_name, "factor", 1, -5, 5, True)
                if index != 0:
                    index -= 1
                    self.limit_constraint_dict[empty.name] = [bone_name, "LIMIT_ROTATION", self.constraint_limits[index]]
                    # self.limit_constraint_dict[empty.name] = [bone_name, "LIMIT_ROTATION", self.no_limits[index]]
            except KeyError:
                pass
