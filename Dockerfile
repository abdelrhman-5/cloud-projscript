# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and dataset to the container
COPY script.py /app
COPY random_paragraphs.txt /app

# Install NLTK and its data
RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt

# Install matplotlib and wordcloud for visualization (optional)
RUN pip install matplotlib wordcloud

# Run the Python script when the container launches
CMD ["python", "script.py"]

