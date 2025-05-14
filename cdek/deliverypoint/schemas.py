from typing import Optional
from dataclasses import dataclass
from enum import Enum
from decimal import Decimal


class DeliveryPointType(Enum):
    POSTAMAT = "POSTAMAT"
    PVZ = "PVZ"
    ALL = "ALL"


@dataclass(frozen=True, kw_only=True)
class PhoneDto:
    number: str = ""
    additional: str = ""


@dataclass(frozen=True, kw_only=True)
class OfficeImageDto:
    number: int = 0
    url: str = ""


@dataclass(frozen=True, kw_only=True)
class OfficeWorkTimeDto:
    day: int = 0
    time: str = ""


@dataclass(frozen=True, kw_only=True)
class LocalTime:
    hour: int = 0
    minute: int = 0
    second: int = 0
    nano: int = 0


@dataclass(frozen=True, kw_only=True)
class OfficeWorkTimeExceptionDto:
    date_start: str = ""
    date_end: str = ""
    time_start: Optional[LocalTime] = None
    time_end: Optional[LocalTime] = None
    is_working: bool = False


@dataclass(frozen=True, kw_only=True)
class OfficeCellDimensionsDto:
    width: int = 0
    height: int = 0
    depth: int = 0


@dataclass(frozen=True, kw_only=True)
class ErrorDto:
    code: str = ""
    message: str = ""


@dataclass(frozen=True, kw_only=True)
class WarningDto:
    code: str = ""
    message: str = ""


@dataclass(frozen=True, kw_only=True)
class OfficeLocationDto:
    country_code: str = ""
    region_code: int = 0
    region: str = ""
    city_code: int = 0
    city: str = ""
    fias_guid: str = ""
    postal_code: str = ""
    longitude: Decimal = Decimal("0")
    latitude: Decimal = Decimal("0")
    address: str = ""
    address_full: str = ""
    city_uuid: str = ""


@dataclass(frozen=True, kw_only=True)
class DeliveryPoint:
    code: str = ""
    name: str = ""
    uuid: str = ""
    address_comment: str = ""
    nearest_station: str = ""
    nearest_metro_station: str = ""
    work_time: str = ""
    phones: Optional[list[PhoneDto]] = None
    email: str = ""
    note: str = ""
    type: str = ""
    owner_code: str = ""
    take_only: bool = False
    is_handout: bool = False
    is_reception: bool = False
    is_dressing_room: bool = False
    is_marketplace: bool = False
    is_ltl: bool = False
    have_cashless: bool = False
    have_cash: bool = False
    have_fast_payment_system: bool = False
    allowed_cod: bool = False
    site: str = ""
    office_image_list: Optional[list[OfficeImageDto]] = None
    work_time_list: Optional[list[OfficeWorkTimeDto]] = None
    work_time_exception_list: Optional[list[OfficeWorkTimeExceptionDto]] = None
    weight_min: Decimal = Decimal("0")
    weight_max: Decimal = Decimal("0")
    dimensions: Optional[OfficeCellDimensionsDto] = None
    errors: Optional[ErrorDto] = None
    warnings: Optional[WarningDto] = None
    location: Optional[OfficeLocationDto] = None
    distance: int = 0
    fulfillment: bool = False
