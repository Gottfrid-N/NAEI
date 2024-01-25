'''
.
,
o
x

p = plosive
!p = click
!b = implosive
p! = ejective
n = nasal
r = trill
'r = tap or flap
. = fricative
.p = affricative
u = approximant

B = Bilabial
p> = Labiolingual
b> = Linguolabial
p- = Dentolabial
b- = Labiodental
|- = Dental
r = Alveolar
k = Post-alveolar
h = Retroflex
b = Palatal
G = Velar
J = Uvular
L = Pharyngeal
|^ = Epiglottal
|v = Glottal
'''

if __name__ == "__main__":
    voices = [".", ",", "o", "x"]
    places = ["B", "p>", "b>", "p-", "b-", "|-", "r", "k", "h", "b", "G", "J", "L", "|^", "|v"]
    diacritics = ["p", "p!", "!p", "!b", "n", "r", "'r", ".", "u"]
    laterals = ["", "l"]
    glyphs = {}
    index = 0
    fill_char = "0"
    prefix = "0x"
    for voice in voices:
        for place in places:
            for diacritic in diacritics:
                for lateral in laterals:
                    glyphs[f"{voice}{place}{diacritic}{lateral}"] = f"{chr(57344 + index)}"
                    index += 1
    print(glyphs)
    print(len(glyphs))
