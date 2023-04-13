import matplotlib.colors as colors

def cmapAlbedo(listed = False):
    pal = ([0.1568627450980392, 0.1450980392156863, 0.19607843137254902], [0.22745098039215686, 0.22745098039215686, 0.40784313725490196], [0.8980392156862745, 0.8470588235294118, 0.796078431372549], [0.9607843137254902, 0.807843137254902, 0.5411764705882353], [0.5568627450980392, 0.403921568627451, 0.33725490196078434])
    if(listed):
        return colors.ListedColormap(pal, name = 'Albedo')
    else:
        return colors.LinearSegmentedColormap.from_list('Albedo', pal)

def cmapAlhaitham(listed = False):
    pal = ([0.09803921568627451, 0.19215686274509805, 0.20392156862745098], [0.21176470588235294, 0.40784313725490196, 0.4196078431372549], [0.2980392156862745, 0.6431372549019608, 0.6352941176470588], [0.6862745098039216, 0.6901960784313725, 0.6705882352941176], [0.5333333333333333, 0.4549019607843137, 0.3411764705882353])
    if(listed):
        return colors.ListedColormap(pal, name = 'Alhaitham')
    else:
        return colors.LinearSegmentedColormap.from_list('Alhaitham', pal)

def cmapAyaka(listed = False):
    pal = ([0.13333333333333333, 0.1411764705882353, 0.28627450980392155], [0.2549019607843137, 0.2980392156862745, 0.5294117647058824], [0.611764705882353, 0.7019607843137254, 0.8313725490196079], [0.9254901960784314, 0.9294117647058824, 0.9215686274509803], [0.6862745098039216, 0.35294117647058826, 0.4627450980392157])
    if(listed):
        return colors.ListedColormap(pal, name = 'Ayaka')
    else:
        return colors.LinearSegmentedColormap.from_list('Ayaka', pal)

def cmapBennett(listed = False):
    pal = ([0.2823529411764706, 0.26666666666666666, 0.37254901960784315], [0.8823529411764706, 0.8431372549019608, 0.7686274509803922], [0.1450980392156863, 0.5098039215686274, 0.4745098039215686], [0.9058823529411765, 0.6862745098039216, 0.18823529411764706], [0.7215686274509804, 0.00784313725490196, 0.0])
    if(listed):
        return colors.ListedColormap(pal, name = 'Bennett')
    else:
        return colors.LinearSegmentedColormap.from_list('Bennett', pal)

def cmapCollei(listed = False):
    pal = ([0.2823529411764706, 0.2980392156862745, 0.13725490196078433], [0.48627450980392156, 0.5254901960784314, 0.2549019607843137], [0.7254901960784313, 0.7764705882352941, 0.47843137254901963], [0.9725490196078431, 0.9058823529411765, 0.8235294117647058], [0.7137254901960784, 0.43137254901960786, 0.592156862745098])
    if(listed):
        return colors.ListedColormap(pal, name = 'Collei')
    else:
        return colors.LinearSegmentedColormap.from_list('Collei', pal)

def cmapDiona(listed = False):
    pal = ([0.2235294117647059, 0.22745098039215686, 0.3254901960784314], [0.8666666666666667, 0.6196078431372549, 0.3568627450980392], [0.8352941176470589, 0.5294117647058824, 0.5176470588235295], [0.9294117647058824, 0.792156862745098, 0.7764705882352941], [0.7137254901960784, 0.5803921568627451, 0.5019607843137255])
    if(listed):
        return colors.ListedColormap(pal, name = 'Diona')
    else:
        return colors.LinearSegmentedColormap.from_list('Diona', pal)

def cmapDori(listed = False):
    pal = ([0.1607843137254902, 0.12156862745098039, 0.15294117647058825], [0.4392156862745098, 0.34901960784313724, 0.5725490196078431], [0.6627450980392157, 0.45098039215686275, 0.6], [0.8392156862745098, 0.5098039215686274, 0.5803921568627451], [0.9529411764705882, 0.7490196078431373, 0.792156862745098])
    if(listed):
        return colors.ListedColormap(pal, name = 'Dori')
    else:
        return colors.LinearSegmentedColormap.from_list('Dori', pal)

def cmapFaruzan(listed = False):
    pal = ([0.17254901960784313, 0.2549019607843137, 0.3137254901960784], [0.36470588235294116, 0.5333333333333333, 0.4823529411764706], [0.43529411764705883, 0.6274509803921569, 0.6745098039215687], [0.7098039215686275, 0.8274509803921568, 0.8509803921568627], [0.9882352941176471, 0.9333333333333333, 0.8862745098039215])
    if(listed):
        return colors.ListedColormap(pal, name = 'Faruzan')
    else:
        return colors.LinearSegmentedColormap.from_list('Faruzan', pal)

def cmapGanyu(listed = False):
    pal = ([0.2, 0.2235294117647059, 0.3568627450980392], [0.36470588235294116, 0.4549019607843137, 0.6352941176470588], [0.7686274509803922, 0.8470588235294118, 0.9490196078431372], [0.9490196078431372, 0.9098039215686274, 0.8901960784313725], [0.48627450980392156, 0.1568627450980392, 0.16862745098039217])
    if(listed):
        return colors.ListedColormap(pal, name = 'Ganyu')
    else:
        return colors.LinearSegmentedColormap.from_list('Ganyu', pal)

def cmapItto(listed = False):
    pal = ([0.12941176470588237, 0.10588235294117647, 0.10588235294117647], [0.3333333333333333, 0.21568627450980393, 0.4], [0.8235294117647058, 0.807843137254902, 0.8235294117647058], [0.9686274509803922, 0.8588235294117647, 0.47058823529411764], [0.5607843137254902, 0.25098039215686274, 0.1843137254901961])
    if(listed):
        return colors.ListedColormap(pal, name = 'Itto')
    else:
        return colors.LinearSegmentedColormap.from_list('Itto', pal)

def cmapJean(listed = False):
    pal = ([0.11372549019607843, 0.10588235294117647, 0.10980392156862745], [0.13333333333333333, 0.27450980392156865, 0.4117647058823529], [0.24313725490196078, 0.45098039215686275, 0.6196078431372549], [0.8980392156862745, 0.8901960784313725, 0.8980392156862745], [0.9254901960784314, 0.788235294117647, 0.6392156862745098])
    if(listed):
        return colors.ListedColormap(pal, name = 'Jean')
    else:
        return colors.LinearSegmentedColormap.from_list('Jean', pal)

def cmapJin(listed = False):
    pal = ([0.11764705882352941, 0.10196078431372549, 0.13333333333333333], [0.3058823529411765, 0.2980392156862745, 0.4470588235294118], [0.403921568627451, 0.6431372549019608, 0.7294117647058823], [0.8274509803921568, 0.5372549019607843, 0.6313725490196078], [0.7254901960784313, 0.3058823529411765, 0.3686274509803922])
    if(listed):
        return colors.ListedColormap(pal, name = 'Jin')
    else:
        return colors.LinearSegmentedColormap.from_list('Jin', pal)

def cmapKazuha(listed = False):
    pal = ([0.12941176470588237, 0.09803921568627451, 0.09411764705882353], [0.6666666666666666, 0.8666666666666667, 0.8392156862745098], [0.9058823529411765, 0.8549019607843137, 0.803921568627451], [0.7647058823529411, 0.2196078431372549, 0.1568627450980392], [0.39215686274509803, 0.10196078431372549, 0.06666666666666667])
    if(listed):
        return colors.ListedColormap(pal, name = 'Kazuha')
    else:
        return colors.LinearSegmentedColormap.from_list('Kazuha', pal)

def cmapKeqing(listed = False):
    pal = ([0.12941176470588237, 0.10196078431372549, 0.24313725490196078], [0.27058823529411763, 0.2, 0.4392156862745098], [0.6470588235294118, 0.592156862745098, 0.7137254901960784], [0.996078431372549, 0.9529411764705882, 0.9098039215686274], [0.8156862745098039, 0.4235294117647059, 0.615686274509804])
    if(listed):
        return colors.ListedColormap(pal, name = 'Keqing')
    else:
        return colors.LinearSegmentedColormap.from_list('Keqing', pal)

def cmapKlee(listed = False):
    pal = ([0.25882352941176473, 0.12156862745098039, 0.10196078431372549], [0.7568627450980392, 0.20784313725490197, 0.11372549019607843], [0.5294117647058824, 0.33725490196078434, 0.2823529411764706], [0.7529411764705882, 0.5098039215686274, 0.4392156862745098], [0.9647058823529412, 0.8823529411764706, 0.7764705882352941])
    if(listed):
        return colors.ListedColormap(pal, name = 'Klee')
    else:
        return colors.LinearSegmentedColormap.from_list('Klee', pal)

def cmapKokomi(listed = False):
    pal = ([0.1803921568627451, 0.17254901960784313, 0.4117647058823529], [0.27450980392156865, 0.28627450980392155, 0.611764705882353], [0.5568627450980392, 0.5529411764705883, 0.7843137254901961], [0.9686274509803922, 0.8862745098039215, 0.8588235294117647], [0.8470588235294118, 0.6392156862745098, 0.596078431372549])
    if(listed):
        return colors.ListedColormap(pal, name = 'Kokomi')
    else:
        return colors.LinearSegmentedColormap.from_list('Kokomi', pal)

def cmapMiko(listed = False):
    pal = ([0.21176470588235294, 0.13333333333333333, 0.1411764705882353], [0.6980392156862745, 0.25882352941176473, 0.2549019607843137], [0.796078431372549, 0.43137254901960786, 0.4549019607843137], [0.9098039215686274, 0.6627450980392157, 0.6509803921568628], [0.8549019607843137, 0.807843137254902, 0.8117647058823529])
    if(listed):
        return colors.ListedColormap(pal, name = 'Miko')
    else:
        return colors.LinearSegmentedColormap.from_list('Miko', pal)

def cmapNahida(listed = False):
    pal = ([0.1803921568627451, 0.1843137254901961, 0.13725490196078433], [0.396078431372549, 0.5333333333333333, 0.45098039215686275], [0.7254901960784313, 0.7803921568627451, 0.5529411764705883], [0.8235294117647058, 0.7490196078431373, 0.6470588235294118], [0.9058823529411765, 0.8901960784313725, 0.8941176470588236])
    if(listed):
        return colors.ListedColormap(pal, name = 'Nahida')
    else:
        return colors.LinearSegmentedColormap.from_list('Nahida', pal)

def cmapNilou(listed = False):
    pal = ([0.0784313725490196, 0.21176470588235294, 0.37254901960784315], [0.4627450980392157, 0.6352941176470588, 0.7254901960784313], [0.7490196078431373, 0.8509803921568627, 0.8980392156862745], [0.9725490196078431, 0.9490196078431372, 0.9254901960784314], [0.8392156862745098, 0.30980392156862746, 0.2196078431372549])
    if(listed):
        return colors.ListedColormap(pal, name = 'Nilou')
    else:
        return colors.LinearSegmentedColormap.from_list('Nilou', pal)

def cmapNoelle(listed = False):
    pal = ([0.2196078431372549, 0.2, 0.23529411764705882], [0.6549019607843137, 0.6235294117647059, 0.7254901960784313], [0.6431372549019608, 0.7019607843137254, 0.5254901960784314], [0.6274509803921569, 0.49019607843137253, 0.40784313725490196], [0.6470588235294118, 0.16862745098039217, 0.3333333333333333])
    if(listed):
        return colors.ListedColormap(pal, name = 'Noelle')
    else:
        return colors.LinearSegmentedColormap.from_list('Noelle', pal)

def cmapRazor(listed = False):
    pal = ([0.13725490196078433, 0.13333333333333333, 0.2196078431372549], [0.4980392156862745, 0.44313725490196076, 0.4196078431372549], [0.596078431372549, 0.6235294117647059, 0.6823529411764706], [0.8901960784313725, 0.7215686274509804, 0.4117647058823529], [0.7098039215686275, 0.6980392156862745, 0.43529411764705883])
    if(listed):
        return colors.ListedColormap(pal, name = 'Razor')
    else:
        return colors.LinearSegmentedColormap.from_list('Razor', pal)

def cmapSayu(listed = False):
    pal = ([0.3568627450980392, 0.2901960784313726, 0.2784313725490196], [0.5490196078431373, 0.36470588235294116, 0.25882352941176473], [0.8549019607843137, 0.5803921568627451, 0.39215686274509803], [0.9490196078431372, 0.8470588235294118, 0.6823529411764706], [0.5019607843137255, 0.6039215686274509, 0.32941176470588235])
    if(listed):
        return colors.ListedColormap(pal, name = 'Sayu')
    else:
        return colors.LinearSegmentedColormap.from_list('Sayu', pal)

def cmapShenhe(listed = False):
    pal = ([0.13725490196078433, 0.16862745098039217, 0.21176470588235294], [0.3176470588235294, 0.48627450980392156, 0.5372549019607843], [0.5254901960784314, 0.5803921568627451, 0.6784313725490196], [0.7058823529411765, 0.7490196078431373, 0.8156862745098039], [0.611764705882353, 0.19215686274509805, 0.1607843137254902])
    if(listed):
        return colors.ListedColormap(pal, name = 'Shenhe')
    else:
        return colors.LinearSegmentedColormap.from_list('Shenhe', pal)

def cmapShogun(listed = False):
    pal = ([0.20784313725490197, 0.14901960784313725, 0.3764705882352941], [0.3333333333333333, 0.23137254901960785, 0.5803921568627451], [0.596078431372549, 0.4470588235294118, 0.792156862745098], [0.9647058823529412, 0.9058823529411765, 0.9294117647058824], [0.37254901960784315, 0.12549019607843137, 0.23921568627450981])
    if(listed):
        return colors.ListedColormap(pal, name = 'Shogun')
    else:
        return colors.LinearSegmentedColormap.from_list('Shogun', pal)

def cmapSucrose(listed = False):
    pal = ([0.10588235294117647, 0.16470588235294117, 0.3137254901960784], [0.3254901960784314, 0.4196078431372549, 0.596078431372549], [0.8705882352941177, 0.9333333333333333, 0.8117647058823529], [0.4823529411764706, 0.6352941176470588, 0.5490196078431373], [0.2823529411764706, 0.49019607843137253, 0.4235294117647059])
    if(listed):
        return colors.ListedColormap(pal, name = 'Sucrose')
    else:
        return colors.LinearSegmentedColormap.from_list('Sucrose', pal)

def cmapTao(listed = False):
    pal = ([0.22745098039215686, 0.10588235294117647, 0.09803921568627451], [0.4823529411764706, 0.34901960784313724, 0.3686274509803922], [0.788235294117647, 0.2784313725490196, 0.21568627450980393], [0.7803921568627451, 0.6274509803921569, 0.5215686274509804], [0.9882352941176471, 0.9411764705882353, 0.8823529411764706])
    if(listed):
        return colors.ListedColormap(pal, name = 'Tao')
    else:
        return colors.LinearSegmentedColormap.from_list('Tao', pal)

def cmapTighnari(listed = False):
    pal = ([0.1411764705882353, 0.19607843137254902, 0.34509803921568627], [0.00392156862745098, 0.5372549019607843, 0.615686274509804], [0.1568627450980392, 0.4470588235294118, 0.27450980392156865], [0.6941176470588235, 0.7686274509803922, 0.30196078431372547], [0.9058823529411765, 0.7803921568627451, 0.21176470588235294], [0.9686274509803922, 0.7490196078431373, 0.38823529411764707], [0.9333333333333333, 0.6901960784313725, 0.6862745098039216], [0.5882352941176471, 0.20392156862745098, 0.3764705882352941], [0.38823529411764707, 0.12156862745098039, 0.4], [0.5529411764705883, 0.3411764705882353, 0.1607843137254902])
    if(listed):
        return colors.ListedColormap(pal, name = 'Tighnari')
    else:
        return colors.LinearSegmentedColormap.from_list('Tighnari', pal)

def cmapVenti(listed = False):
    pal = ([0.11372549019607843, 0.1450980392156863, 0.20784313725490197], [0.11764705882352941, 0.44313725490196076, 0.6313725490196078], [0.2, 0.5411764705882353, 0.4470588235294118], [0.611764705882353, 0.6588235294117647, 0.24705882352941178], [0.8980392156862745, 0.8470588235294118, 0.7333333333333333])
    if(listed):
        return colors.ListedColormap(pal, name = 'Venti')
    else:
        return colors.LinearSegmentedColormap.from_list('Venti', pal)

def cmapXiangling(listed = False):
    pal = ([0.0, 0.0, 0.0], [0.2196078431372549, 0.2823529411764706, 0.44313725490196076], [0.2784313725490196, 0.5215686274509804, 0.35294117647058826], [0.9058823529411765, 0.7411764705882353, 0.2235294117647059], [0.6705882352941176, 0.30980392156862746, 0.24705882352941178])
    if(listed):
        return colors.ListedColormap(pal, name = 'Xiangling')
    else:
        return colors.LinearSegmentedColormap.from_list('Xiangling', pal)

def cmapXiao(listed = False):
    pal = ([0.2, 0.23529411764705882, 0.25882352941176473], [0.19215686274509805, 0.4, 0.34509803921568627], [0.3686274509803922, 0.6509803921568628, 0.611764705882353], [0.7607843137254902, 0.8117647058823529, 0.6352941176470588], [0.6431372549019608, 0.4745098039215686, 0.6196078431372549], [0.4392156862745098, 0.4, 0.5647058823529412])
    if(listed):
        return colors.ListedColormap(pal, name = 'Xiao')
    else:
        return colors.LinearSegmentedColormap.from_list('Xiao', pal)

def cmapYoimiya(listed = False):
    pal = ([0.3803921568627451, 0.11764705882352941, 0.11764705882352941], [0.803921568627451, 0.26666666666666666, 0.19607843137254902], [0.9372549019607843, 0.5686274509803921, 0.38823529411764707], [0.9254901960784314, 0.7607843137254902, 0.6078431372549019], [0.9529411764705882, 0.8509803921568627, 0.7450980392156863])
    if(listed):
        return colors.ListedColormap(pal, name = 'Yoimiya')
    else:
        return colors.LinearSegmentedColormap.from_list('Yoimiya', pal)

def cmapZhongli(listed = False):
    pal = ([0.1843137254901961, 0.13725490196078433, 0.12941176470588237], [0.6666666666666666, 0.30980392156862746, 0.13725490196078433], [0.996078431372549, 0.8470588235294118, 0.4588235294117647], [0.9725490196078431, 0.9215686274509803, 0.8627450980392157], [0.4235294117647059, 0.3843137254901961, 0.47843137254901963])
    if(listed):
        return colors.ListedColormap(pal, name = 'Zhongli')
    else:
        return colors.LinearSegmentedColormap.from_list('Zhongli', pal)

def keys(display: bool = False, format: str or None = 'txt', colormap: bool =False):
    """List all the available keys in a table.

    Parameters
    ----------
    display : bool, optional (default: False)
        Whether to print the keys.
    format : {'txt', 'csv', 'markdown', 'html'}, optinoal (default: 'txt')
        The format of the output table.
    colormap : bool, optional (default: False)
        Whether to show the color list.

    Returns
    -------
    output : str or None
        A table containing all the available keys.
        If `display` is True, return None.
    """
    keys = (["keynames", "albedo", "alhaitham", "ayaka", "bennett", "collei", "diona", "dori", "faruzan", "ganyu", "itto", "jean", "jin", "kazuha", "keqing", "klee", "kokomi", "miko", "nahida", "nilou", "noelle", "razor", "sayu", "shenhe", "shogun", "sucrose", "tao", "tighnari", "venti", "xiangling", "xiao", "yoimiya", "zhongli"], \
            ["en.fullname", "Albedo", "Alhaitham", "Kamizato Ayaka", "Bennett", "Collei", "Diona", "Dori", "Faruzan", "Ganyu", "Arataki Itto", "Jean", "Yun Jin", "Kaedehara Kazuha", "Keqing", "Klee", "Sangonomiya Kokomi", "Yae Miko", "Nahida", "Nilou", "Noelle", "Razor", "Sayu", "Shenhe", "Raiden Shogun", "Sucrose", "Hu Tao", "Tighnari", "Venti", "Xiangling", "Xiao", "Yoimiya", "Zhongli"], \
            ["cn.fullname", "\u963f\u8d1d\u591a", "\u827e\u5c14\u6d77\u68ee", "\u795e\u91cc\u7eeb\u534e", "\u73ed\u5c3c\u7279", "\u67ef\u83b1", "\u8fea\u5965\u5a1c", "\u591a\u8389", "\u73d0\u9732\u73ca", "\u7518\u96e8", "\u8352\u6cf7\u4e00\u6597", "\u7434", "\u4e91\u5807", "\u67ab\u539f\u4e07\u53f6", "\u523b\u6674", "\u53ef\u8389", "\u73ca\u745a\u5bab\u5fc3\u6d77", "\u516b\u91cd\u795e\u5b50", "\u7eb3\u897f\u59b2", "\u59ae\u9732", "\u8bfa\u827e\u5c14", "\u96f7\u6cfd", "\u65e9\u67da", "\u7533\u9e64", "\u96f7\u7535\u5c06\u519b", "\u7802\u7cd6", "\u80e1\u6843", "\u63d0\u7eb3\u91cc", "\u6e29\u8fea", "\u9999\u83f1", "\u9b48", "\u5bb5\u5bab", "\u949f\u79bb"])
    
    try:
        import pandas as pd
    except ImportError:
        import warnings
        warnings.warn('The package "pandas" is not found. The raw output will be returned.\n' +
                      '- To get fancy output, you need to install the "pandas" package.\n' +
                      '- Run `pip install pandas` or `conda install pandas`.\n')
        return rawKeys(keys)
    df = pd.DataFrame({tc[0]: tc[1:] for tc in keys})

    if colormap:
        df['colormaps'] = ''
        for index, row in df.iterrows():
            func = globals()['cmap{}'.format(row['keynames'].capitalize())]
            df.at[index, 'colormaps'] = toHtml(func(listed=True).colors)

    if format == 'txt':
        output = df.to_string(index=False)
    elif format == 'csv':
        output = df.to_csv(index=False)
    elif format == 'markdown':
        try:
            output = df.to_markdown(index=False)
        except ImportError:
            import warnings
            warnings.warn('The package "tabulate" is not found. The html output will be returned.\n' +
                          '- To get markdown output, you need to install the "tabulate" package.\n' +
                          '- Run `pip install tabulate` or `conda install tabulate`.\n')
            output = df.to_html(index=False, escape=False)
    elif format == 'html':
        output = df.to_html(index=False, escape=False)
    else:
        output = df

    if display:
        print(output)
        return
    else:
        return output

def rawKeys(keys, display=False):
    if display:
        nrow = len(keys[0])
        for i in range(nrow):
            for j in range(2):
                print(keys[j][i] + '\t', end = '')
            print(keys[2][i])
        return
    else:
        return keys

def toHtml(colors):
    tbl = '<table><tr>'
    for rgb in colors:
        tbl += '<td style="background-color:rgb(%d,%d,%d);width:10px;heigth:10px;"></td>' % tuple(255*c for c in rgb)
    tbl += '</tr></table>'
    return tbl

