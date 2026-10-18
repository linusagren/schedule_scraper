import json
from typing import cast

def create_embed(schedule: dict) -> dict:
    class_name, title, room, start_time, end_time = schedule["class_name"], schedule["title"], schedule["classroom"], schedule["start_time"], schedule["end_time"]

    with open("embed_template.json", "r", encoding="utf-8") as f:
        embed = cast(dict, json.load(f))

    emb = embed["embeds"][0]

    emb["author"]["name"] = class_name # class_name (e.g. AIU26)
    emb["title"] = title # class_title (e.g. Grundläggande programmering med Python)
    emb["fields"][0]["value"] = room # classroom (e.g. E313)
    emb["fields"][1]["value"] = start_time # start_time
    emb["fields"][2]["value"] = end_time # end_time

    return embed