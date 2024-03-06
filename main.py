from helpers import *
from readme import *


def calculate(participants):
    """
    Вычислить сумму, которую должны перевести участники
    :param participants: словарь с участниками
    """

    # Получить список отсортированных по сумме долга словарей
    sorted_names_by_debt = debt_calculate_by_name(dict(participants))
    all_debts = get_all_debts(dict(participants))

    while all_debts != [0] * len(participants):  # Пока все долги не обнуляться

        # Получить минимальную и максимальную сумму долга
        min_debt, max_debt = sorted_names_by_debt[0][1].get('Долг'), sorted_names_by_debt[-1][-1].get('Долг')

        # Вычислить сумму перевода участника с максимальным долго участнику с минимальным долгом
        transfer_summ = abs(min_debt) if max_debt > abs(min_debt) else max_debt
        print(f"\n{sorted_names_by_debt[-1][0]} Переводит {sorted_names_by_debt[0][0]} {transfer_summ}")

        # Обновить суммы долгов
        debt_credit = min_debt + max_debt
        sorted_names_by_debt[0][1]['Долг'] = 0 if max_debt > abs(min_debt) else debt_credit
        sorted_names_by_debt[-1][-1]['Долг'] = 0 if max_debt < abs(min_debt) else debt_credit

        # Обновить данные, перевычислить долги
        participants = sorted_debt(dict(sorted_names_by_debt))
        sorted_names_by_debt = participants
        all_debts = get_all_debts(dict(participants))
    else:
        print("\nВсе долги рассчитаны\n")


if __name__ == '__main__':
    print_greetings()
    print_rules()
    count = get_participant_count()
    participant_dict = fill_participant_dict(count)
    calculate(participant_dict)
    input("Нажмите Enter для выхода")
