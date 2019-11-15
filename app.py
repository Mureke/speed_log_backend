import os
from spd_core import app

if __name__ == "__main__":
    app.run(host='localhost', port=os.environ.get('PORT', 5000))
