# Alignment free - TP 1

L'objectif du TP est de comparer 5 especes de bactéries entre elles. Vous trouverez les données en suivant [ce lien](https://we.tl/t-ACiDxJko7s)

## Composer le TP

Vous devez forker ce projet puis compléter ses fonctions. Le rendu sera le dépot git dans lequel vous aurrez forké.

Le but est d'obtenir toutes les distances paire Ã  paire des différentes bactéries. Vous devez compléter le README pour y afficher la matrice des distances des bactéries. Vous devez également y indiquer le temps d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. Pour cela vous pouvez utiliser la commande `/usr/bin/time -v`.

En observant les distances obtenues, que pouvez-vous dire des espèces présentes dans cet échantillon ?

## Résultats

Temps d'éxécution :

Espace mémoire maximale :

##### Comparison 1

-   GCF_000006945.2_ASM694v2_genomic.fna and GCF_008244785.1_ASM824478v1_genomic.fna
-   Jaccard distance : 0.9377600401208281

##### Comparison 2

-   GCF_000006945.2_ASM694v2_genomic.fna and GCF_014892695.1_ASM1489269v1_genomic.fna

-   Jaccard distance : 0.001759209614977323

##### Comparison 3

-   GCF_000006945.2_ASM694v2_genomic.fna and GCF_020526745.1_ASM2052674v1_genomic.fna

-   Jaccard distance : 0.0190920175607085

##### Comparison 4

-   GCF_000006945.2_ASM694v2_genomic.fna and GCF_020535205.1_ASM2053520v1_genomic.fna
-   Jaccard distance : 0.017911091864786097

##### Comparison 5

-   GCF_008244785.1_ASM824478v1_genomic.fna and GCF_014892695.1_ASM1489269v1_genomic.fna

-   Jaccard distance : 0.0017680275381898479

##### Comparison 6

-   GCF_008244785.1_ASM824478v1_genomic.fna and GCF_020526745.1_ASM2052674v1_genomic.fna

-   Jaccard distance : 0.019325665509274746

##### Comparison 7

-   GCF_008244785.1_ASM824478v1_genomic.fna and GCF_020535205.1_ASM2053520v1_genomic.fna
-   Jaccard distance : 0.0180139298467147

##### Comparison 8

-   GCF_014892695.1_ASM1489269v1_genomic.fna and GCF_020526745.1_ASM2052674v1_genomic.fna

-   Jaccard distance : 0.001946634861989756

##### Comparison 9

-   GCF_014892695.1_ASM1489269v1_genomic.fna and GCF_020535205.1_ASM2053520v1_genomic.fna

-   Jaccard distance : 0.0039007884600128213

##### Comparison 10

-   GCF_020526745.1_ASM2052674v1_genomic.fna and GCF_020535205.1_ASM2053520v1_genomic.fna

-   Jaccard distance : 0.613905100121123

## INTERPRETATION

Lorsque la distance de jaccard est élevée entre deux espèces, cela signifie que celles-ci ont beaucoup de kmers en commun et donc que leurs génomes partagent beaucoup de similarité. Nous pouvons voir que c'est le cas pour la comparaison 1 et 10. Notamment, pour la comparaison 1 où la distance de jaccard est de 0.93776 et donc ces 2 espèces sont les plus similaires. Nous pouvons émettre l'hypothèse que ces deux espèces sont proches phygénétiquement et ont un ancêtre commun récent. Alors que pour les autres espèces avec une distance faible, celles-ci partagent probablement un ancêtre commun plus éloigné.
