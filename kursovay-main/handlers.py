from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import Router, types
import keyboards as kb

router = Router()

@router.message(Command(commands=['start']))
async def send_welcome(message: types.Message):
    await message.answer('Привет! Я бот от ГУП "Мосгортранс". Я отвечу на некоторые интересующие вопросы:', reply_markup=kb.passengers_menu)

@router.callback_query(lambda c: c.data == 'bilet')
async def show_tariffs_keyboard(callback_query: CallbackQuery):
    current_markup = callback_query.message.reply_markup
    new_markup = kb.tariff_keyboard
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)

@router.callback_query(lambda c: c.data == 'agency')
async def show_tariffs_keyboard(callback_query: CallbackQuery):
    current_markup = callback_query.message.reply_markup
    new_markup = kb.agency
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)

@router.callback_query(lambda c: c.data == 'insurance')
async def show_tariffs_keyboard(callback_query: CallbackQuery):
    current_markup = callback_query.message.reply_markup
    new_markup = kb.insurance
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)

@router.callback_query(lambda c: c.data == 'controllers')
async def show_tariffs_keyboard(callback_query: CallbackQuery):
    current_markup = callback_query.message.reply_markup
    new_markup = kb.controllers
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)

@router.callback_query(lambda c: c.data == 'security')
async def show_tariffs_keyboard(callback_query: CallbackQuery):
    current_markup = callback_query.message.reply_markup
    new_markup = kb.security
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)

@router.callback_query(lambda c: c.data == 'feedback')
async def show_tariffs_keyboard(callback_query: CallbackQuery):
    current_markup = callback_query.message.reply_markup
    new_markup = kb.feedback
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)

@router.callback_query(lambda c: c.data == 'benefits')
async def show_tariffs_keyboard(callback_query: CallbackQuery):
    current_markup = callback_query.message.reply_markup
    new_markup = kb.benefits
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)



@router.callback_query(lambda c: c.data in [
    'zone_a', 'zone_b', 'troika_recharge', 'payment', 'troika_malfunction', 'payment_malfunction'
])
async def handle_tariff_options(callback_query: CallbackQuery):
    if callback_query.data == 'zone_a':
        current_markup = callback_query.message.reply_markup
        new_markup = kb.a_zone
        if current_markup != new_markup:
            await callback_query.message.edit_reply_markup(reply_markup=new_markup)
    elif callback_query.data == 'zone_b':
        new_markup = kb.b_zone
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)
    elif callback_query.data == 'troika_recharge':
        new_markup = kb.troika_recharge
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)
    elif callback_query.data == 'payment':
        new_markup = kb.payment
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)
    elif callback_query.data == 'controllers':
        new_markup = kb.controllers
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)


user_message_ids = {}

@router.callback_query(lambda c: c.data in [
    'wallet_ticket', 'unified_ticket', 'unlimited_ticket'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'wallet_ticket':
        msg = await callback_query.message.answer('Залог при покупке карты "Тройкм" - 150 рублей. Срок возврата - 5 лет. Тариф "90 минут" даёт бесплатную пересадку на метро, монорельсе, МЦК и МЦД и неограниченное количество поездок на наземном транспорте. Бесплатная пересадка при проездах на МДЦ возможна только на метро, монорельсе и МЦК. Бесплатная пересадка между маршрутами наземного транспорта возможна с картой "Тройка", привязанной к личному кабинету в приложении "Метро Москвы"')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'unified_ticket':
        msg = await callback_query.message.answer('Билеты на 1 и 2 поездки действуют 5 дней со дня покупки(включая день покупки). Билеты на 60 поездок реализуются только на карте "Тройка" и действуют 45 дней с момента записи на карту.')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'unlimited_ticket':
        msg = await callback_query.message.answer('Билеты на 1 и 3 суток действуют с момента первого прохода. Начало использования не позднее 10 суток с момента покупки (включая день покупки). Билеты на 30, 90, 365 дней реализуются только на карте «Тройка» и действуют с момента первого прохода. Начало использования (совершения первого прохода) не позднее 10 суток с момента покупки (включая день покупки). По истечении 10 суток срок действия билета начинает')
        user_message_ids[callback_query.from_user.id] = msg.message_id

@router.callback_query(lambda c: c.data in [
    'limit_ticket', 'unlimit_ticket'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'limit_ticket':
        msg = await callback_query.message.answer('Билеты на 1 и 2 поездки действуют 5 дней с момента покупки (включая день покупки). Билеты на 60 поездок реализуются только на карте «Тройка» и действуют 45 дней с момента записи на карту.')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'unlimit_ticket':
        msg = await callback_query.message.answer('Билеты на 30 дней реализуются только на карте «Тройка» и действуют с момента первого прохода. Начало использования (совершения первого прохода) не позднее 10 суток с момента покупки (включая день покупки)')
        user_message_ids[callback_query.from_user.id] = msg.message_id

@router.callback_query(lambda c: c.data in [
    'troika', 'troika_online', 'troika_irl'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'troika':
        msg = await callback_query.message.answer('Билет «Кошелек» на карте «Тройка» дает право на совершение поездок в пределах зачисленной суммы по фиксированным тарифам. Баланс билета «Кошелек» на карте «Тройка» можно пополнить на сумму до 10000 рублей.')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'troika_online':
        msg = await callback_query.message.answer('Пополнить карту «Тройка» можно через бесплатные мобильные приложения. Услуга доступна только для владельцев смартфонов с операционной системой Android и подключенным модулем NFC. Дополнительная активация карты не требуется. Приложение «Метро Москвы» Приложение «Московский транспорт» Приложение «Тройка. Проверка и пополнение» Приложение «Мой умный город».')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'troika_irl':
        msg = await callback_query.message.answer('Пополнить баланс билета «Кошелек» карты «Тройка» можно в кассах и билетных автоматах ГУП «Московский метрополитен», автоматизированных киосках ГУП «Мосгортранс», кассах «Аэроэкспресс» и на терминалах партнеров. Найти ближайшую точку пополнения «Тройки» можно на карте. Баланс билета «Кошелек» карты «Тройка» можно также пополнить удаленно (онлайн) или с помощью SMS-сервиса 3210.')
        user_message_ids[callback_query.from_user.id] = msg.message_id

@router.callback_query(lambda c: c.data in [
    'sochial', 'card_troika', 'bank', 'ticket', 'troika_malfunction', 'payment_malfunction'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'bank':
        msg = await callback_query.message.answer('На наземном транспорте Москвы доступна оплата проезда с помощью бесконтактных банковских карт, а также смартфонов с функцией Mir Pay. В автобусах, электробусах, троллейбусах и трамваях установлены валидаторы, принимающие оплату бесконтактными банковскими картами и смартфонами с функцией бесконтактных платежей. Стоимость проезда 64 рублей.')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'sochial':
        msg = await callback_query.message.answer('Социальную карту учащегося (школьника), студента, ординатора и аспиранта можно использовать для проезда в наземном транспорте, метро, монорельсе и МЦК. На карту можно записать льготные билеты на 30 дней и 90 дней, включая день продажи, но не более срока действия транспортного приложения социальной карты соответственно. Количество поездок не ограничено.  Герои Советского Союза, Российской Федерации, Социалистического Труда и кавалеры орденов Славы могут получить билеты на льготный проезд в кассах Мосгортранс. Сопровождающие инвалидов I группы или детей-инвалидов могут зайти в наземный транспорт с помощью социальной карты инвалида.')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'card_troika':
        msg = await callback_query.message.answer('Разовая поездка на всех видах транспорта по карте «Тройка» по билету «Кошелек» стоит 57 руб., билет на 60 поездок стоит 3420 руб.')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'ticket':
        msg = await callback_query.message.answer('Записать абонементы на пригородные поезда можно в кассах и автоматах на станциях и вокзалах Москвы и МО.')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    # elif callback_query.data == 'troika_malfunction':
    #     msg = await callback_query.message.answer('Если карта «Тройка» неисправна или имеет механических повреждений, обращайтесь: в сервисные центры на станциях БКЛ «Кунцевская», «Проспект Вернадского», «Савёловская» и «Текстильщики», а также по адресу: ул. Старая Басманная, д. 20, корп. 1; в любую кассу метрополитена; в специализированный пункт по продаже билетов ГУП «Мосгортранс»; в пассажирское агентство ГУП «Мосгортранс».')
    #     user_message_ids[callback_query.from_user.id] = msg.message_id
    # elif callback_query.data == 'payment_malfunction':
    #     msg = await callback_query.message.answer('Если во время поездки в наземном транспорте возникла техническая неисправность или ДТП, пассажир имеет право проезжать в следующем автобусе или электробусе без дополнительной оплаты проезда. При себе обязательно нужно иметь билет с отметкой на валидаторе, сделанной в сошедшем с линии транспорте. Пересадка в следующий за неисправным транспортом автобус или электробус того же или других маршрутов в попутном направлении. Бесплатную пересадку организует водитель неисправного транспортного средства.')
    #     user_message_ids[callback_query.from_user.id] = msg.message_id


@router.callback_query(lambda c: c.data in [
    'deistvia', 'prava', 'nelza'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'deistvia':
        msg = await callback_query.message.answer('По первому требованию пассажиров контролёр обязан предъявить для ознакомления служебное удостоверение и назвать свою фамилию. Контролёр должен проявлять выдержку, тактичность и культуру в общении с пассажирами. Проверка наличия проездных документов у пассажиров, их подлинности и срока действия осуществляется с использованием технических средств объективного контроля (переносное устройство контроля; Магнитные технические тестирующие билеты).')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'prava':
        msg = await callback_query.message.answer('-Требовать у пассажиров предъявления (передачи в руки) проездных документов и подтверждающих документов.\n-Изъять у пассажира незаконно использующиеся проездные документы: поддельные, не принадлежащие лицам, неподтвержденные документально (не доказано право на льготу).\n-Изъятие билета (документа) оформляется актом установленной формы, один экземпляр которого выдается пассажиру, предъявившему указанный билет (документ). Требовать от пассажиров неукоснительного соблюдения действующих Правил ')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'nelza':
        msg = await callback_query.message.answer('-Осуществлять контроль без служебного удостоверения.\n-Взыскивать штраф с граждан. Функции по взысканию штрафов возложены на ГКУ «Организатор перевозок».\n-Изымать у пассажира билеты, проездные документы без составления и выдачи первого экземпляра акта установленной формы.\nПо вопросам, связанным с деятельностью контролёров пассажирского транспорта, обращаться по телефонам: 8 (495) 950-42-93, доб. 4238, 4530.')
        user_message_ids[callback_query.from_user.id] = msg.message_id

@router.callback_query(lambda c: c.data in [
    'calls', 'work', 'doks'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'calls':
        msg = await callback_query.message.answer('г. Москва, Лубянский проезд, д. 5, тел.: 8(495)628-83-73 Режим работы: Пн.-чт. с 08.00 до 17.00 Пят. с 08.00 до 15.45 (обед с 12.00 до 12.45)')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'work':
        msg = await callback_query.message.answer('Пассажирское агентство ГУП «Мосгортранс» осуществляет выдачу временных билетов на проезд в наземном городском пассажирском транспорте для студентов и учащихся, а также прием на экспертизу неисправных проездных билетов. Выдача временных билетов на проезд в наземном городском пассажирском транспорте для студентов и учащихся осуществляется на время оформления «постоянной» социальной карты в случае неисправности или утери предыдущего экземпляра при условии наличия оплаченного периода. В Пассажирском агентстве ГУП «Мосгортранс» также можно сдать на экспертизу неисправную транспортную карту «Тройка» и другие виды билетов, оплатить услуги по социальной карте студента или учащегося и перенести ошибочно оплаченный срок действия социальных карт студента или учащегося. С 01.12.2021 выдача изъятой социальной карты, а также временного единого социального билета осуществляется в сувенирном магазине «Московского метрополитена» по адресу Тверская улица, дом 30/2, строение 1, метро «Маяковская», южный вестибюль, выход 2, ежедневно с 8.00 до 20.00. ')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'doks':
        msg = await callback_query.message.answer('Для студентов и учащихся: Акт об изъятии (при наличии); Студенческий билет или справка с места учебы при предъявлении документа, удостоверяющего личность; Если получает доверенное лицо, то нотариально заверенная доверенность, паспорт доверенного лица. Для держателей социальной карты москвича: Акт об изъятии (при наличии); Паспорт; Если получает доверенное лицо, то нотариально заверенная доверенность, доверенного лица. Для держателей ВЕСБ: Акт об изъятии (при наличии); Документ подтверждающий право льготы (пенсионное удостоверение или справка МСЭ); Если получает доверенное лицо, то нотариально заверенная доверенность, пенсионное удостоверение или справка МСЭ держателя карты, паспорт доверенного лица. Для держателей карты дружинника: Акт об изъятии (при наличии); Удостоверение дружинника; Покумент удостоверяющий личность.')
        user_message_ids[callback_query.from_user.id] = msg.message_id

@router.callback_query(lambda c: c.data in [
    'straxovka', 'straxovka_calls'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'straxovka':
        msg = await callback_query.message.answer('Перевозчик обязан предоставлять пассажирам информацию о страховщике (его наименование, место нахождения, почтовый адрес, номер телефона) и договоре обязательного страхования (номер, дата заключения, срок действия) путем размещения этой информации во всех местах продажи билетов или на билете либо на своем официальном сайте.')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'straxovka_calls':
        msg = await callback_query.message.answer('ОАО «СОГАЗ» 107078, Москва, пр-т Академика Сахарова, д. 10 8-800-333-0-888 (круглосуточно, звонок бесплатный) e-mail: sogaz@sogaz.ru www.sogaz.ru')
        user_message_ids[callback_query.from_user.id] = msg.message_id

@router.callback_query(lambda c: c.data in [
    'terror'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'terror':
        msg = await callback_query.message.answer('Запрещается провозить:\n-взрывчатые вещества и оружие (в том числе фейерверки, сигнальные ракеты и т.д.)\n-ядовитые и отравляющие вещества (в том числе материалы с живыми вирусами и т.д.)\n-легковоспламеняющиеся жидкости (краски, растворители и т.д. )\n-воспламеняющиеся твердые вещества\n-радиоактивные материалы и вещества\n-сжатые и сжиженные газы (газы для газовых горелок, жидкий азот и т.д.)\n-окисляющие вещества и органические перекиси\n-токсичные  вещества (в том числе средства от насекомых, гербициды и т.д.)\n-едкие и коррозирующие вещества')
        user_message_ids[callback_query.from_user.id] = msg.message_id

@router.callback_query(lambda c: c.data in [
    'obratka', 'priloga'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'obratka':
        msg = await callback_query.message.answer('Обращения граждан о работе Транспортного комплекса Москвы принимаются через единую электронную форму Департамента транспорта и развития дорожно-транспортной инфраструктуры города Москвы.\nhttps://dt-window.mos.ru/feedback/?iframe=1')
        user_message_ids[callback_query.from_user.id] = msg.message_id
    elif callback_query.data == 'priloga':
        msg = await callback_query.message.answer('Московский транспорт\nОфициальное приложение пассажира Москвы.\n- Не стойте в пробках \n– Передвигайтесь с комфортом! \n- Стройте и выбирайте оптимальный маршрут \n- Пополняйте баланс карты «Тройка», покупайте билеты на Аэроэкспресс и Сити-шаттл прямо в приложении и многое другое \n- Ссылка для скачивания:https://play.google.com/store/apps/details?id=ru.mosgorpass&hl=ru&gl=US&pli=1 \n- Приложение "Тройка". В этом приложении вы можете посмотреть баланс вашей карты «тройка» и пополнить его в случае необходимости: https://play.google.com/store/apps/details?id=by.advasoft.android.troika.app&referrer=utm_source%3Dsite%26utm_medium%3Dsitelink%26utm_content%3Dlinkonsite%26utm_campaign%3Dtroikaapp')
        user_message_ids[callback_query.from_user.id] = msg.message_id

@router.callback_query(lambda c: c.data in [
    'kategorii'
])
async def process_troika_card(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == 'kategorii':
        msg = await callback_query.message.answer('- Дети до 7 лет\n- Дети из многодетных семей в возрасте до 18 лет\n- Родители в многодетной семье\n- Дети-инвалиды, их родители (опекуны, попечители), лица, сопровождающие ребенка-инвалида, а также один из родителей инвалида с детства в возрасте до 23 лет, обучающегося в образовательном учреждении;\n- Дети-сироты и дети, оставшиеся без попечения родителей, лица из числа детей-сирот и детей, оставшихся без попечения родителей, лица, потерявшие в период обучения обоих родителей или единственного родителя, обучающиеся за счет средств бюджета Москвы по очной форме обучения по основным профессиональным образовательным программам и (или) по программам профессиональной подготовки по профессиям рабочих, должностям служащих;\n- Опекуны (попечители), приемные родители, патронатные воспитатели детей, оставшихся без попечения родителей, и детей-сирот в возрасте до 18 лет\n- Предпенсионеры\n- Граждане, награжденные знаками «Почетный донор СССР», «Почетный донор России», «Почетный донор Москвы»\n- Получатели городских мер социальной поддержки, которые не выбрали предоставление услуги в денежном эквиваленте. Это могут быть:\n - Получатели ЕГДВ (ежемесячной городской денежной выплаты):\n   - Труженики тыла\n   - Ветераны труда и приравненные к ним лица\n   - Реабилитированные лица\n   - Граждане, признанные пострадавшими от политических репрессий\n - Пенсионеры:\n   - Участники обороны Москвы\n    - Инвалиды I и II группы по зрению\n    - Члены семей реабилитированных, пострадавших в результате репрессий;\n    - Дети войны (родившиеся в период с 4 сентября 1927 года по 3 сентября 1945 года);\n    - Участники предотвращения Карибского кризиса 1962 года.')
        user_message_ids[callback_query.from_user.id] = msg.message_id



@router.callback_query(lambda c: c.data == 'exit_to_main_menu')
async def exit_to_main_menu(callback_query: CallbackQuery):
    current_markup = callback_query.message.reply_markup
    new_markup = kb.passengers_menu
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)

@router.callback_query(lambda c: c.data == 'exit')
async def exit_to_tariff_menu(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id in user_message_ids:
        await callback_query.bot.delete_message(chat_id=user_id, message_id=user_message_ids[user_id])
        del user_message_ids[user_id]
    current_markup = callback_query.message.reply_markup
    new_markup = kb.passengers_menu
    if current_markup != new_markup:
        await callback_query.message.edit_reply_markup(reply_markup=new_markup)


