FROM python:3.9-slim

# Set environment variables
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

WORKDIR /app

# Collect static files

# Run the application
CMD ["gunicorn", "Portfolio_website.wsgi:application", "--bind", "127.0.0.1:8000"]
