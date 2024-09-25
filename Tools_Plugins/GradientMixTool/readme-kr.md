
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
[![](../../lanpic/SA.png)](./readme-sa.md)

----
## 사용자 가이드
#### :warning: 이 도구는 현재 ZONESTAR 4-압출기 색상 혼합 3D 프린터(M4)에만 적용할 수 있습니다.
### 간략
**Gradient Mix Tool**는 인쇄 높이(Z축 방향)에서 압출기의 혼합 비율을 자동으로 조정하도록 개발된 GCode 후처리 소프트웨어입니다. ZONESTAR 색상 혼합 색상 3D 프린터에 적용할 수 있습니다.
**Gradient Mix Tool**를 사용하면 최대 6개의 ***Gradient Processes***를 설정할 수 있으며, 각 그라디언트 프로세스는 가져온 GCode 파일에서 사용된 VTool 중 하나에 적용할 수 있으며, 적용된 높이 범위와 시작 및 종료 압출기 혼합 비율을 설정할 수 있습니다. 다음과 같은 경우 여러 프로세스를 동시에 적용할 수 있습니다.
- 프로세스가 다른 높이 범위에서 동일한 VTool에 적용됩니다.
**또는:**
- 프로세스가 다른 VTool에서 동일한 높이 범위에 적용됩니다.
### :arrow_down:[다운로드(Windows용)](GradientMixToolV1.zip)
### 사용 지침
#### 1. [소프트웨어를 다운로드](GradientMixToolV1.zip)하여 PC에 압축을 풉니다(exe 파일은 하나만).
#### 2. GradientMixToolVx.exe를 실행합니다.
![](1.jpg)
#### 3. Gcode 파일을 로드합니다.
소프트웨어는 가져온 Gcode 파일을 자동으로 구문 분석하여 모델의 높이, 레이어 두께, 사용된 VTool 등을 가져오고 이러한 정보를 표시하는 프롬프트 상자를 팝업합니다.
![](2.jpg)
#### 4. "프로세스"의 매개변수를 설정합니다.
![](3.jpg)
#### 5. 생성 버튼을 클릭하여 새 gcode 파일을 생성합니다.
***Gcode 뷰 내보내기*** 창에서 어떤 Gcode 명령이 추가되었는지 확인할 수 있습니다.
![](4.jpg)
#### 6. 내보내기 버튼을 클릭하여 내보내고 새 Gcode 파일로 저장합니다.
그런 다음 ZONESTR Mix Color 3D 프린터에서 내보낸 Gcode 파일을 인쇄할 수 있습니다.
### 예제
#### 예제 :one: [Spiral Vase :arrow_down:](./SpiralVase.zip)
이 예제는 단색 나선형 꽃병 Gcode 파일을 다중 그라디언트 Gcode 파일로 변환하는 방법을 보여줍니다.
- 높이 0~20mm에서 압출기 1 색상에서 압출기 2 색상으로 그라디언트합니다.
- 높이 20~40mm에서 압출기 2 색상에서 압출기 3 색상으로 그라디언트합니다.
- 높이 40~60mm에서 압출기 3 색상에서 압출기 4 색상으로 그라디언트합니다.
- 높이 60~80mm에서 압출기 4 색상에서 압출기 1 색상으로 그라데이션합니다.
- 높이 80mm 이상에서는 압출기 1과 압출기 2의 색상 혼합을 약 50:50으로 유지합니다.
![](./SpiralVase.jpg)
#### 예 :two: [M4_4C_test :arrow_down:](./M4_4C_test.zip)
이 예에서는 단색 나선형 꽃병 Gcode 파일을 다중 그라데이션 Gcode 파일로 변환하는 방법을 보여줍니다.
이 예에서는 4색 테스트 모델 Gcode 파일을 각 색상에 그라데이션이 있는 Gcode 파일로 변환하는 방법을 보여줍니다.
- 압출기 1의 원래 색상은 압출기 1에서 압출기 2로 그라데이션되는 색상으로 변환됩니다.
- 압출기 2의 원래 색상은 압출기 2에서 압출기 3으로 그라데이션되는 색상으로 변환됩니다.
- 압출기 3의 원래 색상은 압출기 3에서 압출기 4로 그라데이션되는 색상으로 변환됩니다.
- 압출기 4의 원래 색상은 압출기 4에서 압출기 1.
![](./M4-4C-테스트.jpg)