
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../../lanpic/EN.png)](./readme.md)
[![](../../lanpic/ES.png)](./readme-es.md)
[![](../../lanpic/PT.png)](./readme-pt.md)
[![](../../lanpic/FR.png)](./readme-fr.md)
[![](../../lanpic/DE.png)](./readme-de.md)
[![](../../lanpic/IT.png)](./readme-it.md)
[![](../../lanpic/RU.png)](./readme-ru.md)
[![](../../lanpic/JP.png)](./readme-jp.md)
[![](../../lanpic/KR.png)](./readme-kr.md)
[![](../../lanpic/SA.png)](./readme-ar.md)

----
#  Gradient Mix Tool 渐变混合工具
**渐变混合工具**是一款 GCode 后处理软件，可自动调整挤出机在打印高度（Z 轴方向）的混合比例。可应用于 ZONESTAR 混色彩色 3D 打印机。
#### :warning: 此工具目前仅适用于 ZONESTAR 4 挤出机混色 3D 打印机（M4）。
#### [:arrow_down: 下载](https://github.com/ZONESTAR3D/Slicing-Guide/releases/tag/gmt-v1.2) 

----
## :book:用户指南
**渐变混合工具**允许设置最多 6 个 ***Process***，每个Process可以应用于导入的GCode文件中使用的VTools之一，设置应用的高度范围以及开始和结束挤出机混合比。当以下情况时，可以同时应用多个过程：
- 不同的Process可用于不同Z范围内的同1个VTool。
**或者**
- 不同的Process可用于相同Z范围但是不同的VTools上。
### 使用说明
#### 1. 下载软件并将其解压到您的PC上（仅一个 exe 文件）。
#### 2. 执行 GradientMixToolVx.exe。
![](1.jpg)
#### 3. 加载 Gcode 文件。
软件将自动解析导入的 Gcode 文件以获取模型的高度、层厚度、使用的 VTool 等，并弹出提示框显示这些信息。
![](2.jpg)
#### 4. 设置“Process”的参数。
![](3.jpg)
#### 5. 单击“Genarate”按钮生成新的 gcode文件。
您可以在***Export***窗口中查看添加的Gcode命令，如下图。
![](4.jpg)      
点击滚动条的UP和DOWN按钮可以快速定位到上一个/下一个Gcode插入位置，如下图。
![](5.jpg)
#### 6. 单击“Export”按钮导出并保存到新的Gcode文件。
接下来，您就可以在ZONESTR混色3D打印机上打印导出的Gcode文件。

----
### 例子
#### 例子:one: [螺旋花瓶 :arrow_down:](./SpiralVase.zip)
此例子显示如何将单色螺旋花瓶 Gcode 文件转换为多渐变 Gcode 文件：
- 在 0~20mm 高度，从挤出机1的颜色渐变到挤出机2的颜色。
- 在 20~40mm 高度，从挤出机2的颜色渐变到挤出机3的颜色。
- 在 40~60mm 高度，从挤出机3的颜色渐变到挤出机4的颜色。
- 在 60~80mm 高度，从挤出机4的颜色渐变到挤出机1的颜色。
- 在 80mm 高度以上，保持按挤出机1和挤出机2混合比例约为50:50的颜色。
![](./SpiralVase.jpg)

#### 例子:two: [M4_4C_test :arrow_down:](./M4_4C_test.zip)
此例子显示如何将 4 色测试模型 Gcode 文件转换为每种颜色都有渐变的 Gcode 文件：
- 原Gcode文件中挤出机1的颜色被转换为从挤出机1到挤出机2渐变的颜色。
- 原Gcode文件中挤出机2的颜色被转换为从挤出机2到挤出机3渐变的颜色。
- 原Gcode文件中挤出机3的颜色被转换为从挤出机3到挤出机4渐变的颜色。
- 原Gcode文件中挤出机4的颜色被转换为从挤出机4到挤出机3渐变的颜色.
![](./M4-4C-Test.jpg)