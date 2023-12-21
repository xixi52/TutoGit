# Atelier de Magie Git 🧙‍♂️

## Introduction à Git
Bienvenue dans le royaume enchanté de Git, l'outil qui fait des merveilles pour gérer les potions de code en développement logiciel. C'est un peu comme l'école de sorcellerie Poudlard, mais pour les développeurs.

## 1) Invocation d'un dépôt avec `git init`
Utilisez `git init` pour créer un nouveau grimoire Git, et hop, un fichier .git apparaît comme par magie. Attendez-vous à ce qu'un hibou vous apporte une baguette git, prête à l'emploi dans le monde magique du code.

## 2) Préparation des potions avec `git add`
`git add` prépare les potions à être jetées dans le chaudron magique. C'est comme choisir les ingrédients pour une potion magique. `git add .` ajoute tous les ingrédients, tandis que `git add <ingrédient>` cible spécifiquement le cornichon de dragon dont vous avez besoin.

## 3) Préparation du sort avec `git commit`
Avec `git commit`, enregistrez vos potions dans un sort avec un message descriptif. Pensez à écrire des commentaires magiques pour expliquer pourquoi vous avez ajouté de la licorne en poudre à votre potion de code.

## 4) `git pull` pour rappeler les derniers sorts
`git pull` est comme une cape d'invisibilité qui rappelle les derniers sorts d'un grimoire distant vers votre copie locale. Idéal pour synchroniser les baguettes magiques dans le royaume du développement collaboratif.

**Contexte :**
- Développement magique collaboratif : Comme des élèves de Poudlard travaillant ensemble sur une potion magique.
- Système de contrôle de versions magiques : Git enregistre les différentes versions des sorts, un peu comme les archives de la bibliothèque de Poudlard.

![8a3pxb](https://github.com/xixi52/TutoGit/assets/5670689/347773ab-cb9d-4f0e-aea9-91e5b6763d4e)

## 5) `git diff` pour examiner les différences
`git diff` est comme la carte du Maraudeur, vous permettant de voir les différences entre les versions de sorts. Examinez-les avec l'œil d'un mage pour comprendre les subtilités des changements.

**Utilisation :**
```bash
git diff <ingrédient-source> <ingrédient-cible>
```

## 6) `git merge` pour fusionner des branches
`git merge` combine les pouvoirs de deux branches, un peu comme les cours de sorts combinés à Poudlard. Assurez-vous de résoudre les conflits magiques qui surgissent pendant la fusion, sinon, cela pourrait être pire que la potion de Polynectar.

**Utilisation :**
```bash
git merge <branche-source>
```

## 7) `git tag` pour marquer des versions
`git tag` crée des étiquettes magiques pour marquer des points spécifiques dans l'historique des versions. C'est comme si vous mettiez une étoile d'or sur votre parchemin magique chaque fois que vous atteignez une version stable.

**Création de tags :**
- Annotés : Associés à un message descriptif, comme un journal de potions.
- Légers : Références simples à un sort, comme des notes dans le livre des sorts de Poudlard.

**Utilisation :**
```bash
git tag -a v1.0 -m "Version 1.0" <hash-du-sort>
```

## 8) `git clone` pour copier un grimoire existant
`git clone` copie un grimoire Git existant dans un nouveau repaire magique. C'est un peu comme emprunter le livre "Les Sortilèges Git" à la bibliothèque de Poudlard, sans déranger les Acromentules.

**Options courantes :**
- `--branch <nom-de-branche>` : Clone une branche spécifique, comme choisir un chapitre particulier du livre.
- `--depth <profondeur>` : Crée une réplique superficielle pour économiser de l'espace magique dans votre sac à dos enchanté.

## 9) `git stash` pour mettre de côté des potions temporaires
`git stash` met de côté des potions sans les "commiter". C'est comme mettre des dragées surprises de Bertie Crochue dans votre poche magique pour plus tard. Pratique pour travailler sur d'autres sorts avant de revenir à votre potion initiale.

**Utilisation :**
```bash
git stash
```

## 10) `git checkout` pour diverses métamorphoses
La commande `git checkout` permet de se transformer entre les branches, de créer de nouvelles branches, et de revenir à des états antérieurs des potions. C'est comme utiliser la cape d'invisibilité pour explorer différents univers magiques du développement.

**Exemples :**
```bash
git checkout [branche]
git checkout -b [nouvelle-branche]
git checkout -- [ingrédient]
```
