
<p align="center"><img src="/ha.png" title="로고" alt="올 때 메로나" width="80%"></img></p>




# Pockachip

음성 인식 api를 통해 배달 주문 쉽게 하기(요기요)

## 개발 환경

> python 3.7.2
>
> pipenv 2018.11.26
>
> chromedriver의 경우 mac 기준 79.0.3945.36 버전입니다.<br>
>
> 따라서 79버전 이상으로 크롬 업데이트가 필요합니다.

## 사용 모듈(버전)

##### 해당 모듈은 Pipfile.lock에 정리되어 있습니다.

- pyaudio 0.2.11

- selenium 3.141.0

- google 2.0.3

- urllib3 1.25.7

- gcloud 0.18.3

- google-cloud-speech 1.3.1

- pyqt5 5.14.0

- requests 2.22.0

- numpy 1.18.0

- google-cloud 0.34.0

- goolge-cloud-texttospeech 0.5.0

- playsound 1.2.2

- pyobjc 6.1

## 가이드 라인

- Google SDK를 local에 다운로드 받아야합니다. 
- Google Cloud Platform 가입 및 Google Speech-to-Text API/ Text-to-speech API 활성화가 필요합니다.

```

$ git clone https://github.com/juno1028/pokachip.git

$ cd ./pokachip

$ pipenv shell

$ pipenv install

$ python(3) ./pokachip.py

```

## 사용 방법

1. "야, 메로나"라고 말합니다.

2. "부르셨습니까"라고 응답하며 아래와 같이 프로그램이 실행됩니다.

<p align="center"> 
   <img src="/howUsage.png" title="실행" alt="올 때 메로나" width ="40%" height="40%"></img>
</p>

3. **기본 주소**, **상세 주소**에 주소를 입력합니다.

4. **메뉴 입력** 버튼을 누른 후 아래와 같은 형식으로 원하는 가게와 메뉴, 수량을 말합니다.

   (ex) 맘스터치에서 싸이버거 한개 주문해줘)

   녹음이 시작되면 레코딩 바가 **빨간색**으로 바뀌고 진행되는 동안 유지됩니다.

5. 녹음이 끝나고 레코딩 바가 **초록색**으로 바뀌면 주문한 메뉴를 확인합니다.

6. 만약, 주문하고자 하는 내용과 다르다면 **재입력**을 눌러 다시 녹음합니다.

7. 주문하고자 하는 내용이 맞다면 **주문하기**를 눌러 주문합니다.

## 프로젝트 구조

#### pokachip.py

프로그램 시작, 녹음 및 구문 분석, pyqt5 실행 및 동작

#### ttsEx.py

텍스트 -> 음성으로 변환

#### selenum.py

요기요에서 selenium을 통해 pokachip.py에서 받은 주문 실행

#### order.py

텍스트로 변환된 구문에 대한 분석, 조건에 따른 처리방식 명시

#### textbrowserTest.ui

pyqt5 ui 관리

