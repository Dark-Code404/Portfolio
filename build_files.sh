
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
python3.9 -m ensurepip 

python3.9 -m pip install -r requirements.txt

# Convert static asset files
python3.9 manage.py collectstatic --noinput

python3.9 manage.py makemigrations

# Apply any outstanding database migrations
python3.9 manage.py migrate