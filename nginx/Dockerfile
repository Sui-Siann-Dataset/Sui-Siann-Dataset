FROM python:3.7 AS tsiantuan
MAINTAINER a8568730

RUN apt-get update && apt-get install -y sox normalize-audio

RUN mkdir djangoAdmin
WORKDIR djangoAdmin
COPY requirements.txt .
RUN pip install -r ./requirements.txt
RUN pip install --upgrade https://github.com/i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7/archive/master.zip
COPY . .

# 資料庫囥佇 ./tsu-liāu
RUN sed -i "s/os.path.join(BASE_DIR, 'db.sqlite3')/os.path.join(BASE_DIR, 'tsu-liāu','db.sqlite3')/g"  ./SuiSiannAdmin/settings.py
RUN cat ./SuiSiannAdmin/docker_tsuki.py >> ./SuiSiannAdmin/settings.py
RUN python manage.py collectstatic

FROM nginx:1-alpine

COPY ./nginx/default.conf /etc/nginx/conf.d
COPY --from=tsiantuan /static/ /user/share/nginx/html/static/
