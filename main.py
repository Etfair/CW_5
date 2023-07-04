from DBM import DBManager
import os


database = input('Введите название для базы данных: ')

password: str = os.getenv('pswd_pg')

"""Подключение к БД"""
db = DBManager(host="localhost", database=database.lower(), user="postgres", password=password)
"""Создание БД"""
db.create_database()
"""Создание таблиц employers и vacancies"""
db.create_tables()
"""Добавление информации в таблицы"""
db.insert_data()

while True:
    command = input(
        "Введите 1, чтобы просмотреть сколько вакансий в компании.\n"
        "Введите 2, чтобы просмотреть список всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию.\n"
        "Введите 3, чтобы узнать среднюю зарплату.\n"
        "Введите 4, чтобы узнать вакансии, зарплата по которым выше средней из найденных.\n"
        "Введите 5, чтобы посмотреть вакансии по ключевому слову.\n"
        "exit - для выхода.\n"
    )
    if command.lower() == 'exit':
        break
    elif command == '1':
        db.get_companies_and_vacancies_count()
    elif command == '2':
        db.get_all_vacancies()
    elif command == '3':
        db.get_avg_salary()
    elif command == '4':
        db.get_vacancies_with_higher_salary()
    elif command == '5':
        keyword = input('Введите слово: ')
        db.get_vacancies_with_keyword(keyword.title())
    else:
        break
