#!/bin/bash

set -xeu

cd "$1"


# other possible strategies:
# * -resize '200%'
# * -resize '200%' -unsharp 0x6+0.5+0
# * -adaptive-resize '200%'

for img in *.png; do
    convert "$img" \
        -interpolate Nearest \
        -interpolative-resize '200%' \
        "$img"
done
