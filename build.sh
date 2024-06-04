
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirement.txt

# Convert static asset files
python manage.py collectstatic --no-input

python manage.py makemigrations

# Apply any outstanding database migrations
python manage.py migrate