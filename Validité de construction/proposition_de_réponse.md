# Creativity Index (CI)

## Hypothèse initiale

**Créativité = α · Nouveauté + λ · Valeur + γ · Surprise**

La littérature (Amabile, Kaufman, paradoxe du jugement) établit que β (valeur) est la composante la plus pondérée par des experts. Cependant, trois facteurs propres à Compar:IA suggèrent que cette pondération ne tient pas dans ce contexte.

## Pourquoi λ dominant ne tient pas dans Compar:IA

**Paradoxe du jugement** : les non-experts sous-évaluent la valeur fonctionnelle et surpondèrent la nouveauté perceptuelle. La nouveauté est plus saillante visuellement et demande moins d'expertise pour être détectée les non-experts sont meilleurs juges de la nouveauté que de la valeur.

**Biais de longueur** : une réponse longue semble plus travaillée, plus utile. Ce biais agit comme un proxy de valeur perçue et gonfle artificiellement β, indépendamment de la qualité créative réelle.

**Transitivité stochastique + Davidson** : les jugements sont peu discriminants globalement. C'est la signature du jugement non-expert qui ne s'appuie pas sur un critère stable comme la valeur experte. La composante la plus stable dans les préférences est donc celle qui est la plus immédiatement perceptible, soit la nouveauté et la surprise. À noter que la transitivité stochastique sert aussi de critère de qualité de notre mesure : si l'index CI vérifie la transitivité forte, alors le classement est cohérent et fiable.

## Métriques choisies pour pallier ces problèmes

| Composante | Problème                            | Métrique                 | Pourquoi                                                                                                                                                          |
| ---------- | ------------------------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Valeur     | Paradoxe du jugement                 | BERTScore                 | Mesure la similarité sémantique entre la réponse et le prompt — évalue si la réponse est pertinente et complète sans dépendre d'un jugement humain expert |
| Nouveauté | Biais de longueur + position         | MATTR + randomisation A/B | Diversité lexicale normalisée sur fenêtres fixes, indépendante de la longueur. La randomisation A/B corrige le biais de position                              |
| Surprise   | Subjectivité du jugement non-expert | Divergent Thinking Score  | Mesure la distance sémantique entre concepts associés, indépendamment de la fluidité du texte                                                                 |

## Calcul du CI

**CI = α · MATTR + γ · DTS + λ · BERTScore**

Avec **α > γ > λ**

## Validation de l'index

**Étape 1** 

 Appliquer Bradley-Terry sur les scores CI et vérifier la transitivité stochastique : si A > B et B > C alors A > C.

- 0 violations → index cohérent. Avec des scores continus c'est toujours garanti mathématiquement — contrairement au vote humain qui peut dire A > B > C mais C > A.
- Violations → pondération à revoir.

**Étape 2** 

Comparer le classement CI au classement Bradley-Terry calculé directement depuis les votes Compar:IA. 

Si les deux classements diffèrent, cela montre que les biais déformaient effectivement le classement brut.

## Limite et mise en contexte

Cette mesure débiaisée ne répond pas directement à la question du ministère : quelle place le contenu et l'offre culturelle français ont dans les réponses des IA conversationnelles ?

Le problème observé est que les modèles évalués, français ou internationaux, sont entraînés sur les mêmes données. Même si certains modèles ont des données plus multilingues, la mesure de créativité reflète leur qualité d'entraînement, pas leur diversité culturelle. Le classement obtenu est global et pas spécifiquement lié à la culture française.

Notre mesure débiaisée reste néanmoins prête à être réutilisée dans un contexte mieux adapté. Elle évite le biais de position via une nouvelle présentation des réponses, le biais de longueur via le MATTR, et s'appuie sur l'état de l'art pour chaque métrique. Elle est équilibrée pour un test grand public.

## Pipeline proposé

- Le ministère crée un corpus respectueux des droits d'auteur, riche linguistiquement et ancré dans l'héritage culturel français.
- Un modèle est entraîné sur ce corpus.
- Sa créativité est ensuite évaluée via notre CI sur une interface débiaisée.
- Le grand public intervient sur un corpus pré-filtré par le CI, et des experts valident via des questions non biaisées comme "Aviez-vous anticipé cette réponse ?".
- Comparé à un modèle étranger, ce protocole permettrait de vraiment mesurer l'impact et la place du contenu culturel français dans les réponses des IA conversationnelles.
