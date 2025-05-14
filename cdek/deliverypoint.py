from typing import Any, Optional
from dataclasses import dataclass
from enum import Enum
from decimal import Decimal
import httpx
from cdek._base import CDEKBase


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
    time_start: LocalTime
    time_end: LocalTime
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


class CDEKDeliveryPoint(CDEKBase):
    def fetch_deliverypoints(self, **params: Optional[Any]) -> list[DeliveryPoint]:
        """/v2/deliverypoints
        code
        string
        Example: code=NSK1
        Код ПВЗ

        type
        string
        Example: type=DeliveryPointType.ALL
        Тип офиса. Принимает значения "POSTAMAT", "PVZ", "ALL". При отсутствии параметра принимается значение по умолчанию DeliveryPointType.ALL.

        postal_code
        string
        Example: postal_code=630000
        Почтовый индекс города, для которого необходим список офисов

        city_code
        integer <int32>
        Example: city_code=270
        Код населенного пункта СДЭК (метод "Список населенных пунктов")

        country_code
        string
        Example: country_code=RU
        Код страны в формате ISO_3166-1_alpha-2 (см. “Общероссийский классификатор стран мира”)

        region_code
        integer <int32>
        Example: region_code=5
        Код региона СДЭК

        have_cashless
        boolean
        Example: have_cashless=true
        Наличие терминала оплаты. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        have_cash
        boolean
        Example: have_cash=true
        Есть прием наличных. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        allowed_cod
        boolean
        Example: allowed_cod=true
        Разрешен наложенный платеж. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_dressing_room
        boolean
        Example: is_dressing_room=true
        Наличие примерочной. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        weight_max
        integer <int32>
        Example: weight_max=10
        Максимальный вес в кг, который может принять офис (значения больше 0 - передаются офисы, которые принимают этот вес; 0 - офисы с нулевым весом не передаются; значение не указано - все офисы)

        weight_min
        integer <int32>
        Example: weight_min=5
        Минимальный вес в кг, который принимает офис (при переданном значении будут выводиться офисы с минимальным весом до указанного значения)

        lang
        string
        Example: lang=rus
        Локализация офиса.

        take_only
        boolean
        Example: take_only=true
        Является ли офис только пунктом выдачи. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_handout
        boolean
        Example: is_handout=true
        Является пунктом выдачи. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_reception
        boolean
        Example: is_reception=true
        Есть ли в офисе приём заказов. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_marketplace
        boolean
        Example: is_marketplace=true
        Офис для доставки "До маркетплейса". Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_ltl
        boolean
        Example: is_ltl=true
        Работает ли офис с LTL (сборный груз). Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        fulfillment
        boolean
        Example: fulfillment=true
        Офис с зоной фулфилмента. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        fias_guid
        string <uuid>
        Example: fias_guid=e33970a6-0db6-4e35-832c-cc3312a1833e
        Код города ФИАС

        size
        integer <int32>
        Example: size=1000
        Ограничение выборки результата (размер страницы)

        page
        integer <int32>
        Example: page=2
        Номер страницы выборки результата
        """
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/deliverypoints",
            headers=self._fetch_base_header(),
            params=params,
        )
        return [DeliveryPoint(**record) for record in responce.json()]
