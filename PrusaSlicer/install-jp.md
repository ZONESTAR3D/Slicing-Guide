## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install.md)
[![](../lanpic/ES.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-es.md)
[![](../lanpic/PT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-pt.md)
[![](../lanpic/FR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-fr.md)
[![](../lanpic/DE.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-de.md)
[![](../lanpic/IT.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-it.md)
[![](../lanpic/RU.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-ru.md)
[![](../lanpic/JP.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-jp.md)
[![](../lanpic/KR.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-kr.md)
<!-- [![](./lanpic/SA.png)](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/install-ar.md) -->

----
## PrusaSlicer をダウンロードしてインストールします
### ![](./win.jpg) Windows の場合:
##### ![][VIDEO_INSTALL]
   - 以下のリンクから PrusaSlicer をダウンロードし、PC に解凍します。
     - [:+1: :arrow_down: **PrusaSlicer V2.4.2** をダウンロード][PRUSASLICER_242] (安定版)
     - [:new: :arrow_down: **PrusaSlicer をダウンロード**][PRUSASLICER] (すべて新しいリリース バージョン)

   ### ![](./macos.jpg) MacOS の場合:
   :arrow_down: [**PrusaSlicer with ZONESTAR Profiles dmg file**][PRUSASLICER_IMG] をダウンロードし、PC にインストールします。

   ### ![](./linux.jpg) Linux の場合:
   :arrow_down: [**Prusa Github Page**][PRUSASLICER_RELEASE] から PrusaSlicer をダウンロードし、最新の ZONESTAR 3d プリンター プロファイルをインポートします。

#### ZONESTAR 3D プリンター プロファイルのインポート
- [**:arrow_down:ZONESTAR 3d プリンター プロファイルをダウンロード**](./Profiles.zip) して、PC に解凍します。
- プロファイルを PrusaSlicer ソフトウェアのインストール ディレクトリの "resource/profiles" ディレクトリにコピーします。    
:warning:以前の構成設定を削除する必要がある場合があります。そうしないと、新しいプロファイルを適切に適用できません:warning:    
以前の構成を保存するディレクトリは次のとおりです: ***help>>Show Configuration Floder***。Windows の場合、通常は ***"C:/Users/{your PC name}/AppData/Roaming に保存されます。 /PrusaSlicer[-alpha/beta]"***。 このディレクトリ内のこれらのファイルをすべて削除し、PrusaSlicer を再度実行します。    
![0](./pic/0.png) ![1](./pic/1.png)

-----
## 2. プリンターのセットアップ
- 2.1 prsua-slicer.exe を見つけてクリックして実行します。     
![](pic/run1.png)
- 2.2 プリンターを選択します。「その他のベンダー>>Zonestar FFF>>お使いのプリンターモデル>>終了」。    
![](pic/run2.png)

-----
## 3. プリンターのプリセットを選択します
プリンターのモデル、ホットエンドのタイプ、印刷したい色に応じてプリンター プリセットを選択します。
![](pic/run3.png)
| プリンターシリーズ | 印刷する | ホットエンドのタイプ | プリセット | マシンのデフォルト |
|:----------------------:|:-----------:|:----------------------:|:-----------:|:----------------------:|
| Z5 | 1色または2色 | M2ホットエンド | Z5 + M2 ホットエンド | Z5M2 |
| Z5X | 1色 | ワンカラーホットエンド | Z5X | Z5X |
| Z6 | 1色 | ワンカラーホットエンド | Z6 | Z6 |
| Z8シリーズ | 1色 | 任意 | Z8+1色 | / |
| Z8シリーズ | 1色 | ダイレクトドライブ押出機 | Z8 + DDE | / |
| Z8シリーズ | マルチカラー | M3ホットエンド | Z8 + M3 ホットエンド | Z8S-M3/Z8T/Z8PM3 |
| Z8シリーズ | マルチカラー | M4 ホットエンド | Z8 + M4 ホットエンド | Z8PM4/Z8PM4Pro |
| Z8シリーズ | マルチカラー | E4ホットエンド | Z8 + E4 ホットエンド | / |
| Z9シリーズ | 1色 | 任意 | Z9+1色 | / |
| Z9シリーズ | 1色 | ダイレクトドライブ押出機 | Z8 + DDE | / |
| Z9シリーズ | マルチカラー | M3ホットエンド | Z9 + M3 ホットエンド | Z9M3 |
| Z9シリーズ | マルチカラー | M4 ホットエンド | Z9 + M4 ホットエンド | Z9M4/Z9V5Pro-MK1/2/3 |
| Z9シリーズ | マルチカラー | M4 ホットエンド | Z9 + E4 ホットエンド | Z9V5Pro-MK4 |

(*) マシンのデフォルト: この 3D プリンター モデルで使用されるデフォルトのホットエンド タイプ。

-----
[PRUSASLICER_242]: https://github.com/ZONESTAR3D/Slicing-Guide/releases/tag/PrusaSlicer2.4.2
[PRUSASLICER_IMG]: https://github.com/ZONESTAR3D/Slicing-Guide/releases/tag/2.4.2
[PRUSASLICER]: https://github.com/ZONESTAR3D/Slicing-Guide/releases
[PRUSASLICER_RELEASE]: https://github.com/prusa3d/PrusaSlicer/releases
[VIDEO_INSTALL]: https://github.com/ZONESTAR3D/Slicing-Guide/assets/29502731/ce48a22c-a9aa-45e8-8544-c1c67c7cd021