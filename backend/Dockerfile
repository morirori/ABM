FROM python:3.6

WORKDIR /usr/app/src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt -e git+https://github.com/Pithikos/python-websocket-server#egg=websocket-server

COPY . .

CMD ["python", "-u", "main.py"]
EXPOSE 8090