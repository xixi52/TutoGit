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

## 11) `git pull` pour rappeler et fusionner les sorts distants
`git pull` rappelle les derniers sorts d'un grimoire distant et les fusionne avec votre copie locale. C'est essentiel pour maintenir l'harmonie magique dans le royaume du code, un peu comme une séance de sorts conjoints à Poudlard.

**Utilisation :**
```bash
git pull origin <nom-de-branche>
```

## 12) `git log` pour explorer l'historique des sorts
`git log` vous permet d'explorer l'historique des sorts, affichant les commits avec leurs auteurs, dates et messages associés. Utile pour retracer le chemin parcouru dans le monde magique du développement.

**Utilisation :**
```bash
git log
```

## 13) `git remote` pour gérer les grimoires distants
`git remote` vous permet de gérer les grimoires distants. Vous pouvez ajouter, afficher ou supprimer des liens vers d'autres royaumes magiques. C'est un peu comme avoir des Portoloins vers d'autres écoles de magie.

**Utilisation :**
```bash
git remote add <nom> <url>
git remote -v
git remote rm <nom>
```

## 14) `git fetch` pour récupérer les sorts distants
`git fetch` récupère les sorts distants sans fusionner automatiquement avec votre copie locale. C'est utile lorsque vous voulez voir ce qui se trame dans d'autres coins du royaume avant de fusionner, un peu comme jeter un œil dans la Pens

ine.

**Utilisation :**
```bash
git fetch <grimoire-distant>
```

## 15) `git rebase` pour réorganiser l'ordre des sorts
`git rebase` vous permet de réorganiser l'ordre des sorts en les appliquant les uns après les autres. C'est une manière élégante de maintenir un historique de sorts linéaire, un peu comme enseigner un sort de métamorphose à une classe de première année.


**Utilisation :**
```bash
git rebase <branche-source>
```

## 16) `git blame` pour découvrir l'auteur d'un sort
`git blame` vous révèle l'auteur de chaque ligne dans un fichier, vous aidant à identifier les responsables des sorts particuliers. C'est comme si le Miroir du Risèd vous montrait qui est le meilleur sorcier pour chaque ligne de code.

**Utilisation :**
```bash
git blame <fichier>
```

## 17) `git cherry-pick` pour appliquer des sorts spécifiques
`git cherry-pick` permet d'appliquer des commits spécifiques d'une branche à une autre. Comme choisir des sorts spécifiques dans un grimoire et les utiliser ailleurs, un peu comme transplanter des mandragores.

**Utilisation :**
```bash
git cherry-pick <hash-du-sort>
```

## 18) `git reset` pour annuler des sorts
`git reset` annule les sorts en modifiant la position actuelle de la branche. Utilisez avec prudence, car cela peut altérer le flux temporel de votre royaume magique. C'est comme remonter le temps avec un Retourneur de Temps, mais pour votre code.

**Utilisation :**
```bash
git reset <sort>
```

## 19) `git bisect` pour traquer l'origine d'un sort maléfique
`git bisect` vous aide à traquer l'origine d'un problème en effectuant une recherche binaire dans l'historique des sorts. C'est comme chercher le Horcruxe responsable des problèmes dans votre code.

**Utilisation :**
```bash
git bisect start
git bisect bad
git bisect good <commit>
```

## 20) `git remote prune` pour nettoyer les liens inutilisés
`git remote prune` nettoie les liens vers des grimoires distants qui n'existent plus. Une manière de maintenir la propreté dans votre royaume magique, un peu comme le Balai de Frêne qui nettoie le terrain de Quidditch.

**Utilisation :**
```bash
git remote prune <grimoire-distant>
```

Avec ces nouvelles commandes, votre baguette git devrait être prête à manier une variété de sorts pour toutes les situations magiques dans le royaume du développement logiciel. 🌟🔮
En résumé, Git offre des fonctionnalités magiques pour la gestion de versions, la collaboration, et la sauvegarde des potions. Ces commandes magiques sont essentielles pour un flux de travail envoûtant. 🌟🔮 N'oubliez pas de jeter une pièce de monnaie dans le puits magique avant chaque `commit` pour la bonne fortune! Et rappelez-vous, le stagiaire du code c'est un peu comme le Choixpeau Magique, il choisit toujours la bonne branche. 🧙‍♂️✨
