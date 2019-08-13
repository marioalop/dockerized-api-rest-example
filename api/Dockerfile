FROM python:3.7.3-stretch

WORKDIR /src

RUN apt-get update && apt-get install -y python3-pip && \
    apt-get install -y bash git vim python3-redis python3-psycopg2 supervisor && \
    rm -rf /var/cache/apk/*

COPY . /src/

RUN pip3 install -r requirements.txt && \
    cp supervisord.conf /etc/supervisord.conf && \
    echo "DONE!"

EXPOSE 8000

CMD ["supervisord"]
