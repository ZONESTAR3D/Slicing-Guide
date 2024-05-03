----
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuide_M4.md)
[![](../lanpic/ES.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-es.md)
[![](../lanpic/PT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-pt.md)
[![](../lanpic/FR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-fr.md)
[![](../lanpic/DE.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-de.md)
[![](../lanpic/IT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-it.md)
[![](../lanpic/RU.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-ru.md)
[![](../lanpic/JP.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-jp.md)
[![](../lanpic/KR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-kr.md)
<!-- [![](./lanpic/SA.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/PrusaSlicerGuideM4-ar.md) -->


----
## :warning: ATTENTION S'IL VOUS PLAÎT :warning:
### Veuillez faire attention à distinguer le type d'extrémité chaude
Veuillez faire attention à distinguer le type d'extrémité chaude que vous avez utilisé : **mix color (M4)** hot end ou **non mix color (E4)** hot end.
<u>**Si vous imprimez un fichier Gcode découpé sur le hot end M4 avec un hot end E4, cela peut bloquer le hot end, vice versa.**</u>
Si vous ne savez pas ce qui est différent entre les hotend E4 et M4, veuillez vous référer à [**ici**][FAQ_M4E4].

----
## Découpage multicolore pour hotend M4
#### :loudspeaker: ce manuel est pris comme exemple du Z9V5Pro-MK3
### :movie_camera: [**Tutoriel vidéo**](https://youtu.be/_Ww2RFGlLNA)
[![](https://img.youtube.com/vi/_Ww2RFGlLNA/0.jpg)](https://www.youtube.com/watch?v=_Ww2RFGlLNA)

### Étape 1: choisissez les préréglages d'imprimante "Z9 + M4 hotend"
![](./pic/slicingM4-1.png)
### Étape 2: charger les fichiers de modèle 3D (fichier stl/obj/AMF etc.)
![](./pic/loadstl_1.png) ![](./pic/loadstl_2.png)
- :memo: Habituellement, un "modèle divisé" est nécessaire pour imprimer des fichiers de modèle 3D multicolores, c'est-à-dire qu'un modèle 3D a été divisé en plusieurs fichiers STL en fonction des couleurs, et ces fichiers utilisent la même position de coordonnées d'origine afin qu'ils puissent être fusionné correctement.
- :star2: PrusaSlicer a une nouvelle fonctionnalité puissante, il peut peindre un fichier de modèle 3D en plusieurs couleurs, pour plus de détails, veuillez vous référer à :movie_camera: [**Guide de découpage - Convertir un fichier 3D d'une couleur en plusieurs couleurs**](https://youtu.be/Yx4fKDRGEJ4).
##### [![](https://img.youtube.com/vi/Yx4fKDRGEJ4/0.jpg)](https://www.youtube.com/watch?v=Yx4fKDRGEJ4)

### Étape 3: Choisissez le type de filament et définissez la couleur du filament
![](./pic/filament_color.png)
### Étape 4: Attribuer les extrudeuses à différentes pièces
![](./pic/assign_extruder.png)
### Étape 5: Redimensionner, couper, faire pivoter, déplacer le modèle 3D si besoin
![](./pic/slicing_adjust.png)
### Étape 6: Définir les paramètres d'impression
#### :warning: Veuillez noter que la "Rétraction lorsque l'outil est désactivé" doit être définie sur 0.
![](./pic/switch_length.jpg)
#### définir la hauteur de la couche, la vitesse d'impression, le support, le remplissage, etc.
![](./pic/slicing_set.png)
Vous devez définir ces paramètres en fonction de la forme du modèle et de vos exigences en matière de qualité d'impression. Même pour certains modèles, l'impression ne peut pas être effectuée normalement sans assistance. Pour plus de détails, veuillez consulter :
- :point_right: [**Présentation de PrusaSlicer**](https://help.prusa3d.com/article/general-info_1910)
- :point_right: [**Manuel d'utilisation Slic3r**](https://manual.slic3r.org/)
  
### Étape 7: Définir les paramètres de la "tour d'essuyage"
Vous remarquerez peut-être qu'un carré apparaîtra dans la figure découpée, appelée "Wipe tower" dans PrusaSlicer. Parce que pour l'imprimante multicolore, lors du changement d'extrudeuse, il y a toujours les filaments de couleur précédents à l'intérieur du hotend, il doit être propre avant d'imprimer une autre couleur.
###### ![](./pic/wipe_tower.png)
Afin d'obtenir un meilleur effet de nettoyage et de minimiser les déchets de filament, nous pouvons régler le volume de purge en fonction de différentes couleurs. Veuillez consulter le tableau suivant, les colonnes montrent l'extrudeuse précédente et les lignes montrent la prochaine extrudeuse à imprimer. Lorsque nous passons de l'extrudeuse avec des filaments de couleur plus claire à l'extrudeuse avec des filaments de couleur plus foncée, nous pouvons définir un "volume de purge" plus petit. Au contraire, lorsque nous passons de l'extrudeuse avec des filaments de couleur plus foncée à l'extrudeuse avec des filaments de couleur plus claire, nous devons définir un "volume de purge" plus grand.
###### ![](./pic/slicingM4-2.png)
### Étape 8: Découper
![](./pic/slicing_go.png)
### Étape 9: Prévisualisez le résultat découpé (fichier gcode), puis enregistrez-le dans le fichier gcode sur votre PC, puis copiez-le sur la carte SD
![](./pic/slicing_save.png)

----
## Comment imprimer plus de 4 couleurs à l'aide du hot end M4
L'extrémité chaude de mélange de couleurs M4 peut mélanger 2 à 4 filaments d'extrudeuses réels pour produire un nouveau filament de couleur, et ce nouveau filament de couleur peut être utilisé comme une nouvelle extrudeuse (appelée **"extrudeuse virtuelle"**), les étapes de fonctionnement sont les suivantes :
***L'exemple suivant montre comment configurer 6 extrudeuses : 4 extrudeuses réelles et 2 extrudeuses virtuelles. E5 est mélangé à 50% E1 et 50% E2, E6 est mélangé à 50% E3 et 50% E4.***
### Étape 1 : Ajouter des extrudeuses virtuelles
###### ![](./pic/slicingM4_6c_1.png)     
:warning: Nous vous suggérons de **enregistrer**<sup>1</sup> les paramètres dans un **nouveau profil**<sup>2</sup>.

### Étape 2 : Définir le taux de mélange de la nouvelle « extrudeuse virtuelle »
#### Ajoutez les commandes "Définir le taux de mélange" à "Démarrer Gcode".
###### ![](./pic/slicingM4_6c_2.png)
:warning: Nous suggérons que ces g-codes soient placés au début du "Démarrer le G-code".
>
     ;Définir le taux de mélange
     ;E5 = 50%E1 + 50%E2
     M163 S0P50
     M163 S1P50
     M163 S2P0
     M163 S3P0
     M164 S4
     ;E6 = 50%E3 + 50%E4
     M163 S0P0
     M163 S1P0
     M163 S2P50
     M163 S3P50
     M164 S5

#### :memo: Introduction aux commandes "M163" et "M164"
>
     M163: Définir un seul facteur de mélange pour une extrudeuse de mélange, doit être suivi de M164 pour les normaliser et les valider.
      S[index] L'index du canal (extrudeur réel) à définir
      P[float] La valeur de mélange de (0,0 ~ 100,0)
      R Réinitialiser tous les paramètres de l'extrudeuse de mélange par défaut

     M164: Normaliser et valider le taux de mélange sur une extrudeuse virtuelle.
      S[index] L'extrudeuse virtuelle à stocker
  
     Normaliser: mettre à l'échelle automatiquement les valeurs du rapport de mélange de chaque extrudeuse pour répondre aux exigences de la machine

### Étape 3: Attribuez les nouvelles extrudeuses virtuelles au modèle 3D et au découpage
Vous pouvez désormais attribuer 6 extrudeuses au modèle 3D, le processus de découpage est exactement le même que pour les 4 extrudeuses.
1. Choisissez le profil d'imprimante.
2. Définissez la couleur du filament des nouveaux extrudeurs.
3. Attribuez l'extrudeuse à la partie du modèle 3D.
###### ![](./pic/slicingM4_6c_3.png)

----
## Annexe
### [:book: guide d'utilisation du hotend M4](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/M4)
### [:book: Guide d'utilisation de la fonctionnalité de mélange des couleurs](https://github.com/ZONESTAR3D/Document-and-User-Guide/tree/master/Mixing_Color)
### [:arrow_down:Test des fichiers gcode pour le hot end M4](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/test_gcode/M4/readme.md)


----
[FAQ_M4E4]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/FAQ_M4E4.md


