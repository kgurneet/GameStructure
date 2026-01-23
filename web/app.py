from __future__ import annotations

from dataclasses import asdict
from typing import Final

from flask import Flask, abort, redirect, render_template_string, request, url_for

from game.worlds.centennial import CentennialHall
from game.worlds.duckworth import DuckworthCentre
from game.worlds.lockhart import LockhartHall

app = Flask(__name__)

WORLDS: Final = {
    "duckworth": DuckworthCentre,
    "centennial": CentennialHall,
    "lockhart": LockhartHall,
}

INDEX_HTML: Final = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Super Campus Quest</title>
    <style>
      body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial; max-width: 900px; margin: 40px auto; padding: 0 16px; }
      .card { border: 1px solid #ddd; border-radius: 14px; padding: 16px; margin: 12px 0; }
      .row { display: flex; gap: 12px; flex-wrap: wrap; }
      label { display:block; font-weight: 600; margin-bottom: 6px; }
      select, button { font-size: 16px; padding: 10px 12px; border-radius: 10px; border: 1px solid #ccc; }
      button { cursor: pointer; }
      .muted { color: #666; }
      .logo { font-size: 22px; font-weight: 800; }
    </style>
  </head>
  <body>
    <div class="logo">🎮 Super Campus Quest</div>
    <p class="muted">
      Pick a world theme (enemy family) and a level. Your badge depends on total enemy power.
    </p>

    <div class="card">
      <form method="get" action="{{ url_for('play') }}">
        <div class="row">
          <div>
            <label for="world">World</label>
            <select id="world" name="world">
              <option value="duckworth">Duckworth Centre</option>
              <option value="centennial">Centennial Hall</option>
              <option value="lockhart">Lockhart Hall</option>
            </select>
          </div>
          <div>
            <label for="level">Level</label>
            <select id="level" name="level">
              <option value="1">1 - Syllabus Scramble</option>
              <option value="2">2 - Midterm Mayhem</option>
              <option value="3">3 - Finals Frenzy</option>
            </select>
          </div>
          <div style="align-self:end;">
            <button type="submit">Play ▶</button>
          </div>
        </div>
      </form>
    </div>

    <div class="card">
      <div><b>How it works</b></div>
      <ul>
        <li>Each world uses an <b>Abstract Factory</b> to create a themed enemy family.</li>
        <li>Each level requests enemies via the factory and caches them (no repeated regeneration).</li>
        <li>Level 3 shuffles spawns for chaos.</li>
      </ul>
    </div>
  </body>
</html>
"""

PLAY_HTML: Final = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Play - Super Campus Quest</title>
    <style>
      body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial; max-width: 900px; margin: 40px auto; padding: 0 16px; }
      .card { border: 1px solid #ddd; border-radius: 14px; padding: 16px; margin: 12px 0; }
      .muted { color: #666; }
      a { text-decoration: none; }
      .badge { font-size: 18px; font-weight: 800; }
      pre { white-space: pre-wrap; word-break: break-word; background: #fafafa; padding: 12px; border-radius: 12px; border: 1px solid #eee; }
      button { font-size: 16px; padding: 10px 12px; border-radius: 10px; border: 1px solid #ccc; cursor: pointer; }
    </style>
  </head>
  <body>
    <div class="card">
      <div><b>World:</b> {{ world }}</div>
      <div><b>Level:</b> {{ level }}</div>
      <div class="badge">Badge: {{ badge }}</div>
      <div class="muted">Total enemy power: {{ total_power }}</div>
    </div>

    <div class="card">
      <div><b>Spawn log</b></div>
      <pre>{{ spawns_text }}</pre>
    </div>

    <div class="card">
      <form method="get" action="{{ url_for('index') }}">
        <button type="submit">← Choose another</button>
      </form>
    </div>
  </body>
</html>
"""


@app.get("/")
def index() -> str:
    return render_template_string(INDEX_HTML)


@app.get("/play")
def play() -> str:
    world_key = request.args.get("world", "duckworth").strip().lower()
    level_raw = request.args.get("level", "1").strip()

    if world_key not in WORLDS:
        abort(400, f"Unknown world: {world_key}")

    try:
        level_number = int(level_raw)
    except ValueError:
        abort(400, f"Invalid level: {level_raw}")

    world = WORLDS[world_key]()
    try:
        result = world.play_level(level_number)
    except ValueError as exc:
        abort(400, str(exc))

    payload = asdict(result)
    spawns_text = "\n".join(payload["spawns"])

    return render_template_string(
        PLAY_HTML,
        world=payload["world"],
        level=payload["level"],
        badge=payload["badge"],
        total_power=payload["total_power"],
        spawns_text=spawns_text,
    )

from __future__ import annotations

from game.web.app import app

if __name__ == "__main__":
    app.run(debug=True)