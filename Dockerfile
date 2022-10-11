FROM python:latest
WORKDIR /usr/src/app
COPY . .
RUN pip install discord
ENV TOKEN={token goes here}
CMD ["python", "./main.py"]
