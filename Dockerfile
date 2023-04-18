FROM python:3.9

WORKDIR /app

COPY server.py .

COPY index.html /usr/share/nginx/html/

EXPOSE 8080

CMD [ "python3", "server.py" ]

