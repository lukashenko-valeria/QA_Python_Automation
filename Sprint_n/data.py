BASE_URL = "https://ez-route.stand.praktikum-services.ru/"

# Предустановленные адреса
ADDRESS_ONE = "Хамовнический вал, 34"
ADDRESS_TWO = "Зубовский бульвар, 37"

# Cписок тарифов такси
TARIFF_LIST = ["Рабочий", "Сонный", "Отпускной", "Разговорчивый", "Утешительный", "Глянцевый"]

# Тексты на карточках тарифов
class TariffText:
    WORK = {"title": "Рабочий", "description": "Для деловых особ, которых отвлекают"}
    SLEEP = {"title": "Сонный", "description": "Для тех, кто не выспался"}
    HOLIDAY = {"title": "Отпускной", "description": "Если пришла пора отдохнуть"}
    TALK = {"title": "Разговорчивый", "description": "Если мысли не выходят из головы"}
    GLAD = {"title": "Утешительный", "description": "Если хочется свернуться калачиком"}
    GLAM = {"title": "Глянцевый", "description": "Если нужно блистать"}

# Тексты в полях дополнительной панели
class ExtraPanelText:
    PHONE = "Телефон"
    PAY_METHOD = "Способ оплаты"
    COMMENT = "Комментарий водителю..."
    REQS = "Требования к заказу"
    ORDER = "Ввести номер и заказать"

# Тексты на панели ожидания такси
class WaitTaxiText:
    TITLE = "Поиск машины"
    CANCEL_BUTTON = "Отменить"
    DETAILS_BUTTON = "Детали"
    FINISH_ORDER = " мин. и приедет"
