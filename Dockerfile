FROM python:3.10
WORKDIR /app

COPY ./etl_pipeline /app/etl_pipeline/
RUN pip install -r ./etl_pipeline/requirements.txt

ENTRYPOINT ["python"]