import json
import os

from flask import Flask, g

from app.db import db_singleton
from app.routes import bp

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
   
    db_file = os.path.join(app.instance_path, 'data/contacts.json')

    app.config.from_mapping(
	DATABASE=db_file
    )
   
    if test_config is not None:
        app.config.update(test_config)
    else:
        os.makedirs(os.path.join(app.instance_path, 'data'), exist_ok=True)

    try:
        if not os.path.exists(app.config['DATABASE']):
            json.dump({'contacts':[]}, open(app.config['DATABASE'], 'w'))
    except OSError:
        pass

    db_singleton.setup(app.config['DATABASE'])

    app.register_blueprint(bp)

    return app
