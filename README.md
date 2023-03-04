## Setup database
Is needed to install postrgres and create user tonnie.

CREATE USER tonnie PASSWORD 'tonnie';

CREATEA DATABASE data OWNER tonnie;

## Install dependecies
pip3 install -r requirements.txt

## Setup database
flask db init

flask db migrate -m "Create Tables"

flask db upgrade

## Run project
python3 -m flask run


