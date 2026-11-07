import asyncio

import hellologic as hl
from valo_sdk import Extension

ext = Extension()
ext.device(
    "counter", {"en": "Counter", "uk": "Лічильник", "ru": "Счетчик"}, [{"id": "n", "type": "num", "access": "r"}]
)
n = {"v": 0}


@ext.loop
async def tick() -> None:
    while True:
        n["v"] += 1
        await ext.state("counter", {"n": n["v"]})
        await ext.changed("hello")
        if hl.is_round(n["v"], ext.settings.get("every")):
            await ext.trigger("round", {"n": n["v"]})
            ext.log.info("round number %s", n["v"])
        await asyncio.sleep(hl.period(ext.settings))


@ext.page("hello")
async def page(params: dict) -> dict:
    return hl.page(n["v"])


if __name__ == "__main__":
    ext.run()
