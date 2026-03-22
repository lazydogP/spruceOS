
class LoadedFont:
    def __init__(self, font, line_height, font_path, fallback_font=None, fallback_font_path=None):
        self.font = font
        self.line_height = line_height
        self.font_path = font_path
        self.fallback_font = fallback_font
        self.fallback_font_path = fallback_font_path
