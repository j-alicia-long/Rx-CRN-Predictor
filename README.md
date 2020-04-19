# Rx-fitme
A CRN risk factor predictor to help physicians combat CRN (cost-related non-adherence) for low-income and other affected patients.

### Development Setup

Clone the project and run the docker container:
```
git clone [url]
cd Rx-CRN-Predictor
docker-compose up
```
The Django server runs from the `web` service, PostgreSQL runs from `db`, and the ML API runs from `api`.

Note: If you get an "access denied error" during `docker-compose up`, run `chmod +x entrypoint.sh`.


## Running the tests

To run the test suite:
```
docker-compose exec web bash    # exec into the django server container
python manage.py test           # run the django test suite
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [PostgreSQL](https://www.postgresql.org/) - Database
* [Heroku](https://www.postgresql.org/) - Deployment


## Authors

* **Jennifer Long** - [j-alicia-long](https://github.com/j-alicia-long) - Django project, Full-stack
* **Ishaan Dey** - [ishaandey](https://github.com/ishaandey) - ML


## Acknowledgments

* The lovely HackCville Deploy staff (Chris, Jedidiah, Harrison)
