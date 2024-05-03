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
## :warning: ATTENZIONE PER FAVORE :warning:
### Prestare attenzione a distinguere il tipo di hot end: hot end M4 o hot end E4.
Si prega di prestare attenzione a distinguere il tipo di hot-end: quello utilizzato è **mix color (M4)** hot end o **non mix color (E4)** hot end.    
<u>**Se stampi un file gcode suddiviso su un hot-end M4 con un hot-end E4, potrebbe bloccare l'hot-end e viceversa.**</u>   
Se non sai cosa c'è di diverso tra l'hotend E4 e M4, fai riferimento a [qui][FAQ_M4E4].

-----
## Slicing multi-colore per l'hotend E4
***Prendiamo come esempio Z9V5Pro-MK4***
##### :movie_camera: [**Tutorial video**](https://youtu.be/aets9JZ92iU)
[![](https://img.youtube.com/vi/aets9JZ92iU/0.jpg)](https://www.youtube.com/watch?v=aets9JZ92iU)
### Passaggio 1: scegli le preimpostazioni della stampante "Z9 + E4 hotend"
![](pic/slicingE4-1.png)
### Passaggio 2: caricare i file del modello 3D (file stl/obj/AMF ecc.)
![](pic/loadstl_1.png) ![](pic/loadstl_2.png)     
- :memo: Di solito, il "modello diviso" è necessario per stampare file di modelli 3D a più colori, ovvero un modello 3D è stato diviso in più file STL in base ai colori e questi file utilizzano la stessa posizione delle coordinate di origine in modo che possano essere uniti correttamente.    
- :star2: PrusaSlicer ha una nuova potente funzionalità, può dipingere un file di modello 3D in più colori, per i dettagli, fare riferimento a :movie_camera: [**Guida allo slicing - Converti file 3D di un colore in più colori**](https://youtu.be/Yx4fKDRGEJ4)  
##### [![](https://img.youtube.com/vi/Yx4fKDRGEJ4/0.jpg)](https://www.youtube.com/watch?v=Yx4fKDRGEJ4)
### Passaggio 3: scegli il tipo di filamento e imposta il colore del filamento
![](pic/filament_color.png)
### Passaggio 4: assegna gli estrusori a parti diverse
![](pic/assign_extruder.png)
### Passaggio 5: ridimensiona, taglia, ruota e sposta il modello 3D se necessario
![](pic/slicing_adjust.png)
### Passaggio 6: definire le impostazioni di stampa
#### Imposta "Retrazione" e "Retrazione quando l'utensile è disabilitato"
Si prega di distinguere tra 2 tipi di ***"Retrazione"***:
1. Il solito ***"Retrazione"*** si riferisce alla stampa di fili sottili dello stesso colore, quando la stampante si sposta da un punto a un altro, i fili sottili vengono tirati indietro per una certa distanza per ridurre il deflusso del filo sottile ugello filettato. :warning: ***"Lunghezza di retrazione"*** deve essere inferiore a 10 mm per l'hot end E4.    
2. ***"Retrazione quando lo strumento è disabilitato"*** si riferisce al processo di estrazione del filo sottile dall'estremità calda quando la stampante passa da un filo sottile a un altro. :warning: ***"Retrazione quando l'utensile è disabilitato"*** dovrebbe essere impostato su 0 perché abbiamo aggiunto ***"Personalizza codici G"*** nel ***"Cambia codice Gutensile"*** a gestire in modo più efficace il processo di commutazione dei filamenti. Per ulteriori dettagli, fare riferimento a [**tool-change-gcode**][TOOLCHANGE_GCODE].    
![](pic/slicingE4-4.jpg)

#### Imposta l'altezza del livello, la velocità di stampa, il supporto, il riempimento, ecc.
![](pic/slicing_set.png)    
È necessario impostare questi parametri in base alla forma del modello e ai requisiti di qualità di stampa. Anche per alcuni modelli, la stampa non può essere completata normalmente senza supporto. Per i dettagli fare riferimento a:   
- :point_right: [**Introduzione a PrusaSlicer**](https://help.prusa3d.com/article/general-info_1910)   
- :point_right: [**Manuale utente Slic3r**](https://manual.slic3r.org/)

### Passaggio 7: imposta i parametri per *wipe tower*
Potresti notare che apparirà un quadrato nella figura tagliata, che si chiama "Wipe tower" in PrusaSlicer. Poiché per la stampante multicolore, quando si cambia estrusore, ci sono ancora i filamenti del colore precedente all'interno dell'hotend, è necessario pulirli prima di stampare un altro colore.    
![](pic/wipe_tower.png)    
Per ottenere un migliore effetto pulente e ridurre al minimo lo spreco di filamento, possiamo impostare il volume di spurgo in base ai diversi colori. Consultare la tabella seguente, le colonne mostrano l'estrusore precedente e le righe mostrano l'estrusore successivo da stampare. Quando passiamo dall'estrusore con filamenti di colore più chiaro all'estrusore con filamenti di colore più scuro, possiamo impostare un "volume di spurgo" più piccolo. Al contrario, quando passiamo dall'estrusore con filamenti di colore più scuro all'estrusore con filamento di colore più scuro, dobbiamo impostare un "volume di spurgo" maggiore.    
:warning: ***La lunghezza di retrazione deve essere inferiore a 10 mm, altrimenti potrebbe causare il blocco dell'hotend.***
:star: Per l'hotend E4, sono rimasti pochi filamenti nell'hotend, quindi possiamo utilizzare un volume di spurgo più piccolo sulla torre di pulizia.
![](pic/slicingE4-2.png)
### Passaggio 8: affettare
![](pic/slicing_go.png)
### Passaggio 9: visualizzare l'anteprima del risultato suddiviso (file gcode), quindi salvare nel file gcode sul PC e quindi copiare sulla scheda SD   
![](pic/slicing_save.png)    
:star: Quando visualizzi l'anteprima del file gcode, puoi vedere che sul lato del letto appariranno alcune linee di stampa aggiuntive, che servono per precaricare i filamenti. Per informazioni dettagliate su come precaricare il filamento, fare riferimento a [**:book: Guida per l'utente dell'hotend E4**][E4_USERGUIDE].   
![](pic/slicingE4-3.png)

-----
## Appendice
### Introduzione del codice G personalizzato
Se hai installato correttamente il file dei profili della stampante 3D ZONESTAR, vedrai che abbiamo aggiunto alcuni codici gcode in ***"Impostazioni stampante>>Codice G personalizzato"***.  
Per i dettagli sul "codice G personalizzato", fare riferimento a [:book: **Descrizione del codice G personalizzato**](./Custom_Gcode.md)   
![](./pic/Custom_Gcode.jpg)
### [:book: Guida all'uso dell'hot end E4][E4_USERGUIDE]
### [:arrow_down: Prova i file gcode per l'hot end E4][E4_GCODE]