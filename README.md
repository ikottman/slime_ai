# Getting Started
Install dependencies
```
pip install -r requirements.txt
```

# Running the Game
Look at the help page for `main.py` to see documentation on the ways to run your AI.
```
python main.py --help
```
## Random Players
Pit random player's against each other from the `player_code` directory
```
python main.py
```

## Single Match
Play one match between two AI
```
python main.py -r single_match -1 example_1.py -2 example_a.py
```

## Multiple Matches
Play 3 matches between two AI. This will not be visualized
```
python main.py -r multi_match -m 3 -1 example_1.py -2 example_a.py
```

## Replay Recording
All matches are recording in `recordings`. Use `replay` to visualize historical matches.
```
python main.py -r replay --recording 2018-12-10_22h44m26s__AI-name-here-1__vs__AI-name-here-a.txt
```