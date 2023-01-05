#!/bin/bash

set -xeu

cd "$1"

for img in *.png; do
    convert "$img" -resize '200%' "$img"
done
