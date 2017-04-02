FROM python:3-onbuild

RUN python ./app/setup.py

CMD ["python", "./app/app.py"]
