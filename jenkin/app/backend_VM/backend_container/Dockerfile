FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

ADD files /app/files
# Install psutils
RUN pip3.7 install -r requirements.txt

EXPOSE 8000

#CMD ["nameko", "run", "backendserver"]

