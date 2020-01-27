# A propos de Git et Github

*Créé le 27/01/2020*

Ressources :
https://www.youtube.com/watch?v=hPfgekYUKgk
https://www.youtube.com/watch?v=4o9qzbssfII

## Git
https://git-scm.com/

Janvier 2020 : Installation de 2.25.0
Latest update: January 13th 2020

Paramétrage initial

    git config --global user.name "José Relland" 

    git config --global user.email --global "jose.relland@gmail.com"


## pour info, un git help
<pre>
'C:\>git help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing
one

work on the current change (see also: git help everyday)
   add               Add file contents to the index
   mv                Move or rename a file, a directory, or a symlink
   restore           Restore working tree files
   rm                Remove files from the working tree and from the index
   sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)
   bisect            Use binary search to find the commit that introduced a bug
   diff              Show changes between commits, commit and working tree, etc
   grep              Print lines matching a pattern
   log               Show commit logs
   show              Show various types of objects
   status            Show the working tree status

grow, mark and tweak your common history
   branch            List, create, or delete branches
   commit            Record changes to the repository
   merge             Join two or more development histories together
   rebase            Reapply commits on top of another base tip
   reset             Reset current HEAD to the specified state
   switch            Switch branches
   tag               Create, list, delete or verify a tag object signed with GPG


collaborate (see also: git help workflows)
   fetch             Download objects and refs from another repository
   pull              Fetch from and integrate with another repository or a local
 branch
   push              Update remote refs along with associated objects

</pre>

Création du répertoire c>/python/mooc

Initialisation de git dans ce répertoire

'C:\python\mooc>git init
Initialized empty Git repository in C:/python/mooc/.git/'

'git status'
inidque "No commit yet"

## Le commit des fichiers dans le  répertoire se fait en deux étapes

1. Sélection des fichiers à commiter
'git add index.html'

2. Lancer la commande de commit avec un commentaire pour dire pourquoi on fait cette mise à jour
'git commit -m "Premier commit"'

## Github

