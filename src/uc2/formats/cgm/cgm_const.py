# -*- coding: utf-8 -*-
#
#  Copyright (C) 2017-2019 by Igor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from uc2 import sk2const

CGM_SIGNATURE = 0x0020

_reserved = 'Reserved for future'

CGM_CLS = {
    0: 'Delimiter elements',
    1: 'Metafile Descriptor elements',
    2: 'Picture Descriptor elements',
    3: 'Control elements',
    4: 'Graphical Primitive elements',
    5: 'Attribute elements',
    6: 'Escape element',
    7: 'External elements',
    8: 'Segment Control/Attribute',
    9: 'Application Struct. Descriptor',
    10: _reserved,
    11: _reserved,
    12: _reserved,
    13: _reserved,
    14: _reserved,
    15: _reserved,
}

NOOP = 0x0000
BEGIN_METAFILE = 0x0020
END_METAFILE = 0x0040
BEGIN_PICTURE = 0x0060
BEGIN_PICTURE_BODY = 0x0080
END_PICTURE = 0x00A0
BEGIN_SEGMENT = 0x00C0
END_SEGMENT = 0x00E0
BEGIN_FIGURE = 0x0100
END_FIGURE = 0x0120
BEGIN_PROTECTION_REGION = 0x01A0
END_PROTECTION_REGION = 0x01C0
BEGIN_COMPOUND_LINE = 0x01E0
END_COMPOUND_LINE = 0x0200
BEGIN_COMPOUND_TEXT_PATH = 0x0220
END_COMPOUND_TEXT_PATH = 0x0240
BEGIN_TILE_ARRAY = 0x0260
END_TILE_ARRAY = 0x0280
BEGIN_APPLICATION_STRUCTURE = 0x02A0
BEGIN_APPLICATION_STRUCTURE_BODY = 0x02C0
END_APPLICATION_STRUCTURE = 0x02E0
METAFILE_VERSION = 0x1020
METAFILE_DESCRIPTION = 0x1040
VDC_TYPE = 0x1060
INTEGER_PRECISION = 0x1080
REAL_PRECISION = 0x10A0
INDEX_PRECISION = 0x10C0
COLOUR_PRECISION = 0x10E0
COLOUR_INDEX_PRECISION = 0x1100
MAXIMUM_COLOUR_INDEX = 0x1120
COLOUR_VALUE_EXTENT = 0x1140
METAFILE_ELEMENT_LIST = 0x1160
METAFILE_DEFAULTS_REPLACEMENT = 0x1180
FONT_LIST = 0x11A0
CHARACTER_SET_LIST = 0x11C0
CHARACTER_CODING_ANNOUNCER = 0x11E0
NAME_PRECISION = 0x1200
MAXIMUM_VDC_EXTENT = 0x1220
SEGMENT_PRIORITY_EXTENT = 0x1240
COLOUR_MODEL = 0x1260
COLOUR_CALIBRATION = 0x1280
FONT_PROPERTIES = 0x12A0
GLYPH_MAPPING = 0x12C0
SYMBOL_LIBRARY_LIST = 0x12E0
PICTURE_DIRECTORY = 0x1300
SCALING_MODE = 0x2020
COLOUR_SELECTION_MODE = 0x2040
LINE_WIDTH_SPECIFICATION_MODE = 0x2060
MARKER_SIZE_SPECIFICATION_MODE = 0x2080
EDGE_WIDTH_SPECIFICATION_MODE = 0x20A0
VDC_EXTENT = 0x20C0
BACKGROUND_COLOUR = 0x20E0
DEVICE_VIEWPORT = 0x2100
DEVICE_VIEWPORT_SPECIFICATION_MODE = 0x2120
DEVICE_VIEWPORT_MAPPING = 0x2140
LINE_REPRESENTATION = 0x2160
MARKER_REPRESENTATION = 0x2180
TEXT_REPRESENTATION = 0x21A0
FILL_REPRESENTATION = 0x21C0
EDGE_REPRESENTATION = 0x21E0
INTERIOR_STYLE_SPECIFICATION_MODE = 0x2200
LINE_AND_EDGE_TYPE_DEFINITION = 0x2220
HATCH_STYLE_DEFINITION = 0x2240
GEOMETRIC_PATTERN_DEFINITION = 0x2260
APPLICATION_STRUCTURE_DIRECTORY = 0x2280
VDC_INTEGER_PRECISION = 0x3020
VDC_REAL_PRECISION = 0x3040
AUXILIARY_COLOUR = 0x3060
TRANSPARENCY = 0x3080
CLIP_RECTANGLE = 0x30A0
CLIP_INDICATOR = 0x30C0
LINE_CLIPPING_MODE = 0x30E0
MARKER_CLIPPING_MODE = 0x3100
EDGE_CLIPPING_MODE = 0x3120
NEW_REGION = 0x3140
SAVE_PRIMITIVE_CONTEXT = 0x3160
RESTORE_PRIMITIVE_CONTEXT = 0x3180
PROTECTION_REGION_INDICATOR = 0x3220
GENERALIZED_TEXT_PATH_MODE = 0x3240
MITRE_LIMIT = 0x3260
TRANSPARENT_CELL_COLOUR = 0x3280
POLYLINE = 0x4020
DISJOINT_POLYLINE = 0x4040
POLYMARKER = 0x4060
TEXT = 0x4080
RESTRICTED_TEXT = 0x40A0
APPEND_TEXT = 0x40C0
POLYGON = 0x40E0
POLYGON_SET = 0x4100
CELL_ARRAY = 0x4120
GENERALIZED_DRAWING_PRIMITIVE = 0x4140
RECTANGLE = 0x4160
CIRCLE = 0x4180
CIRCULAR_ARC_3_POINT = 0x41A0
CIRCULAR_ARC_3_POINT_CLOSE = 0x41C0
CIRCULAR_ARC_CENTRE = 0x41E0
CIRCULAR_ARC_CENTRE_CLOSE = 0x4200
ELLIPSE = 0x4220
ELLIPTICAL_ARC = 0x4240
ELLIPTICAL_ARC_CLOSE = 0x4260
CIRCULAR_ARC_CENTRE_REVERSED = 0x4280
CONNECTING_EDGE = 0x42A0
HYPERBOLIC_ARC = 0x42C0
PARABOLIC_ARC = 0x42E0
NON_UNIFORM_B_SPLINE = 0x4300
NON_UNIFORM_RATIONAL_B_SPLINE = 0x4320
POLYBEZIER = 0x4340
POLYSYMBOL = 0x4360
BITONAL_TILE = 0x4380
TILE = 0x43A0
LINE_BUNDLE_INDEX = 0x5020
LINE_TYPE = 0x5040
LINE_WIDTH = 0x5060
LINE_COLOUR = 0x5080
MARKER_BUNDLE_INDEX = 0x50A0
MARKER_TYPE = 0x50C0
MARKER_SIZE = 0x50E0
MARKER_COLOUR = 0x5100
TEXT_BUNDLE_INDEX = 0x5120
TEXT_FONT_INDEX = 0x5140
TEXT_PRECISION = 0x5160
CHARACTER_EXPANSION_FACTOR = 0x5180
CHARACTER_SPACING = 0x51A0
TEXT_COLOUR = 0x51C0
CHARACTER_HEIGHT = 0x51E0
CHARACTER_ORIENTATION = 0x5200
TEXT_PATH = 0x5220
TEXT_ALIGNMENT = 0x5240
CHARACTER_SET_INDEX = 0x5260
ALTERNATE_CHARACTER_SET_INDEX = 0x5280
FILL_BUNDLE_INDEX = 0x52A0
INTERIOR_STYLE = 0x52C0
FILL_COLOUR = 0x52E0
HATCH_INDEX = 0x5300
PATTERN_INDEX = 0x5320
EDGE_BUNDLE_INDEX = 0x5340
EDGE_TYPE = 0x5360
EDGE_WIDTH = 0x5380
EDGE_COLOUR = 0x53A0
EDGE_VISIBILITY = 0x53C0
FILL_REFERENCE_POINT = 0x53E0
PATTERN_TABLE = 0x5400
PATTERN_SIZE = 0x5420
COLOUR_TABLE = 0x5440
ASPECT_SOURCE_FLAGS = 0x5460
PICK_IDENTIFIER = 0x5480
LINE_CAP = 0x54A0
LINE_JOIN = 0x54C0
LINE_TYPE_CONTINUATION = 0x54E0
LINE_TYPE_INITIAL_OFFSET = 0x5500
TEXT_SCORE_TYPE = 0x5520
RESTRICTED_TEXT_TYPE = 0x5540
INTERPOLATED_INTERIOR = 0x5560
EDGE_CAP = 0x5580
EDGE_JOIN = 0x55A0
EDGE_TYPE_CONTINUATION = 0x55C0
EDGE_TYPE_INITIAL_OFFSET = 0x55E0
SYMBOL_LIBRARY_INDEX = 0x5600
SYMBOL_COLOUR = 0x5620
SYMBOL_SIZE = 0x5640
SYMBOL_ORIENTATION = 0x5660
ESCAPE = 0x6020
MESSAGE = 0x7020
APPLICATION_DATA = 0x7040
COPY_SEGMENT = 0x8020
INHERITANCE_FILTER = 0x8040
CLIP_INHERITANCE = 0x8060
SEGMENT_TRANSFORMATION = 0x8080
SEGMENT_HIGHLIGHTING = 0x80A0
SEGMENT_DISPLAY_PRIORITY = 0x80C0
SEGMENT_PICK_PRIORITY = 0x80E0
APPLICATION_STRUCTURE_ATTRIBUTE = 0x9020

CGM_ID = {
    0x0000: 'noop',
    0x0020: 'BEGIN METAFILE',
    0x0040: 'END METAFILE',
    0x0060: 'BEGIN PICTURE',
    0x0080: 'BEGIN PICTURE BODY',
    0x00A0: 'END PICTURE',
    0x00C0: 'BEGIN SEGMENT',
    0x00E0: 'END SEGMENT',
    0x0100: 'BEGIN FIGURE',
    0x0120: 'END FIGURE',
    0x01A0: 'BEGIN PROTECTION REGION',
    0x01C0: 'END PROTECTION REGION',
    0x01E0: 'BEGIN COMPOUND LINE',
    0x0200: 'END COMPOUND LINE',
    0x0220: 'BEGIN COMPOUND TEXT PATH',
    0x0240: 'END COMPOUND TEXT PATH',
    0x0260: 'BEGIN TILE ARRAY',
    0x0280: 'END TILE ARRAY',
    0x02A0: 'BEGIN APPLICATION STRUCTURE',
    0x02C0: 'BEGIN APPLICATION STRUCTURE BODY',
    0x02E0: 'END APPLICATION STRUCTURE',
    0x1020: 'METAFILE VERSION',
    0x1040: 'METAFILE DESCRIPTION',
    0x1060: 'VDC TYPE',
    0x1080: 'INTEGER PRECISION',
    0x10A0: 'REAL PRECISION',
    0x10C0: 'INDEX PRECISION',
    0x10E0: 'COLOUR PRECISION',
    0x1100: 'COLOUR INDEX PRECISION',
    0x1120: 'MAXIMUM COLOUR INDEX',
    0x1140: 'COLOUR VALUE EXTENT',
    0x1160: 'METAFILE ELEMENT LIST',
    0x1180: 'METAFILE DEFAULTS REPLACEMENT',
    0x11A0: 'FONT LIST',
    0x11C0: 'CHARACTER SET LIST',
    0x11E0: 'CHARACTER CODING ANNOUNCER',
    0x1200: 'NAME PRECISION',
    0x1220: 'MAXIMUM VDC EXTENT',
    0x1240: 'SEGMENT PRIORITY EXTENT',
    0x1260: 'COLOUR MODEL',
    0x1280: 'COLOUR CALIBRATION',
    0x12A0: 'FONT PROPERTIES',
    0x12C0: 'GLYPH MAPPING',
    0x12E0: 'SYMBOL LIBRARY LIST',
    0x1300: 'PICTURE DIRECTORY',
    0x2020: 'SCALING MODE',
    0x2040: 'COLOUR SELECTION MODE',
    0x2060: 'LINE WIDTH SPECIFICATION MODE',
    0x2080: 'MARKER SIZE SPECIFICATION MODE',
    0x20A0: 'EDGE WIDTH SPECIFICATION MODE',
    0x20C0: 'VDC EXTENT',
    0x20E0: 'BACKGROUND COLOUR',
    0x2100: 'DEVICE VIEWPORT',
    0x2120: 'DEVICE VIEWPORT SPECIFICATION MODE',
    0x2140: 'DEVICE VIEWPORT MAPPING',
    0x2160: 'LINE REPRESENTATION',
    0x2180: 'MARKER REPRESENTATION',
    0x21A0: 'TEXT REPRESENTATION',
    0x21C0: 'FILL REPRESENTATION',
    0x21E0: 'EDGE REPRESENTATION',
    0x2200: 'INTERIOR STYLE SPECIFICATION MODE',
    0x2220: 'LINE AND EDGE TYPE DEFINITION',
    0x2240: 'HATCH STYLE DEFINITION',
    0x2260: 'GEOMETRIC PATTERN DEFINITION',
    0x2280: 'APPLICATION STRUCTURE DIRECTORY',
    0x3020: 'VDC INTEGER PRECISION',
    0x3040: 'VDC REAL PRECISION',
    0x3060: 'AUXILIARY COLOUR',
    0x3080: 'TRANSPARENCY',
    0x30A0: 'CLIP RECTANGLE',
    0x30C0: 'CLIP INDICATOR',
    0x30E0: 'LINE CLIPPING MODE',
    0x3100: 'MARKER CLIPPING MODE',
    0x3120: 'EDGE CLIPPING MODE',
    0x3140: 'NEW REGION',
    0x3160: 'SAVE PRIMITIVE CONTEXT',
    0x3180: 'RESTORE PRIMITIVE CONTEXT',
    0x3220: 'PROTECTION REGION INDICATOR',
    0x3240: 'GENERALIZED TEXT PATH MODE',
    0x3260: 'MITRE LIMIT',
    0x3280: 'TRANSPARENT CELL COLOUR',
    0x4020: 'POLYLINE',
    0x4040: 'DISJOINT POLYLINE',
    0x4060: 'POLYMARKER',
    0x4080: 'TEXT',
    0x40A0: 'RESTRICTED TEXT',
    0x40C0: 'APPEND TEXT',
    0x40E0: 'POLYGON',
    0x4100: 'POLYGON SET',
    0x4120: 'CELL ARRAY',
    0x4140: 'GENERALIZED DRAWING PRIMITIVE',
    0x4160: 'RECTANGLE',
    0x4180: 'CIRCLE',
    0x41A0: 'CIRCULAR ARC 3 POINT',
    0x41C0: 'CIRCULAR ARC 3 POINT CLOSE',
    0x41E0: 'CIRCULAR ARC CENTRE',
    0x4200: 'CIRCULAR ARC CENTRE CLOSE',
    0x4220: 'ELLIPSE',
    0x4240: 'ELLIPTICAL ARC',
    0x4260: 'ELLIPTICAL ARC CLOSE',
    0x4280: 'CIRCULAR ARC CENTRE REVERSED',
    0x42A0: 'CONNECTING EDGE',
    0x42C0: 'HYPERBOLIC ARC',
    0x42E0: 'PARABOLIC ARC',
    0x4300: 'NON-UNIFORM B-SPLINE',
    0x4320: 'NON-UNIFORM RATIONAL B-SPLINE',
    0x4340: 'POLYBEZIER',
    0x4360: 'POLYSYMBOL',
    0x4380: 'BITONAL TILE',
    0x43A0: 'TILE',
    0x5020: 'LINE BUNDLE INDEX',
    0x5040: 'LINE TYPE',
    0x5060: 'LINE WIDTH',
    0x5080: 'LINE COLOUR',
    0x50A0: 'MARKER BUNDLE INDEX',
    0x50C0: 'MARKER TYPE',
    0x50E0: 'MARKER SIZE',
    0x5100: 'MARKER COLOUR',
    0x5120: 'TEXT BUNDLE INDEX',
    0x5140: 'TEXT FONT INDEX',
    0x5160: 'TEXT PRECISION',
    0x5180: 'CHARACTER EXPANSION FACTOR',
    0x51A0: 'CHARACTER SPACING',
    0x51C0: 'TEXT COLOUR',
    0x51E0: 'CHARACTER HEIGHT',
    0x5200: 'CHARACTER ORIENTATION',
    0x5220: 'TEXT PATH',
    0x5240: 'TEXT ALIGNMENT',
    0x5260: 'CHARACTER SET INDEX',
    0x5280: 'ALTERNATE CHARACTER SET INDEX',
    0x52A0: 'FILL BUNDLE INDEX',
    0x52C0: 'INTERIOR STYLE',
    0x52E0: 'FILL COLOUR',
    0x5300: 'HATCH INDEX',
    0x5320: 'PATTERN INDEX',
    0x5340: 'EDGE BUNDLE INDEX',
    0x5360: 'EDGE TYPE',
    0x5380: 'EDGE WIDTH',
    0x53A0: 'EDGE COLOUR',
    0x53C0: 'EDGE VISIBILITY',
    0x53E0: 'FILL REFERENCE POINT',
    0x5400: 'PATTERN TABLE',
    0x5420: 'PATTERN SIZE',
    0x5440: 'COLOUR TABLE',
    0x5460: 'ASPECT SOURCE FLAGS',
    0x5480: 'PICK IDENTIFIER',
    0x54A0: 'LINE CAP',
    0x54C0: 'LINE JOIN',
    0x54E0: 'LINE TYPE CONTINUATION',
    0x5500: 'LINE TYPE INITIAL OFFSET',
    0x5520: 'TEXT SCORE TYPE',
    0x5540: 'RESTRICTED TEXT TYPE',
    0x5560: 'INTERPOLATED INTERIOR',
    0x5580: 'EDGE CAP',
    0x55A0: 'EDGE JOIN',
    0x55C0: 'EDGE TYPE CONTINUATION',
    0x55E0: 'EDGE TYPE INITIAL OFFSET',
    0x5600: 'SYMBOL LIBRARY INDEX',
    0x5620: 'SYMBOL COLOUR',
    0x5640: 'SYMBOL SIZE',
    0x5660: 'SYMBOL ORIENTATION',
    0x6020: 'ESCAPE',
    0x7020: 'MESSAGE',
    0x7040: 'APPLICATION DATA',
    0x8020: 'COPY SEGMENT',
    0x8040: 'INHERITANCE FILTER',
    0x8060: 'CLIP INHERITANCE',
    0x8080: 'SEGMENT TRANSFORMATION',
    0x80A0: 'SEGMENT HIGHLIGHTING',
    0x80C0: 'SEGMENT DISPLAY PRIORITY',
    0x80E0: 'SEGMENT PICK PRIORITY',
    0x9020: 'APPLICATION STRUCTURE ATTRIBUTE',
}

VDC_TYPE_INT = 0
VDC_TYPE_REAL = 1

LINE_DASHTABLE = ((), (4, 4), (1, 1), (4, 1, 1, 1), (4, 1, 1, 1, 1, 1))
VDC_INT_EXTEND = ((0, 0), (32767, 32767))
VDC_REAL_EXTEND = ((0.0, 0.0), (1.0, 1.0))
BLACK_COLOR = (0.0, 0.0, 0.0)
FIXED_REAL_PRECISION = 1
REAL_PRECISION_MAP = {
    (16, 16): 0,  # 32 bit fixed precision
    (32, 32): 1,  # 64 bit fixed precision
    (9, 23): 2,  # 32 bit floating point
    (12, 52): 3,  # 64 bit floating point
}

COLOR_PRECISION_MAP = {
    8: ">BBB",
    16: ">HHH",
    32: ">III",
}


COLOR_INDEX_PRECISION_MAP = {
    8: ">B",
    16: ">H",
    32: ">I",
}


def create_color_table(sz):
    mx = 1
    bs = 0
    while mx < sz:
        mx = mx * 2
        bs = bs + 1
    cb = bs / 3
    tb = bs % 3
    mc = (1 << (cb + tb)) - 1.0
    table = mx * [(0.0, 0.0, 0.0)]
    for i in range(mx):
        j = i + mx - 1
        j = j % mx
        red, grn, blu = 0, 0, 0
        for k in range(cb):
            red = (red << 1) + j % 2
            j = j >> 1
            grn = (grn << 1) + j % 2
            j = j >> 1
            blu = (blu << 1) + j % 2
            j = j >> 1
        tint = j
        red = (red << tb) + tint
        grn = (grn << tb) + tint
        blu = (blu << tb) + tint
        table[i] = (red / mc, grn / mc, blu / mc)
    return table


CGM_INIT = {
    'intprec': 1,  # 16 bits,
    'intsize': 2,
    'inxprec': 1,  # 16 bits,
    'inxsize': 2,
    'realprec': 0,  # 32 bits fixed point
    'realsize': 4,
    'color': {},
    'color.absstruct': ">BBB",
    'color.inxstruct': ">B",
    'color.mode': 0,
    'color.maxindex': 63,
    'color.table': create_color_table(64),
    'color.offset': (0.0, 0.0, 0.0),
    'color.scale': (255.0, 255.0, 255.0),
    'vdc': {},
    'vdc.type': 0,  # integers,
    'vdc.realprec': 0,  # 32 bits fixed point
    'vdc.realsize': 4,
    'vdc.intprec': 1,  # 16 bits,
    'vdc.intsize': 2,
    'vdc.prec': None,  # integers, 16 bit
    'vdc.size': None,
    'vdc.intextend': VDC_INT_EXTEND,
    'vdc.realextend': VDC_REAL_EXTEND,
    'vdc.extend': VDC_INT_EXTEND,
    'fill': {},
    'fill.type': 1,
    'fill.color': BLACK_COLOR,
    'line': {},
    'line.type': 1,
    'line.color': BLACK_COLOR,
    'line.widthmode': 0,
    'line.width': None,
    'line.dashtable': LINE_DASHTABLE,
    'edge': {},
    'edge.type': 1,
    'edge.color': BLACK_COLOR,
    'edge.widthmode': 0,
    'edge.width': None,
    'edge.dashtable': LINE_DASHTABLE,
    'edge.visible': 0,
    'fonts': [],
    'text': {},
    'text.fontindex': 0,
    'text.height': None,
    'text.expansion': 1.0,
    'text.spacing': 0.0,
    'text.orientation': ((0.0, 1.0), (1.0, 0.0)),  # Up , Base vector
    'text.path': 0,  # right
    'text.alignment': 1,
    'text.color': BLACK_COLOR,
    'marker': {},
    'marker.sizemode': 0,
    'marker.type': 3,
    'marker.size': None,
    'clip': {},
    'clip.mode': 1,
    'clip.rect': VDC_INT_EXTEND,
    'scale': {},
    'scale.mode': 0,  # abstract
    'scale.metric': 0.0,
}

TEXT_ALIGNMENT_MAP = {
    1: sk2const.TEXT_ALIGN_LEFT,
    2: sk2const.TEXT_ALIGN_CENTER,
    3: sk2const.TEXT_ALIGN_RIGHT,
}
