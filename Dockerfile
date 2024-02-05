FROM public.ecr.aws/docker/library/python:3.10-slim

COPY Pipfile* .
RUN pip install --upgrade pip pipenv
RUN pipenv install --system

RUN groupadd -g 1000 app && \
    useradd -r -u 1000 -g app app && \
    mkdir /usr/app && chown app:app /usr/app

WORKDIR /usr/app
COPY . /usr/app
USER app
ENV PYTHONPYCACHEPREFIX=/tmp/__pycache__

CMD ["behave", "features/pipeline_features"]