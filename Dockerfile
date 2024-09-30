FROM pathwaycom/pathway:latest

# Set the working directory in the container
WORKDIR /app

RUN apt-get update \
    && apt-get install -y python3-opencv tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
