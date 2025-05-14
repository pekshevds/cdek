from typing import Optional
from dataclasses import dataclass
from decimal import Decimal
from cdek.deliverypoint.schemas import ErrorDto, WarningDto


@dataclass(frozen=True, kw_only=True)
class CalculatorAvailableTariffsResponseDeliveryModeDto:
    delivery_mode: str = ""
    delivery_mode_name: str = ""
    tariff_code: int = 0


@dataclass(frozen=True, kw_only=True)
class CalculatorAvailableTariffsResponseAdditionalOrderTypesParamDto:
    without_additional_order_type: bool = False
    additional_order_types: Optional[list[str]] = None


@dataclass(frozen=True, kw_only=True)
class CalculatorAvailableTariffsResponseTariffCodeDto:
    tariff_name: str = ""
    weight_min: Decimal = Decimal("0")
    weight_max: Decimal = Decimal("0")
    weight_calc_max: Decimal = Decimal("0")
    length_min: int = 0
    length_max: int = 0
    width_min: int = 0
    width_max: int = 0
    height_min: int = 0
    height_max: int = 0
    order_types: Optional[list[str]] = None
    payer_contragent_type: Optional[list[str]] = None
    recipient_contragent_type: Optional[list[str]] = None
    delivery_modes: Optional[
        list[CalculatorAvailableTariffsResponseDeliveryModeDto]
    ] = None
    additional_order_types_param: Optional[
        list[CalculatorAvailableTariffsResponseDeliveryModeDto]
    ] = None


@dataclass(frozen=True, kw_only=True)
class AllTariffCodes:
    tariff_codes: list[CalculatorAvailableTariffsResponseTariffCodeDto]


@dataclass(frozen=True, kw_only=True)
class CalculatorLocationDto:
    code: int = 0
    postal_code: str = ""
    country_code: str = ""
    city: str = ""
    address: str = ""
    contragent_type: str = ""


@dataclass(frozen=True, kw_only=True)
class CalcPackageRequestDto:
    weight: int = 0
    length: int = 0
    width: int = 0
    height: int = 0


@dataclass(frozen=True, kw_only=True)
class DeliveryDateRangeDto:
    min: str = ""
    max: str = ""


@dataclass(frozen=True, kw_only=True)
class TariffCodeDto:
    tariff_code: int
    tariff_name: str
    tariff_description: str = ""
    delivery_mode: int
    delivery_sum: Decimal
    period_min: int
    period_max: int
    calendar_min: int = 0
    calendar_max: int = 0
    delivery_date_range: Optional[DeliveryDateRangeDto] = None
    errors: Optional[ErrorDto] = None
    warnings: Optional[WarningDto] = None


@dataclass(frozen=True, kw_only=True)
class TariffListCodes:
    tariff_codes: list[TariffCodeDto]


@dataclass(frozen=True, kw_only=True)
class CalcAdditionalServiceDto:
    code: str = ""
    cparameterode: str = ""


@dataclass(frozen=True, kw_only=True)
class CalcResponseAdditionalServiceDto:
    code: str
    sum: Decimal
    total_sum: Decimal
    discount_percent: Decimal
    discount_sum: Decimal
    vat_rate: Decimal
    vat_sum: Decimal


@dataclass(frozen=True, kw_only=True)
class TariffCode:
    delivery_sum: Decimal
    period_min: int
    period_max: int
    calendar_min: int = 0
    calendar_max: int = 0
    weight_calc: int
    services: Optional[list[CalcResponseAdditionalServiceDto]] = None
    total_sum: Decimal
    currency: str
    errors: Optional[list[ErrorDto]] = None
    warnings: Optional[list[WarningDto]] = None
    delivery_date_range: Optional[DeliveryDateRangeDto] = None
