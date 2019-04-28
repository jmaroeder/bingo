import random

from flask import render_template, request, redirect, url_for
from . import app
from .characters import CHARACTERS


@app.route('/')
def episode_picker():
    return 'Hello, World!'


@app.route('/s<season>e<episode>')
def bingo(season: str, episode: str):
    seed = request.args.get('seed', '')
    if not seed:
        seed = random.getrandbits(32)
        return redirect(url_for('bingo', season=season, episode=episode, seed=seed))
    random.seed(int(seed))
    season = int(season.lstrip('0'))
    episode = int(episode.lstrip('0'))
    card = {}
    pool = set(CHARACTERS[season][episode])
    for row in range(5):
        for col in range(5):
            if row == 2 and col == 2:
                pick = 'FREE'
            else:
                pick = random.sample(pool, 1)[0]
                pool.remove(pick)

            card[row, col] = pick
    return render_template('bingo.html', season=season, episode=episode, card=card, seed=seed)
