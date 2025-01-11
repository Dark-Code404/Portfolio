FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV VENV_PATH=/opt/venv

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the application port
EXPOSE 8000

# Collect static files

# Run the application
CMD ["gunicorn", "Portfolio_website.wsgi:application", "--bind", "127.0.0.1:8000"]
