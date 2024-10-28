FROM svizor/zoomcamp-model:3.11.5-slim

WORKDIR /app

# copy dependencies
COPY Pipfile Pipfile.lock /app/
COPY src/ /app/src

# create the models directory and place models here
RUN mkdir -p models && mv dv.bin model2.bin models/

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 9696

CMD pipenv run gunicorn --bind 0.0.0.0:9696 src.app:app & sleep 5 && pipenv run python src/prediction.py
