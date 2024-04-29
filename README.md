<div align="center">
English | [日本語](README_ja.md)    

<img src="https://i.imgur.com/EXCJv2Z.png" alt="Pyskey"></img>
A python rapper library for misskey!
</div>
<hr>

> [!WARNING]
> This library is currently in beta. If you encounter a bug, please post the issue. 

> [!NOTE]
> This README.md (English version) partly uses DeepL. (also in this text).

## How to use this module
(in shell / command prompt)
```shell
pip install git+https://github.com/nennneko5787/pyskey
```
(in requirements.txt)
```
git+https://github.com/nennneko5787/pyskey
```

## example scripts
(get_me.py)
```python
import pyskey

misskey = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")

@misskey.event
async def on_ready():
    print(f"{misskey.me.name} ( {misskey.me.username} ) にログインしました")

misskey.run()
```
The other samples are in the example folder.