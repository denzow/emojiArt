from .fonts import FONT_DATA


class EmojiArt:

    def __init__(self):
        pass

    def render_text(self, text):
        result = ''
        for c in text:
            result += self._render_char(c)

        return result

    def _render_char(self, char):
        bitmaps = FONT_DATA.get(char)
        char_lines = []
        for bitmap in bitmaps:
            char_lines.append(''.join([str(b).replace('0', ' ').replace('1', '#') for b in bitmap]))

        return '\n'.join(char_lines)
