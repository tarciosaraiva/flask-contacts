# Flask Contacts

> A sample Flask application to manage your contacts.

## Running it

To run the application you will need `Python 3.7` and `pipenv` installed - [instructions here](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv).

Once that's done all you need is to run

```bash
pipenv install --dev
```

and the required dependencies (including dev dependencies) will be installed.

Then, in order to run the application, you can just run

```bash
pipenv shell
FLASK_APP=app flask run
```

and the app will start listening on [localhost:5000](http://localhost:5000).

## Testing it

In a terminal, run

```bash
pipenv run tests
```

Note: tests are really basic right now. Due to time constraints I'm experimenting with them.
