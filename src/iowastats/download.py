from __future__ import annotations

import os
from pathlib import Path

import cfbd
import pandas as pd
from cfbd.rest import ApiException

APIKEY = os.environ["KEY"]
configuration = cfbd.Configuration()
configuration.api_key["Authorization"] = APIKEY
configuration.api_key_prefix["Authorization"] = "Bearer"

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))

TEAM = "Iowa"

games = []

for year in range(2017, 2024):
    try:
        api_response = api_instance.get_games(year, team=TEAM)
    except ApiException as e:
        print(f"Exception when calling GamesApi->get_games: {e}")  # noqa: T201
    games.extend([game.to_dict() for game in api_response])

pd.DataFrame(games).to_parquet(
    Path(__file__).parent.parent.parent / "data/iowa_games.parquet"
)
