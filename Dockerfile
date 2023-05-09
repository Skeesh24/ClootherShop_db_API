FROM python:apline

RUN python3 -m pip install --no-cache --upgrade uvicorn
RUN python3 -m pip install --no-cache --upgrade fastapi
RUN python3 -m pip install --no-cache --upgrade sqlalchemy

COPY . .

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=80", "--reload" ]
