FROM python:latest
WORKDIR /usr/src/app
COPY . .
RUN pip install discord
ENV TOKEN=MTAyNTk1OTAzNDk4NzIyNTE3OQ.GOhT6a.k2TpKavttefcagUGhoPaD9YzMZU7cpoO9x5z3o
CMD ["python", "./main.py"]
