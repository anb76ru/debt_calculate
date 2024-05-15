def get_participant_count():
    """Получить количество участников мероприятия"""

    participant_count = int(input("Введите количество участников мероприятия: "))
    return participant_count


def fill_participant_dict(count_names):
    """
    Заполнить имена и затраты в словаре участников
    :param count_names: количество участников
    """

    participant_dict = {}

    for i in range(count_names):
        name, expenses = input("Введите имя и сумму затрат через пробел: ").split()
        participant_dict[name] = {"Затраты": round(float(expenses), 2)}

    return participant_dict


def get_total_expenses(participants: dict):
    """
    Получить сумму общих затрат
    :param participants: словарь с участниками
    """

    total_expenses = sum([d.get('Затраты') for d in participants.values()])
    print(f'\nОбщая сумма затрат составляет: {total_expenses}\n')
    return total_expenses


def get_average_expenses(participants: dict):
    """
    Получить среднюю сумму затрат
    :param participants: словарь с участниками
    """

    average_expenses = round(get_total_expenses(participants) / len(participants), 2)
    print(f'\nСредняя сумма затрат составляет: {average_expenses}\n')
    return average_expenses


def debt_calculate_by_name(participants: dict):
    """
    Рассчитать долг для каждого участника
    :param participants: словарь с участниками
    """

    average_expenses = get_average_expenses(participants)
    for name, data in participants.items():
        data["Долг"] = round(average_expenses - data.get("Затраты"), 2)
    return sorted_debt(participants)


def sorted_debt(participants: dict) -> list:
    """
    Отсортировать участников по сумме долга
    :param participants: словарь с участниками
    :return: список словарей (особенность сортировки)
    """

    return sorted(participants.items(), key=lambda item: item[1].get('Долг'))


def get_all_debts(participants):
    """
    Получить списов с суммами долгов
    :param participants: словарь с участниками
    """

    return [v.get('Долг') if abs(v.get('Долг')) >= 0.01 else 0 for v in participants.values()]
