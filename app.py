import os
from spd_core import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port=os.environ.get('PORT', 5000))
