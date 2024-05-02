COLOR_CANVAS_DARK = "rgb(33,33,33)"
COLOR_CANVAS_LIGHT = "rgb(252, 252, 252)"
COLOR_PLOT_TEXT_LIGHT = "rgb(52, 49, 49)"
COLOR_PLOT_TEXT_DARK = "rgb(252, 252, 252)"
COLOR_ZERO_LINE_LIGHT = "green"
COLOR_ZERO_LINE_DARK = "limegreen"
COLOR_BEAM = "red"
COLOR_DETECTOR = "#D3D3D3"
COLOR_PAD = "slateblue"
COLOR_PATIENT = "#CE967C"
COLOR_SOURCE = "#D3D3D3"
COLOR_TABLE = "#D3D3D3"
COLOR_SLIDER_BACKGROUND = "red"
COLOR_SLIDER_BORDER_LIGHT = "rgb(252,252,252)"
COLOR_SLIDER_BORDER_DARK = "rgb(45,45,45)"
COLOR_SLIDER_TICK_LIGHT = "rgb(52, 49, 49)"
COLOR_SLIDER_TICK_DARK = "white"

COLOR_GRID_DARK = "rgb(99,99,99)"
COLOR_GRID_LIGHT = "rgb(99,99,99)"

COLOR_WIRE_FRAME_BEAM = "red"
COLOR_WIRE_FRAME_DETECTOR = "darkslategray"
COLOR_WIRE_FRAME_PAD = "#3f3f3f"
COLOR_WIRE_FRAME_TABLE = "#3f3f3f"

DATA_DS_IRP = "DSIRP"

KEY_PARAM_MODE = "mode"
KEY_PARAM_RDSR_FILENAME = "rdsr_filename"
KEY_PARAM_ESTIMATE_K_TAB = "estimate_k_tab"
KEY_PARAM_K_TAB_VAL = "k_tab_val"
KEY_PARAM_PHANTOM_MODEL = "model"
KEY_PARAM_HUMAN_MESH = "human_mesh"
KEY_PARAM_INHERENT_FILTRATION = "inherent_filtration"

DIMENSION_PLANE_LENGTH = "plane_length"
DIMENSION_PLANE_RESOLUTION = "plane_resolution"
DIMENSION_PLANE_WIDTH = "plane_width"

DIMENSION_CYLINDER_LENGTH = "cylinder_length"
DIMENSION_CYLINDER_RADII_A = "cylinder_radii_a"
DIMENSION_CYLINDER_RADII_B = "cylinder_radii_b"
DIMENSION_CYLINDER_RESOLUTION = "cylinder_resolution"

DIMENSION_TABLE_LENGTH = "table_length"
DIMENSION_TABLE_WIDTH = "table_width"
DIMENSION_TABLE_THICKNESS = "table_thickness"

DIMENSION_PAD_LENGTH = "pad_length"
DIMENSION_PAD_WIDTH = "pad_width"
DIMENSION_PAD_THICKNESS = "pad_thickness"

DIMENSION_UNIT_KEY = "unit"
DIMENSION_UNIT_CM = "cm"

FIELD_SIZE_MODE_ACTUAL_SHUTTER_DISTANCE = "ASD"
FIELD_SIZE_MODE_COLLIMATED_FIELD_AREA = "CFA"

KEY_RDSR_ACQUISITION_DATA = "AcquisitionData"
KEY_RDSR_COMMENT = "Comment"
KEY_RDSR_CONCEPT_CODE_SEQUENCE = "ConceptCodeSequence"
KEY_RDSR_CONTENT_SEQUENCE = "ContentSequence"
KEY_RDSR_DATE_TIME = "DateTime"
KEY_RDSR_DETECTORSIZE_MM = "DetectorSize_mm"
KEY_RDSR_EVENT_XRAY_DATA = "Irradiation Event X-Ray Data"
KEY_RDSR_II_DIAMETER_SRDATA = "iiDiameter SRData"
KEY_RDSR_MANUFACTURER = "Manufacturer"
KEY_RDSR_MANUFACTURER_MODEL_NAME = "ManufacturerModelName"
KEY_RDSR_MEASURED_VALUE_SEQUENCE = "MeasuredValueSequence"
KEY_RDSR_TEXT_VALUE = "TextValue"
KEY_RDSR_UID = "UID"
KEY_RDSR_FILTER_MATERIAL_COPPER = "Copper or Copper compound"
KEY_RDSR_FILTER_MATERIAL_ALUMINUM = "Aluminum or Aluminum compound"
KEY_RDSR_FILTER_MIN = "XRayFilterThicknessMinimum_mm"
KEY_RDSR_FILTER_MAX = "XRayFilterThicknessMaximum_mm"
KEY_RDSR_FILTER_MATERIAL = "XRayFilterMaterial"
KEY_RDSR_FILTER_TYPE = "XRayFilterType"
KEY_RDSR_DISTANCE_SOURCE_DETECTOR = "DistanceSourcetoDetector_mm"

KEY_NORMALIZATION_DETECTOR_SIDE_LENGTH = "detector_side_length"
KEY_NORMALIZATION_FIELD_SIZE_MODE = "field_size_mode"
KEY_NORMALIZATION_KVP = "kVp"
KEY_NORMALIZATION_MANUFACTURER = "manufacturer"
KEY_NORMALIZATION_MODELS = "models"
KEY_NORMALIZATION_FILTER_SIZE_ALUMINUM = "filter_thickness_Al"
KEY_NORMALIZATION_FILTER_SIZE_COPPER = "filter_thickness_Cu"
KEY_NORMALIZATION_DISTANCE_SOURCE_DETECTOR = "DSD"
KEY_NORMALIZATION_DISTANCE_SOURCE_ISOCENTER = "DSI"
KEY_NORMALIZATION_DISTANCE_ISOCENTER_DETECTOR = "DID"
KEY_NORMALIZATION_DISTANCE_SOURCE_IRP = "DSIRP"
KEY_NORMALIZATION_MODEL_NAME = "model"
KEY_NORMALIZATION_ACQUISITION_TYPE = "acquisition_type"
KEY_NORMALIZATION_ACQUISITION_PLANE = "acquisition_plane"
KEY_NORMALIZATION_AIR_KERMA = "K_IRP"


IRRADIATION_EVENT_PROCEDURE_KEY_BEAM = "Beam"
IRRADIATION_EVENT_PROCEDURE_KEY_DETECTORS = "Detectors"
IRRADIATION_EVENT_PROCEDURE_KEY_PAD = "Pad"
IRRADIATION_EVENT_PROCEDURE_KEY_PATIENT = "Patient"
IRRADIATION_EVENT_PROCEDURE_KEY_SOURCE = "Source"
IRRADIATION_EVENT_PROCEDURE_KEY_TABLE = "Table"
IRRADIATION_EVENT_PROCEDURE_KEY_WIRE_FRAME_BEAM = "WF Beam"
IRRADIATION_EVENT_PROCEDURE_KEY_WIRE_FRAME_DETECTORS = "WF Detectors"
IRRADIATION_EVENT_PROCEDURE_KEY_WIRE_FRAME_PAD = "WF Pad"
IRRADIATION_EVENT_PROCEDURE_KEY_WIRE_FRAME_TABLE = "WF Table"
IRRADIATION_EVENT_STEP_KEY_ARGUMENTS = "args"
IRRADIATION_EVENT_STEP_KEY_LABEL = "label"
IRRADIATION_EVENT_STEP_KEY_METHOD = "method"

MAX_EVENT_FOR_PATIENT_INCLUSION_IN_PROCEDURE_KEY = "max_events_for_patient_inclusion"

MESH_NAME_PAD = "Support pad"
MESH_OPACITY_BEAM = 0.4

MODE_CALCULATE_DOSE = "calculate_dose"
MODE_PLOT_EVENT = "plot_event"
MODE_PLOT_PROCEDURE = "plot_procedure"
MODE_PLOT_SETUP = "plot_setup"
MODE_PLOT_DOSEMAP = "plot_dosemap"
MODE_DARK_MODE = "dark_mode"
MODE_INTERACTIVITY = "interactivity"

OUTPUT_KEY_CORRECTION_BACK_SCATTER = "k_bs"
OUTPUT_KEY_CORRECTION_INVERSE_SQUARE_LAW = "k_isq"
OUTPUT_KEY_CORRECTION_MEDIUM = "k_med"
OUTPUT_KEY_CORRECTION_TABLE = "k_tab"
OUTPUT_KEY_DOSE_MAP = "dose_map"
OUTPUT_KEY_HITS = "hits"
OUTPUT_KEY_KERMA = "kerma"

PHANTOM_MESH_ADULT_MALE = "hudfrid"

PHANTOM_MODEL_CYLINDER = "cylinder"
PHANTOM_MODEL_HUMAN = "human"
PHANTOM_MODEL_PAD = "pad"
PHANTOM_MODEL_PLANE = "plane"
PHANTOM_HUMAN_MESH_SPARSE_MODEL_ENDING = "_reduced_1000t"
PHANTOM_MODEL_TABLE = "table"


PLOT_AXIS_TITLE_X = "X - LON [cm]"
PLOT_AXIS_TITLE_Y = "Y - VER [cm]"
PLOT_AXIS_TITLE_Z = "Z - LAT [cm]"

PLOT_FONT_FAMILY = "Arial"
PLOT_FONT_SIZE = 14

PLOT_HOVERLABEL_FONT_FAMILY = "Arial"
PLOT_HOVERLABEL_FONT_SIZE = 14

PLOT_TITLE_FONT_FAMILY = "Arial"
PLOT_TITLE_FONT_SIZE = 14

PLOT_EVENT_INDEX_KEY = "plot_event_index"

PLOT_SLIDER_BORDER_WIDTH = 3
PLOT_SLIDER_FONT_SIZE_CURRENT = 18
PLOT_SLIDER_FONT_SIZE_GENERAL = 14
PLOT_SLIDER_PADDING = dict(b=0, t=0, l=25, r=25)
PLOT_SLIDER_PADDING_NOTEBOOK = dict(b=0, t=0, l=20, r=20)

PLOT_WIREFRAME_LINE_WIDTH = 4
PLOT_DRAGMODE = "orbit"

PLOT_ASPECTMODE_SETUP_AND_EVENT = "data"
PLOT_ASPECTMODE_PLOT_DOSEMAP = "data"

PLOT_ASPECTMODE_PLOT_PROCEDURE = "cube"
PLOT_ORDER_STATIC = ["right", "back", "left", "front"]

PLOT_PROCEDURE_AXIS_RANGE_X = [-300, 300]
PLOT_PROCEDURE_AXIS_RANGE_Y = [-300, 300]
PLOT_PROCEDURE_AXIS_RANGE_Z = [-300, 300]

# shift size of the entire image to the left to remove whitespace in plot
PLOT_GROUND_SHIFT_X_STATIC = 50

# shift size of each of the four subplots to hide all but 1 colorscale
PLOT_SHIFT_X_STATIC = [0 * 70, 1 * 70, 2 * 70, 3 * 70]

# size of each static subplot
PLOT_BASE_SIZE_STATIC = 297


PLOT_SOURCE_SIZE = 8
PLOT_FILE_TYPE_STATIC = ".png"

PLOT_LIGHTNING_DIFFUSE = 0.5
PLOT_LIGHTNING_AMBIENT = 0.5

PLOT_SLIDER_TRANSITION = dict(duration=300, easing="quad-in-out")

PLOT_ZERO_LINE_WIDTH = 5

PLOT_HEIGHT_NOTEBOOK = 800
PLOT_WIDTH_NOTEBOOK = None

PLOT_HEIGHT = None
PLOT_WIDTH = None

PLOT_MARGIN_NOTEBOOK = dict(l=5, r=5, b=5, t=40)
PLOT_MARGIN = dict(l=0, r=0, b=100, t=40)

# plot camera angles for static dosemaps
PLOT_EYE_BACK = dict(eye=dict(x=0, y=+2.5, z=0))
PLOT_EYE_FRONT = dict(eye=dict(x=0, y=-2.5, z=0))
PLOT_EYE_LEFT = dict(eye=dict(x=2.5, y=+1.5, z=0))
PLOT_EYE_RIGHT = dict(eye=dict(x=-2.5, y=+1.5, z=0))

PLOT_TRACE_ORDER_PHANTOM_WIREFRAME = [0, 4, 5, 1, 0, 3, 7, 4, 7, 6, 5, 1, 2, 3, 2, 6]
PLOT_TRACE_ORDER_BEAM_WIREFRAME = [0, 1, 2, 0, 2, 3, 0, 3, 4, 0, 1, 4, 0]
PLOT_TRACE_ORDER_DETECTOR_WIREFRAME = [0, 0 + 4, 0, 1, 1 + 4, 1, 2, 2 + 4, 2, 3, 3 + 4, 3, 0, 4, 5, 6, 7, 4]

OFFSET_LATERAL_KEY = "d_lat"
OFFSET_VERTICAL_KEY = "d_ver"
OFFSET_LONGITUDINAL_KEY = "d_lon"

RESOLUTION_SPARSE = "sparse"
RESOLUTION_DENSE = "dense"

RUN_ARGUMENTS_MODE_HEADLESS = "headless"
RUN_ARGUMENTS_MODE_GUI = "gui"
RUN_ARGUMENTS_OUTPUT_DICT = "dict"
RUN_ARGUMENTS_OUTPUT_JSON = "json"
RUN_ARGUMENTS_OUTPUT_HTML = "html"
RUN_ARGUMENTS_VALID_OUTPUT_FORMATS = (RUN_ARGUMENTS_OUTPUT_DICT, RUN_ARGUMENTS_OUTPUT_HTML, RUN_ARGUMENTS_OUTPUT_JSON)

TABULATED_FIELD_SIDE_LENGTHS_IN_CM = [5, 10, 20, 25, 35]

# Offset needed to show plane phantom correctly
VISUAL_OFFSET_PHANTOM_MODEL_PLANE = -0.01
MODE_NOTEBOOK_MODE = "notebook_mode"

PLOT_HEIGHT_KEY = "height"
PLOT_WIDTH_KEY = "width"

DOSEMAP_COLORSCALE_KEY = "colorscale"
# Available colorscales are documented here:
# https://plotly.com/python/builtin-colorscales/
DOSEMAP_COLORSCALE = "jet"
# amp

PATIENT_ORIENTATION_HEAD_FIRST_SUPINE = "head_first_supine"
PATIENT_ORIENTATION_FEET_FIRST_SUPINE = "feet_first_supine"
