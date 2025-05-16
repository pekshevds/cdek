from cdek import (
    CDEKLocation,
    RegionsRequestDto,
    V2LocationCitiesRequestDto,
    PostalcodeRequestDto,
    SuggestCityRequestDto,
)


def test__fetch_regions(location: CDEKLocation) -> None:
    """fetch_regions"""
    assert location.fetch_regions(RegionsRequestDto(country_codes=["RU"])) is not None


def test__fetch_cities(location: CDEKLocation) -> None:
    """fetch_cities"""
    assert (
        location.fetch_cities(V2LocationCitiesRequestDto(country_codes=["RU"]))
        is not None
    )


def test__fetch_postalcodes(location: CDEKLocation) -> None:
    """fetch_postalcodes
    81921 - Малая Сунь
    """
    assert location.fetch_postalcodes(PostalcodeRequestDto(code=81921)) is not None


def test__fetch_suggest_cities(location: CDEKLocation) -> None:
    """fetch_suggest_cities"""
    assert (
        location.fetch_suggest_cities(SuggestCityRequestDto(name="Круглое Поле"))
        is not None
    )
