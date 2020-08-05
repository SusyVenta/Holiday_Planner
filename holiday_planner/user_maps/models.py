from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from PIL import Image
from users.models import Profile
from .select_countries_and_cities import select_countries_options, select_cities_options
import json
from multiselectfield import MultiSelectField


class PlacesVisited(models.Model):
    """
    Model to populate drop-down menus with countries visited.
    to see places visited by user: request.user.placesvisited.countries
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """ COUNTRIES VISITED BY CONTINENT """
    asian_countries_choices = select_countries_options("Asia")
    european_countries_choices = select_countries_options("Europe")
    african_countries_choices = select_countries_options("Africa")
    antarctic_countries_choices = select_countries_options("Antarctica")
    oceania_countries_choices = select_countries_options("Oceania")
    south_america_countries_choices = select_countries_options("South America")
    north_america_countries_choices = select_countries_options("North America")

    asian_countries = MultiSelectField(choices=asian_countries_choices, null=True, blank=True)
    european_countries = MultiSelectField(choices=european_countries_choices, null=True, blank=True)
    african_countries = MultiSelectField(choices=african_countries_choices, null=True, blank=True)
    antarctic_countries = MultiSelectField(choices=antarctic_countries_choices, null=True, blank=True)
    oceania_countries = MultiSelectField(choices=oceania_countries_choices, null=True, blank=True)
    south_american_countries = MultiSelectField(choices=south_america_countries_choices, null=True, blank=True)
    north_american_countries = MultiSelectField(choices=north_america_countries_choices, null=True, blank=True)

    def __str__(self):
        return f"{self.user} visited countries checkbox"

    class Meta:
        """ define nemes to be displayed on admin page """
        verbose_name_plural = "Countries visited checkbox multiple selections"


class CitiesVisitedCountry(models.Model):
    """ Every user can have multiple countries visited. Each instance of this class will save oen country """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.country_name}"

    class Meta:
        """ define nemes to be displayed on admin page """
        verbose_name = "Country visited"
        verbose_name_plural = "Countries visited"


class CitiesVisited(models.Model):
    """ For each country visited, save selection of cities visited """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Afghanistan_cities = MultiSelectField(choices=select_cities_options("Afghanistan"), null=True, blank=True)
    Albania_cities = MultiSelectField(choices=select_cities_options("Albania"), null=True, blank=True)
    Algeria_cities = MultiSelectField(choices=select_cities_options("Algeria"), null=True, blank=True)
    AmericanSamoa_cities = MultiSelectField(choices=select_cities_options("American Samoa"), null=True, blank=True)
    Andorra_cities = MultiSelectField(choices=select_cities_options("Andorra"), null=True, blank=True)
    Angola_cities = MultiSelectField(choices=select_cities_options("Angola"), null=True, blank=True)
    Anguilla_cities = MultiSelectField(choices=select_cities_options("Anguilla"), null=True, blank=True)
    Antarctica_cities = MultiSelectField(choices=select_cities_options("Antarctica"), null=True, blank=True)
    AntiguaandBarbuda_cities = MultiSelectField(choices=select_cities_options("Antigua and Barbuda"), null=True,
                                                blank=True)
    Argentina_cities = MultiSelectField(choices=select_cities_options("Argentina"), null=True, blank=True)
    Armenia_cities = MultiSelectField(choices=select_cities_options("Armenia"), null=True, blank=True)
    Aruba_cities = MultiSelectField(choices=select_cities_options("Aruba"), null=True, blank=True)
    Australia_cities = MultiSelectField(choices=select_cities_options("Australia"), null=True, blank=True)
    Austria_cities = MultiSelectField(choices=select_cities_options("Austria"), null=True, blank=True)
    Azerbaijan_cities = MultiSelectField(choices=select_cities_options("Azerbaijan"), null=True, blank=True)
    Bahamas_cities = MultiSelectField(choices=select_cities_options("Bahamas"), null=True, blank=True)
    Bahrain_cities = MultiSelectField(choices=select_cities_options("Bahrain"), null=True, blank=True)
    Bangladesh_cities = MultiSelectField(choices=select_cities_options("Bangladesh"), null=True, blank=True)
    Barbados_cities = MultiSelectField(choices=select_cities_options("Barbados"), null=True, blank=True)
    Belarus_cities = MultiSelectField(choices=select_cities_options("Belarus"), null=True, blank=True)
    Belgium_cities = MultiSelectField(choices=select_cities_options("Belgium"), null=True, blank=True)
    Belize_cities = MultiSelectField(choices=select_cities_options("Belize"), null=True, blank=True)
    Benin_cities = MultiSelectField(choices=select_cities_options("Benin"), null=True, blank=True)
    Bermuda_cities = MultiSelectField(choices=select_cities_options("Bermuda"), null=True, blank=True)
    Bhutan_cities = MultiSelectField(choices=select_cities_options("Bhutan"), null=True, blank=True)
    Bolivia_cities = MultiSelectField(choices=select_cities_options("Bolivia"), null=True, blank=True)
    BosniaandHerzegovina_cities = MultiSelectField(choices=select_cities_options("Bosnia and Herzegovina"), null=True,
                                                   blank=True)
    Botswana_cities = MultiSelectField(choices=select_cities_options("Botswana"), null=True, blank=True)
    BouvetIsland_cities = MultiSelectField(choices=select_cities_options("Bouvet Island"), null=True, blank=True)
    Brazil_cities = MultiSelectField(choices=select_cities_options("Brazil"), null=True, blank=True)
    BritishIndianOceanTerritory_cities = MultiSelectField(
        choices=select_cities_options("British Indian Ocean Territory"), null=True, blank=True)
    BruneiDarussalam_cities = MultiSelectField(choices=select_cities_options("Brunei Darussalam"), null=True,
                                               blank=True)
    Bulgaria_cities = MultiSelectField(choices=select_cities_options("Bulgaria"), null=True, blank=True)
    BurkinaFaso_cities = MultiSelectField(choices=select_cities_options("Burkina Faso"), null=True, blank=True)
    Burundi_cities = MultiSelectField(choices=select_cities_options("Burundi"), null=True, blank=True)
    Cambodia_cities = MultiSelectField(choices=select_cities_options("Cambodia"), null=True, blank=True)
    Cameroon_cities = MultiSelectField(choices=select_cities_options("Cameroon"), null=True, blank=True)
    Canada_cities = MultiSelectField(choices=select_cities_options("Canada"), null=True, blank=True)
    CapeVerde_cities = MultiSelectField(choices=select_cities_options("Cape Verde"), null=True, blank=True)
    CaymanIslands_cities = MultiSelectField(choices=select_cities_options("Cayman Islands"), null=True, blank=True)
    CentralAfricanRepublic_cities = MultiSelectField(choices=select_cities_options("Central African Republic"),
                                                     null=True, blank=True)
    Chad_cities = MultiSelectField(choices=select_cities_options("Chad"), null=True, blank=True)
    Chile_cities = MultiSelectField(choices=select_cities_options("Chile"), null=True, blank=True)
    China_cities = MultiSelectField(choices=select_cities_options("China"), null=True, blank=True)
    ChristmasIsland_cities = MultiSelectField(choices=select_cities_options("Christmas Island"), null=True, blank=True)
    CocosKeelingIslands_cities = MultiSelectField(choices=select_cities_options("Cocos (Keeling) Islands"), null=True,
                                                  blank=True)
    Colombia_cities = MultiSelectField(choices=select_cities_options("Colombia"), null=True, blank=True)
    Comoros_cities = MultiSelectField(choices=select_cities_options("Comoros"), null=True, blank=True)
    DemocraticRepublicofCongo_cities = MultiSelectField(choices=select_cities_options("Democratic Republic of Congo"),
                                                        null=True, blank=True)
    CookIslands_cities = MultiSelectField(choices=select_cities_options("Cook Islands"), null=True, blank=True)
    CostaRica_cities = MultiSelectField(choices=select_cities_options("Costa Rica"), null=True, blank=True)
    Croatia_cities = MultiSelectField(choices=select_cities_options("Croatia"), null=True, blank=True)
    Cuba_cities = MultiSelectField(choices=select_cities_options("Cuba"), null=True, blank=True)
    Cyprus_cities = MultiSelectField(choices=select_cities_options("Cyprus"), null=True, blank=True)
    CzechRepublic_cities = MultiSelectField(choices=select_cities_options("Czech Republic"), null=True, blank=True)
    Denmark_cities = MultiSelectField(choices=select_cities_options("Denmark"), null=True, blank=True)
    Djibouti_cities = MultiSelectField(choices=select_cities_options("Djibouti"), null=True, blank=True)
    Dominica_cities = MultiSelectField(choices=select_cities_options("Dominica"), null=True, blank=True)
    DominicanRepublic_cities = MultiSelectField(choices=select_cities_options("Dominican Republic"), null=True,
                                                blank=True)
    EastTimor_cities = MultiSelectField(choices=select_cities_options("East Timor"), null=True, blank=True)
    Ecuador_cities = MultiSelectField(choices=select_cities_options("Ecuador"), null=True, blank=True)
    Egypt_cities = MultiSelectField(choices=select_cities_options("Egypt"), null=True, blank=True)
    ElSalvador_cities = MultiSelectField(choices=select_cities_options("El Salvador"), null=True, blank=True)
    EquatorialGuinea_cities = MultiSelectField(choices=select_cities_options("Equatorial Guinea"), null=True,
                                               blank=True)
    Eritrea_cities = MultiSelectField(choices=select_cities_options("Eritrea"), null=True, blank=True)
    Estonia_cities = MultiSelectField(choices=select_cities_options("Estonia"), null=True, blank=True)
    Ethiopia_cities = MultiSelectField(choices=select_cities_options("Ethiopia"), null=True, blank=True)
    FalklandIslands_cities = MultiSelectField(choices=select_cities_options("Falkland Islands"), null=True, blank=True)
    FaroeIslands_cities = MultiSelectField(choices=select_cities_options("Faroe Islands"), null=True, blank=True)
    Fiji_cities = MultiSelectField(choices=select_cities_options("Fiji"), null=True, blank=True)
    Finland_cities = MultiSelectField(choices=select_cities_options("Finland"), null=True, blank=True)
    France_cities = MultiSelectField(choices=select_cities_options("France"), null=True, blank=True)
    FrenchGuiana_cities = MultiSelectField(choices=select_cities_options("French Guiana"), null=True, blank=True)
    FrenchPolynesia_cities = MultiSelectField(choices=select_cities_options("French Polynesia"), null=True, blank=True)
    FrenchSouthernandAntarcticLands_cities = MultiSelectField(
        choices=select_cities_options("French Southern and Antarctic Lands"), null=True, blank=True)
    Gabon_cities = MultiSelectField(choices=select_cities_options("Gabon"), null=True, blank=True)
    Gambia_cities = MultiSelectField(choices=select_cities_options("Gambia"), null=True, blank=True)
    Georgia_cities = MultiSelectField(choices=select_cities_options("Georgia"), null=True, blank=True)
    Germany_cities = MultiSelectField(choices=select_cities_options("Germany"), null=True, blank=True)
    Ghana_cities = MultiSelectField(choices=select_cities_options("Ghana"), null=True, blank=True)
    Gibraltar_cities = MultiSelectField(choices=select_cities_options("Gibraltar"), null=True, blank=True)
    Greece_cities = MultiSelectField(choices=select_cities_options("Greece"), null=True, blank=True)
    Greenland_cities = MultiSelectField(choices=select_cities_options("Greenland"), null=True, blank=True)
    Grenada_cities = MultiSelectField(choices=select_cities_options("Grenada"), null=True, blank=True)
    Guadeloupe_cities = MultiSelectField(choices=select_cities_options("Guadeloupe"), null=True, blank=True)
    Guam_cities = MultiSelectField(choices=select_cities_options("Guam"), null=True, blank=True)
    Guatemala_cities = MultiSelectField(choices=select_cities_options("Guatemala"), null=True, blank=True)
    Guinea_cities = MultiSelectField(choices=select_cities_options("Guinea"), null=True, blank=True)
    GuineaBissau_cities = MultiSelectField(choices=select_cities_options("Guinea-Bissau"), null=True, blank=True)
    Guyana_cities = MultiSelectField(choices=select_cities_options("Guyana"), null=True, blank=True)
    Haiti_cities = MultiSelectField(choices=select_cities_options("Haiti"), null=True, blank=True)
    HeardIslandandMcDonaldIslands_cities = MultiSelectField(
        choices=select_cities_options("Heard Island and McDonald Islands"), null=True, blank=True)
    HolySeeVaticanCity_cities = MultiSelectField(choices=select_cities_options("Holy See (Vatican City)"), null=True,
                                                 blank=True)
    Honduras_cities = MultiSelectField(choices=select_cities_options("Honduras"), null=True, blank=True)
    HongKong_cities = MultiSelectField(choices=select_cities_options("Hong Kong"), null=True, blank=True)
    Hungary_cities = MultiSelectField(choices=select_cities_options("Hungary"), null=True, blank=True)
    Iceland_cities = MultiSelectField(choices=select_cities_options("Iceland"), null=True, blank=True)
    India_cities = MultiSelectField(choices=select_cities_options("India"), null=True, blank=True)
    Indonesia_cities = MultiSelectField(choices=select_cities_options("Indonesia"), null=True, blank=True)
    Iran_cities = MultiSelectField(choices=select_cities_options("Iran"), null=True, blank=True)
    Iraq_cities = MultiSelectField(choices=select_cities_options("Iraq"), null=True, blank=True)
    Ireland_cities = MultiSelectField(choices=select_cities_options("Ireland"), null=True, blank=True)
    Israel_cities = MultiSelectField(choices=select_cities_options("Israel"), null=True, blank=True)
    Italy_cities = MultiSelectField(choices=select_cities_options("Italy"), null=True, blank=True)
    CotedIvoire_cities = MultiSelectField(choices=select_cities_options("Cote d'Ivoire"), null=True, blank=True)
    Jamaica_cities = MultiSelectField(choices=select_cities_options("Jamaica"), null=True, blank=True)
    Japan_cities = MultiSelectField(choices=select_cities_options("Japan"), null=True, blank=True)
    Jordan_cities = MultiSelectField(choices=select_cities_options("Jordan"), null=True, blank=True)
    Kazakhstan_cities = MultiSelectField(choices=select_cities_options("Kazakhstan"), null=True, blank=True)
    Kenya_cities = MultiSelectField(choices=select_cities_options("Kenya"), null=True, blank=True)
    Kiribati_cities = MultiSelectField(choices=select_cities_options("Kiribati"), null=True, blank=True)
    Kuwait_cities = MultiSelectField(choices=select_cities_options("Kuwait"), null=True, blank=True)
    Kyrgyzstan_cities = MultiSelectField(choices=select_cities_options("Kyrgyzstan"), null=True, blank=True)
    Laos_cities = MultiSelectField(choices=select_cities_options("Laos"), null=True, blank=True)
    Latvia_cities = MultiSelectField(choices=select_cities_options("Latvia"), null=True, blank=True)
    Lebanon_cities = MultiSelectField(choices=select_cities_options("Lebanon"), null=True, blank=True)
    Lesotho_cities = MultiSelectField(choices=select_cities_options("Lesotho"), null=True, blank=True)
    Liberia_cities = MultiSelectField(choices=select_cities_options("Liberia"), null=True, blank=True)
    LibyanArabJamahiriya_cities = MultiSelectField(choices=select_cities_options("Libyan Arab Jamahiriya"), null=True,
                                                   blank=True)
    Liechtenstein_cities = MultiSelectField(choices=select_cities_options("Liechtenstein"), null=True, blank=True)
    Lithuania_cities = MultiSelectField(choices=select_cities_options("Lithuania"), null=True, blank=True)
    Luxembourg_cities = MultiSelectField(choices=select_cities_options("Luxembourg"), null=True, blank=True)
    Macau_cities = MultiSelectField(choices=select_cities_options("Macau"), null=True, blank=True)
    Macedonia_cities = MultiSelectField(choices=select_cities_options("Macedonia"), null=True, blank=True)
    Madagascar_cities = MultiSelectField(choices=select_cities_options("Madagascar"), null=True, blank=True)
    Malawi_cities = MultiSelectField(choices=select_cities_options("Malawi"), null=True, blank=True)
    Malaysia_cities = MultiSelectField(choices=select_cities_options("Malaysia"), null=True, blank=True)
    Maldives_cities = MultiSelectField(choices=select_cities_options("Maldives"), null=True, blank=True)
    Mali_cities = MultiSelectField(choices=select_cities_options("Mali"), null=True, blank=True)
    Malta_cities = MultiSelectField(choices=select_cities_options("Malta"), null=True, blank=True)
    MarshallIslands_cities = MultiSelectField(choices=select_cities_options("Marshall Islands"), null=True, blank=True)
    Martinique_cities = MultiSelectField(choices=select_cities_options("Martinique"), null=True, blank=True)
    Mauritania_cities = MultiSelectField(choices=select_cities_options("Mauritania"), null=True, blank=True)
    Mauritius_cities = MultiSelectField(choices=select_cities_options("Mauritius"), null=True, blank=True)
    Mayotte_cities = MultiSelectField(choices=select_cities_options("Mayotte"), null=True, blank=True)
    Mexico_cities = MultiSelectField(choices=select_cities_options("Mexico"), null=True, blank=True)
    MicronesiaFederatedStatesof_cities = MultiSelectField(
        choices=select_cities_options("Micronesia, Federated States of"), null=True, blank=True)
    Moldova_cities = MultiSelectField(choices=select_cities_options("Moldova"), null=True, blank=True)
    Monaco_cities = MultiSelectField(choices=select_cities_options("Monaco"), null=True, blank=True)
    Mongolia_cities = MultiSelectField(choices=select_cities_options("Mongolia"), null=True, blank=True)
    Montserrat_cities = MultiSelectField(choices=select_cities_options("Montserrat"), null=True, blank=True)
    Morocco_cities = MultiSelectField(choices=select_cities_options("Morocco"), null=True, blank=True)
    Mozambique_cities = MultiSelectField(choices=select_cities_options("Mozambique"), null=True, blank=True)
    MjanmaBirma_cities = MultiSelectField(choices=select_cities_options("Mjanma(Birma)"), null=True, blank=True)
    Namibia_cities = MultiSelectField(choices=select_cities_options("Namibia"), null=True, blank=True)
    Nauru_cities = MultiSelectField(choices=select_cities_options("Nauru"), null=True, blank=True)
    Nepal_cities = MultiSelectField(choices=select_cities_options("Nepal"), null=True, blank=True)
    Netherlands_cities = MultiSelectField(choices=select_cities_options("Netherlands"), null=True, blank=True)
    NetherlandsAntilles_cities = MultiSelectField(choices=select_cities_options("Netherlands Antilles"), null=True,
                                                  blank=True)
    NewCaledonia_cities = MultiSelectField(choices=select_cities_options("New Caledonia"), null=True, blank=True)
    NewZealand_cities = MultiSelectField(choices=select_cities_options("New Zealand"), null=True, blank=True)
    Nicaragua_cities = MultiSelectField(choices=select_cities_options("Nicaragua"), null=True, blank=True)
    Niger_cities = MultiSelectField(choices=select_cities_options("Niger"), null=True, blank=True)
    Nigeria_cities = MultiSelectField(choices=select_cities_options("Nigeria"), null=True, blank=True)
    Niue_cities = MultiSelectField(choices=select_cities_options("Niue"), null=True, blank=True)
    NorfolkIsland_cities = MultiSelectField(choices=select_cities_options("Norfolk Island"), null=True, blank=True)
    NorthKorea_cities = MultiSelectField(choices=select_cities_options("North Korea"), null=True, blank=True)
    NorthernMarianaIslands_cities = MultiSelectField(choices=select_cities_options("Northern Mariana Islands"),
                                                     null=True, blank=True)
    Norway_cities = MultiSelectField(choices=select_cities_options("Norway"), null=True, blank=True)
    Oman_cities = MultiSelectField(choices=select_cities_options("Oman"), null=True, blank=True)
    Pakistan_cities = MultiSelectField(choices=select_cities_options("Pakistan"), null=True, blank=True)
    Palau_cities = MultiSelectField(choices=select_cities_options("Palau"), null=True, blank=True)
    Palestine_cities = MultiSelectField(choices=select_cities_options("Palestine"), null=True, blank=True)
    Panama_cities = MultiSelectField(choices=select_cities_options("Panama"), null=True, blank=True)
    PapuaNewGuinea_cities = MultiSelectField(choices=select_cities_options("Papua New Guinea"), null=True, blank=True)
    Paraguay_cities = MultiSelectField(choices=select_cities_options("Paraguay"), null=True, blank=True)
    Peru_cities = MultiSelectField(choices=select_cities_options("Peru"), null=True, blank=True)
    Philippines_cities = MultiSelectField(choices=select_cities_options("Philippines"), null=True, blank=True)
    PitcairnIslands_cities = MultiSelectField(choices=select_cities_options("Pitcairn Islands"), null=True, blank=True)
    Poland_cities = MultiSelectField(choices=select_cities_options("Poland"), null=True, blank=True)
    Portugal_cities = MultiSelectField(choices=select_cities_options("Portugal"), null=True, blank=True)
    PuertoRico_cities = MultiSelectField(choices=select_cities_options("Puerto Rico"), null=True, blank=True)
    Qatar_cities = MultiSelectField(choices=select_cities_options("Qatar"), null=True, blank=True)
    Reunion_cities = MultiSelectField(choices=select_cities_options("Reunion"), null=True, blank=True)
    Romania_cities = MultiSelectField(choices=select_cities_options("Romania"), null=True, blank=True)
    Russia_cities = MultiSelectField(choices=select_cities_options("Russia"), null=True, blank=True)
    Rwanda_cities = MultiSelectField(choices=select_cities_options("Rwanda"), null=True, blank=True)
    SaintHelena_cities = MultiSelectField(choices=select_cities_options("Saint Helena"), null=True, blank=True)
    SaintKittsandNevis_cities = MultiSelectField(choices=select_cities_options("Saint Kitts and Nevis"), null=True,
                                                 blank=True)
    SaintLucia_cities = MultiSelectField(choices=select_cities_options("Saint Lucia"), null=True, blank=True)
    SaintPierreandMiquelon_cities = MultiSelectField(choices=select_cities_options("Saint Pierre and Miquelon"),
                                                     null=True, blank=True)
    SaintVincentandtheGrenadines_cities = MultiSelectField(
        choices=select_cities_options("Saint Vincent and the Grenadines"), null=True, blank=True)
    Samoa_cities = MultiSelectField(choices=select_cities_options("Samoa"), null=True, blank=True)
    SanMarino_cities = MultiSelectField(choices=select_cities_options("San Marino"), null=True, blank=True)
    SaoTomeandPrincipe_cities = MultiSelectField(choices=select_cities_options("Sao Tome and Principe"), null=True,
                                                 blank=True)
    SaudiArabia_cities = MultiSelectField(choices=select_cities_options("Saudi Arabia"), null=True, blank=True)
    Senegal_cities = MultiSelectField(choices=select_cities_options("Senegal"), null=True, blank=True)
    Seychelles_cities = MultiSelectField(choices=select_cities_options("Seychelles"), null=True, blank=True)
    SierraLeone_cities = MultiSelectField(choices=select_cities_options("Sierra Leone"), null=True, blank=True)
    Singapore_cities = MultiSelectField(choices=select_cities_options("Singapore"), null=True, blank=True)
    Slovakia_cities = MultiSelectField(choices=select_cities_options("Slovakia"), null=True, blank=True)
    Slovenia_cities = MultiSelectField(choices=select_cities_options("Slovenia"), null=True, blank=True)
    SolomonIslands_cities = MultiSelectField(choices=select_cities_options("Solomon Islands"), null=True, blank=True)
    Somalia_cities = MultiSelectField(choices=select_cities_options("Somalia"), null=True, blank=True)
    SouthAfrica_cities = MultiSelectField(choices=select_cities_options("South Africa"), null=True, blank=True)
    SouthGeorgiaSouthSandwichIslands_cities = MultiSelectField(
        choices=select_cities_options("South Georgia South Sandwich Islands"), null=True, blank=True)
    SouthKorea_cities = MultiSelectField(choices=select_cities_options("South Korea"), null=True, blank=True)
    Spain_cities = MultiSelectField(choices=select_cities_options("Spain"), null=True, blank=True)
    SriLanka_cities = MultiSelectField(choices=select_cities_options("Sri Lanka"), null=True, blank=True)
    Sudan_cities = MultiSelectField(choices=select_cities_options("Sudan"), null=True, blank=True)
    Suriname_cities = MultiSelectField(choices=select_cities_options("Suriname"), null=True, blank=True)
    Svalbard_cities = MultiSelectField(choices=select_cities_options("Svalbard"), null=True, blank=True)
    Swaziland_cities = MultiSelectField(choices=select_cities_options("Swaziland"), null=True, blank=True)
    Sweden_cities = MultiSelectField(choices=select_cities_options("Sweden"), null=True, blank=True)
    Switzerland_cities = MultiSelectField(choices=select_cities_options("Switzerland"), null=True, blank=True)
    Syria_cities = MultiSelectField(choices=select_cities_options("Syria"), null=True, blank=True)
    Taiwan_cities = MultiSelectField(choices=select_cities_options("Taiwan"), null=True, blank=True)
    Tajikistan_cities = MultiSelectField(choices=select_cities_options("Tajikistan"), null=True, blank=True)
    Tanzania_cities = MultiSelectField(choices=select_cities_options("Tanzania"), null=True, blank=True)
    Thailand_cities = MultiSelectField(choices=select_cities_options("Thailand"), null=True, blank=True)
    Togo_cities = MultiSelectField(choices=select_cities_options("Togo"), null=True, blank=True)
    Tokelau_cities = MultiSelectField(choices=select_cities_options("Tokelau"), null=True, blank=True)
    Tonga_cities = MultiSelectField(choices=select_cities_options("Tonga"), null=True, blank=True)
    TrinidadandTobago_cities = MultiSelectField(choices=select_cities_options("Trinidad and Tobago"), null=True,
                                                blank=True)
    Tunisia_cities = MultiSelectField(choices=select_cities_options("Tunisia"), null=True, blank=True)
    Turkey_cities = MultiSelectField(choices=select_cities_options("Turkey"), null=True, blank=True)
    Turkmenistan_cities = MultiSelectField(choices=select_cities_options("Turkmenistan"), null=True, blank=True)
    TurksandCaicosIslands_cities = MultiSelectField(choices=select_cities_options("Turks and Caicos Islands"),
                                                    null=True, blank=True)
    Tuvalu_cities = MultiSelectField(choices=select_cities_options("Tuvalu"), null=True, blank=True)
    Uganda_cities = MultiSelectField(choices=select_cities_options("Uganda"), null=True, blank=True)
    Ukraine_cities = MultiSelectField(choices=select_cities_options("Ukraine"), null=True, blank=True)
    UnitedArabEmirates_cities = MultiSelectField(choices=select_cities_options("United Arab Emirates"), null=True,
                                                 blank=True)
    UnitedKingdom_cities = MultiSelectField(choices=select_cities_options("United Kingdom"), null=True, blank=True)
    UnitedStates_cities = MultiSelectField(choices=select_cities_options("United States"), null=True, blank=True)
    UnitedStatesMinorOutlyingIslands_cities = MultiSelectField(
        choices=select_cities_options("United States Minor Outlying Islands"), null=True, blank=True)
    Uruguay_cities = MultiSelectField(choices=select_cities_options("Uruguay"), null=True, blank=True)
    Uzbekistan_cities = MultiSelectField(choices=select_cities_options("Uzbekistan"), null=True, blank=True)
    Vanuatu_cities = MultiSelectField(choices=select_cities_options("Vanuatu"), null=True, blank=True)
    Venezuela_cities = MultiSelectField(choices=select_cities_options("Venezuela"), null=True, blank=True)
    Vietnam_cities = MultiSelectField(choices=select_cities_options("Vietnam"), null=True, blank=True)
    BritishVirginIslands_cities = MultiSelectField(choices=select_cities_options("British Virgin Islands"), null=True,
                                                   blank=True)
    UnitedStatesVirginIslands_cities = MultiSelectField(choices=select_cities_options("United States Virgin Islands"),
                                                        null=True, blank=True)
    WallisandFutunaIslands_cities = MultiSelectField(choices=select_cities_options("Wallis and Futuna Islands"),
                                                     null=True, blank=True)
    WesternSahara_cities = MultiSelectField(choices=select_cities_options("Western Sahara"), null=True, blank=True)
    Yemen_cities = MultiSelectField(choices=select_cities_options("Yemen"), null=True, blank=True)
    Zambia_cities = MultiSelectField(choices=select_cities_options("Zambia"), null=True, blank=True)
    Zimbabwe_cities = MultiSelectField(choices=select_cities_options("Zimbabwe"), null=True, blank=True)
    IsleofMan_cities = MultiSelectField(choices=select_cities_options("Isle of Man"), null=True, blank=True)
    Montenegro_cities = MultiSelectField(choices=select_cities_options("Montenegro"), null=True, blank=True)
    AlandIslands_cities = MultiSelectField(choices=select_cities_options("Aland Islands"), null=True, blank=True)
    Serbia_cities = MultiSelectField(choices=select_cities_options("Serbia"), null=True, blank=True)

    def __str__(self):
        return f"visited cities for user {self.user} checkbox"

    class Meta:
        """ define nemes to be displayed on admin page """
        verbose_name_plural = "Cities visited checkbox multiple selections"
