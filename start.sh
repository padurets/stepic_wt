virtualenv --python=python3.4 python
source python/bin/activate
pip install -r requirements.txt
nohup gunicorn -b 0.0.0.0:8080 hello:app &
cd ask
nohup gunicorn -b 0.0.0.0:8000 ask.wsgi &
nohup sudo gunicorn -b 127.0.0.1:80 ask.wsgi &