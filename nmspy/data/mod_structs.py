from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from ctypes import _Pointer

import nmspy.data.struct_types as stypes

import ctypes
import ctypes.wintypes

from nmspy.data import common, enums as nms_enums
from pymhf.core.calling import call_function
# from nmspy.data.types import core, simple
from pymhf.extensions.cpptypes import std
from pymhf.core.memutils import map_struct
from pymhf.core.utils import safe_assign_enum

class cGcBinoculars(ctypes.Structure):
    MarkerModel: common.TkHandle

cGcBinoculars._fields_ = [
    ("_padding0", ctypes.c_ubyte * 0x760),
    ("MarkerModel", common.TkHandle),
]

class cGcDiscoveryData(ctypes.Structure):
    _fields_ = [
        ("universeAddress", ctypes.c_uint64),
    ]