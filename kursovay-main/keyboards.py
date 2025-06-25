from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Главное меню
passengers_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тарифы и билеты', callback_data='bilet')],
    [InlineKeyboardButton(text='Контролёры', callback_data='controllers')],
    [InlineKeyboardButton(text='Пассажирское агенство "ГУП Мосгортранс"', callback_data='agency')],
    [InlineKeyboardButton(text='Страхование пассажиров', callback_data='insurance')],
    [InlineKeyboardButton(text='Обеспечение антитеррористической безопасности', callback_data='security')],
    [InlineKeyboardButton(text='Обратная связь', callback_data='feedback')],
    [InlineKeyboardButton(text='Льготы на проезд', callback_data='benefits')]
])

#Меню Тарифы и билеты
tariff_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тарифная зона А', callback_data='zone_a')],
    [InlineKeyboardButton(text='Тарифная зона Б', callback_data='zone_b')],
    [InlineKeyboardButton(text='Пополнение карты "Тройка"', callback_data='troika_recharge')],
    [InlineKeyboardButton(text='Оплата проезда', callback_data='payment')],
    [InlineKeyboardButton(text='Выход в главное меню', callback_data='exit_to_main_menu')]
])

#Меню Тарифная зона А
a_zone = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Билет "Кошелёк" на карте Тройка', callback_data='wallet_ticket')],
    [InlineKeyboardButton(text='Билет "Единый" на количество поездок', callback_data='unified_ticket')],
    [InlineKeyboardButton(text='Билет без лимита поездок', callback_data='unlimited_ticket')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Тарифная зона Б
b_zone = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Билеты на количество поездок', callback_data='limit_ticket')],
    [InlineKeyboardButton(text='Билеты без лимита поездок', callback_data='unlimit_ticket')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Тарифная зона Пополнение карты тройка
troika_recharge = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Билет "Кошелёк" на карте "Тройка"', callback_data='troika')],
    [InlineKeyboardButton(text='Пополнение карты "Тройка" через приложение', callback_data='troika_online')],
    [InlineKeyboardButton(text='Пополнение карты "Тройка" в кассах и автоматах', callback_data='troika_irl')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Оплата проезда
payment = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Социальной картой', callback_data='sochial')],
    [InlineKeyboardButton(text='Картой "Тройка"', callback_data='card_troika')],
    [InlineKeyboardButton(text='Банковской картой', callback_data='bank')],
    [InlineKeyboardButton(text='Проездные билеты', callback_data='ticket')],
    #[InlineKeyboardButton(text='При неисправности карты "Тройка"', callback_data='troika_malfunction')],
    #[InlineKeyboardButton(text='Оплата проезда при неисправности', callback_data='payment_malfunction')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Контролёры
controllers = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Действия контролёров при проверке', callback_data='deistvia')],
    [InlineKeyboardButton(text='Контролёр имеет право', callback_data='prava')],
    [InlineKeyboardButton(text='Контролёрам категорически запрещено', callback_data='nelza')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Пассажирское агенство "ГУП Мосгортранс"
agency = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Контакты', callback_data='calls')],
    [InlineKeyboardButton(text='Деятельность', callback_data='work')],
    [InlineKeyboardButton(text='Перечень документов для получения изъятых карт', callback_data='doks')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Страхование пассажиров
insurance = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Об обязательном страховании пассажиров', callback_data='straxovka')],
    [InlineKeyboardButton(text='Контакты страховой компании', callback_data='straxovka_calls')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Обеспечение антитеррористической безопасности
security = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перечень запрещённых к провозу веществ и предметов', callback_data='terror')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Обратная связь
feedback = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Обратная связь', callback_data='obratka')],
    [InlineKeyboardButton(text='Приложение', callback_data='priloga')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])

#Меню Обеспечение антитеррористической безопасности
benefits = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Категории людей, которым доступен бесплатный проезд', callback_data='kategorii')],
    [InlineKeyboardButton(text='Выход', callback_data='exit')]
])