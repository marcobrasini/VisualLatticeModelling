from math import sqrt

PeriodicTable = {
    'H' : {'radius': 0.53, 'color': [255,255,255]},
    'He': {'radius': 0.31, 'color': [217,255,255]},
    'Li': {'radius': 1.67, 'color': [204,128,255]},
    'Be': {'radius': 1.12, 'color': [194,255,  0]},
    'B' : {'radius': 0.87, 'color': [255,181,181]},
    'C' : {'radius': 0.67, 'color': [144,144,144]},
    'N' : {'radius': 0.56, 'color': [ 48, 80,248]},
    'O' : {'radius': 0.48, 'color': [255, 13, 13]},
    'F' : {'radius': 0.42, 'color': [144,224, 80]},
    'Ne': {'radius': 0.38, 'color': [179,227,245]},
    'Na': {'radius': 1.90, 'color': [171,92,242]},
    'Mg': {'radius': 1.45, 'color': [138,255,  0]},
    'Al': {'radius': 1.18, 'color': [191,166,166]},
    'Si': {'radius': 1.11, 'color': [240,200,160]},
    'P' : {'radius': 0.98, 'color': [255,128,  0]},
    'S' : {'radius': 0.88, 'color': [255,255, 48]},
    'Cl': {'radius': 0.79, 'color': [ 31,240, 31]},
    'Ar': {'radius': 0.71, 'color': [128,209,227]},
    'K' : {'radius': 2.43, 'color': [143, 64,212]},
    'Ca': {'radius': 1.94, 'color': [ 61,255,  0]},
    'Sc': {'radius': 1.84, 'color': [230,230,230]},
    'Ti': {'radius': 1.76, 'color': [191,194,199]},
    'V' : {'radius': 1.71, 'color': [166,166,171]},
    'Cr': {'radius': 1.66, 'color': [138,153,199]},
    'Mn': {'radius': 1.61, 'color': [156,122,199]},
    'Fe': {'radius': 1.56, 'color': [224,102,51]},
    'Co': {'radius': 1.52, 'color': [240,144,160]},
    'Ni': {'radius': 1.49, 'color': [ 80,208, 80]},
    'Cu': {'radius': 1.45, 'color': [200,128,51]},
    'Zn': {'radius': 1.42, 'color': [125,128,176]},
    'Ga': {'radius': 1.36, 'color': [194,143,143]},
    'Ge': {'radius': 1.25, 'color': [102,143,143]},
    'As': {'radius': 1.14, 'color': [189,128,227]},
    'Se': {'radius': 1.03, 'color': [255,161,  0]},
    'Br': {'radius': 0.94, 'color': [166, 41,41]},
    'Kr': {'radius': 0.88, 'color': [ 92,184,209]},
    'Rb': {'radius': 2.65, 'color': [112, 46,176]},
    'Sr': {'radius': 2.19, 'color': [  0,255,  0]},
    'Y' : {'radius': 2.12, 'color': [148,255,255]},
    'Zr': {'radius': 2.06, 'color': [148,224,224]},
    'Nb': {'radius': 1.98, 'color': [115,194,201]},
    'Mo': {'radius': 1.90, 'color': [ 84,181,181]},
    'Tc': {'radius': 1.83, 'color': [ 59,158,158]},
    'Ru': {'radius': 1.78, 'color': [ 36,143,143]},
    'Rh': {'radius': 1.73, 'color': [ 10,125,140]},
    'Pd': {'radius': 1.69, 'color': [  0,105,133]},
    'Ag': {'radius': 1.65, 'color': [192,192,192]},
    'Cd': {'radius': 1.61, 'color': [255,217,143]},
    'In': {'radius': 1.56, 'color': [166,117,115]},
    'Sn': {'radius': 1.45, 'color': [102,128,128]},
    'Sb': {'radius': 1.33, 'color': [158, 99,181]},
    'Te': {'radius': 1.23, 'color': [212,122,  0]},
    'I' : {'radius': 1.15, 'color': [148,  0,148]},
    'Xe': {'radius': 1.08, 'color': [ 66,158,176]},
    'Cs': {'radius': 2.98, 'color': [ 87, 23,143]},
    'Ba': {'radius': 2.53, 'color': [  0,201,  0]},
}


def default_radius(atom):
    radius = PeriodicTable[atom]['radius']
    return sqrt(radius)/2

def default_color(atom):
    color = PeriodicTable[atom]['color']
    return [c/255 for c in color]
