import argparse

from emojiart.emojiart import EmojiArt


def init():
    parser = argparse.ArgumentParser(description='Never Forget TANKS.', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-t',
        '--target-text',
        type=str,
        required=True,
        dest='target_text',
        help='target text'
    )
    parser.add_argument(
        '-n',
        '--on-char',
        type=str,
        required=True,
        dest='on_char',
        help='on character'
    )
    parser.add_argument(
        '-f',
        '--of-char',
        type=str,
        required=True,
        dest='off_char',
        help='off character'
    )
    parser.add_argument(
        '-l',
        '--line-length',
        type=int,
        required=False,
        default=3,
        dest='line_length',
        help='line lenght'
    )
    args = parser.parse_args()
    return args.target_text, args.on_char, args.off_char, args.line_length

def T(text_box):
    text_map = text_box.strip('\n').split('\n')
    t_text_map = list(zip(*text_map))
    return '\n'.join([''.join(reversed(x)) for x in t_text_map]) + '\n'


def main(text, on, off, line_length):
    e = EmojiArt()
    result = []
    for part in [text[i: i+line_length] for i in range(0, len(text), line_length)]:
        base_text = e.render_text(part)
        if line_length == 1:
            base_text = T(base_text)
        result.append(base_text.replace('#', on).replace(' ', off))
    print(''.join(result))


if __name__ == '__main__':
    target_text, on_char, off_char, line_length = init()
    main(target_text, on_char, off_char, line_length)