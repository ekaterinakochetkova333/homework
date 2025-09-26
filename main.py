from src.generators import filter_by_currency
from src.process_bank import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.transactions_read import transactions_read_csv, transactions_read_excel
from src.utils import read_json_file
from src.widget import get_data, mask_account_card

while True:
    print('*' * 40)
    dict_type_files = {
        '1': 'Получить информацию о транзакциях из JSON-файла',
        '2': 'Получить информацию о транзакциях из CSV-файла',
        '3': 'Получить информацию о транзакциях из XLSX-файла'
    }
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:')
    for key, name in dict_type_files.items():
        print(f'{key}. {name}')

    type_file = input()
    if type_file not in dict_type_files:
        print('Такого варианта нет!')
        continue

    transactions = []
    if type_file == '1':
        print("Для обработки выбран JSON-файл.")
        transactions = read_json_file('data/operations.json')
    elif type_file == '2':
        print("Для обработки выбран CSV-файл.")
        transactions = transactions_read_csv('data/transactions.csv')
#        print(transactions)
    elif type_file == '3':
        print("Для обработки выбран XLSX-файл.")
        transactions = transactions_read_excel('data/transactions_excel.xlsx')

    dict_state_transaction = [
        'EXECUTED',
        'CANCELED',
        'PENDING'
    ]
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print(f"Доступные для фильтровки статусы: {dict_state_transaction[0]}, {dict_state_transaction[1]}, {dict_state_transaction[2]}")
    state_transaction = input().lower()
    if state_transaction == dict_state_transaction[0].lower():
        print(f"Операции отфильтрованы по статусу {dict_state_transaction[0]}")
        transactions = filter_by_state(transactions, dict_state_transaction[0])
        print(transactions)
    elif state_transaction == dict_state_transaction[1].lower():
        print(f"Операции отфильтрованы по статусу {dict_state_transaction[1]}")
        transactions = filter_by_state(transactions, dict_state_transaction[1])
        print(transactions)
    elif state_transaction == dict_state_transaction[2].lower():
        print(f"Операции отфильтрованы по статусу {dict_state_transaction[2]}")
        transactions = filter_by_state(transactions, dict_state_transaction[2])
        print(transactions)
    else:
        print(f'Статус операции {state_transaction} недоступен')
        continue

    print("Отсортировать операции по дате? Да/Нет")
    answer_date = input()
    if answer_date == 'Да':
        transactions = sort_by_date(transactions)
        print(transactions)

    print("Отсортировать по возрастанию или по убыванию?")
    answer_sorted = input()
    if answer_sorted == 'по возрастанию':
        transactions = sorted(transactions, key=lambda x: x['id'])
        print(transactions)
    elif answer_sorted == 'по убыванию':
        transactions = sorted(transactions, key=lambda x: x['id'], reverse=True)
        print(transactions)

    print("Выводить только рублевые транзакции? Да/Нет")
    answer_transaction = input()
    if answer_transaction == 'Да':
        transactions = filter_by_currency(transactions, 'RUB')
        transactions = list(transactions)
        print(transactions)

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer_bank_search = input()
    if answer_bank_search == 'Да':
        transactions = process_bank_search(transactions, input("Введите слово для фильтрации: "))
        print(transactions)

    print("Распечатываю итоговый список транзакций...")
    print(f'Всего банковских операций в выборке: {len(transactions)}')
    if len(transactions) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        for item in transactions:
            print(f'{get_data(item.get('date'))} {item.get('description')}')
            print(f'{(mask_account_card(item.get('from')) + ' -> ' if 'from' in item else '')}{mask_account_card(item.get('to'))}')
            print(f'Сумма: {item['operationAmount']['amount']}')
