import string
import matplotlib.pyplot
import matplotlib.backends.backend_pdf

from channel_enum import ChannelYUV
from feature_vector import FeatureVector
from feature_config import FeatureConfig
from feature_extraction import FeatureExtractor

colors = [
  '#808080', # 1
  '#556b2f', # 2
  '#a0522d', # 3
  '#808000', # 4
  '#483d8b', # 5
  '#008000', # 6
  '#3cb371', # 7
  '#008080', # 8
  '#000080', # 9
  '#9acd32', # 10
  '#32cd32', # 11
  '#7f007f', # 12
  '#b03060', # 13
  '#d2b48c', # 14
  '#ff0000', # 15
  '#00ced1', # 16
  '#ffa500', # 17
  '#ffff00', # 18
  '#7cfc00', # 19
  '#8a2be2', # 20
  '#dc143c', # 21
  '#00bfff', # 22
  '#f4a460', # 23
  '#0000ff', # 24
  '#f08080', # 25
  '#b0c4de', # 26
  '#ff00ff', # 27
  '#f0e68c', # 28
  '#6495ed', # 29
  '#dda0dd', # 30
  '#ff1493', # 31
  '#7b68ee', # 32
  '#ee82ee', # 33
  '#98fb98', # 34
  '#7fffd4', # 35
  '#ffc0cb'  # 36
]

def plot(vec: FeatureVector, feature_config: FeatureConfig):
    for cnt, hist in enumerate(vec.histograms):
        matplotlib.pyplot.hist(hist[0], label=f'{feature_config.dct_coefficients[cnt]}', color=colors[cnt], density=True, stacked=True)


def plot_single(img_path: string, feature_config: FeatureConfig, plot_name: string):
    feature_extractor = FeatureExtractor(feature_config)
    feat_vec = feature_extractor.extract_feature_vector(img_path)
    plot(feat_vec, feature_config)

    matplotlib.pyplot.legend()
    matplotlib.pyplot.xlabel('Coeff value')
    matplotlib.pyplot.savefig(f'{plot_name}_plot.png')
    matplotlib.pyplot.show()


outputs = [
  'heic',
  'jp2',
  'jpg',
  'jxl',
  'jxr',
  'webp'
]

def plot_outputs(feature_config: FeatureConfig, metric: string, img_name: string):
    for output in outputs:
        matplotlib.pyplot.figure(figsize=(10,10))
        img_path = f"images/output/{metric}/{output}/{img_name}.{output}.png"
        feature_extractor = FeatureExtractor(feature_config)
        feat_vec = feature_extractor.extract_feature_vector(img_path)
        plot(feat_vec, feature_config)
        matplotlib.pyplot.legend()
        matplotlib.pyplot.xlabel(f"{output}: DCT coefficient values")
        matplotlib.pyplot.ylabel("Rel. distribution")


    pdf = matplotlib.backends.backend_pdf.PdfPages(f"plots/{metric}_{img_name}.pdf")
    for fig in range(1, matplotlib.pyplot.figure().number): ## will open an empty extra figure :(
        pdf.savefig( fig )
    pdf.close()


if __name__ == '__main__':
    coeffs = []
    block_size = 6
    for i in range(0, block_size):
        for j in range(0, block_size):
            coeffs.append((i,j))

    feature_config = FeatureConfig(color_channel=ChannelYUV.V, block_size=8, bin_width=0.1, dct_coefficients=coeffs[1:])
    
    img_path = "images/output/psnr_32/webp/Buildings.0004.webp.png"
    # plot_single(img_path, feature_config, "psnr_30_webp_Buildings.0004")
    plot_outputs(feature_config, "psnr_32.0", "Buildings.0008")


