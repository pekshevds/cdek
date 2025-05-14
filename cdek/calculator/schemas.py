from typing import Optional
from dataclasses import dataclass
from decimal import Decimal
from cdek.deliverypoint import ErrorDto, WarningDto


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
    tariff_code: int = 0
    tariff_name: str = ""
    tariff_description: str = ""
    delivery_mode: int = 0
    delivery_sum: Decimal = Decimal("0")
    period_min: int = 0
    period_max: int = 0
    calendar_min: int = 0
    calendar_max: int = 0
    delivery_date_range: Optional[DeliveryDateRangeDto] = None
    errors: Optional[ErrorDto] = None
    warnings: Optional[WarningDto] = None


@dataclass(frozen=True, kw_only=True)
class CalcAdditionalServiceDto:
    code: str = ""
    cparameterode: str = ""


@dataclass(frozen=True, kw_only=True)
class CalcResponseAdditionalServiceDto:
    code: str = ""
    sum: Decimal = Decimal("0")
    total_sum: Decimal = Decimal("0")
    discount_percent: Decimal = Decimal("0")
    discount_sum: Decimal = Decimal("0")
    vat_rate: Decimal = Decimal("0")
    vat_sum: Decimal = Decimal("0")


@dataclass(frozen=True, kw_only=True)
class TariffCode:
    delivery_sum: Decimal = Decimal("0")
    period_min: int = 0
    period_max: int = 0
    calendar_min: int = 0
    calendar_max: int = 0
    weight_calc: int = 0
    services: Optional[list[CalcResponseAdditionalServiceDto]] = None
    total_sum: Decimal = Decimal("0")
    currency: str = ""
    errors: Optional[list[ErrorDto]] = None
    warnings: Optional[list[WarningDto]] = None
    delivery_date_range: Optional[DeliveryDateRangeDto] = None
