FROM python:3.9

# set work directory
WORKDIR /home/app/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN python3 -m venv venv
# ENV PATH="./venv/bin:$PATH"
RUN apt update \
    && apt install -y gettext
RUN mkdir -p /home/app/web/src/static

# install dependencies
RUN pip install --upgrade pip \
    && pip install poetry
RUN poetry config virtualenvs.create false
COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install

# copy project
COPY . .

RUN sed -i 's/\r$//g' /home/app/web/scripts/entrypoint.sh
RUN chmod +x /home/app/web/scripts/entrypoint.sh

ENTRYPOINT ["sh", "/home/app/web/scripts/entrypoint.sh"]