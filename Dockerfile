FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    flake8 \
    mutmut==2.5.1 \
    mypy \
    pylint \
    pytest \
    pytest-cov
