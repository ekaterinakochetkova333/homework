from src.transactions_read import transactions_read_csv, transactions_read_excel

transactions_return = transactions_read_csv('data/transactions.csv')
print(transactions_return)


transactions_return = transactions_read_excel('data/transactions_excel.xlsx')
print(transactions_return)
