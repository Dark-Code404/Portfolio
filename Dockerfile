# Use an official Python image
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

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Portfolio_website.wsgi:application"]
