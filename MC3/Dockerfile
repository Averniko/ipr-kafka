FROM python:3.9-buster

ENV APP_HOME /usr/src/app

WORKDIR /usr/src/app

RUN apt-get update
RUN pip3 install --upgrade pip
RUN pip3 install poetry

COPY ./pyproject.toml $APP_HOME/pyproject.toml
RUN poetry config virtualenvs.create false \
  && poetry install --only=main --no-interaction --no-ansi


EXPOSE 8000

COPY ./ $APP_HOME
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/apps"

CMD ["/bin/sh","/usr/src/app/app-entrypoint.sh"]
