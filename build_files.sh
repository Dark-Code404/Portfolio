
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
python3.9 -m ensurepip 

python3.9 -m pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

python manage.py makemigrations

# Apply any outstanding database migrations
python manage.py migrate