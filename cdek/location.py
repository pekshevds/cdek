from typing import Any
from dataclasses import dataclass
from decimal import Decimal
import httpx
from cdek import CDEKToken


@dataclass(frozen=True, kw_only=True)
class Region:
    region: str = ""
    region_code: int = 0
    country: str = ""
    country_code: str = ""


@dataclass(frozen=True, kw_only=True)
class City:
    code: int = 0
    city_uuid: str = ""
    city: str = ""
    fias_guid: str = ""
    kladr_code: str = ""
    country_code: str
    country: str = ""
    region: str = ""
    region_code: int = 0
    sub_region: str = ""
    longitude: Decimal = Decimal("0")
    latitude: Decimal = Decimal("0")
    time_zone: str = ""
    payment_limit: Decimal = Decimal("0")


@dataclass(frozen=True, kw_only=True)
class PostalCode:
    code: int
    postal_codes: list[str]


@dataclass(frozen=True, kw_only=True)
class SuggestCity:
    city_uuid: str
    code: int
    full_name: str


class CDEKLocation:
    def __init__(self, token: CDEKToken, fake: bool = True):
        self.__token = token
        self.__fake = fake

    def _fetch_base_url(self) -> str:
        return "https://api.edu.cdek.ru" if self.__fake else "https://api.cdek.ru"

    def _fetch_base_header(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {str(self.__token)}"}

    def fetch_regions(
        self,
        country_codes: list[str],
        size: int = 1000,
        page: int = 0,
        lang: str = "rus",
    ) -> list[Region]:
        """/v2/location/regions"""
        params: dict[str, Any] = dict()
        params["country_codes"] = country_codes
        params["size"] = size
        params["page"] = page
        params["lang"] = lang

        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/location/regions",
            headers=self._fetch_base_header(),
            params=params,
        )
        return [Region(**record) for record in responce.json()]

    def fetch_cities(
        self,
        country_codes: list[str],
        region_code: int,
        fias_guid: str = "",
        postal_code: str = "",
        code: int = 0,
        city: str = "",
        payment_limit: Decimal = Decimal("0"),
        size: int = 1000,
        page: int = 0,
        lang: str = "rus",
    ) -> list[City]:
        """/v2/location/cities"""
        params: dict[str, Any] = dict()
        params["country_codes"] = country_codes
        params["region_code"] = region_code
        if fias_guid:
            params["fias_guid"] = fias_guid
        if postal_code:
            params["postal_code"] = postal_code
        if code:
            params["code"] = code
        if city:
            params["city"] = city
        if payment_limit:
            params["payment_limit"] = payment_limit
        params["size"] = size
        params["page"] = page
        params["lang"] = lang
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/location/cities",
            headers=self._fetch_base_header(),
            params=params,
        )
        return [City(**record) for record in responce.json()]

    def fetch_postalcodes(self, code: int) -> PostalCode:
        """/v2/location/postalcodes"""
        params: dict[str, Any] = dict()
        params["code"] = code
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/location/postalcodes",
            headers=self._fetch_base_header(),
            params=params,
        )
        return PostalCode(**responce.json())

    def fetch_suggest_cities(
        self, name: str, country_code: str = ""
    ) -> list[SuggestCity]:
        """/v2/location/suggest/cities"""
        params: dict[str, Any] = dict()
        params["name"] = name
        if country_code:
            params["country_code"] = country_code
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/location/suggest/cities",
            headers=self._fetch_base_header(),
            params=params,
        )
        return [SuggestCity(**record) for record in responce.json()]
