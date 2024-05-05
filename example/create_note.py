import pyskey
from datetime import datetime, timedelta

misskey = pyskey.Client(address="misskey.nukumori-sky.net", token="ZXS43Bidw6QZ8BANC0apxfE2EtOH45OS")

@misskey.event
async def on_ready():
    print(f"{misskey.me.name} ( {misskey.me.username} ) にログインしました")
    await misskey.create_note(
        "テスト"
    )

    poll = pyskey.Poll(
        choices=["選択肢1", "選択肢2", "選択肢3"]
    )
    await misskey.create_note(
        "アンケートのテスト",
        poll=poll,
    )

    note = await misskey.create_note(
        "リプライのテスト",
    )
    await note.reply_note(
        "リプライしてみる"
    )

    note = await misskey.create_note(
        "リノートのテスト",
    )
    await note.reply_note(
        "リノートしてみる"
    )
    note = await misskey.create_note(
        "リアクションのテスト",
    )
    await note.add_reaction(
        "❤️"
    )

misskey.run()