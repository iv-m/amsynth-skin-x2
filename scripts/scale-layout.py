#!/usr/bin/env python3
#
# Simple script to scale up amsynth skins

import configparser


SCALE_FACTOR = 2.0
FIELDS = ('pos_x', 'pos_y', 'width', 'height')


def scale(section, field, factor=SCALE_FACTOR):
    if field not in section:
        return
    value = int(section[field])
    section[field] = str(int(SCALE_FACTOR * value))


def main(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    for section in config.values():
        for field in FIELDS:
            scale(section, field)
    with open(filename, 'w') as layout_file:
        config.write(layout_file)


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
