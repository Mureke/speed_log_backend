import os
from spd_core import app
from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    app.run(host='localhost', port=os.environ.get('PORT', 5000))
