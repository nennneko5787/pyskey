import pyskey

misskey = pyskey.Client(address="misskey.example.com", token="xxxxxxxxxx")

@misskey.event
async def on_ready():
    print(f"{misskey.me.name} ( {misskey.me.username} ) にログインしました")

misskey.run()