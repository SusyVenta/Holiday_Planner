import folium
import os
from holiday_planner.settings import BASE_DIR


class MapCreation:
    def create_base_map(self, countries_list=None):
        """ font awesome icons: https://www.w3schools.com/icons/fontawesome_icons_webapp.asp"""
        base_map = folium.Map(location=[30, 5], zoom_start=2, tiles=None)
        folium.TileLayer(tiles="CartoDB positron", name='Base map').add_to(base_map)
        save_path = os.path.join(BASE_DIR, "user_maps", "static", "user_maps", "static_map.html")
        folium.Marker(location=[49.61167, 6.13],
                      popup="Home",
                      tooltip="Luxembourg",
                      icon=folium.Icon(color="orange", icon="fa-check-square-o", prefix="fa")).add_to(base_map)
        countries_coordinates_path = os.path.join(BASE_DIR, "user_maps", "static", "user_maps", "world.json")
        if not countries_list:
            folium.GeoJson(data=open(countries_coordinates_path, "r", encoding="utf-8-sig").read(),
                           name="Countries visited",
                           style_function=lambda country_data: {
                               'fillColor': "green",
                               'fillOpacity': 0.3,
                               'color': 'purple',
                               'line_opacity': 0.2,
                               'weight': 0.2
                           }
                           ).add_to(base_map)
        else:
            folium.GeoJson(data=open(countries_coordinates_path, "r", encoding="utf-8-sig").read(),
                           name="Countries visited",
                           style_function=lambda country_data: {
                               'fillColor': self.get_color(country_data, countries_list),
                               'fillOpacity': 0.3,
                               'color': 'purple',
                               'line_opacity': 0.2,
                               'weight': 0.2
                           }
                           ).add_to(base_map)

        folium.LayerControl().add_to(base_map)
        base_map.save(save_path)

    def get_color(self, country_data, countries_list):
        """
        function which returns color of the map.
        if name of chosen country is equal to the country name from json file it returns red colour
        for that country, if not it returns blue"""

        for x in countries_list:
            if x in country_data['properties']['NAME']:
                return 'blue'
        else:
            return 'green'