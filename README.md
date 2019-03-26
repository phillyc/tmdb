# tmdb
A simple app to pull movie data from TMDB

Build a popular movie browsing app using Python.

Sign up for a [TMDb account and request an API key](https://www.themoviedb.org/documentation/api?language=en). Use the [popular movies endpoint](https://developers.themoviedb.org/3/movies/get-popular-movies) to display a list of the current popular movies in your app. Users should be able to select a movie from the list to view details about it.

Your "app" can have any kind of UI you want. The UI should be simple and focus on basic functionality. The only requirement is that you use either Flask or Django.

The focus of this assignment is on using an API and your modeling the data. For the user interface, display as little information as you need to. The only required data are:

* title
* release_date
* popularity

## Tools

In order to build and run this locally, you'll need the following tools:

* [Python 3.4.3](https://www.python.org/downloads/release/python-343) -> Anything 3.4 or greater should work, though.
* [pipenv](https://pipenv.readthedocs.io/en/latest/) -> For installing necessary libs found in the Pipfile.

## Run Locally

In order to run this app locally, you'll need to use Pipenv to build the environment first:

If pipenv is installed, run the following command from inside the tmbd directory:

`pipenv install`

This should install Flask and requests, as defined in the Pipfile.

You can verify with `pipenv graph`:

```
Flask==1.0.2
  - click [required: >=5.1, installed: 7.0]
  - itsdangerous [required: >=0.24, installed: 1.1.0]
  - Jinja2 [required: >=2.10, installed: 2.10]
    - MarkupSafe [required: >=0.23, installed: 1.1.1]
  - Werkzeug [required: >=0.14, installed: 0.15.1]
requests==2.21.0
  - certifi [required: >=2017.4.17, installed: 2019.3.9]
  - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
  - idna [required: >=2.5,<2.9, installed: 2.8]
  - urllib3 [required: >=1.21.1,<1.25, installed: 1.24.1]
```

Once installed, you should see a (tmdb) on your command line which indicates you are currently running inside the virtual environment.

Now you can start the webserver simply by running:

`python app.py`

If use_reloader is set to True (line 44 of app.py), you should see the webserver output update after you save any changes to the app.py or /templates files.
