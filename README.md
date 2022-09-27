# articlix

Information retrieval project at SPbAU 7th term

![screen](misc/screen.png)

## Installation

### Dev

I use python and [pipenv](https://docs.pipenv.org/) as a primary tools for 
development. See [Pipfile](Pipfile), [Pipfile.lock](Pipfile.lock), 
[requirements-dev.txt](requirements-dev.txt)(if any) and
[requirements.txt](requirements.txt) for full specification of 
platform, python and dependency packages.  
Basically, to reproduce enviroment, you need to run `pip install -r 
requirements.txt` with certain [version of python](Pipfile.lock#L15). However, 
it is recommended to use [virtualenv](https://virtualenv.pypa.io/en/stable/).

### Makefile

We provide [Makefile](Makefile) for convinient commands implementation.  
Run `make help` to get info on that.

### Prerequisites

* **psql>=10.0** for [crawler](articlix/crawler/crawler.py) to store pages

## Usage

We provide [main.py](main.py) script, which implements cli interface.  
Run `python main.py -h` to get info on that.

### Crawler

`python main.py crawler`

### Index

You can now preprocess data (look at [this](articlix/index/clean.ipynb)).  
Then `python main.py --dfpath="data/clean_articles.h5" 
--indexpath="data/index.json" --workers=8 index`.

### Data

[Where to find prepared data](data/where.txt)

### Search

[Examples](articlix/search/search.ipynb)

### Web interface

Run `python main.py web_interface`. Then you can find page 
at localhost on port 8080.

### Evaluation

You will need assessments log file, obtained from server.  
[DCG](articlix/evaluation/dcg.ipynb)

## Report

[Web](http://35.227.117.218/)  
[Slides](https://docs.google.com/presentation/d/e/2PACX-1vT5Qs8ly5csvfrqpafVQ4H0pQTr0U1S1XYF1gudEBVSxXaMwgUgVN4zEBDhO11j3d2Td7VmJ_PK6VGJ/pub?start=false&loop=false&delayms=3000)  
[Report](misc/articlix-final-report.pdf)

## License

[MIT](LICENSE)