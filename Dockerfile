FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set environment variables (can be overridden)
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "main.py"]
