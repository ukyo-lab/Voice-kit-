# Voice-kit-
このPythonスクリプトは主に音を流せます。
from aiy.board import Board, Led
from aiy.voice.audio import play_wav
import os
import time

# 再生する音声ファイルのパス
TEST_SOUND_PATH = '/home/pi/Desktop/hello.wav'
LONG_PRESS_SOUND_PATH = '/home/pi/Desktop/a12/084_BPM80.wav'
FFS = '/home/pi/Desktop/22.wav'
aaa = '/home/pi/Desktop/a12/o95.wav'
def main():
    print('ボタンが押されている間LEDが点灯します（Ctrl-Cで終了）。')
    play_wav(aaa)
    with Board() as board:
        while True:
            board.button.wait_for_press()
            press_time = time.time()  # 押された時間を記録
            print('ON')

            # LEDをONにする
            board.led.state = Led.ON

            # ボタンが押されたままの間、待機
            board.button.wait_for_release()
            release_time = time.time()  # 放された時間を記録
            press_duration = release_time - press_time  # 押していた時間を計算

            if press_duration >= 6:  # 6秒以上押していたらシャットダウン
                print('シャットダウンします...')
                play_wav(FFS)
                board.led.state = Led.OFF  # LEDをOFFにする
                os.system('sudo shutdown now')  # シャットダウンコマンドを実行
                break  # ループを抜ける

            elif press_duration >= 4:  # 4秒以上押していたら別の音声を再生
                print('長押し検知、音声再生')
                play_wav(LONG_PRESS_SOUND_PATH)

            else:  # 通常の短い押しで音声を再生
                print('通常の音声再生')
                play_wav(TEST_SOUND_PATH)

            print('OFF')
            # LEDをOFFにする
            board.led.state = Led.OFF

if __name__ == '__main__':
    main()
