from django.contrib import admin
import algoliasearch_django as algoliasearch

from .models import Cars

algoliasearch.register(Cars)
admin.site.register(Cars)
