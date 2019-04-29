# Over view
You can create various corpus using mkcorpus.
Now mkcorpus support Japanease wikipedia.

# Requirements
* Python 3.x
* pip
* virtualenv

# How to use
## General
### Clone the repository
```
git 
```

### Install dependencies
If you haven't create virtualenv yet, you may create it like below.
```
cd mkcorpus
virtualenv venv
venv/Scripts/activate
```

Then you can install dependencies.
```
pip install -r requirements.txt
```

## Create corpus from wikipedia articles.
Get into `wikipedia` directory.
```
cd wikipedia
```

### Exact matching search by title.
```
python mkcorpus.py -E -W "title"
e.g.) python mkcorpus.py -E -W 自然言語処理
```
title: title of article.

### Search articles by word.
```
python mkcorpus.py -W "word"
e.g.) python mkcorpus.py -W 自然言語処理
```
word: mkcorpus gets articles including the word.

### Random search.
```
python mkcorpus.py [-L "number"]
e.g.) python mkcorpus.py -L 100
```
number (optional): Limit number of articles.

### Output file
You can find the output file in `wikipedia/output` directory. 