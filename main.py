from cdek import (
    CDEKAuth,
    CDEKToken,
    CDEKLocation,
    RegionsRequestDto,
    V2LocationCitiesRequestDto,
    SuggestCityRequestDto,
    SuggestCityRequestDto,
    fetch_fake_client_id,
    fetch_fake_client_secret,
)


def main() -> None:
    cdek_auth = CDEKAuth(
        client_id=fetch_fake_client_id(),
        client_secret=fetch_fake_client_secret(),
    )
    location = CDEKLocation(CDEKToken(cdek_auth))
    """regions = location.fetch_regions(RegionsRequestDto(country_codes=["RU"]))
    if regions:
        regions.sort(key=lambda region: region.country_code)
        for region in regions:
            print(region)"""

    """cities = location.fetch_cities(V2LocationCitiesRequestDto(country_codes=["RU"], region_code=39))
    if cities:
        cities.sort(key=lambda city: city.country_code)
        for city in cities:
            print(city)"""
    postalcodes = location.fetch_suggest_cities(SuggestCityRequestDto(name="разумное"))
    print(postalcodes)


if __name__ == "__main__":
    main()
