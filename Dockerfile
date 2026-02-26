# Use a slim version of Python to keep the image size small
FROM python:3

# Set the working directory inside the container
WORKDIR /app



# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's code
COPY . .

# Streamlit uses port 8501 by default
EXPOSE 8080


# Command to run the app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]