from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from ctypes import _Pointer

import nmspy.data.struct_types as stypes

import ctypes
import ctypes.wintypes

from nmspy.data import common, enums as nms_enums
from nmspy.data.structs import cGcNGui
from pymhf.core.calling import call_function
# from nmspy.data.types import core, simple
from pymhf.extensions.cpptypes import std
from pymhf.core.memutils import map_struct
from pymhf.core.utils import safe_assign_enum

#------------------------------------------------------------------------------------User Added Structs----------------------------------------------------------------------------------------------------

class HMONITOR__(ctypes.Structure):
    _fields_ = [
        ("unused", ctypes.c_int32),
    ]

class HICON__(ctypes.Structure):
    _fields_ = [
        ("unused", ctypes.c_int32),
    ]

class HWND__(ctypes.Structure):
    _fields_ = [
        ("unused", ctypes.c_int32),
    ]

class GLFWgammaramp(ctypes.Structure):
    _fields_ = [
        ("red", ctypes.POINTER(ctypes.c_uint16)),
        ("green", ctypes.POINTER(ctypes.c_uint16)),
        ("blue", ctypes.POINTER(ctypes.c_uint16)),
        ("size", ctypes.c_uint32),
    ]

class _GLFWcursorWin32(ctypes.Structure):
    _fields_ = [
        ("handle", ctypes.POINTER(HICON__)),
    ]

class _GLFWcursor(ctypes.Structure):
    next: _Pointer[_GLFWcursor]
    win32: "_GLFWcursorWin32"

_GLFWcursor._fields_ = [
    ("next", ctypes.POINTER(_GLFWcursor)),
    ("win32", _GLFWcursorWin32),
]

class _GLFWmonitorWin32(ctypes.Structure):
    _fields_ = [
        ("handle", ctypes.POINTER(HMONITOR__)),
        ("adapterName", std.array[ctypes.c_wchar, 32]),
        ("adapterString", std.array[ctypes.c_wchar, 32]),
        ("displayName", std.array[ctypes.c_wchar, 32]),
        ("adpaterId", std.array[ctypes.c_wchar, 128]),
        ("adapterKey", std.array[ctypes.c_wchar, 128]),
        ("publicAdapterName", std.array[ctypes.c_char, 32]),
        ("publicDisplayName", std.array[ctypes.c_char, 32]),
        ("modesPruned", ctypes.c_int32),
        ("modeChanged", ctypes.c_int32),
    ]




class GLFWvidmode(ctypes.Structure):
    _fields_ = [
        ("width", ctypes.c_int32),
        ("height", ctypes.c_int32),
        ("redBits", ctypes.c_int32),
        ("greedBits", ctypes.c_int32),
        ("blueBits", ctypes.c_int32),
        ("refreshRate", ctypes.c_int32),
    ]

class _GLFWwindowwin32(ctypes.Structure):
    _fields_ = [
        ("handle", ctypes.POINTER(HWND__)),
        ("bigIcon", ctypes.POINTER(HICON__)),
        ("smallIcon", ctypes.POINTER(HICON__)),
        ("cursorTracked", ctypes.c_int32),
        ("frameAction", ctypes.c_int32),
        ("iconified", ctypes.c_int32),
        ("maximized", ctypes.c_int32),
        ("transparent", ctypes.c_int32),
        ("scaleToMonitor", ctypes.c_int32),
        ("lastCursorPosX", ctypes.c_int32),
        ("lastCursorPosY", ctypes.c_int32),
        ("centerX", ctypes.c_int32),
        ("centerY", ctypes.c_int32),
        ("blankCursor", ctypes.POINTER(HICON__)),
    ]

class _GLFWmonitor(ctypes.Structure):
    name: _Pointer[ctypes.c_char]
    userPointer: int
    widthMM: int
    heightMM: int
    #window: "GLFWwindow"
    modes: "GLFWvidmode"
    modeCount: int
    currentMode: "GLFWvidmode"
    originalRamp: "GLFWgammaramp"
    currentRamp: "GLFWgammaramp"
    adapterVram: int
    win32: "_GLFWmonitorWin32"

_GLFWmonitor._fields_ = [
    ("name", ctypes.c_char),
    ("userPointer", ctypes.c_int32),
    ("widthMM", ctypes.c_int32),
    ("heightMM", ctypes.c_int32),
    #("window", GLFWwindow),
    ("padding0", ctypes.c_byte * 0x390),
    ("modes", GLFWvidmode),
    ("modeCount", ctypes.c_int32),
    ("currentMode", GLFWvidmode),
    ("originalRamp", GLFWgammaramp),
    ("currentRamp", GLFWgammaramp),
    ("adapterVram", ctypes.c_int64),
    ("win32", _GLFWmonitorWin32),
]

class GLFWwindow(ctypes.Structure):
    next: _Pointer[GLFWwindow]
    resizable: ctypes.c_int32
    decorated: ctypes.c_int32
    autoIconify: ctypes.c_int32
    floating: ctypes.c_int32
    focusOnShow: ctypes.c_int32
    shouldClose: ctypes.c_int32
    userPointer: int
    videoMode: GLFWvidmode
    monitor: _GLFWmonitor
    cursor: _GLFWcursor
    minwidth: ctypes.c_int32
    minheight: ctypes.c_int32
    maxwidth: ctypes.c_int32
    maxheight: ctypes.c_int32
    numer: ctypes.c_int32
    denom: ctypes.c_int32
    stickyKeys: ctypes.c_int32
    stickyMouseButtons: ctypes.c_int32
    lockKeyMods: ctypes.c_int32
    cursorMode: ctypes.c_int32
    mouseButtons: std.array[ctypes.c_char, 8]
    keys: std.array[ctypes.c_char, 349]
    virtualCursorPosX: ctypes.c_longdouble
    virtualCursorPosY: ctypes.c_longdouble
    rawMouseMotion: ctypes.c_int32
    #context: "_GLFWcontext"
    win32: "_GLFWwindowwin32"

GLFWwindow._fields_ = [
    ("next", ctypes.POINTER(GLFWwindow)),
    ("resizable", ctypes.c_int32),
    ("decorated", ctypes.c_int32),
    ("autoIconify", ctypes.c_int32),
    ("floating", ctypes.c_int32),
    ("focusOnShow", ctypes.c_int32),
    ("shouldClose", ctypes.c_int32),
    ("userPointer", ctypes.c_int32),
    ("videoMode", GLFWvidmode),
    ("monitor", _GLFWmonitor),
    ("cursor", _GLFWcursor),
    ("minwidth", ctypes.c_int32),
    ("minheight", ctypes.c_int32),
    ("maxwidth", ctypes.c_int32),
    ("maxheight", ctypes.c_int32),
    ("numer", ctypes.c_int32),
    ("denom", ctypes.c_int32),
    ("stickyKeys", ctypes.c_int32),
    ("stickyMouseButtons", ctypes.c_int32),
    ("lockKeyMods", ctypes.c_int32),
    ("cursorMode", ctypes.c_int32),
    ("mouseButtons", std.array[ctypes.c_char, 8]),
    ("keys", std.array[ctypes.c_char, 349]),
    ("virtualCursorPosX", ctypes.c_longdouble),
    ("virtualCursorPosY", ctypes.c_longdouble),
    ("rawMouseMotion", ctypes.c_int32),
    #("context", _GLFWcontext),
    ("buffer0", ctypes.c_ubyte * 0xC8),
    ("win32", _GLFWwindowwin32),
]


class cGcPlayerController_vtbl(ctypes.Structure):
    cGcPlayerController_dtor_0: bytes
    GetButtonInput: bytes
    GetAnalogInput: bytes

cGcPlayerController_vtbl._fields_ = [
    ("cGcPlayerController_dtor_0", ctypes.c_ubyte * 0x8),
    ("GetButtonInput", ctypes.c_ubyte * 0x8),
    ("GetAnalogInput", ctypes.c_ubyte * 0x8),
]

class cGcPlayerController(ctypes.Structure):
    __vftable: _Pointer["cGcPlayerController_vtbl"]

cGcPlayerController._fields_ = [
    ("__vftable", ctypes.POINTER(cGcPlayerController_vtbl)),
]

class cGcHumanController(cGcPlayerController, ctypes.Structure):
    _mePort: ctypes.c_int32

cGcHumanController._fields_ = [
    ("_mePort", ctypes.c_int32),
]

class VkExtent3D(ctypes.Structure):
     _fields_ = [
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("depth", ctypes.c_uint32),
        ]

class VkImageCreateInfo(ctypes.Structure):
     _fields_ = [
        ("sType", ctypes.c_int32),
        ("pNext", ctypes.c_void_p),
        ("flags", ctypes.c_uint32),
        ("imageType", ctypes.c_int32),
        ("format", ctypes.c_int32),
        ("extent", VkExtent3D),
        ("levels", ctypes.c_uint32),
        ("arrayLayers", ctypes.c_uint32),
        ("samples", ctypes.c_int32),
        ("tiling", ctypes.c_int32),
        ("usage", ctypes.c_uint32),
        ("sharingMode", ctypes.c_int32),
        ("queueFamilyIndexCount", ctypes.c_uint32),
        ("pQueueFamilyIndices", ctypes.POINTER(ctypes.c_uint32)),
        ("initialLayout", ctypes.c_int32),
        ]

class cTkNGuiAlignment(ctypes.Structure):
     _fields_ = [
        ("vertical", ctypes.c_int32),
        ("horizontal", ctypes.c_int32),
        ]

class cGcAccessibleOverride_Layout(ctypes.Structure):
     _fields_ = [
        ("accessibleOverride_Layout", ctypes.c_int32),
        ("floatValue", ctypes.c_float),
        ]

class cGcVROverride_Layout(ctypes.Structure):
     _fields_ = [
        ("vROverride_Layout", ctypes.c_int32),
        ("floatValue", ctypes.c_float),
        ]

class cGcNGuiLayoutData(ctypes.Structure):
     _fields_ = [
        ("vROverrides", common.cTkDynamicArray[cGcVROverride_Layout]),
        ("accessibleOverrides", common.cTkDynamicArray[cGcAccessibleOverride_Layout]),
        ("positionX", ctypes.c_float),
        ("positionY", ctypes.c_float),
        ("width", ctypes.c_float),
        ("height", ctypes.c_float),
        ("constrainAspect", ctypes.c_float),
        ("maxWidth", ctypes.c_float),
        ("align", cTkNGuiAlignment),
        ("widthPercentage", ctypes.c_ubyte),
        ("heightPercentage", ctypes.c_ubyte),
        ("constrainProportions", ctypes.c_ubyte),
        ("forceAspect", ctypes.c_ubyte),
        ("anchor", ctypes.c_ubyte),
        ("anchorPercent", ctypes.c_ubyte),
        ("sameLine", ctypes.c_ubyte),
        ("slowCursorOnHover", ctypes.c_ubyte),
        ]

class cTkNGuiForcedStyle(ctypes.Structure):
     _fields_ = [
        ("nGuiForcedStyle", ctypes.c_int32),
        ]

class cTkCurveType(ctypes.Structure):
     _fields_ = [
        ("curve", ctypes.c_int32),
        ]

class cTkNGuiGraphicStyleData(ctypes.Structure):
     _fields_ = [
        ("colour", common.Colour),
        ("iconColour", common.Colour),
        ("strokeColour", common.Colour),
        ("gradientColour", common.Colour),
        ("strokeGradientColour", common.Colour),
        ("paddingX", ctypes.c_float),
        ("paddingY", ctypes.c_float),
        ("marginX", ctypes.c_float),
        ("marginY", ctypes.c_float),
        ("gradientStartOffset", ctypes.c_float),
        ("gradientEndOffset", ctypes.c_float),
        ("cornerRadius", ctypes.c_float),
        ("strokeSize", ctypes.c_float),
        ("image", ctypes.c_int32),
        ("icon", ctypes.c_int32),
        ("desaturation", ctypes.c_float),
        ("strokeGradientOffset", ctypes.c_float),
        ("strokeGradientFeather", ctypes.c_float),
        ("shape", ctypes.c_int32),
        ("gradient", ctypes.c_int32),
        ("solidColour", ctypes.c_ubyte),
        ("hasDropShadow", ctypes.c_ubyte),
        ("hasOuterGradient", ctypes.c_ubyte),
        ("hasInnerGradient", ctypes.c_ubyte),
        ("gradientOffsetPercent", ctypes.c_ubyte),
        ("strokeGradient", ctypes.c_ubyte),
        ]

class cTkClassPointer(ctypes.Structure):
     _fields_ = [
        #("classData", cTkClassPointer.cTkClassPointerData),
        ("className", common.cTkFixedString[0x3F]),
        ("classFixed", ctypes.c_ubyte),
        ("classNameHash", ctypes.c_uint64),
        ]

class cTkNGuiGraphicStyle(ctypes.Structure):
     _fields_ = [
        ("default", cTkNGuiGraphicStyleData),
        ("highlight", cTkNGuiGraphicStyleData),
        ("active", cTkNGuiGraphicStyleData),
        ("customMinStart", common.Vector2f),
        ("customMaxStart", common.Vector2f),
        ("highlightTime", ctypes.c_float),
        ("highlightScale", ctypes.c_float),
        ("globalFade", ctypes.c_float),
        ("animTime", ctypes.c_float),
        ("animSplit", ctypes.c_float),
        ("animCurve1", cTkCurveType),
        ("animCurve2", cTkCurveType),
        ("animate", ctypes.c_int32),
        ("inheritStyleFromParentLayer", ctypes.c_ubyte),
        ]

class cGcNGuiElementData(ctypes.Structure):
     _fields_ = [
        ("ID", common.TkID[0x10]),
        ("presetID", common.TkID[0x10]),
        ("isHidden", ctypes.c_ubyte),
        ("forcedStyle", cTkNGuiForcedStyle),
        ("layout", cGcNGuiLayoutData),
        ]

class cTkBBox2d(ctypes.Structure):
     _fields_ = [
        ("min", common.Vector2f),
        ("max", common.Vector2f),
        ]


class cGcNGuiLayerData(ctypes.Structure):
     _fields_ = [
        ("elementData", cGcNGuiElementData),
        ("style", cTkNGuiGraphicStyle),
        ("image", common.cTkFixedString[0x80]),
        ("children", common.cTkDynamicArray[cTkClassPointer]),
        ("dataFilename", common.cTkFixedString[0x80]),
        ("altMode", ctypes.c_int32),
        ]

class cTkTextureStreamFuncs(ctypes.Structure):
    streamFunc: bytes
    streamDeleteFunc: bytes
    abortBakeFunc: bytes
    evictFunc: bytes
    beginProbeFunc: bytes
    completeProbeFunc: bytes
    gatherProbeFunc: bytes
    isVirtualTexture: bool

cTkTextureStreamFuncs._fields_ = [
    ("streamFunc", ctypes.c_ubyte * 0x8),
    ("streamDeleteFunc", ctypes.c_ubyte * 0x8),
    ("abortBakeFunc", ctypes.c_ubyte * 0x8),
    ("evictFunc", ctypes.c_ubyte * 0x8),
    ("beginProbeFunc", ctypes.c_ubyte * 0x8),
    ("completeProbeFunc", ctypes.c_ubyte * 0x8),
    ("gatherProbeFunc", ctypes.c_ubyte * 0x8),
    ("isVirtualTexture", ctypes.c_ubyte),
]

class cGcPlayer(ctypes.Structure):
    #position: cTkVector3 -> (common.Vector3f, common.Vector3f)
    #controller: _Pointer["cGcPlayerController"]
    position: common.Vector3f
    running: bool
    stamina_state: int
    stamina: float
    #aimToggleActive: bool
    #aimBeingHeld: bool

    """ 
       {
    "name": "mpController",
    "type": "cGcPlayerController *",
    "offset": 456,
    "size": 8
   },
    {
     "name": "mPosition",
     "type": "cTkVector3",
     "offset": 592,
     "size": 16
    },
    {
     "name": "mbRunning",
     "type": "bool",
     "offset": 12322,
     "size": 1
    },
    {
     "name": "mbMoving",
     "type": "bool",
     "offset": 13085,
     "size": 1
    },
    {
     "name": "mfFreeSprintTimer",
     "type": "float",
     "offset": 13268,
     "size": 4
    },
    {
     "name": "mfFreeSprintDuration",
     "type": "float",
     "offset": 13272,
     "size": 4
    },
    {
     "name": "mbSprintIsFree",
     "type": "bool",
     "offset": 13276,
     "size": 1
    },
    {
     "name": "meStaminaState",
     "type": "cGcPlayer::eStaminaState",
     "offset": 21388,
     "size": 4
    },
        {
     "name": "mfStamina",
     "type": "float",
     "offset": 21392,
     "size": 4
    },
    {
     "name": "mbAimToggleActive",
     "type": "bool",
     "offset": 21772,
     "size": 1
    },
    {
     "name": "mbAimBeingHeld",
     "type": "bool",
     "offset": 21774,
     "size": 1
    }, """
         
cGcPlayer._fields_ = [
    ("_padding0", ctypes.c_ubyte * 592), #456),
    #("controller", ctypes.POINTER(cGcPlayerController)),
    #("_padding1", ctypes.c_ubyte * 144), 
    ("position", common.Vector3f),
    ("_padding2", ctypes.c_ubyte * 11714), 
    ("running", ctypes.c_ubyte),
    ("_padding3", ctypes.c_ubyte* 9065),
    ("stamina_state", ctypes.c_int32),
    ("stamina", ctypes.c_float),
    #("_padding4", ctypes.c_ubyte * 376),
    #("aimToggleActive", ctypes.c_ubyte),
    #("_padding5", ctypes.c_ubyte),
    #("aimBeingHeld", ctypes.c_ubyte),
]

class cTkTextureBase(ctypes.Structure):
    type: ctypes.c_int32
    format: std.array[ctypes.c_uint8, 0x1]
    textureAddressMode: ctypes.c_int32
    textureFilterMode: ctypes.c_int32
    textureReductionMode: ctypes.c_int32
    isSRGB: bool
    isShadowMap: bool
    width: int
    height: int
    depth: int
    numMips: int
    anisotropy: int
    dataSize: int
    memorySize: int
    mipStatsCounterIndex: std.array[ctypes.c_int16, 0x4]
    finestResidentPixelCount: int
    finestMipVisible: int
    numClampedPixels: int
    lastFetchedFrame: int
    fileStartOffset: int
    streamFuncs: _Pointer["cTkTextureStreamFuncs"]
    streamFuncContext: int
    mipZeroSize: int
    evictedSize: int
    evictableMips: int
    evictedMips: int
    allocatedFromStreamingStore: bool
    allocatedWithMipBias: bool
    evictionCountdown: int

cTkTextureBase._fields_ = [
    ("type", ctypes.c_int32),
    ("format", std.array[ctypes.c_uint8, 0x1]),
    ("textureAddressMode", ctypes.c_int32),
    ("textureFilterMode", ctypes.c_int32),
    ("textureReductionMode", ctypes.c_int32),
    ("isSRGB", ctypes.c_ubyte),
    ("isShadowMap", ctypes.c_ubyte),
    ("width", ctypes.c_int32),
    ("height", ctypes.c_int32),
    ("depth", ctypes.c_int32),
    ("numMips", ctypes.c_int16),
    ("anisotropy", ctypes.c_int16),
    ("dataSize", ctypes.c_int32),
    ("memorySize", ctypes.c_int32),
    ("mipStatsCounterIndex", std.array[ctypes.c_int16, 0x4]),
    ("finestResidentPixelCount", ctypes.c_int32),
    ("finestMipVisible", ctypes.c_int32),
    ("numClampedPixels", ctypes.c_int32),
    ("lastFetchedFrame", ctypes.c_int32),
    ("fileStartOffset", ctypes.c_int32),
    ("streamFuncs", ctypes.POINTER(cTkTextureStreamFuncs)),
    ("streamFuncContext", ctypes.c_void_p),
    ("mipZeroSize", ctypes.c_int32),
    ("evictedSize", ctypes.c_int32),
    ("evictableMips", ctypes.c_int16),
    ("evictedMips", ctypes.c_int16),
    ("allocatedFromStreamingStore", ctypes.c_ubyte),
    ("allocatedWithMipBias", ctypes.c_ubyte),
    ("evictionCountdown", ctypes.c_uint8),
]

class ITkNGuiDraggable_vtbl(ctypes.Structure):
    Render: bytes
    GetType: bytes

ITkNGuiDraggable_vtbl._fields_ = [
    ("Render", ctypes.c_ubyte * 0x8),
    ("GetType", ctypes.c_ubyte * 0x8),
]

class ITkNGuiDraggable(ctypes.Structure):
    __vftable: _Pointer["ITkNGuiDraggable_vtbl"]

ITkNGuiDraggable._fields_ = [
    ("__vftable", ctypes.POINTER(ITkNGuiDraggable_vtbl)),
]

class cGcNGuiElement:
  class sGcNGuiElementAnimSettings(ctypes.Structure):
    _bf_0: int

cGcNGuiElement.sGcNGuiElementAnimSettings._fields_ = [
    ("_bf_0", ctypes.c_int8),
]

class cGcNGuiLayer(cGcNGuiElement, ctypes.Structure):
    elements: std.vector[_Pointer["cGcNGuiElement"]]
    layerElements: std.vector[_Pointer["cGcNGuiLayer"]]
    pinnedPositions: std.vector[common.Vector2f]
    previousGraphicsStyle: "cTkNGuiGraphicStyleData"
    renderFunction: bytes
    renderFunctionData: int
    layerData: _Pointer["cGcNGuiLayerData"]
    elementHashTable: bytes
    uniqueID: int
    expanded: bool

class cGcNGuiElement(ITkNGuiDraggable, ctypes.Structure):
        _fields_ = [
            ("contentBBox", cTkBBox2d),
            ("parallaxOffset", common.Vector2f),
            ("undoMoveEvent", ctypes.c_ubyte * 0x8),
            ("undoResizeEvent", ctypes.c_ubyte * 0x8),
            ("undoLayoutEvent", ctypes.c_ubyte * 0x8),
            ("parent", ctypes.POINTER(cGcNGuiLayer)),
            ("elementData", ctypes.POINTER(cGcNGuiElementData)),
            ("inputThisFrame", ctypes.c_int32),
            ("layoutChangeEvent", ctypes.c_int32),
            ("requestAnim", ctypes.c_int32),
            ("anim", cGcNGuiElement.sGcNGuiElementAnimSettings),
        ]
        contentBBox: "cTkBBox2d"
        parallaxOffset: common.Vector2f
        undoMoveEvent: bytes
        undoResizeEvent: bytes
        undoLayoutEvent: bytes
        parent: _Pointer["cGcNGuiLayer"]
        elementData: _Pointer["cGcNGuiElementData"]
        inputThisFrame: ctypes.c_int32
        layoutChangeEvent: ctypes.c_int32
        requestAnim: ctypes.c_int32
        anim: "cGcNGuiElement.sGcNGuiElementAnimSettings"


cGcNGuiLayer._fields_ = [
        ("elements",std.vector[ctypes.POINTER(cGcNGuiElement)]),
        ("layerElements",std.vector[ctypes.POINTER(cGcNGuiLayer)]),
        ("pinnedPositions",std.vector[common.Vector2f]),
        ("previousGraphicsStyle",cTkNGuiGraphicStyleData),
        ("renderFunction",ctypes.c_ubyte * 0x8),
        ("renderFunctionData",ctypes.c_void_p),
        ("layerData",ctypes.POINTER(cGcNGuiLayerData)),
        ("elementHashTable",ctypes.c_ubyte * 0x8),
        ("uniqueID",ctypes.c_uint64),
        ("expanded",ctypes.c_ubyte),
    ]

class cTk2dObject_vtbl(ctypes.Structure):
     _fields_ = [
        ("Construct", ctypes.c_ubyte * 0x8),
        ("Prepare", ctypes.c_ubyte * 0x8),
        ("Update", ctypes.c_ubyte * 0x8),
        ("Render", ctypes.c_ubyte * 0x8),
        ("Release", ctypes.c_ubyte * 0x8),
        ("Destruct", ctypes.c_ubyte * 0x8),
        ("SetPosition", ctypes.c_ubyte * 0x8),
        ("GetPosition", ctypes.c_ubyte * 0x8),
        ("GetPosition_40", ctypes.c_ubyte * 0x8),
        ("GetWorldTopLeft", ctypes.c_ubyte * 0x8),
        ("SetSize", ctypes.c_ubyte * 0x8),
        ("GetSize", ctypes.c_ubyte * 0x8),
        ("SetColour", ctypes.c_ubyte * 0x8),
        ("GetColour", ctypes.c_ubyte * 0x8),
        ("SetAlignment", ctypes.c_ubyte * 0x8),
        ("GetAlignment", ctypes.c_ubyte * 0x8),
        ("RemoveAllObjects", ctypes.c_ubyte * 0x8),
        ]

class cTk2dObject(ctypes.Structure):
    __vftable: _Pointer["cTk2dObject_vtbl"]
    colour: common.Colour
    position: common.Vector2f
    size: common.Vector2f
    alignment: common.Vector2f
    nextSibling: _Pointer["cTk2dObject"]

cTk2dObject._fields_ = [
        ("__vftable", ctypes.POINTER(cTk2dObject_vtbl)),
        ("colour", common.Colour),
        ("position", common.Vector2f),
        ("size", common.Vector2f),
        ("alignment", common.Vector2f),
        ("nextSibling", ctypes.POINTER(cTk2dObject)),
        ]

class cGcNGuiLayer(cGcNGuiElement, ctypes.Structure):
    elements: std.vector[_Pointer["cGcNGuiElement"]]
    layerElements: std.vector[_Pointer["cGcNGuiLayer"]]
    pinnedPositions: std.vector[common.Vector2f]
    previousGraphicsStyle: "cTkNGuiGraphicStyleData"
    renderFunction: bytes
    renderFunctionData: int
    layerData: _Pointer["cGcNGuiLayerData"]
    elementHashTable: bytes
    uniqueID: int
    expanded: bool
     
cGcNGuiLayer._fields_ = [
    ("elements", std.vector[ctypes.POINTER(cGcNGuiElement)]),
    ("layerElements", std.vector[ctypes.POINTER(cGcNGuiLayer)]),
    ("pinnedPositions", std.vector[common.Vector2f]),
    ("previousGraphicsStyle", cTkNGuiGraphicStyleData),
    ("renderFunction", ctypes.c_ubyte * 0x8),
    ("renderFunctionData", ctypes.c_void_p),
    ("layerData", ctypes.POINTER(cGcNGuiLayerData)),
    ("elementHashTable", ctypes.c_ubyte * 0x8),
    ("uniqueID", ctypes.c_uint64),
    ("expanded", ctypes.c_ubyte),
]

class cTkSmartResHandle(ctypes.Structure):
     _fields_ = [
        ("internalHandle", ctypes.c_ubyte * 0x4),
        ]

class VkExtent3D(ctypes.Structure):
     _fields_ = [
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("depth", ctypes.c_uint32),
        ]

class TkDeviceMemory(ctypes.Structure):
     _fields_ = [
        ("alloc", ctypes.c_ubyte * 0x8), #ctypes.POINTER(VmaAllocation_T)),
        ("memory", ctypes.c_ubyte * 0x8), #ctypes.POINTER("struct VkDeviceMemory_T")),
        ("offset", ctypes.c_uint64),
        ]

class cTkNGuiGraphicStyleData(ctypes.Structure):
     _fields_ = [
        ("colour", common.Colour),
        ("iconColour", common.Colour),
        ("strokeColour", common.Colour),
        ("gradientColour", common.Colour),
        ("strokeGradientColour", common.Colour),
        ("paddingX", ctypes.c_float),
        ("paddingY", ctypes.c_float),
        ("marginX", ctypes.c_float),
        ("marginY", ctypes.c_float),
        ("gradientStartOffset", ctypes.c_float),
        ("gradientEndOffset", ctypes.c_float),
        ("cornerRadius", ctypes.c_float),
        ("strokeSize", ctypes.c_float),
        ("image", ctypes.c_int32),
        ("icon", ctypes.c_int32),
        ("desaturation", ctypes.c_float),
        ("strokeGradientOffset", ctypes.c_float),
        ("strokeGradientFeather", ctypes.c_float),
        ("shape", ctypes.c_int32),
        ("gradient", ctypes.c_int32),
        ("solidColour", ctypes.c_ubyte),
        ("hasDropShadow", ctypes.c_ubyte),
        ("hasOuterGradient", ctypes.c_ubyte),
        ("hasInnerGradient", ctypes.c_ubyte),
        ("gradientOffsetPercent", ctypes.c_ubyte),
        ("strokeGradient", ctypes.c_ubyte),
    ]

class cTkTexture(cTkTextureBase, ctypes.Structure):
     _fields_ = [
        ("textureData", ctypes.c_void_p),
        ("texture", ctypes.c_ubyte * 0x8),
        ("imageDesc", VkImageCreateInfo),
        ("textureMemory", TkDeviceMemory),
        ("textureSrvMips", ctypes.c_ubyte * 0x8), #std.array[ctypes.POINTER("struct VkImageView_T"), 0xE]),
        ("resourceState", std.array[ctypes.c_int32, 0xE]),
        ("depthOnly", ctypes.c_ubyte),
        ("textureSrv", ctypes.c_ubyte * 0x8),
        ("textureUav", ctypes.c_ubyte * 0x8), #ctypes.POINTER("struct VkImageView_T")),
        ("sampler", ctypes.c_ubyte * 0x8),
        ("lodClamp", ctypes.c_float),
        ("mapping", ctypes.POINTER(ctypes.c_uint16)),
        ("evictableMipPageCount", std.array[ctypes.c_uint16, 0x10]),
        ("mipStartPage", std.array[ctypes.c_uint16, 0x10]),
        ("tailOffset", ctypes.c_uint64),
        ("tailArrayStride", ctypes.c_uint64),
        ("ultraMips", ctypes.c_uint16),
        ("detailableMips", ctypes.c_uint16),
        ("lodBias", ctypes.c_float),
        ("numPages", ctypes.c_int32),
        ("evictedPages", ctypes.c_int32),
        ("mipZeroPages", ctypes.c_int16),
        ("mipZeroUnusedPages", ctypes.c_int16),
        ("isPartiallyResident", ctypes.c_ubyte),
    ]   

class cTkDynamicTexture(ctypes.Structure):
    _fields_ = [
        ("renderTarget", cTkSmartResHandle),
        ("width", ctypes.c_int32),
        ("height", ctypes.c_int32),
    ]

class cTk2dImage(ctypes.Structure):
    _fields_ = [
        ("uVs",std.array[common.Vector2f, 0x4]),
        ("texture",ctypes.POINTER(cTkTexture)),
        ("dynamicTexture",ctypes.POINTER(cTkDynamicTexture)),
        ("textureMipLevel",ctypes.c_float),
        ("visible",ctypes.c_ubyte),
        ("tiledUV",ctypes.c_ubyte),
        ("isRenderTarget",ctypes.c_ubyte),
    ] 
"""     uVs: cTkVector2[4] -> (std.array[common.Vector2f, 0x4], std.array[common.Vector2f, 0x4])
    texture: cTkTexture * -> (ctypes.POINTER(cTkTexture), _Pointer[cTkTexture])
    dynamicTexture: cTkDynamicTexture * -> (ctypes.POINTER(cTkDynamicTexture), _Pointer[cTkDynamicTexture])
    textureMipLevel: float -> (ctypes.c_float, float)
    visible: bool -> (ctypes.c_ubyte, bool)
    tiledUV: bool -> (ctypes.c_ubyte, bool)
    isRenderTarget: bool -> (ctypes.c_ubyte, bool) """

class cTk2dLayer(ctypes.Structure):
    _fields_ = [
        ("bitArray",common.cTkBitArray[ctypes.c_uint64, 512]),
        ("blendMode",ctypes.c_int32),
        ("firstChild",ctypes.POINTER(cTk2dObject)),
        ("isVisible",ctypes.c_ubyte),
        ("dynamicSize",ctypes.c_ubyte),
        ("scale",common.Vector2f),
        ("angle",ctypes.c_float),
    ]

class cTk3dLayer(ctypes.Structure):
    _fields_ = [
        ("worldPosition",common.Vector3f),
        ("screenPosition",common.Vector4f),
        ("screenPositionLeft",common.Vector4f),
        ("screenPositionRight",common.Vector4f),
        ("screenDepth",ctypes.c_float),
        ("defaultDistToCamera",ctypes.c_float),
        ("minScale",ctypes.c_float),
        ("maxScale",ctypes.c_float),
        ("testZ",ctypes.c_int32),
        ("enable3d",ctypes.c_ubyte),
        ("scale3d",ctypes.c_ubyte),
    ]

""" class cGcStatusMessageDefinitions(ctypes.Structure):
    messages: common.cTkDynamicArray[cGcStatusMessageDefinition]
    missionMarkupColour: common.Colour
    petVocabulary: bytes
    petChatTemplates: bytes
    friendlyDroneChatTemplates: bytes

cGcStatusMessageDefinitions._fields_ = [
    ("messages", common.cTkDynamicArray[cGcStatusMessageDefinition]),
    ("missionMarkupColour", common.Colour),
    ("petVocabulary", ctypes.c_ubyte * 0x348),
    ("petChatTemplates", ctypes.c_ubyte * 0x498),
    ("friendlyDroneChatTemplates", ctypes.c_ubyte * 0xA0),
] """

""" class cGcNGui(ctypes.Structure):
    _fields_ = [
        ("root", cGcNGuiLayer),
        ("input", cTkNGuiInput),
        ("useInput", ctypes.c_ubyte),
        ("pixelatio", ctypes.c_float),
        ("fullscreen", ctypes.c_byte),
        ("customSize", common.Vector2f),
        ("hasCustomSize", ctypes.c_byte),
        ("isInWorld", ctypes.c_ubyte),
        ("tk3dLayer", cTk3dLayer),
        ("tk2dImage", cTk2dImage),    
    ]  """

class cGcPlayerHUD(ctypes.Structure):
    _fields_ = [
        ("lPosition", common.Vector3f), #cTkVector3
    ]
    lPosition: common.Vector3f

class cGcBinoculars(ctypes.Structure):
    MarkerModel: common.TkHandle
    BinocularMarkerGui: _Pointer["cGcNGui"] 
    DiscoveryGui: _Pointer["cGcNGui"]

cGcBinoculars._fields_ = [
    ("_padding0", ctypes.c_ubyte * 1912),
    ("MarkerModel", common.TkHandle),
    ("_padding1912", ctypes.c_ubyte * 84),
    ("BinocularMarkerGui", ctypes.POINTER(cGcNGui)),
    ("DiscoveryGui", ctypes.POINTER(cGcNGui)),
]

