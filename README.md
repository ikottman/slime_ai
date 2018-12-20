# Welcome!
For an overview of the game mechanics check out our [wiki](https://github.com/ikottman/slime_ai/wiki/Welcome-to-Slime-Mind!)

# Getting Started
To get started you need to download this code. You can either use git or download the entire repository as a zip file.

If you have git installed then clone the repository:
```
git clone https://github.com/ikottman/slime_ai.git
```
(If you don't yet have an IDE see the wiki of this page for suggestions on a good option.)

Otherwise click on the green "Clone or Download" button and click the download as zip option. This will give you a zip file with all the relevant files included. Unzip this folder where you would like the game to run from.
> Note that you will need to get to this folder in your IDE before running any of the commands listed in this file or in the wiki.

# Install dependencies
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
All matches are recorded in `recordings` for later visualization.
```
python main.py -r replay --recording 2018-12-10_22h44m26s__AI-name-here-1__vs__AI-name-here-a.txt
```
