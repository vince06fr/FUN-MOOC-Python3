# Semaine 1. Introduction au MOOC et aux outils Python
---

## Vidéo 1 - Organisation du MOOC

- Suite d'un précédent MOOC 2.7
- Basé sur Python 2.6
- Structure du cours :
    - Tronc commun avec traits marquants :
        - Code lilsible
        - Tout est objet
        - Liaison lexicale
        - Typage dynamique
        - Itérations
        - Espaces de nommage
    - Modules optionnels (deux dernières semaines)
        - Data Science : numpy, matplotlib, pandas
        - Programmation asynchrone : paradigme de coroutines, librairie asyscio
        - Sujets avancés : attributs, décorateurs, métaclasses
    - Objectifs
        - Codes propres
        - Lire du code (lisez le plus possible)
        - Bien utiliser les librairies tierces

## Vidéo 2 - Pourquoi Python

- Langage très lisible (ex C++, Java et Javascript)
    - Syntaxe orienté sur la présentation
- Traits dominants
    - La facilité d'accès est un but
    - Pragmatique (comme régler de la meilleure façon de régler un pb)
- Historique
    - Python 1.0 Janvier 1994 (rupture de compatibilité)
    - Python 2.0 Octobre 2000
    - Python 3.0 Décembre 2008
    - Python 3.6 (celle du cours) Décembre 2016
    - Une seule rupture de compatibilité en 25 ans
    - Python 2.7 jusqu'en 2020
- Stable
- Librairie standard
- Portable
- Très grosse base de code
- Code pur ou possibilité d'intégrer du C/C++ pour des applications rapides
- Développement rapide
    - Gestion automatique de la mémoire
    - Langage interprété + Notebook Jupiter
- Gouvernance
    - Python Software Foundation
    - Débat démocratique, décision par Guido Rossum, BDFL, Benevolent Dictator For Life
- Langage le plus populaire en 2016 (second Java)

### Installer la distribution standard Python

- Distinguons :
    - Le **terminal** (le Shell, l'invite de commandes (cmd)), avec le prompt $ ou >,
        - Lancement de l'interpréteur du python3 installé par `py`

            Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit 
            (AMD64)] on win32

        - avec `py -0`, on la liste des python installés
        - Avec py -2.7, lancement de python 2.7... si installé
    - Interpréteur Python, avec >>>
        - L'interpréteur est lancé à partir du terminal : par `py`   (voir ci-dessus)
        - Ou de l'icône de l'application
        - Retour au terminal avec `exit()`

### $ sudo apt-get install python3 Installation de base pour le cours

[Download Python](https://www.python.org/downloads/)

- Installation sur Linux (bien que certainement déjà installé)

    $ sudo apt-get install python3
    $ sudo apt-get install idle3

### Installation de bibliothèques complémentaires : pip

[pip](https://pypi.org/project/pip/)

- Version pip 20.0.1 à janvier 2020
- Pour lancer pip : `pip install pip`
- Bibliothèques aussi accessible avec les packages Linux (apt-get...)
- par Anaconda, [https://www.anaconda.com/](https://www.anaconda.com/), l'environnement le plus complet
    - Son gestionnaire de paquets se nomme `conda`
- Voir aussi Jupyter Noeebooks, avec ses fichiers au format .ipynb

### Lecture

- Juillet 2018, Guido van Rossum quitte la fonction de BDFL
- Le zen de Python
- 

    #le Zen de Python
    import this

    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

### Documentation

- [http://fr.wikipedia.org/wiki/Python_(langage)](http://fr.wikipedia.org/wiki/Python_%28langage%29)
- Python en français

[FrenchLanguage - Python Wiki](https://wiki.python.org/moin/FrenchLanguage)

- Toute la documentation

[3.8.1 Documentation](https://docs.python.org/3/)

- Initiative de traduction en français

[3.8.1 Documentation](https://docs.python.org/fr/3/)

Discours introductif de Guido van Rossum à la PyCon2016, Portland, Oregon

[https://www.youtube.com/watch?v=YgtL4S7Hrwo](https://www.youtube.com/watch?v=YgtL4S7Hrwo)

- La licence de Python

[History and License - Python 3.8.1 documentation](https://docs.python.org/3/license.html)

- La [Python Sorfware Foundation](https://www.python.org/psf) est basée au USA
    - 9450 SW Gemini Dr., ECM# 90772, Beaverton, OR 97008, USA.

### Processus de développement, les Python Enhancement Proposals (PEP)

[PEP 0 -- Index of Python Enhancement Proposals (PEPs)](https://legacy.python.org/dev/peps/)

# Vidéo 3 - Interpréteur, Idle et ipython

### Idle, l'interpréteur de Pithon

- Pré-installé avec Windows 8 ???
- Idle est un interpréteur de commandes :). Il en existe beaucoup d'autres
- Son menu à l'ouverture (éditeur) **Shell**

> File | Edit | Shell | Debug | Options | Window | Help

- Menu File, il est possible de sauvegarder son écran en fichier Python (.py) et de le réouvrir plus tard
- Une fois sauvegardé en **.py**, le menu d'Idle est modifié
    - Note : parfois la sauvegarde python est en .txt qu'il faut renommer en .py

> File | Edit | Format | Run | Options | Window | Help

- Pour exécuter un programme à partir de l'interpréteur Idle :
    - Il faut ouvrir le fichier .py (`File > Open`) et cliquer sur le fichier
    - Le programme s'ouvre dans une nouvelle fenêtre
    - Dans cette nouvelle fenêtre, faire `Run > Run Module (F5)`, l'interpréteur et réinitialisé et le programme exéuté
    - Désormais, dans l'interpréteur de Idle, vous pouvez executer les fonctions du programme

     jusqu'à ce que vous réinitialisr le shell :)

### Installation de ipython

- Il est recommander d'installer Anaconda sur ipython.org

### Installation Anaconda3 2019.10 64bit sur Windows 8

- J'ai un compte sur

[](https://anaconda.org)

- Se lance à partir de l'application de Windows

[Getting started with Anaconda - Anaconda documentation](https://docs.anaconda.com/anaconda/user-guide/getting-started/)

- Anaconda installe un serveur sur [localhost](http://localhost) :) accessible avec `localhost:8888`

[](http://localhost:8888/tree/Anaconda3)

- Il y a une liste impressionnante de répertoires et programmes !
- C:\Users\jose\Anaconda3 - environ 3 GB
- Python 3.7 (au lieu de 3.8.6 déjà installé !)

# Video 4 - Les notebooks

Gestion par Cellules "programmes" ou "media"

- Sur Windows,
    - Ctrl + Entrée, on reste dans la même cellule
    - Maj + Entrée, on passe à la cellule suivante
- Suite de calculs dans une cellule, c'est la dernière expression qui sera retournée
    - Il faut utiliser print() pour chaque expression que l'on veut voir retournée !
    - Faire attention à ce que l'ordre d'exécution du programme corresponde à l'ordre d'exécution des cellules. Par exemple, exécuter la cellule affectant la variable puis la cellule de celle tratant de cette même variable.
- Explications du Notebook du cours
    - Les pages sont modifiables et sauvegardables
    - On revient au document du cours par `File > Reset to Original`
    - Téléchargement  du .ipynb par File > Download
    - D'autres format sont téléchargeables
        - En sélectionnant l'extension : .html, .py (le texte passe en commentaires)...
    - Possibilité de partager son ipynb sur le forum par `File > Share static version`

### Premier programme avec la suite de Fibonacci

- Pas une étude de programme, juste le lancement par le terminal et par l'interpréteur
- Programmes complémenaires avec turtle
    - Programme python téléchargé en .txt, renommé en .py

# Vidéo 5. Notions de variable, d'objet et typage dynamique

- Objet contient
    - Des données
    - et des méthodes
- Type
    - Données et méthodes par défaut
- Exemples d'**objet "spam"** dont le type est **Sring**,
    - Contient la données "spam"
    - et des méthodes natives comme .upper() (lié au type **String** Les parenthèses sont importantes car elles déclenchent la fonction
    - Pour invoquer la méthode upper() de 'spam' on écrit
        - `'spam'.upper()`
- Nom de variable :
    - Lettres ou chiffres et _ (possible mais éviter de commencer un nom de variables sauf variables système ou dédiées)

    - Les majuscules (nom de classes) et minuscules (nom de variables) ont de l'importance
    - Ne doit pas commencer par un nombre
    - Nommage explicite
- Expérience de variables :  espace de nommage
    - c'est le dernier nommage avec la même variable qui remporte l'affectation
    - C'est le type dynamique, **c'est l'objet qui créer le type, pas la variable**
    - Lorsque l'on supprime la variable, le **garbage collector** va "nettoryer les objets" et libérer la mémoire
- Règle de nommage PEP8

[PEP 8 -- Style Guide for Python Code](https://legacy.python.org/dev/peps/pep-0008/#descriptive-naming-styles)

- Mot-clé Python interdit en programmation, réservé par le langage
    - Liste complète, en gras les nouveaux par rapport à Python2

**False	await**	else	import	pass
**None**	break	except	in	raise
True	class	finally	is	return
and	continue	for	lambda	try
as	def	from	**nonlocal**	while
assert	del	global	not	with
**async**	elif	if	or	yield

[2. Lexical analysis - Python 3.8.1 documentation](https://docs.python.org/3/reference/lexical_analysis.html#keywords)

### La function Type()

- Permet de connaître le type d'un objet
- `type(1)` ⇒ int ou `type('spam')` ⇒ str

- le type est attaché à la variable
    - x = 1
    - type(x) ⇒ int

    Autre exemple

    x = [1, 2, 3]
    type(x) ⇒ list

### La function isinstance()

- proche de type() mais plus intéressante car elle permet de tester un objet (et sa variable) pour vérifier qu'une opération est permise par exemple
    - `isinstance(26, int)`
    - `True`

### Compléments

- **type-checking**, le contrôle de type
- **duck typing**... "si cela à l'aspect d'un cannard, c'est que c'est un canard"
- **Type hints** depuis python-3.5, il est possible d'ajouter des annotations de type

# Vidéo 6. Les types numériques

### Type integer "int"

- Permet des chiffres très grands
- 1, 58...

### Type float "float"

- Plus limité en précision pour les très petits chiffres (sur 53 bits - 15 chiffres significatifs)
- 1.5, 3.14

### Type complex "complex"

- Partie réel et partie complex (j représentant la partie imaginaire, en Python appelé j (i en français !)
    - c = 4 + 5j (Création) c=4+5j (le résultat)

### Les opérations sur les numériques

- division
    - naturelle : 6 / 3 donne 0.5
    - division avec un entier : 3 // 6 donne 0
    - le modulo ; 3 % 6 donne 3
- racine : 3 ** 3 (double étoile)
- valeur absolue : abs(-4) donne 4

### Type booléen "bool"

- True et False avec majuscule
- Symbole mathématique
- `from math import e`, pi permet des opérations comme :

        n = 1
        print("n=", n, "racine = ", e**((2.j*pi*n)/3))

### Chaîne de caractères

- `chaine = "Bonjour le monde !"`
- `type(chaine)` donne `str`
- conversion chaînes
    - la function input retourne une chaine, même si l'on rentre des nombres
    - `reponse = input("quel est votre âge ? ")`
    - `quel est votre âge ? 56`
    - Il n'est pas possible de faire une opération sur le nombre 56, il faut le convertir en integer : `age = int(reponse)`, `type(age)` donne `int`
- Simplification en intégrant la conversion dans la function input
    - `print("le double de votre age est", 2***int(reponse)**)`
- Les fonctions de transformation :

    Type	Fonction
    Entier	int
    Flottant	float
    Complexe	complex
    Chaîne	str

### Très grands nombres, entiers et bases

- on peut les écrire ainsi :
    - tres_grand_nombre = `23_456_789_012_345` donne `23456789012345`
    - Les soulignés ne seront pas traités dans l'affichage
- Base 2

        deux_cents = 0**b**11001000
        200

- Base 8

        deux_cents = 0**o**310

- Base 16

        deux_cents = 0**x**c8

- Pour les autres bases :
    - Utilisation de la fonction int, en passant un paramètre de la base, ici base 4

        deux_cents = int('3020', 4)

### Opérations et Affectation dans variable (de la forme +=)

- Faire en une fois une opération et une affection

    entier = 10
    entier += 2   # Opération et affectation dans la variable
    print('entier', entier)
    entier 12

- Equivalent à :

    entier = 10
    entier = entier + 2  # économise la réécriture de la variable... si
                         # c'est la même variable
    print('entier', entier)
    entier 12

- Voir aussi : -= , *=,  /=, **= 2 (le carré), %=, //= ainsi que le décalage >>2 (décalage à droite de deux pas à droite
- Sur les chaînes, listes... principalement pour le +

    liste = [0, 3, 5]
    print('liste', liste)
    
    liste += ['a', 'b']
    print('après ajout', liste)
    
    Résultat :
    liste [0, 3, 5]
    après ajout [0, 3, 5, 'a', 'b']

- Autres cas

    liste = [0, 3, 5]
    print('liste', liste)
    
    liste *= 3
    print('après ajout', liste)
    
    Résultat : 
    liste [0, 3, 5]
    après ajout [0, 3, 5, 0, 3, 5, 0, 3, 5]

### Notions sur la précisions des calculs flottants

contrairement aux entiers où le calcul est toujours exact, les flottants peuvent poser un problème de précision lié à la technique de codage sous forme binaire

    0.2 + 0.4
    Réultat :
    0.6000000000000001

    0.3 - 0.1 == 0.2
    Résultat :
    False

- Solution avec des fractions, fonction `Fraction` de `fractions`

    # on importe le module fractions, qui lui-même définit 
    # le symbole Fraction
    from fractions import Fraction
    
    # et cette fois, les calculs sont exacts, 
    # et l'expression retourne bien True
    Fraction(3, 10) - Fraction(1, 10) == Fraction(2, 10)
    Résultat :
    True

- ou plus lisible

    Fraction('0.3') - Fraction('0.1') == Fraction('2/10')
    Résultat :
    True

- et ceci

    Fraction(5, 3) - 2 == Fraction(-1, 3)
    Résultat :
    True

- Autres solutions avec `Decimal` de decimal

    from decimal import Decimal
    
    Decimal('0.3') - Decimal('0.1') == Decimal('0.2')
    Résultat :
    True

### Compléments sur les flottants, fraction et décimal

- [tutoriel sur les nombres flottants](https://docs.python.org/3/tutorial/floatingpoint.html)
- [documentation sur la classe Fraction](https://docs.python.org/3/library/fractions.html)
- [documentation sur la classe Decimal](https://docs.python.org/3/library/decimal.html)
- [présentation plus fouillée sur l'encodage des flottants (en anglais)](http://www.oxfordmathcenter.com/drupal7/node/43)

## Opérations bit à bit (bitwise)

- Et &
- Ou |
- Ouexclusif ^
- Décalage
    - Décalage à gauche revient à décaler les bits, donc une division de 2^4 = 1

        49 << 4
        Résultat :
        784

    > 𝑥49          → (0,1,1,0,0,0,1)
    𝑥49 >> 4 → (0,0,0,0,0,1,1)→2+1→3

### Utilisation de bin

    bin(49)
    Résultat :
    '0b110001'

### Compléments sur les opérations bit à bit

[https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

### Compléments sur estimer le plus petit flottant

Exemple

    10**-320
    Retourne : 1e-320
    
    Alors que 
    10**-330
    Retourne : 0.0  # Erreur, il a été en fait arrondi

- Pour trouver le plus petit flottant, faire des appoximations

    10**-323
    Retourne : 1e-323    # Le plus petit flottant
    # Alors que 
    10**-324
    Retourne : 0.0 

### Compléments sur estimer le plus grand flottant

    10**450    # ici, pas de problème, car ce sont des integers
    
    Mais ici
    10**450.0
    Retourne une erreur **OverflowError**
    OverflowError: (34, 'Numerical result out of range')

- Par approximations successives
    - la limite pour les grands nombres se situe entre les deux valeurs 10^300 et 10^310.

    10**300.  # le point final pour un float
    retourne : 1e+300
    
    Alors que 
    10**310.
    Reourne une OverflowError

    10**308.
    Retourne : 1e+308
    
    Mais
    10**309.    # La limite maximale
    Reourne une OverflowError

### Avec la fonction sys.info_float

    import sys
    print(sys.float_info)
    Retourne :  
    sys.float_info(max=1.7976931348623157e+308, 
    max_exp=1024, 
    max_10_exp=308, 
    min=2.2250738585072014e-308, 
    min_exp=-1021, 
    min_10_exp=-307, 
    dig=15, 
    mant_dig=53, 
    epsilon=2.220446049250313e-16, 
    radix=2, 
    rounds=1)

    print("Flottant minimum", sys.float_info.min)
    print("Flottant maximum", sys.float_info.max)
    print("Flottant maximul exposant", sys.float_info.max_exp)
    print("Flottant minimum exposant", sys.float_info.min_exp)
    print("Flottant minimum puissance de 10", sys.float_info.min_10_exp)
    print("Flottant maximum puissance de 10", sys.float_info.max_10_exp)
    print("Flottant minimum", sys.float_info.dig)
    
    Ceux-ci n'ont pas fonctionné
    # print("Flottant minimum", sys.mant_dig)
    # print("Flottant minimum", sys.epsilon)
    # print("Flottant minimum", sys.radix)
    # print("Flottant minimum", sys.rounds)

Plus d'info ici : [https://docs.python.org/3/library/sys.html#sys.float_info](https://docs.python.org/3/library/sys.html#sys.float_info)

- Accès aux éléments

    print("Flottant minimum", sys.float_info.min)
    print("Flottant maximum", sys.float_info.max)
    Retourne :
    Flottant minimum 2.2250738585072014e-308
    Flottant maximum 1.7976931348623157e+308

### Complément sur les nombres dénormaux

[Denormal number](https://en.wikipedia.org/wiki/Denormal%5Fnumber)
