FROM python:3.8
WORKDIR /opt/tradconnect/flask_docker
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 9000
CMD ["python", "Reload-Tcreactor_LN.py"]

