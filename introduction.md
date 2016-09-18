# Initiation au Python 2, orienté 3D et VFX

Le python est le langage de référence pour la 3D et le VFX. Il est embarqué dans la plupart des logiciels
majeurs (Maya, 3DS Max, Blender, Nuke, Mari, ...)

Il a probablement été si bien adopté pour les nombreux avantages qu'il présente :

- **Haut-niveau**, c'est à dire qu'on se préoccupe plus de la lisibilité du code, que de ce qui passe
réellement au niveau matériel

- **Interprêté**, par opposition à compilé. Permet une portabilité totale du code, au prix d'une legère
perte en performance

- **Syntaxe**, un maximum de signes de 'ponctuation' on été enlevés, par rapport aux autres
langages (pas de point-virgule à la fin de chaque ligne, pas de crochet pour définir les blocs de code, ...)

## Les bases du Python

Pour pouvoir utiliser Python, il faut connaitre certaines bases de la programmation, qui sont communes à la plupart
des langages.

### Variables

Une variable peut être imaginée comme un conteneur. C'est un objet qui stocke en mémoire un certain nombre
d'informations, pour pouvoir les utiliser plusieurs fois, à plusieurs moments.

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

Dans l'exemple précédent, il était question de nombres entiers. En programmation, on manipule différents types de
données, comme des nombres réels, du texte, des listes d'autres objets, ...

Dans certains langages, une variable doit être déclarée avec un type, et ce type ne peut être changé pendant toute
la durée de vie de la variable.

En python, une variable peut changer de type à n'importe quel moment de son existence

```python
ma_variable = 5  # Entier

ma_variable = "bonjour"  # Chaine de caracteres
```

Les principaux types d'objets sont les suivants

| Nom | Type | Description |
| --- | --- | --- |
| Entier | `ìnt` | Les nombres entiers |
| Flotant | `float` | Les nombres réels |
| Booléen | `bool` | Vrai ou Faux |
| Chaîne | `str` | Texte |
| Iterable | `list`, `dict`, `tuple`... | Contiennent un certain nombre d'autres objets |

### Syntaxe

Un des grands avantages du Python est sa syntaxe. Elle est lisible et minimaliste.

Pour définir un bloc de code (fonction, test, boucle), la plupart des langages utilisent les accolades,
les points virgules, et d'autres signes

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

Ici, 10 et 5 sont additionnés, et le resultat est assigné à `ma_variable`

Il est possible d'effectuer des opérations sur des variables

```python
prix_au_kilo = 5
nombre_kilo = 2

prix_total = prix_au_kilo * nombre_kilo
```

Les principaux opérateurs sont les suivants

| Nom | Signe | Description |
| --- | --- | --- |
| Addition | `+` | L'addition |
| Soustraction | `-` | La soustraction |
| Multiplication | `*` | La multiplication |
| Division | `/` | La division |
| Exposant | `**` | La mise à la puissance |
| Modulo | `%` | Reste de la division Euclidienne |

### Test / Comparaison

Comparaison valeurs

Operations booleenes

If elif else

### Fonctions

### Iterables

### Boucles

##