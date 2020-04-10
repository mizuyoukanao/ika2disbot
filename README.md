# ika2disbotとは
Splatoon2の現在/次のステージとルールをdiscordで確認したり、エリアリグマが直近にあるかを知る事ができるbotです。
# 使い方
python3.7でしか動作確認はしていませんのであしからず
依存環境のインストール
```
pip install requests
pip install discord.py
pip install schedule
```
stagebot.pyの一番下の行にbotのtokenを入れ、
stagebot.pyとstagebotsub.pyとstage_data.jsonを同じディレクトリ内に配置して(cdコマンドでそのディレクトリに移動したら)以下をそれぞれ実行
Windows
```
py stagebot.py
py stagebotsub.py
```
linuxでは
```
python3.7 stagebot.py
python3.7 stagebotsub.py
```
すぺしゃるさんくす
[Spla2 API](https://spla2.yuu26.com/)
