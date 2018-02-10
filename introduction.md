# Initiation au Python 2, orienté 3D et VFX

Le python est le langage de référence pour la 3D et le VFX. Il est embarqué dans la plupart des logiciels
majeurs (Maya, 3DS Max, Blender, Nuke, Mari, ...)

Il a probablement été si bien adopté pour les nombreux avantages qu'il présente :

- **Haut-niveau** : On peut se concentrer d'avantage sur la lisibilité du code, plutôt que sur ce qui passe réellement au niveau matériel

- **Interprêté** : par opposition à compilé. Facilite la portabilité du code, au prix d'une perte en performance

- **Syntaxe** : un maximum de signes de 'ponctuation' on été enlevés, par rapport aux autres langages (pas de point-virgule à la fin de chaque ligne, pas de crochet pour définir les blocs de code, ...)

## Les bases du Python

Pour pouvoir utiliser Python, il faut connaitre certaines bases de la programmation, qui sont communes à la plupart des langages.

### Concept de base

Programmer c'est dicter à la machine une suite d'instruction à éxecuter, dans un certain ordre, et sous certaines conditions.

### Variables

Une variable peut être imaginée comme un conteneur. C'est un objet qui stocke en mémoire un certain nombre d'informations, pour pouvoir les utiliser plusieurs fois, à plusieurs moments.

Créer une variable s'appelle **déclaration**

Attribuer une valeur à une variable s'appelle **assignation**

En python, pour déclarer une variable, il suffit de lui assigner une valeur

```python
ma_variable = 5
```

Il est possible ensuite d'utiliser ou réattribuer cette variable plus loin dans le code

```python
print ma_variable * 2  # Utilisation

ma_variable = 10  # Reassignation
```

### Types

Dans l'exemple précédent, il était question de nombres entiers. En programmation, on manipule différents types de données, comme des nombres réels, du texte, des listes d'autres objets, ...

Dans certains langages, une variable doit être déclarée avec un type, et ce type ne peut plus être changé pendant toute la durée de vie de la variable.

En python, une variable peut changer de type à n'importe quel moment de son existence

```python
ma_variable = 5  # Entier

ma_variable = "bonjour"  # Chaine de caracteres
```

_Cela permet une certaine flexibilité, mais cela apporte aussi un certain nombre de problèmes éventuels. **Mieux vaut se tenir à un type par variable**_

Les principaux types d'objets sont les suivants

| Nom | Type | Description |
| --- | --- | --- |
| Entier | `ìnt` | Les nombres entiers |
| Flotant | `float` | Les nombres réels |
| Booléen | `bool` | Vrai ou Faux |
| Chaîne | `str` | Texte |
| Iterable | `list`, `dict`, `tuple`... | Contiennent un certain nombre d'autres objets, agencés d'une certaine manière |

### Syntaxe

Un des grands avantages du Python est sa syntaxe. Elle est lisible et minimaliste.

Par exemple, pour définir un bloc de code (fonction, test, boucle, ...) la plupart des langages utilisent les accolades, les points virgules, et d'autres signes

Exemple en C#

```C#
using System;

class HelloWorld
{
 public static void Main()
 {
  Console.WriteLine("hello world!");
 }
}
```

En, python c'est l'indentation qui défini les blocs. Cela a deux avantages :

- Ca force à indenter son code
- Ca supprime un grand nombres d'accolades dans le code

Exemple

```Python
import sys

class HelloWorld(object):
    def main(self):
        print "Hello world!"
```

Les commentaires sont marqués avec le caractère `#`

Exemple

```Python
# Dire bonjour au monde
print "Hello world!"
```

### Mathématiques basiques

Lorsque l'on veut combiner différentes valeurs, on utlise des **opérateurs**

L'exemple le plus simple est celui de l'addition

```python
ma_variable = 10 + 5
```

Ici, 10 et 5 sont additionnés, et le résultat est assigné à `ma_variable`

Il est possible d'effectuer des opérations sur des variables

```python
prix_au_kilo = 5
poids_en_kilo = 2

prix_total = prix_au_kilo * poids_en_kilo
```

Les principaux opérateurs sont les suivants

| Nom | Signe | Description |
| --- | --- | --- |
| Addition | `+` | L'addition |
| Soustraction | `-` | La soustraction |
| Multiplication | `*` | La multiplication |
| Division | `/` | La division |
| Division Entière | `//` | Partie entière de la division |
| Exposant | `**` | La mise à la puissance |
| Modulo | `%` | Reste de la division Euclidienne |

### Test / Comparaison

Il existe des opérateurs de comparaison. Ces opérateurs renvoient un booléen, selon si la comparaison est vraie ou fausse.

Il existe des opérateurs de comparaison pour l'égalité, la superiorité, l'inferiorité, ...

Exemple

```Pyhton
10 > 5  # True
5 > 10  # False
```

Comme les opérateurs précédents, il est possible de les utiliser avec des variables

Les principaux opérateurs sont les suivants

| Nom | Signe | Description |
| --- | --- | --- |
| Egal | `==` | Opérateur d'égalité |
| Inégal | `!=` | Opérateur d'inégalité |
| Supérieur stricte | `>` | Opérateur de supériorité stricte |
| Supérieur ou égal | `>=` | Opérateur de supériorité |
| Inférieur stricte | `<` | Opérateur d'inferiorité stricte |
| Inférieur ou égal | `<=` | Opérateur d'inferiorité |
| Unicité | `is` | Teste s'il s'agit du même objet |
| Non unicité | `is not` | Teste s'il ne s'agit pas du même objet |

Afin de pouvoir executer du code selon un cas ou l'autre, on utilise une structure de contrôle. 
Elle utilise les mots-clef `if`, `elif` et `else`

Exemple

```Python
# Calculs savants
prix_au_kilo = 5
nombre_kilo = 2
prix_total = prix_au_kilo * nombre_kilo

# Moins de 50 euros, ca passe
if prix_total < 50:
    print "J'achete !"

# Plus de 500 euros, quelle arnaque
elif prix_total >= 500:
    print "C'est trop cher !"

# Sinon je sais pas trop
else:
    print "J'hesite"
```

### Fonctions

Pour permettre d'organiser et pour éviter de recopier du code s'il est réutilisé, il est possible de définir des
fonctions.

Une fonction est un bloc de code à qui zéro, un, ou plusieurs **arguments** va être passé, et qui va renvoyer
une **valeur retour**.

Exemple
```Python
# Definition de la fonction
def ma_reaction(prix):
    # Moins de 50 euros, ca passe
    if prix < 50:
        return "J'achete !"

    # Plus de 500 euros, quelle arnaque
    elif prix >= 500:
        return "C'est trop cher !"

    # Sinon je sais pas trop
    else:
        return "J'hesite"

# Calculs savants
prix_au_kilo = 5
nombre_kilo = 2
prix_total = prix_au_kilo * nombre_kilo

# Utilisation de la fonction
print ma_reaction(prix_total)
```

#### Unpacking

Il est possible d'assigner plusieurs variables simultanément.

```Python
a, b, c = ["a", "b", "c"]
```

Pratique pour retourner plusieurs valeurs depuis une fonction

```Python
def ma_fonction():
    return "a", "b", "c"
    
a, b, c = ma_fonction()
```
Les crochets sont facultatifs, cela créé un `tuple` implicitement

### Itérables

Il existe dans la plupart des langages un moyen de grouper les objets dans d'autres objets. L'exemple le plus simple
est la liste.

#### La liste : `list()`

En Python, une liste est déclarée et assignée comme suit :

```Python
mes_legumes_favoris = ['Choux', 'Salsifi', 'Endive', 'Brocoli']
```

Il est ensuite possible d'effectuer des opérations et des tests sur la liste et ses éléments

Il est possible de tester si un element est présent dans la liste

```Python
mes_legumes_favoris = ['Choux', 'Salsifi', 'Endive', 'Brocoli']

if 'Poireau' in mes_legumes_favoris:
    print "J'adore le poireau"
```

Il est possible d'ajouter un element à la liste

```Python
# J'ai des legumes favoris
mes_legumes_favoris = ['Choux', 'Salsifi', 'Endive', 'Brocoli']

print 'Poireau' in mes_legumes_favoris  # False

# Je me rend compte que j'adore le poireau
mes_legumes_favoris.append("Poireau")

print 'Poireau' in mes_legumes_favoris  # True
```

Bien d'autres opérations sont possibles (tri, suppression d'élement, ...)

#### Le dictionnaire : `dict()`

Un dictionnaire associe une liste de **clefs** à une liste de **valeurs**. Il peut s'apparenter à un tableau
à deux colones.

Exemple

| Numéro de place de parking | Propriétaire |
| --- | --- |
| 1 | César |
| 2 | Napoléon |
| 3 | Attila |
| 4 | Marie-Antoinette |

En Python

```Python
attribution_parking = {1: 'Cesar', 2: 'Napoleon', 3: 'Attila', 4: 'Marie-Antoinette'}
```

Plus lisiblement

```Python
attribution_parking = {
    1: 'Cesar',
    2: 'Napoleon',
    3: 'Attila',
    4: 'Marie-Antoinette'
}
```

### Boucles

Les boucles permettent d'executer de manière répétitive (itérative) un bloc de code

Chaque répétition est appelé une **itération**

#### Boucle `for`

Il est souvent pratique de pouvoir **parcourir** les **éléments** d'un itérable, pour effectuer un traitement par
lot. Il existe pour cela la boucle `for`

Exemple avec des listes

```Python
# J'ai des legumes favoris
mes_legumes_favoris = ['Choux', 'Salsifi', 'Endive', 'Brocoli']

# Ingredients du plat du jour a la brasserie
ingredients = ['Tomate', 'Haricots', 'Lard', 'Endive', 'Bechamel']

# Prepare une variable pour savoir si je vais a la brasserie ce midi
brasserie_ce_midi = False

# Chaque ingredient du plat du jour
for ingredient in ingredients:
    # S'il s'agit d'un de mes legumes favoris
    if ingredient in mes_legumes_favoris:
        # Je vais aller a la brasserie
        brasserie_ce_midi = True

# Ennonce le resultat
print brasserie_ce_midi
```

Exemple avec un dictionnaire

```Python
le_dict = {1: "a", 2:"b", 3:"c"}


for clef, valeur in le_dict.items():
    print "clef : {clef}, valeur : {valeur}".format(
        clef=clef,
        valeur=valeur
    )
```

#### Boucle `while`

La boucle while permet d'executer du code tant qu'une condition est validée (`True`)

Exemple

```Python
# Je me suis decide a aller a la brasserie
j_ai_faim = True

while j_ai_faim:
    # Manger un peu
    manger_un_peu()
    # Verifier si j'ai encore faim
    j_ai_faim = ai_je_encore_faim()

print "J'ai plus faim, j'arrete la, ou alors juste un petit dessert"
```

### Modules / Packages

Python permet d'organiser le code en fichiers et en dossiers. Les fonctions sont ensuite accessibles grace à la commande `import`

#### Module

Tout fichier `.py` est un module, et il accessible à la commande `import` s'il est dans le même dossier que le script courant, ou s'il est dans le `$PYTHONPATH`

Arborescence

```plain
 + /racine
    + mon_module.py
    + mon_script.py
```

Exemple d'import depuis `mon_script.py`

```python
import mon_module

print mon_module.ma_fonction()
```

Autre exemple : le module `math`

```python
import math

racine_carree = math.sqrt(25)
print racine_carree
```

#### Package

Un package est un dossier contenant plusieurs modules. Il doit comporter un fichier `__init__.py`, qui le plus souvent est vide, ou contient simplement des `import`.

Arborescence

```plain
 + /racine
    + /mon_package
    |  + __init__.py
    |  + module_1.py
    |  + module_2.py
    + mon_script.py
```

Exemple d'import depuis `mon_script.py`

```python
import mon_package.module1
from mon_package import module2

print mon_package.module1.ma_fonction1()
print module2.ma_fonction2()
```
