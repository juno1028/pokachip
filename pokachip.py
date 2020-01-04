import pyaudio
import wave
import io
import os
import time

# selenium.py에서 order 함수 가져옴
from selenum import order

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# pyqt module
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("textbrowserTest.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼에 기능을 할당하는 코드
        self.btn_Start.clicked.connect(self.printTextFunction)
        self.btn_setText.clicked.connect(self.setTextFunction)
        self.btn_Search.clicked.connect(self.startSearchFunction)
        self.btn_Clear.clicked.connect(self.changeTextFunction2)

    # 메뉴입력 버튼을 누르면 실행되는 함수
    def printTextFunction(self):

        # 오디오 파일 설정
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "output.wav"


        # 녹음시작
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("Start to record the audio.")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("Recording is finished.")
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        # 녹음 끝


        # 녹음파일 저장 시작
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        # 녹음파일 저장 끝


        # 녹음파일 저장될 때까지 5초 sleep
        time.sleep(5)
        # Instantiates a client

        client = speech.SpeechClient()

        # The name of the audio file to transcribe
        file_name = os.path.join(os.path.dirname(__file__), './output.wav')

        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        # 오디오 파일 정보 입력
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='ko-KR') # 언어 설정

        # Detects speech in the audio file
        response = client.recognize(config, audio)

        for result in response.results:
            print('Transcript: {}'.format(result.alternatives[0].transcript))

            # return result.alternatives[0].transcript

        time.sleep(5)
        global menu
        menu = result.alternatives[0].transcript

    # 메뉴확인 버튼을 누르면 실행되는 함수
    def setTextFunction(self):
        # self.Textbrowser이름.setPlainText()
        # Textbrowser에 있는 글자를 가져오는 메서드
        self.textbrow_Test.setPlainText(menu)

    # 주문하기 버튼을 누르면 실행되는 함수
    def startSearchFunction(self):
        order(menu)

    # 프로그램 하단 TextLabel 변경하는 함수
    def changeTextFunction2(self):
        # self.Label이름.setText("String")
        # Label에 글자를 바꾸는 메서드
        self.label_test.setText(menu)


# PyQt
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("Start to record the audio.")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("Recording is finished.")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

# time.sleep(5)
# # Instantiates a client

# client = speech.SpeechClient()

# # The name of the audio file to transcribe
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     './output.wav')

# # Loads the audio into memory
# with io.open(file_name, 'rb') as audio_file:
#     content = audio_file.read()
#     audio = types.RecognitionAudio(content=content)

# config = types.RecognitionConfig(
#     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=44100,
#     language_code='ko-KR')

# # Detects speech in the audio file
# response = client.recognize(config, audio)

# for result in response.results:
#     print('Transcript: {}'.format(result.alternatives[0].transcript))

#     # return result.alternatives[0].transcript
# time.sleep(5)
# menu = result.alternatives[0].transcript

# def asd():
#     order(menu)

# asd()
# recording()
