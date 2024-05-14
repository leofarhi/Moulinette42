### Moulinette 42 - Février 2024

Cette moulinette a été conçue pendant la piscine de février 2024 à l'école 42.

Il ne s'agit pas de la vraie moulinette, mais d'une tentative de reproduction de l'originale basée sur des suppositions et des indices.

Elle ne propose pas de solutions aux exercices, elle se contente de comparer vos résultats avec ceux attendus ou supposés.

Il est possible que des erreurs subsistent (personnellement, ceux que je publie sont ceux où j'ai eu 100 %). De plus, l'administration peut avoir modifié les consignes entre-temps.

#### Installation :

Téléchargez le dépôt sur votre ordinateur et assurez-vous d'avoir Python 3 installé.
Ensuite, je vous conseille de créer un alias comme indiqué ci-dessous :

```bash
alias mln='python3 /home/<emplacement>/Moulinette42/Moulinette.py'
```

#### Utilisation :

La moulinette s'intègre à votre projet (à la racine du dépôt git du projet) sans y apporter de modifications.
Elle copie vos fichiers dans un dossier temporaire pour effectuer ses tests.

Dans votre dépôt, utilisez `pwd` pour obtenir le chemin absolu. Ensuite, exécutez `mln all` pour afficher toutes les corrections que peut apporter la moulinette.
Par exemple, pour corriger le C_00 de la piscine, utilisez :

```bash
mln Piscine.C_00
```

Lors de la première exécution de la commande, le programme vous demandera le chemin de votre dépôt (que vous avez obtenu avec `pwd`).
En cas de problème de répertoire, vous pouvez les modifier dans le fichier `config.json` dans le dossier de la moulinette.

Vous pouvez lancer les exercices d'un projet indépendamment en utilisant par exemple :

```bash
mln Piscine.C_00 ex00
```
