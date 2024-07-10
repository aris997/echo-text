FROM python3.12

USER root

RUN apt-get install ffmpeg

RUN makedir app

WORKDIR /app

USER 1001

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app" "--host", "0.0.0.0", "--port", "8000", "--reload"]