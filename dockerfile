# Use a specific Python version
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Default command
CMD ["python"]