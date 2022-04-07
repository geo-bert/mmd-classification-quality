Images are taken fromm [MIT VisTex](https://vismod.media.mit.edu/vismod/imagery/VisionTexture/vistex.html)

## JPEG XL:
- PNG/PNG
- cjxl INPUT OUTPUT -q QUALITY
- djxl INPUT OUTPUT

## WebP:
- PNG/PNG
- Quality kann float sein, hat PSNR flag
- cwebp -q QUALITY INPUT -o OUTPUT
- dwebp INPUT -o OUTPUT

## JPEG XR:
- TIF/TIF
- Quality kann float sein
- JxrEncApp -q QUALITY -i INPUT -o OUTPUT
- JxrDecApp -i INPUT -o OUTPUT

## JPEG:
- PPM/PPM
- Imagemagick dann wahrscheinlich weil wir dann PNG/PNG können
- cjpeg -q QUALITY -outfile OUTPUT INPUT
- djpeg -outfile OUTPUT INPUT

## HEIC:
- PNG/PNG
- heif-enc -q QUALITY -o OUTPUT INPUT
- Unklar was für ein Decoder hergenommen wird, aber mit Imagemagick gehts
- magick INPUT OUTPUT

## JPEG 2000:
- PNG/PNG
- Quality ist PSNR, also nicht 0-100
- opj_compress -q QUALITY -i INPUT -o OUTPUT
- Wenn nicht PSNR also: magick INPUT -quality QUALITY OUTPUT
- opj_decompress -i INPUT -o OUTPUT

How to install matlab engine: [here](https://de.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
