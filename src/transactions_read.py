import csv
import pandas


def transactions_read_csv(path):
    """Функция для считывания финансовых операций из CSV"""
    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)


def transactions_read_excel(path):
    """Функция для считывания финансовых операций из Excel"""
    excel_data = pandas.read_excel(path).to_dict('records')
    return excel_data
