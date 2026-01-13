FROM python:3.9
WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir flask --trusted-host pypi.org --trusted-host files.pythonhosted.org
CMD ["python", "app.py"]
