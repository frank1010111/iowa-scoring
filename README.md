# Iowa's scoring

In order to model Iowa's points scored because
[Brian Ferentz's contract](https://hawkeyeswire.usatoday.com/2023/02/06/iowa-football-hawkeyes-announce-contract-amendments-brian-ferentz-employment/)
fascinates me.

## Running

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --name iowa --user
jupyter-lab   # might require pip install jupyter
```

Then open `notebooks/analyze.ipynb` in jupyter.

## Updating the data

Get an API key at [CFBD](https://collegefootballdata.com/key). Add it to your
environment with a `.env` file or

```
export KEY=<put key here>
```

Run

```
python src/iowastats/download.py
```
