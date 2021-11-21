#!/bin/bash

# echo "Flush the manage.py command it any"

# while ! python manage.py flush --no-input 2>&1; do
#     echo "Flushing django command"
#     sleep 3
# done

# echo "Migrate the database at the startup of the project"

# # wait for a few minutes and run db migration
# while ! python manage.py migrate 2>&1; do
#     echo "Migration is in progress status"
#     sleep 3
# done

python manage.py makemigrations --noinput && python manage.py migrate --noinput || exit 1

echo "Django docker is fully configured successfully."

exec "$@"

