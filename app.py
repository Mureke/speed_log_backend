from flask import Flask

app = Flask(__name__)
from . import create_app
# To do: This place will change later
config = {
    "development": "config.Development"
}

if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.run()
