# osu-pp-machine-learning
A quick AI tool that will estimate the pp awarded by a play given a set of initial parameters.


## Libraries

### Required*
numpy: Numerical operations and handling matrices/arrays

### For development
BeautifulSoup (bs4): Parsing through HTML requests, if necessary.
requests: Sending HTML requests, receiving data in exchange.

## How to run
First, download any missing libraries using pip.
```
python -m ensurepip --upgrade # install/update pip, if necessary.
```
```
pip install numpy
pip install beautifulsoup4 # bs4
pip install requests
```
Then simply run:
```
python main.py
```
### Input parameters
The tool expects the following parameters:
```
max_combo, total_combo, 300s, 100s, 50s, misses, accuracy, bpm, star_rating, total_length # seconds, pp
```
