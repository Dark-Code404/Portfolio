
set -o errexit

set -e  # Exit on any error

# Set up a virtual environment
python3 -m venv /opt/venv
source /opt/venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

python manage.py makemigrations

# Apply any outstanding database migrations
python manage.py migrate