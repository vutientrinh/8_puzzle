# colors

BLACK = '#23272a'
WHITE = '#ffffff'
GREY = '#2c2f33'
PURPLE = '#4e5d94'
RED = '#C70039'
YELLOW = '#faa61a'
GREEN = '#186F65'
LIGHT_GREEN = '#B5CB99'

# widget properties

BASIC_FRAME_PROPERTIES = {
    'background': BLACK
}

HEADING_LABEL_PROPERTIES = {
    'font': ('Tw Cen MT', 50, 'bold'),
    'background': BLACK,
    'foreground': YELLOW
}

SUBHEADING_LABEL_PROPERTIES = {
    'font': ('Nunito', 18, 'italic'),
    'background': BLACK,
    'foreground': WHITE
}

TEXT_LABEL_PROPERTIES = {
    'font': ('Tw Cen MT', 20, 'bold'),
    'background': BLACK,
    'foreground': WHITE
}

PRIMARY_BUTTON_PROPERTIES = {
    'font': ('Tw Cen MT Condensed', 18, 'bold'),
    'background': LIGHT_GREEN,
    'foreground': WHITE,
    'activebackground': GREEN,
    'activeforeground': WHITE,
    'width': 10,
    'border': 0,
    'relief': 'raised'
}

SECONDARY_BUTTON_PROPERTIES = {
    'font': ('Tw Cen MT Condensed', 18, 'bold'),
    'background': RED,
    'foreground': WHITE,
    'activebackground': YELLOW,
    'activeforeground': WHITE,
    'width': 8,
    'border': 0,
    'relief': 'raised'
}

TERTIARY_BUTTON_PROPERTIES = {
    'font': ('Tw Cen MT Condensed', 18, 'bold'),
    'background': YELLOW,
    'foreground': WHITE,
    'activebackground': GREY,
    'activeforeground': WHITE,
    'width': 8,
    'border': 0,
    'relief': 'raised'
}

TILE_BUTTON_PROPERTIES = {
    'background': BLACK,
    'foreground': BLACK,
    'activebackground': BLACK,
    'activeforeground': BLACK,
    'disabledforeground': BLACK,
    'border': 0
}
