# Events Planners
#### A site that is used to host events.

## Description
A web application that that helps people find events

[Behaviour Specifications](specs.md)

## Table of content
1. [Description](#description)
2. [Setup and installations](#setup-and-installations)
3. [Contributing](#contributing)
4. [Bugs](#bugs)
5. [License](#[license](license))


## Setup and installations

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - Django
    - Postgresql

#### Clone the Repo and enter the project folder.
```bash
git clone git@github.com:newtonkiragu/events.git && cd events
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv venv
```

```bash
source venv/bin/activate
```

#### Create Database
Create a database on your local machine

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<secret_key>'
DB_NAME='events'
DB_USER='<username>'
DB_PASSWORD='<paswword>'
DB_HOST='localhost'
DB_PORT='5432'
DEBUG=True
ALLOWED_HOSTS='*'
MODE='dev'

```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Run migrations
```bash
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome!

## Bugs
No known bugs if a bug is found create an issue in the [issues section](https://github.com/newtonkiragu/events/issues) of the repository.
