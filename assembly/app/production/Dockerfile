FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY assembly/app/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /project /usr/src/app

RUN mypy .
RUN pytest tests/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
