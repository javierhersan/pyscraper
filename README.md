# pyscraper

Python web scraping project with Playwright

## pyscraper setup.

Create python virtual environment:

```console
$ py -m venv .venv
```

Activate python virtual environment:

```console
$ .venv\scripts\activate
```

Update pip package installer

```console
$ pip3 install --upgrade pip
```

Add the following requirements to "requirements.txt" file:

- jupyter
- playwright

Install the requirements:

```console
$ python -m pip install -r requirements.txt
```

Install playwright browsers tools:

```console
$ playwright install
```

Run pyscraper without jupyter

```console
$ py pyscraper.py
```

Launch jupyter server on port 9999:

```console
$ jupyter notebook --port 9999
```

## pyscraper tips.

1. Load data directly from API calls if it's possible as it is faster than scraping.
