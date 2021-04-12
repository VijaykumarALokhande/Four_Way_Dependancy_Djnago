from django.contrib import admin
from .models import Person, Country, State, District, City

admin.site.register(Person)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
