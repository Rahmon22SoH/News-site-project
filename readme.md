### Description


### About the project

### Project setup
 ./run.sh

Flask-Migrate

flask db init

flask db migrate -m "Initial migration."

flask db upgrade

flask db stamp # id Migrate


Запустим Celery

Celery запускается немного по разному на Windows и Linux/Mac

Linux/Mac: celery -A tasks worker -B --loglevel=info

Windows: set FORKED_BY_MULTIPROCESSING=1
            && celery -A tasks worker --loglevel=info