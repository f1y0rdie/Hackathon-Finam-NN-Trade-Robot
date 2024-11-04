"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import FinamPy.proto.common_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _OrderProperty:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OrderPropertyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OrderProperty.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ORDER_PROPERTY_UNSPECIFIED: _OrderProperty.ValueType  # 0
    """Value is not specified. Do not use.
    Значение не указано. Не использовать.
    """
    ORDER_PROPERTY_PUT_IN_QUEUE: _OrderProperty.ValueType  # 1
    """The residual of partially matched order is to stay in OrderBook.
    Неисполненная часть заявки помещается в очередь заявок биржи.
    """
    ORDER_PROPERTY_CANCEL_BALANCE: _OrderProperty.ValueType  # 2
    """The residual of partially matched order is to be cancelled.
    Неисполненная часть заявки снимается с торгов.
    """
    ORDER_PROPERTY_IMM_OR_CANCEL: _OrderProperty.ValueType  # 3
    """Filling the order only in case the posibility of immediate and full execution.
    Сделки совершаются только в том случае, если заявка может быть удовлетворена полностью и сразу при выставлении.
    """

class OrderProperty(_OrderProperty, metaclass=_OrderPropertyEnumTypeWrapper):
    """Order placement properties.
    Поведение заявки при выставлении в стакан.
    """

ORDER_PROPERTY_UNSPECIFIED: OrderProperty.ValueType  # 0
"""Value is not specified. Do not use.
Значение не указано. Не использовать.
"""
ORDER_PROPERTY_PUT_IN_QUEUE: OrderProperty.ValueType  # 1
"""The residual of partially matched order is to stay in OrderBook.
Неисполненная часть заявки помещается в очередь заявок биржи.
"""
ORDER_PROPERTY_CANCEL_BALANCE: OrderProperty.ValueType  # 2
"""The residual of partially matched order is to be cancelled.
Неисполненная часть заявки снимается с торгов.
"""
ORDER_PROPERTY_IMM_OR_CANCEL: OrderProperty.ValueType  # 3
"""Filling the order only in case the posibility of immediate and full execution.
Сделки совершаются только в том случае, если заявка может быть удовлетворена полностью и сразу при выставлении.
"""
global___OrderProperty = OrderProperty

class _OrderConditionType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OrderConditionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OrderConditionType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ORDER_CONDITION_TYPE_UNSPECIFIED: _OrderConditionType.ValueType  # 0
    """Value is not specified. Do not use.
    Значение не указано. Не использовать.
    """
    ORDER_CONDITION_TYPE_BID: _OrderConditionType.ValueType  # 1
    """Best Bid.
    Лучшая цена покупки.
    """
    ORDER_CONDITION_TYPE_BID_OR_LAST: _OrderConditionType.ValueType  # 2
    """Best Bid or Last trade price and higher.
    Лучшая цена покупки или сделка по заданной цене и выше.
    """
    ORDER_CONDITION_TYPE_ASK: _OrderConditionType.ValueType  # 3
    """Best Ask.
    Лучшая цена продажи.
    """
    ORDER_CONDITION_TYPE_ASK_OR_LAST: _OrderConditionType.ValueType  # 4
    """Best Ask or Last trade price and lower.
    Лучшая цена продажи или сделка по заданной цене и ниже.
    """
    ORDER_CONDITION_TYPE_TIME: _OrderConditionType.ValueType  # 5
    """Placement time. Parameter OrderCondition.time must be set.
    Время выставления заявки на Биржу. Параметр OrderCondition.time должен быть установлен.
    """
    ORDER_CONDITION_TYPE_COV_DOWN: _OrderConditionType.ValueType  # 6
    """Coverage below specified.
    Обеспеченность ниже заданной.
    """
    ORDER_CONDITION_TYPE_COV_UP: _OrderConditionType.ValueType  # 7
    """Coverage above specified.
    Обеспеченность выше заданной.
    """
    ORDER_CONDITION_TYPE_LAST_UP: _OrderConditionType.ValueType  # 8
    """Last trade price and higher.
    Сделка на рынке по заданной цене или выше.
    """
    ORDER_CONDITION_TYPE_LAST_DOWN: _OrderConditionType.ValueType  # 9
    """Last trade price and lower.
    Сделка на рынке по заданной цене или ниже.
    """

class OrderConditionType(_OrderConditionType, metaclass=_OrderConditionTypeEnumTypeWrapper):
    """Conditional order types.
    Типы условных ордеров.
    """

ORDER_CONDITION_TYPE_UNSPECIFIED: OrderConditionType.ValueType  # 0
"""Value is not specified. Do not use.
Значение не указано. Не использовать.
"""
ORDER_CONDITION_TYPE_BID: OrderConditionType.ValueType  # 1
"""Best Bid.
Лучшая цена покупки.
"""
ORDER_CONDITION_TYPE_BID_OR_LAST: OrderConditionType.ValueType  # 2
"""Best Bid or Last trade price and higher.
Лучшая цена покупки или сделка по заданной цене и выше.
"""
ORDER_CONDITION_TYPE_ASK: OrderConditionType.ValueType  # 3
"""Best Ask.
Лучшая цена продажи.
"""
ORDER_CONDITION_TYPE_ASK_OR_LAST: OrderConditionType.ValueType  # 4
"""Best Ask or Last trade price and lower.
Лучшая цена продажи или сделка по заданной цене и ниже.
"""
ORDER_CONDITION_TYPE_TIME: OrderConditionType.ValueType  # 5
"""Placement time. Parameter OrderCondition.time must be set.
Время выставления заявки на Биржу. Параметр OrderCondition.time должен быть установлен.
"""
ORDER_CONDITION_TYPE_COV_DOWN: OrderConditionType.ValueType  # 6
"""Coverage below specified.
Обеспеченность ниже заданной.
"""
ORDER_CONDITION_TYPE_COV_UP: OrderConditionType.ValueType  # 7
"""Coverage above specified.
Обеспеченность выше заданной.
"""
ORDER_CONDITION_TYPE_LAST_UP: OrderConditionType.ValueType  # 8
"""Last trade price and higher.
Сделка на рынке по заданной цене или выше.
"""
ORDER_CONDITION_TYPE_LAST_DOWN: OrderConditionType.ValueType  # 9
"""Last trade price and lower.
Сделка на рынке по заданной цене или ниже.
"""
global___OrderConditionType = OrderConditionType

class _OrderStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OrderStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OrderStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ORDER_STATUS_UNSPECIFIED: _OrderStatus.ValueType  # 0
    """Value is not specified. Do not use.
    Значение не указано. Не использовать.
    """
    ORDER_STATUS_NONE: _OrderStatus.ValueType  # 1
    """Order is not in OrderBook.
    Заявка не выставлена.
    """
    ORDER_STATUS_ACTIVE: _OrderStatus.ValueType  # 2
    """Order is in OrderBook.
    Заявка выставлена.
    """
    ORDER_STATUS_CANCELLED: _OrderStatus.ValueType  # 3
    """Order is canceled.
    Заявка отменена.
    """
    ORDER_STATUS_MATCHED: _OrderStatus.ValueType  # 4
    """Order is matched.
    Заявка исполнена.
    """

class OrderStatus(_OrderStatus, metaclass=_OrderStatusEnumTypeWrapper):
    """Order status.
    Состояние заявки.
    """

ORDER_STATUS_UNSPECIFIED: OrderStatus.ValueType  # 0
"""Value is not specified. Do not use.
Значение не указано. Не использовать.
"""
ORDER_STATUS_NONE: OrderStatus.ValueType  # 1
"""Order is not in OrderBook.
Заявка не выставлена.
"""
ORDER_STATUS_ACTIVE: OrderStatus.ValueType  # 2
"""Order is in OrderBook.
Заявка выставлена.
"""
ORDER_STATUS_CANCELLED: OrderStatus.ValueType  # 3
"""Order is canceled.
Заявка отменена.
"""
ORDER_STATUS_MATCHED: OrderStatus.ValueType  # 4
"""Order is matched.
Заявка исполнена.
"""
global___OrderStatus = OrderStatus

@typing.final
class OrderCondition(google.protobuf.message.Message):
    """Order placement properties.
    Свойства выставления заявок.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    type: global___OrderConditionType.ValueType
    """Condition type.
    Тип условия.
    """
    price: builtins.float
    """Conditional value.
    Значение для условия.
    """
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Placement time.
        Время выставления.
        """

    def __init__(
        self,
        *,
        type: global___OrderConditionType.ValueType = ...,
        price: builtins.float = ...,
        time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time", b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["price", b"price", "time", b"time", "type", b"type"]) -> None: ...

global___OrderCondition = OrderCondition

@typing.final
class NewOrderRequest(google.protobuf.message.Message):
    """New Order Request.
    Запрос на создание заявки.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    SECURITY_BOARD_FIELD_NUMBER: builtins.int
    SECURITY_CODE_FIELD_NUMBER: builtins.int
    BUY_SELL_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    USE_CREDIT_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    PROPERTY_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    VALID_BEFORE_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    security_board: builtins.str
    """Trading Board.
    Режим торгов.
    """
    security_code: builtins.str
    """Security Code.
    Тикер инструмента.
    """
    buy_sell: FinamPy.proto.common_pb2.BuySell.ValueType
    """Transaction direction.
    Направление сделки.
    """
    quantity: builtins.int
    """Order volume in lots.
    Количество лотов инструмента для заявки.
    """
    use_credit: builtins.bool
    """Use credit. Not available in derivative market.
    Использовать кредит. Недоступно для срочного рынка.
    """
    property: global___OrderProperty.ValueType
    """Unfilled order execution property.
    Свойства исполнения частично исполненных заявок.
    """
    @property
    def price(self) -> google.protobuf.wrappers_pb2.DoubleValue:
        """Order price. Use "null" to place Market Order.
        Цена заявки. Используйте "null", чтобы выставить рыночную заявку.
        """

    @property
    def condition(self) -> global___OrderCondition:
        """Order placement properties.
        Свойства выставления заявок.
        """

    @property
    def valid_before(self) -> FinamPy.proto.common_pb2.OrderValidBefore:
        """Order lifetime condition.
        Условие по времени действия заявки.
        """

    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        security_board: builtins.str = ...,
        security_code: builtins.str = ...,
        buy_sell: FinamPy.proto.common_pb2.BuySell.ValueType = ...,
        quantity: builtins.int = ...,
        use_credit: builtins.bool = ...,
        price: google.protobuf.wrappers_pb2.DoubleValue | None = ...,
        property: global___OrderProperty.ValueType = ...,
        condition: global___OrderCondition | None = ...,
        valid_before: FinamPy.proto.common_pb2.OrderValidBefore | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["condition", b"condition", "price", b"price", "valid_before", b"valid_before"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["buy_sell", b"buy_sell", "client_id", b"client_id", "condition", b"condition", "price", b"price", "property", b"property", "quantity", b"quantity", "security_board", b"security_board", "security_code", b"security_code", "use_credit", b"use_credit", "valid_before", b"valid_before"]) -> None: ...

global___NewOrderRequest = NewOrderRequest

@typing.final
class NewOrderResult(google.protobuf.message.Message):
    """NewOrderRequest result.
    Результат выполнения NewOrderRequest.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    TRANSACTION_ID_FIELD_NUMBER: builtins.int
    SECURITY_CODE_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account Id.
    Идентификатор торгового счёта.
    """
    transaction_id: builtins.int
    """Transaction Id, which can be used to cancel order or find corresponding order_no in Event service.
    Идентификатор транзакции, который может быть использован для отмены заявки или определения номера заявки в сервисе событий.
    """
    security_code: builtins.str
    """Security Code.
    Тикер инструмента.
    """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        transaction_id: builtins.int = ...,
        security_code: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client_id", b"client_id", "security_code", b"security_code", "transaction_id", b"transaction_id"]) -> None: ...

global___NewOrderResult = NewOrderResult

@typing.final
class CancelOrderRequest(google.protobuf.message.Message):
    """Cancel Order Request.
    Запрос на отмену заявки.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    TRANSACTION_ID_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account Id.
    Идентификатор торгового счёта.
    """
    transaction_id: builtins.int
    """Transaction Id, which can be used to cancel order or find corresponding order_no in Event service.
    Идентификатор транзакции, который может быть использован для отмены заявки или определения номера заявки в сервисе событий.
    """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        transaction_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client_id", b"client_id", "transaction_id", b"transaction_id"]) -> None: ...

global___CancelOrderRequest = CancelOrderRequest

@typing.final
class CancelOrderResult(google.protobuf.message.Message):
    """CancelOrderRequest result.
    Результат выполнения CancelOrderRequest.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    TRANSACTION_ID_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account Id.
    Идентификатор торгового счёта.
    """
    transaction_id: builtins.int
    """Transaction Id, which can be used to cancel order or find corresponding order_no in Event service.
    Идентификатор транзакции, который может быть использован для отмены заявки или определения номера заявки в сервисе событий.
    """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        transaction_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client_id", b"client_id", "transaction_id", b"transaction_id"]) -> None: ...

global___CancelOrderResult = CancelOrderResult

@typing.final
class GetOrdersRequest(google.protobuf.message.Message):
    """Get Orders Request.
    Запрос списка заявок.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    INCLUDE_MATCHED_FIELD_NUMBER: builtins.int
    INCLUDE_CANCELED_FIELD_NUMBER: builtins.int
    INCLUDE_ACTIVE_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    include_matched: builtins.bool
    """Include executed orders in response.
    Вернуть исполненные заявки.
    """
    include_canceled: builtins.bool
    """Include canceled orders in response.
    Вернуть отмененные заявки.
    """
    include_active: builtins.bool
    """Include active orders in response.
    Вернуть активные заявки.
    """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        include_matched: builtins.bool = ...,
        include_canceled: builtins.bool = ...,
        include_active: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client_id", b"client_id", "include_active", b"include_active", "include_canceled", b"include_canceled", "include_matched", b"include_matched"]) -> None: ...

global___GetOrdersRequest = GetOrdersRequest

@typing.final
class Order(google.protobuf.message.Message):
    """Order.
    Заявка.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORDER_NO_FIELD_NUMBER: builtins.int
    TRANSACTION_ID_FIELD_NUMBER: builtins.int
    SECURITY_CODE_FIELD_NUMBER: builtins.int
    CLIENT_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    BUY_SELL_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    BALANCE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    CURRENCY_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    VALID_BEFORE_FIELD_NUMBER: builtins.int
    ACCEPTED_AT_FIELD_NUMBER: builtins.int
    SECURITY_BOARD_FIELD_NUMBER: builtins.int
    MARKET_FIELD_NUMBER: builtins.int
    order_no: builtins.int
    """Order No. Appear only when an order is placed in OrderBook.
    Биржевой номер заявки. Появляется после того, как заявка попадает в стакан.
    """
    transaction_id: builtins.int
    """Transaction Id . Assigned when a command for new order creation is sent.
    Идентификатор транзакции. Назначается после подачи команды на создание новой заявки.
    """
    security_code: builtins.str
    """Security Code.
    Тикер инструмента.
    """
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    status: global___OrderStatus.ValueType
    """Order status.
    Состояние заявки.
    """
    buy_sell: FinamPy.proto.common_pb2.BuySell.ValueType
    """Transaction direction.
    Направление сделки.
    """
    price: builtins.float
    """Lot price.
    Цена за лот.
    """
    quantity: builtins.int
    """Volume in lots.
    Количество, в лотах.
    """
    balance: builtins.int
    """Residual volume in lots.
    Неисполненный остаток, в лотах.
    """
    message: builtins.str
    """Rejection reason or conditional order resolution.
    Причина отказа или вердикт по условной заявке.
    """
    currency: builtins.str
    """Price currency.
    Валюта цены.
    """
    security_board: builtins.str
    """Security Board.
    Основной режим торгов инструмента.
    """
    market: FinamPy.proto.common_pb2.Market.ValueType
    """Market.
    Рынок.
    """
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of Order placement in UTC.
        Время регистрации заявки на бирже. В UTC.
        """

    @property
    def condition(self) -> global___OrderCondition:
        """Conditional order properties.
        Параметры условной заявки.
        """

    @property
    def valid_before(self) -> FinamPy.proto.common_pb2.OrderValidBefore:
        """Order lifetime.
        Время действия заявки.
        """

    @property
    def accepted_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of order registration on the server in UTC.
        Время, когда заявка была зарегистрирована на сервере. В UTC.
        """

    def __init__(
        self,
        *,
        order_no: builtins.int = ...,
        transaction_id: builtins.int = ...,
        security_code: builtins.str = ...,
        client_id: builtins.str = ...,
        status: global___OrderStatus.ValueType = ...,
        buy_sell: FinamPy.proto.common_pb2.BuySell.ValueType = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        price: builtins.float = ...,
        quantity: builtins.int = ...,
        balance: builtins.int = ...,
        message: builtins.str = ...,
        currency: builtins.str = ...,
        condition: global___OrderCondition | None = ...,
        valid_before: FinamPy.proto.common_pb2.OrderValidBefore | None = ...,
        accepted_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        security_board: builtins.str = ...,
        market: FinamPy.proto.common_pb2.Market.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["accepted_at", b"accepted_at", "condition", b"condition", "created_at", b"created_at", "valid_before", b"valid_before"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["accepted_at", b"accepted_at", "balance", b"balance", "buy_sell", b"buy_sell", "client_id", b"client_id", "condition", b"condition", "created_at", b"created_at", "currency", b"currency", "market", b"market", "message", b"message", "order_no", b"order_no", "price", b"price", "quantity", b"quantity", "security_board", b"security_board", "security_code", b"security_code", "status", b"status", "transaction_id", b"transaction_id", "valid_before", b"valid_before"]) -> None: ...

global___Order = Order

@typing.final
class GetOrdersResult(google.protobuf.message.Message):
    """GetOrdersRequest result.
    Результат GetOrdersRequest.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    ORDERS_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    @property
    def orders(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Order]:
        """Orders list.
        Список заявок.
        """

    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        orders: collections.abc.Iterable[global___Order] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client_id", b"client_id", "orders", b"orders"]) -> None: ...

global___GetOrdersResult = GetOrdersResult
