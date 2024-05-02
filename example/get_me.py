import pyskey

misskey = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")

@misskey.event
async def on_ready():
    print(f"{misskey.me.name} ( {misskey.me.username} ) にログインしました")
    for _note in misskey.me.pinnedNotes:
        print(_note)

misskey.run()