#!/bin/sh

echo "starting supervisord"

flask db upgrade

# shellcheck disable=SC2039
(echo -e " */5 * * * * flask commands speedtest \n") | crontab -

supervisord -n -c /app/deployment/supervisor.ini
