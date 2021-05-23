# Djangovue

Very simple example of running multiple vue js 3.x apps rendered by django using django webpack loader.


# Build & Setup

    docker-compose build
    cd apps/vue/src
    yarn
    cd ../../../
    docker-compose run --rm django ./manage.py migrate
    docker-compose run --rm django ./manage.py createsuperuser

# Run

    docker-compose up

## Visit 

    http://localhost:8000/app1/
