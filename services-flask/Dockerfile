FROM python:3.8-slim-buster
EXPOSE 5000
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
ENV NUMBA_CACHE_DIR=/tmp/numba_cache
CMD ["python","app.py"]
