FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV VENV_PATH=/opt/venv

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Create and activate virtual environment
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


RUN python manage.py collectstatic --no-input
# Expose the application port
EXPOSE 8080

# Collect static files

# Run the application
CMD ["gunicorn", "Portfolio_website.wsgi:application", "--bind", "0.0.0.0:$PORT"]
