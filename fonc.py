import re

exemple = '''
P1 est un produit composé de P2 et P3
P2 est un produit élémentaire
P5 est un produit composé de P1 et P4
P4 est un produit élémentaire
P9 est un produit composé de P1, P6 et P4
P10 est un produit composé de P3 et P5
P11 est un produit composé de P5 et P3
'''

elementaires = re.findall("(P\d+) est un produit élémentaire", exemple)
print("Produits élémentaires:", elementaires)

trois_produits = re.findall("(P\d+) est un produit composé de (?:P\d+, ){2}P\d+", exemple)
print("Produits composés de trois produits:", trois_produits)


p3_p5 = re.findall("(P\d+) est un produit composé de P3 et P5", exemple)
print("Produits composés seulement de P3 et P5:", p3_p5)
sans_p2 = re.findall("(P\d+) est un produit composé de ((?!P2).)*$", exemple)
print("Produits composés qui n'ont pas P2:", sans_p2)

composants_p9 = re.findall("P9 est un produit composé de ((?:P\d+, )*(?:P\d+))", exemple)
composants_p9 = re.findall("P\d+", composants_p9[0])
print("Produits qui composent P9:", composants_p9)