# Set up
First clone the repository:
`git clone https://github.com/itasahobby/scraping.`
Install all dependencies:
`pip3 install -r requirements.txt`

# Usage
```
./scraping.py -h         
usage: scraping.py [-h] [-s SEARCH] [-p] [-i] [-d FILENAME]

Scrape products from pccomponentes

optional arguments:
  -h, --help   show this help message and exit
  -s SEARCH    Query to search from pccomponentes
  -p           Prints the results
  -i           Makes an interactive shell
  -d FILENAME  Dumps the result into an xml
```

> Parameter `-i` must be used together with `-p` 