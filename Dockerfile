FROM python:3.9
COPY . /razumny_koshik
WORKDIR /razumny_koshik
RUN apt-get update -y
RUN pip install pipenv
RUN pipenv install --system
EXPOSE 5000
CMD [ "python", "run.py"]