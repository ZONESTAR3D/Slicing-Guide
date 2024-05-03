[FAQ_M4E4]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/FAQ_M4E4.md
[TOOLCHANGE_GCODE]: https://github.com/ZONESTAR3D/Slicing-Guide/blob/master/PrusaSlicer/Custom_Gcode.md#tool-change-g-code
[E4_USERGUIDE]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/E4/User_guide
[E4_GCODE]: https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/test_gcode/E4/readme.md

----
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme.md)
[![](../lanpic/ES.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-es.md)
[![](../lanpic/PT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-pt.md)
[![](../lanpic/FR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-fr.md)
[![](../lanpic/DE.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-de.md)
[![](../lanpic/IT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-it.md)
[![](../lanpic/RU.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-ru.md)
[![](../lanpic/JP.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-jp.md)
[![](../lanpic/KR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-kr.md)
<!-- [![](./lanpic/SA.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/readme-ar.md) -->

----
## :warning: ATTENTION S'IL VOUS PLAÎT :warning:
### Veuillez faire attention à distinguer le type de hot end : Hot end M4 ou E4 hot end.
Veuillez faire attention à distinguer le type d'extrémité chaude que vous avez utilisé: **mix color (M4)** hot end ou **non mix color (E4)** hot end.
<u>**Si vous imprimez un fichier Gcode découpé sur le hot end M4 avec un hot end E4, cela peut bloquer le hot end, vice versa.**</u>
Si vous ne savez pas ce qui est différent entre les hotend E4 et M4, veuillez vous référer à [ici][FAQ_M4E4].

-----
## Découpage multicolore pour le hotend E4
***Prenons l'exemple du Z9V5Pro-MK4***
##### :movie_camera: [**Tutoriel vidéo**](https://youtu.be/aets9JZ92iU)
[![](https://img.youtube.com/vi/aets9JZ92iU/0.jpg)](https://www.youtube.com/watch?v=aets9JZ92iU)
### Étape 1: choisissez les préréglages d'imprimante "Z9 + E4 hotend"
![](pic/slicingE4-1.png)
### Étape 2: charger les fichiers de modèle 3D (fichier stl/obj/AMF etc.)
![](pic/loadstl_1.png) ![](pic/loadstl_2.png)     
- :memo: Habituellement, un "modèle divisé" est nécessaire pour imprimer des fichiers de modèle 3D multicolores, c'est-à-dire qu'un modèle 3D a été divisé en plusieurs fichiers STL en fonction des couleurs, et ces fichiers utilisent la même position de coordonnées d'origine afin qu'ils puissent être fusionné correctement.
- :star2: PrusaSlicer a une nouvelle fonctionnalité puissante, il peut peindre un fichier de modèle 3D en plusieurs couleurs, pour plus de détails, veuillez vous référer à :movie_camera: [**Guide de découpage - Convertir un fichier 3D d'une couleur en plusieurs couleurs**](https://youtu.be/Yx4fKDRGEJ4)
##### [![](https://img.youtube.com/vi/Yx4fKDRGEJ4/0.jpg)](https://www.youtube.com/watch?v=Yx4fKDRGEJ4)
### Étape 3: Choisissez le type de filament et définissez la couleur du filament
![](pic/filament_color.png)
### Étape 4: Attribuer les extrudeuses à différentes pièces
![](pic/assign_extruder.png)
### Étape 5: Redimensionner, couper, faire pivoter, déplacer le modèle 3D si besoin
![](pic/slicing_adjust.png)
### Étape 6: Définir les paramètres d'impression
#### Définir "Rétraction" et "Rétraction lorsque l'outil est désactivé"
Veuillez distinguer 2 types de ***« Rétractation »*** :
1. Le *** habituel « Rétraction » *** fait référence à l'impression de fils fins de la même couleur, lorsque l'imprimante se déplace d'un point à un autre, les fils fins sont tirés un peu en arrière pour réduire la sortie des fils fins. buse filetée. :warning: ***"Longueur de rétraction"*** doit être inférieur à 10 mm pour l'extrémité chaude E4.
2. ***« Rétraction lorsque l'outil est désactivé »*** fait référence au processus de retrait du fil fin hors de l'extrémité chaude lorsque l'imprimante passe d'un fil fin à un autre. :warning: ***"Rétraction lorsque l'outil est désactivé"*** doit être défini sur 0 car nous avons ajouté ***"Personnaliser les codes G"*** dans le ***"Changement d'outil Gcode"*** à gérer plus efficacement le processus de changement de filament. Pour plus de détails, veuillez vous référer à [**tool-change-gcode**][TOOLCHANGE_GCODE].     
![](pic/slicingE4-4.jpg)

#### Définissez la hauteur de la couche, la vitesse d'impression, le support, le remplissage, etc.
![](pic/slicing_set.png)     
Vous devez définir ces paramètres en fonction de la forme du modèle et de vos exigences en matière de qualité d'impression. Même pour certains modèles, l'impression ne peut pas être effectuée normalement sans assistance. Pour plus de détails, veuillez consulter:
- :point_right: [**Présentation de PrusaSlicer**](https://help.prusa3d.com/article/general-info_1910)   
- :point_right: [**Manuel d'utilisation Slic3r**](https://manual.slic3r.org/)

### Étape 7: Définir les paramètres de la *tour de nettoyage*
Vous remarquerez peut-être qu'un carré apparaîtra dans la figure découpée, appelée "Wipe tower" dans PrusaSlicer. Parce que pour l'imprimante multicolore, lors du changement d'extrudeuse, il y a toujours les filaments de couleur précédents à l'intérieur du hotend, il doit être propre avant d'imprimer une autre couleur.    
![](pic/wipe_tower.png)     
Afin d'obtenir un meilleur effet de nettoyage et de minimiser les déchets de filament, nous pouvons régler le volume de purge en fonction de différentes couleurs. Veuillez consulter le tableau suivant, les colonnes montrent l'extrudeuse précédente et les lignes montrent la prochaine extrudeuse à imprimer. Lorsque nous passons de l'extrudeuse avec des filaments de couleur plus claire à l'extrudeuse avec des filaments de couleur plus foncée, nous pouvons définir un "volume de purge" plus petit. Au contraire, lorsque nous passons de l'extrudeuse avec des filaments de couleur plus foncée à l'extrudeuse avec des filaments de couleur plus foncée, nous devons définir un "volume de purge" plus grand.    
:warning: ***La longueur de rétraction doit être inférieure à 10 mm, sinon cela pourrait entraîner un blocage de la hotend.***
:star: Pour le hotend E4, il reste peu de filaments dans l'extrémité chaude, nous pouvons donc utiliser un volume de purge plus petit sur la tour d'essuyage.
![](pic/slicingE4-2.png)
### Étape 8 : Découper
![](pic/slicing_go.png)
### Étape 9 : Prévisualisez le résultat découpé (fichier gcode), puis enregistrez-le dans le fichier gcode sur votre PC, puis copiez-le sur la carte SD   
![](pic/slicing_save.png)   
:star: Lors de la prévisualisation du fichier gcode, vous pouvez voir que des lignes d'impression supplémentaires apparaîtront sur le côté du lit, destinées au préchargement des filaments. Pour plus de détails sur la façon de précharger le filament, veuillez vous référer au [**:book: E4 Hotend user guide**][E4_USERGUIDE].    
![](pic/slicingE4-3.png)

-----
## Annexe
### Introduction de la personnalisation du G-code
Si vous avez correctement installé le fichier Profils de l'imprimante 3D ZONESTAR, vous verrez que nous avons ajouté quelques codes gcode dans ***"Paramètres de l'imprimante>>G-code personnalisé"***.
Pour plus de détails sur le « G-code personnalisé », veuillez vous référer à [:book: **Description du Gcode personnalisé**](./Custom_Gcode.md)   
![](./pic/Custom_Gcode.jpg)
### [:book: Guide d'utilisation du hot end E4][E4_USERGUIDE]
### [:arrow_down: Tester les fichiers gcode pour le hot end E4][E4_GCODE]