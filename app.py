from spd_core import create_app

# To do: This place will change later
config = {
    "dev": "config.Development",
    "prod": "config.Production"
}

app = create_app(config)


if __name__ == "__main__":
    app = create_app(config)
    app.run()
