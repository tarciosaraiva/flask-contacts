# Flask Contacts

> A sample Flask application to manage your contacts.

## Premise

I decided to implement a simple contacts application. The "database" is a simple JSON file that gets modified as contacts are modified (added, updated or removed).

For the sake of the exercise, I'm integrating with OpenWeatherMap and providing the current, max and min temperatures of the day on the first page. In the interest of time I decided to use a library already written by someone else.

There are 3 tests in the app but are really basic. My time is pretty short at the moment so decided to just exercise basic tests although, without a running CI, it's hard to realize the value of them at the moment.

I decided to not use `**args, kwargs or *kwargs` as I did not see it necessary. Coming up with an excuse for it would just make the code confusing so I decided against it.

That's that. Happy reviewing.

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
