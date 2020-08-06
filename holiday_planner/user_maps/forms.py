from django import forms
from .models import PlacesVisited, CitiesVisited, CitiesVisitedCountry

'''
CountriesUpdateForm class displays and retrieves information from the multiple choice menus, in order specified below.
'''


class CountriesUpdateForm(forms.ModelForm):
    class Meta:
        model = PlacesVisited
        fields = ['asian_countries', 'european_countries', 'oceania_countries', 'african_countries',
                  'south_american_countries', 'north_american_countries', 'antarctic_countries']


class CitiesUpdateForm(forms.ModelForm):
    class Meta:
        model = CitiesVisited
        fields = ['Afghanistan_cities', 'Albania_cities', 'Algeria_cities', 'AmericanSamoa_cities', 'Andorra_cities',
                  'Angola_cities', 'Anguilla_cities', 'Antarctica_cities', 'AntiguaandBarbuda_cities',
                  'Argentina_cities', 'Armenia_cities', 'Aruba_cities', 'Australia_cities', 'Austria_cities',
                  'Azerbaijan_cities', 'Bahamas_cities', 'Bahrain_cities', 'Bangladesh_cities', 'Barbados_cities',
                  'Belarus_cities', 'Belgium_cities', 'Belize_cities', 'Benin_cities', 'Bermuda_cities',
                  'Bhutan_cities', 'Bolivia_cities', 'BosniaandHerzegovina_cities', 'Botswana_cities',
                  'BouvetIsland_cities', 'Brazil_cities', 'BritishIndianOceanTerritory_cities',
                  'BruneiDarussalam_cities', 'Bulgaria_cities', 'BurkinaFaso_cities', 'Burundi_cities',
                  'Cambodia_cities', 'Cameroon_cities', 'Canada_cities', 'CapeVerde_cities', 'CaymanIslands_cities',
                  'CentralAfricanRepublic_cities', 'Chad_cities', 'Chile_cities', 'China_cities',
                  'ChristmasIsland_cities', 'CocosKeelingIslands_cities', 'Colombia_cities', 'Comoros_cities',
                  'DemocraticRepublicofCongo_cities', 'CookIslands_cities', 'CostaRica_cities', 'Croatia_cities',
                  'Cuba_cities', 'Cyprus_cities', 'CzechRepublic_cities', 'Denmark_cities', 'Djibouti_cities',
                  'Dominica_cities', 'DominicanRepublic_cities', 'EastTimor_cities', 'Ecuador_cities', 'Egypt_cities',
                  'ElSalvador_cities', 'EquatorialGuinea_cities', 'Eritrea_cities', 'Estonia_cities', 'Ethiopia_cities',
                  'FalklandIslands_cities', 'FaroeIslands_cities', 'Fiji_cities', 'Finland_cities', 'France_cities',
                  'FrenchGuiana_cities', 'FrenchPolynesia_cities', 'FrenchSouthernandAntarcticLands_cities',
                  'Gabon_cities', 'Gambia_cities', 'Georgia_cities', 'Germany_cities', 'Ghana_cities',
                  'Gibraltar_cities', 'Greece_cities', 'Greenland_cities', 'Grenada_cities', 'Guadeloupe_cities',
                  'Guam_cities', 'Guatemala_cities', 'Guinea_cities', 'GuineaBissau_cities', 'Guyana_cities',
                  'Haiti_cities', 'HeardIslandandMcDonaldIslands_cities', 'HolySeeVaticanCity_cities',
                  'Honduras_cities', 'HongKong_cities', 'Hungary_cities', 'Iceland_cities', 'India_cities',
                  'Indonesia_cities', 'Iran_cities', 'Iraq_cities', 'Ireland_cities', 'Israel_cities',
                  'Italy_cities', 'CotedIvoire_cities', 'Jamaica_cities', 'Japan_cities', 'Jordan_cities',
                  'Kazakhstan_cities', 'Kenya_cities', 'Kiribati_cities', 'Kuwait_cities', 'Kyrgyzstan_cities',
                  'Laos_cities', 'Latvia_cities', 'Lebanon_cities', 'Lesotho_cities', 'Liberia_cities',
                  'LibyanArabJamahiriya_cities', 'Liechtenstein_cities', 'Lithuania_cities', 'Luxembourg_cities',
                  'Macau_cities', 'Macedonia_cities', 'Madagascar_cities', 'Malawi_cities', 'Malaysia_cities',
                  'Maldives_cities', 'Mali_cities', 'Malta_cities', 'MarshallIslands_cities', 'Martinique_cities',
                  'Mauritania_cities', 'Mauritius_cities', 'Mayotte_cities', 'Mexico_cities',
                  'MicronesiaFederatedStatesof_cities', 'Moldova_cities', 'Monaco_cities', 'Mongolia_cities',
                  'Montserrat_cities', 'Morocco_cities', 'Mozambique_cities', 'MjanmaBirma_cities', 'Namibia_cities',
                  'Nauru_cities', 'Nepal_cities', 'Netherlands_cities', 'NetherlandsAntilles_cities',
                  'NewCaledonia_cities', 'NewZealand_cities', 'Nicaragua_cities', 'Niger_cities', 'Nigeria_cities',
                  'Niue_cities', 'NorfolkIsland_cities', 'NorthKorea_cities', 'NorthernMarianaIslands_cities',
                  'Norway_cities', 'Oman_cities', 'Pakistan_cities', 'Palau_cities', 'Palestine_cities',
                  'Panama_cities', 'PapuaNewGuinea_cities', 'Paraguay_cities', 'Peru_cities', 'Philippines_cities',
                  'PitcairnIslands_cities', 'Poland_cities', 'Portugal_cities', 'PuertoRico_cities', 'Qatar_cities',
                  'Reunion_cities', 'Romania_cities', 'Russia_cities', 'Rwanda_cities', 'SaintHelena_cities',
                  'SaintKittsandNevis_cities', 'SaintLucia_cities', 'SaintPierreandMiquelon_cities',
                  'SaintVincentandtheGrenadines_cities', 'Samoa_cities', 'SanMarino_cities',
                  'SaoTomeandPrincipe_cities', 'SaudiArabia_cities', 'Senegal_cities', 'Seychelles_cities',
                  'SierraLeone_cities', 'Singapore_cities', 'Slovakia_cities', 'Slovenia_cities',
                  'SolomonIslands_cities', 'Somalia_cities', 'SouthAfrica_cities',
                  'SouthGeorgiaSouthSandwichIslands_cities', 'SouthKorea_cities', 'Spain_cities',
                  'SriLanka_cities', 'Sudan_cities', 'Suriname_cities', 'Svalbard_cities', 'Swaziland_cities',
                  'Sweden_cities', 'Switzerland_cities', 'Syria_cities', 'Taiwan_cities', 'Tajikistan_cities',
                  'Tanzania_cities', 'Thailand_cities', 'Togo_cities', 'Tokelau_cities', 'Tonga_cities',
                  'TrinidadandTobago_cities', 'Tunisia_cities', 'Turkey_cities', 'Turkmenistan_cities',
                  'TurksandCaicosIslands_cities', 'Tuvalu_cities', 'Uganda_cities', 'Ukraine_cities',
                  'UnitedArabEmirates_cities', 'UnitedKingdom_cities', 'UnitedStates_cities',
                  'UnitedStatesMinorOutlyingIslands_cities', 'Uruguay_cities', 'Uzbekistan_cities',
                  'Vanuatu_cities', 'Venezuela_cities', 'Vietnam_cities', 'BritishVirginIslands_cities',
                  'UnitedStatesVirginIslands_cities', 'WallisandFutunaIslands_cities', 'WesternSahara_cities',
                  'Yemen_cities', 'Zambia_cities', 'Zimbabwe_cities', 'IsleofMan_cities', 'Montenegro_cities',
                  'AlandIslands_cities', 'Serbia_cities']


class SingleCountryUpdateForm(forms.ModelForm):
    class Meta:
        model = CitiesVisitedCountry
        fields = ['country_name']
