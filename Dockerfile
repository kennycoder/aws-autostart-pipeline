FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
COPY ./build/nginx-custom.conf /etc/nginx/conf.d/nginx.conf
RUN pip install boto3 botostubs aws-xray-sdk --user
