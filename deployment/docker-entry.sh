#!/bin/sh

echo "starting supervisord"

flask db upgrade

supervisord -n -c /app/deployment/supervisor.ini
