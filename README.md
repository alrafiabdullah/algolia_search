# Algolia Search

##

## Requirements

- Considering you already have an account set up in [Algolia](https://www.algolia.com/pricing/)
- Create and activate a virtual environment
- Run `pip install -r requirements.txt`
- Create `secrets.json` with the following contents:

```
{
    "DJANGO_SECRET_KEY": "",
    "ALGOLIA_APPLICATION_ID": "",
    "ALGOLIA_API_KEY": ""
}
```

> Must be the Admin API Key

- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Run `python manage.py runserver`

##

## Active Endpoints

> [127.0.0.1:8000?car_name=ANY_CAR_ATTRIBUTE](http://127.0.0.1:8000?car_name) - GET - searches for the car

> [127.0.0.1:8000](http://127.0.0.1:8000) - POST - creates 1000 car records

##
