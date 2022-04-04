FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY bibliotheque.ini /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
