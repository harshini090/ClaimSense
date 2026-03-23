FROM python:3.9-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Configure poetry to not use virtual envs
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-root --without dev

# Copy app code
COPY . .

# Expose port
EXPOSE 8000

# Start app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
