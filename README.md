# PostgresClasses

fonte dos nossos dados: https://www.kaggle.com/datasets/joebeachcapital/fast-food

# HOW TO
* 1. Clone its repository:
    - git clone https://github.com/victor-s-santos/Postgres-Classes

* 2. Build the image:
    - cd Postgres-Classes
    - docker-compose up --build

* 3. Execute the python script:
    - cd python |`to get the terminal inside python directory`
    - python -m venv .venv |`to create a python virtualenv`
    - source .venv/bin/activate | `to use the created virtualenv in the previous step`
    - python main.py | `to execute the main.py script`

* 4. Optionally: Create a dump file from the populated database:
    - pg_dump -h localhost -U postgres mcdonalds_health_db -f sql/mcdonalds_health_db.sql
