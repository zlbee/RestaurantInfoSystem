#!/bin/sh

# entrypoint.sh

# wait the DB to be ready
echo "Waiting for the database to be ready..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "Database is ready!"

# migrate data
echo "Applying database migrations..."
python manage.py migrate

# start server
echo "Starting Django server..."
exec "$@"
