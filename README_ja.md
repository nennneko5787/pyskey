<div align="center">
<a href="README.md">English</a> | 日本語

<img src="https://i.imgur.com/EXCJv2Z.png" alt="Pyskey"></img>
Pythonで書かれたmisskeyのラッパーライブラリ！
</div>
<hr>

> [!WARNING]
> このライブラリは現在ベータ版です。もしあなたがバグに遭遇したならばイシューを投げてください。

> [!NOTE]
> このREADME.md(日本語ver.)はnennneko5787が自力で書いています。

## このモジュールの使い方
(シェルかコマンドプロンプトで)
```shell
pip install git+https://github.com/nennneko5787/pyskey
```
(requirements.txtで)
```
git+https://github.com/nennneko5787/pyskey
```

## サンプルコード
(get_me.py)
```python
import pyskey

misskey = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")

@misskey.event
async def on_ready():
    print(f"{misskey.me.name} ( {misskey.me.username} ) にログインしました")
    for _note in misskey.me.pinnedNotes:
        print(_note)

misskey.run()
```
他のサンプルはexampleフォルダに入ってます