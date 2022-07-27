FROM alpine:latest

WORKDIR /app

# Install python/pip
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --update --no-cache \
    sudo \
    nginx \
    gcc libc-dev build-base alpine-sdk \
    g++ snappy snappy-dev libexecinfo libexecinfo-dev \
    krb5-pkinit krb5-dev krb5 \
    python3 python3-dev && \
    ln -sf python3 /usr/bin/python && \
    apk --no-cache add ca-certificates wget && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk && \
    apk add glibc-2.28-r0.apk
    #&& rm -rf /var/lib/apt/lists/*

RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade pip setuptools

RUN addgroup -S django && adduser -G django -S django && \
    echo "django ALL=(root) NOPASSWD: $(which nginx)" >> /etc/sudoers && \
    mkdir -p /var/www/static && chown django:django /var/www/static && \
    touch /tmp/nginx.pid && chown django:django /tmp/nginx.pid && \
    mkdir -p /var/log/nginx && chown django:django /var/log/nginx && \
    mkdir -p /var/lib/nginx && chown django:django /var/lib/nginx

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

RUN apk add --update --no-cache sed

# Modify erroneous files
RUN cd /usr/lib/python3.10/site-packages/graphene_django/ && \
    find . -type f -exec sed -i "s/force_text/force_str/g" {} \;

RUN cd /usr/lib/python3.10/site-packages/graphql_jwt/ && \
    find . -type f -exec sed -i "s/ugettext/gettext/g" {} \;

RUN cd /usr/lib/python3.10/site-packages/graphql_jwt/ && \
    KEYWORD="Signal(providing_args=['request', 'user'])"; \
    ESCAPED_KEYWORD=$(printf '%s\n' "$KEYWORD" | sed -e 's/[]\/$*.^[]/\\&/g'); \
    REPLACE="Signal()"; \
    ESCAPED_REPLACE=$(printf '%s\n' "$REPLACE" | sed -e 's/[\/&]/\\&/g'); \
    find . -type f -exec sed -i "s/$ESCAPED_KEYWORD/$ESCAPED_REPLACE/g" {} \;

RUN cd /usr/lib/python3.10/site-packages/graphql_jwt/refresh_token/ && \
    export KEYWORD="Signal(providing_args=['request', 'refresh_token'])" && \
    export ESCAPED_KEYWORD=$(printf '%s\n' "$KEYWORD" | sed -e 's/[]\/$*.^[]/\\&/g') && \
    export REPLACE="Signal()" && \
    export ESCAPED_REPLACE=$(printf '%s\n' "$REPLACE" | sed -e 's/[\/&]/\\&/g') && \
    find . -type f -exec sed -i "s/$ESCAPED_KEYWORD/$ESCAPED_REPLACE/g" {} \;

USER django

ENV SECRET_KEY=INSECURE_PLACEHOLDER \
    HOST='*' \
    DB_HOST='db' \
    DB_NAME='default_db' \
    DB_USER='root' \
    DB_PASSWORD='root' \
    DJANGO_SUPERUSER_USERNAME='admin' \
    DJANGO_SUPERUSER_PASSWORD='django-todo-react' \
    DJANGO_SUPERUSER_EMAIL='issamoutassourt@gmail.com'

# Now copy in our code, and run it
COPY --chown=django:django . /app


## Collect static files
COPY nginx.conf /etc/nginx/nginx.conf
#RUN python3 -u manage.py collectstatic --link
RUN python3 -u manage.py migrate
RUN python3 -u manage.py createsuperuser --noinput

## Now copy in our code, and run it
COPY . /app
EXPOSE 8000
CMD sudo nginx && \
    gunicorn --config gunicorn_config.py djangodocker.wsgi
