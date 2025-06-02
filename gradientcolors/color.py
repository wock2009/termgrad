
cleangreen = [
    (144, 238, 144),
    (102, 255, 153),
    (51, 255, 170),
    (0, 255, 191),
    (0, 255, 128),
    (0, 255, 64),
]

yellow_gradient = [
    (255, 255, 204),
    (255, 255, 153),
    (255, 255, 102),
    (255, 255, 51),
    (204, 204, 0),
    (153, 153, 0),
]

grey_gradient = [
    (224, 224, 224),
    (192, 192, 192),
    (160, 160, 160),
    (128, 128, 128),
    (96, 96, 96),
    (64, 64, 64),
]


purple_night = [
    (204, 153, 255),
    (170, 102, 238),
    (136, 68, 221),
    (102, 34, 204),
    (68, 0, 187),
    (34, 0, 136),
]

frozen_blue = [
    (200, 240, 255),
    (160, 220, 255),
    (120, 200, 255),
    (80, 180, 255),
    (40, 160, 255),
    (0, 140, 255),
]

pastel_rainbow = [
    (255, 192, 203),
    (255, 223, 186),
    (255, 255, 186),
    (186, 255, 201),
    (186, 225, 255),
    (201, 186, 255),
]

infrared_red = [
    (255, 80, 80),
    (230, 60, 60),
    (200, 40, 40),
    (170, 20, 20),
    (140, 0, 0),
    (100, 0, 0),
]

toxic_green = [
    (192, 255, 62),
    (162, 255, 42),
    (132, 255, 22),
    (102, 255, 2),
    (72, 225, 0),
    (42, 195, 0),
]

cappuccino = [
    (210, 180, 140),
    (186, 140, 105),
    (160, 110, 80),
    (130, 90, 60),
    (100, 70, 40),
    (70, 50, 30),
]

minty_fresh = [
    (180, 255, 220),
    (140, 255, 200),
    (100, 255, 180),
    (60, 255, 160),
    (20, 255, 140),
    (0, 220, 120),
]



def _color_text_gradient(text: str, gradient: list[tuple[int, int, int]]) -> str:
    lines = text.split('\n')
    colored_lines = []
    for i, line in enumerate(lines):
        r, g, b = gradient[i % len(gradient)]
        colored_lines.append(f"\033[38;2;{r};{g};{b}m{line}\033[0m")
    return '\n'.join(colored_lines)



def color_text_cleangreen(text: str) -> str:
    return _color_text_gradient(text, cleangreen)

def color_text_yellow_gradient(text: str) -> str:
    return _color_text_gradient(text, yellow_gradient)

def color_text_grey_gradient(text: str) -> str:
    return _color_text_gradient(text, grey_gradient)

def color_text_purple_night(text: str) -> str:
    return _color_text_gradient(text, purple_night)

def color_text_frozen_blue(text: str) -> str:
    return _color_text_gradient(text, frozen_blue)

def color_text_pastel_rainbow(text: str) -> str:
    return _color_text_gradient(text, pastel_rainbow)

def color_text_infrared_red(text: str) -> str:
    return _color_text_gradient(text, infrared_red)

def color_text_toxic_green(text: str) -> str:
    return _color_text_gradient(text, toxic_green)

def color_text_cappuccino(text: str) -> str:
    return _color_text_gradient(text, cappuccino)

def color_text_minty_fresh(text: str) -> str:
    return _color_text_gradient(text, minty_fresh)
