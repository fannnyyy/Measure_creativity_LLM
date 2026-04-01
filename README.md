# Compar:IA Analyse de la créativité des modèles de langage

## Maëlys HANOIRE, Gaël GARNIER, Raphaël VIGNAL, Fanny BADOULES

## Contexte

Compar:IA est une plateforme lancée en octobre 2024 permettant à des utilisateurs de comparer les réponses de différents modèles d'IA conversationnels. Le ministère de la Culture cherche à évaluer la place du contenu culturel français dans les réponses de ces modèles. Ce projet propose une approche empirique et critique de cette question via la mesure de la créativité.

### Problématiques

Comment mobiliser les IA culturelles – en particulier via [compar:IA](https://comparia.beta.gouv.fr/) – pour :

* mieux comprendre les usages des IA génératives conversationnelles ;
* explorer les biais, styles, impacts et performances des modèles en français et sur des contenus culturels ;
* proposer des outils, analyses ou visualisations permettant
  d’alimenter la réflexion sur l’ouverture et l’exploitation des données
  culturelles par l’IA.

### Données

https://huggingface.co/collections/comparIA/jeux-de-donnees-compar-ia

```
data/
    comparia-votes/         # votes des utilisateurs (≈150k sur 400k conversations)
    comparia-reactions/     # réactions détaillées (liked, creative, useful, incorrect...)
    comparia-conversations/ # corpus global des conversations (400k+)
```

## Hypothèse et Creativity Index (CI)

### Hypothèse initiale (inadaptée au contexte)

La littérature (Amabile, Kaufman) établit que la valeur est la composante dominante dans le jugement expert de la créativité : β > α > γ. Cette pondération ne tient pas dans Compar:IA pour trois raisons : le paradoxe du jugement non-expert, le biais de longueur comme proxy de valeur perçue, et la faible discriminabilité des jugements révélée par Davidson et la transitivité stochastique.

### Pondération révisée

α (Nouveauté) > γ (Surprise) > β (Valeur)

### Métriques proposées

| Composante | Problème corrigé           | Métrique                               |
| ---------- | ---------------------------- | --------------------------------------- |
| Nouveauté | Biais de longueur + position | MATTR + randomisation A/B               |
| Valeur     | Paradoxe du jugement         | BERTScore (similarité prompt/réponse) |
| Surprise   | Subjectivité non-experte    | Divergent Thinking Score                |

### Calcul

**CI = α · MATTR + γ · DTS + β · BERTScore** avec α > γ > β

### Validation

Bradley-Terry appliqué aux scores CI + vérification de la transitivité stochastique. Avec des scores continus, 0 violation est garanti mathématiquement, ce qui confirme la cohérence du classement. La comparaison avec le classement BT brut permet de vérifier si les biais déformaient effectivement le classement initial.

## Limite principale

Les modèles évalués, français ou internationaux, sont tous entraînés sur les mêmes données. La mesure de créativité reflète leur qualité d'entraînement, pas leur ancrage culturel français. Le CI débiaisé mesure la créativité globale, pas la présence du contenu culturel français.

## Pipeline proposé pour la suite

1. Le ministère constitue un corpus respectueux des droits d'auteur, ancré dans l'héritage culturel français
2. Un modèle est entraîné sur ce corpus
3. Sa créativité est évaluée via le CI sur une interface débiaisée
4. Le grand public intervient sur un corpus pré-filtré par le CI
5. Des experts valident via des questions non biaisées ("Aviez-vous anticipé cette réponse ?")
6. Comparaison avec un modèle étranger → mesure réelle de l'impact du contenu culturel français

## Dépendances

```bash
pip install pandas numpy scipy scikit-learn
```

## Références

- Amabile, T. M. (1982). Social psychology of creativity: A consensual assessment technique. *Journal of Personality and Social Psychology*
- Boden, M. A. (2004). *The Creative Mind: Myths and Mechanisms*
- Davidson, R. R. (1970). On extending the Bradley-Terry model to accommodate ties in paired comparison experiments
