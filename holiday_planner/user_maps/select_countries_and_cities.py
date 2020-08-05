from holiday_planner.settings import BASE_DIR
import os
import json


def select_cities_options(country_in):
    """
    country_in = 'United States'
    Returns a list with tuple of cities for country_in. Will be used to populate city by country drop-down menus.
    """
    options_by_country = []
    if country_in == "Default":
        options_by_country.append((" ", " "))
        return options_by_country
    with open(os.path.join(BASE_DIR, 'user_maps', 'static', 'user_maps', 'cities_by_country.json'), mode='r') as file:
        content = json.load(file)
        for country in content:
            if country == str(country_in):
                for city in content[country]:
                    options_by_country.append((city, city))
    return options_by_country


def select_countries_options(continent):
    """
    Function used by model 'PlacesVisited' to populate drop-down menus by continent with all country options.
    It is using a json file('country_by_continent.json').
    It sorts a countries' names by continent and saves it as an lists for all continents.
    Function returns options for all continent.
    """
    options_europe = []
    options_asia = []
    options_north_america = []
    options_south_america = []
    options_oceania = []
    options_antarctica = []
    options_africa = []

    with open(os.path.join(BASE_DIR, 'user_maps', 'static', 'user_maps', 'country_by_continent.json'), mode='r') as file:
        content = json.load(file)
        for x in content:
            if x['continent'] == 'Europe':
                 options_europe.append((x['country'], x['country']))
            if x['continent'] == 'Asia':
                options_asia.append((x['country'], x['country']))
            if x['continent'] == 'Africa':
                options_africa.append((x['country'], x['country']))
            if x['continent'] == 'Antarctica':
                options_antarctica.append((x['country'], x['country']))
            if x['continent'] == 'Oceania':
                options_oceania.append((x['country'], x['country']))
            if x['continent'] == 'South America':
                options_south_america.append((x['country'], x['country']))
            if x['continent'] == 'North America':
                options_north_america.append((x['country'], x['country']))

    if continent == 'Europe':
        return options_europe
    elif continent == 'Asia':
        return options_asia
    elif continent == 'Africa':
        return options_africa
    elif continent == 'Antarctica':
        return options_antarctica
    elif continent == 'Oceania':
        return options_oceania
    elif continent == 'South America':
        return options_south_america
    elif continent == 'North America':
        return options_north_america


def construct_cities_model():
    """ substitute:
    - spaces with _
    - apostrophe with nothing

    """
    with open(os.path.join(BASE_DIR, 'user_maps', 'static', 'user_maps', 'country_by_continent.json'), mode='r') as file:
        content = json.load(file)
        for x in content:
            country = x['country']
            country_variable = country.replace("-", "").replace(" ", "").replace("'", "").replace("(", "")\
                .replace(")", "").replace(",", "")
            print(f'\n\nclass {country_variable}CitiesVisited(models.Model):\n\tuser = models.OneToOneField(User, '
                  f'on_delete=models.CASCADE)\n\tcountry = models.CharField(max_length=50)\n\tcities '
                  f'= MultiSelectField(choices=select_cities_options("{country}"), null=True, '
                  'blank=True)\n\tdef __str__(self):\n\t\treturn f"visited cities for country {self.country} '
                  f'checkbox"\n\tclass Meta:\n\t\tverbose_name_plural = "{country_variable} cities visited checkbox '
                  f'multiple selections"')


# construct_cities_model()

#
# class AfghanistanCitiesVisited(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     country = models.CharField(max_length=50)
#     Afghanistan_cities = MultiSelectField(choices=select_cities_options("Afghanistan"), null=True, blank=True)
#
#     def __str__(self):
#         return f"visited cities for country {self.country} checkbox"
#
#     class Meta:
#         """ define nemes to be displayed on admin page """
#         verbose_name_plural = "Afghanistan cities visited checkbox multiple selections"