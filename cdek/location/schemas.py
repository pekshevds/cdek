from typing import Optional
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, kw_only=True)
class RegionsRequestDto:
    country_codes: Optional[list[str]] = None
    size: Optional[int] = 1000
    page: Optional[int] = 0
    lang: Optional[str] = "rus"


@dataclass(frozen=True, kw_only=True)
class Region:
    region: str
    region_code: int = 0
    country: str
    country_code: str


@dataclass(frozen=True, kw_only=True)
class V2LocationCitiesRequestDto:
    country_codes: Optional[list[str]] = None
    region_code: Optional[int] = None
    fias_guid: Optional[str] = None
    postal_code: Optional[str] = None
    code: Optional[int] = None
    city: Optional[str] = None
    payment_limit: Optional[Decimal] = None
    size: Optional[int] = 1000
    page: Optional[int] = 0
    lang: Optional[str] = "rus"


@dataclass(frozen=True, kw_only=True)
class City:
    code: int
    city_uuid: str
    kladr_code: Optional[str] = None
    city: str
    fias_guid: Optional[str] = None
    country_code: str
    country: str
    region: str
    region_code: int = 0
    sub_region: Optional[str] = None
    longitude: Optional[Decimal] = None
    latitude: Optional[Decimal] = None
    time_zone: Optional[str] = None
    payment_limit: Decimal


@dataclass(frozen=True, kw_only=True)
class PostalcodeRequestDto:
    code: int


@dataclass(frozen=True, kw_only=True)
class PostalCode:
    code: int
    postal_codes: list[str]


@dataclass(frozen=True, kw_only=True)
class SuggestCityRequestDto:
    name: str
    country_code: Optional[str] = None


@dataclass(frozen=True, kw_only=True)
class SuggestCity:
    city_uuid: str
    code: int
    full_name: str
