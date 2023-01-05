
# x2 skin for amsynth

A skin for [amsynth](https://amsynth.github.io/) - Analog Modelling Synthesizer.

This skin was automatically generated (see `scripts` directory) from the default skin of `amsynth 1.13.0`, by upscaling all the images 2x. You may want to use it on HDPI devices.

# Usage

```bash
export AMSYNTH_SKIN=/path/to/x2
```

# Experimenting with other resizing methods and coefficients

Create local original-images branch:


```bash
git branch original-images origin/original-images
```


Now, you can checkout the original images and then upscale them using (edited) provided script:


```bash
git checkout original-images -- x2/*.png; ./scripts/scale-images.sh x2
```

# License

GPLv2+.
