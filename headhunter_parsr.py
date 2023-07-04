import requests


class HeadHunter:
    def __init__(self):
        self.employers_id = [int(data['id']) for data in self.get_employers()]

    def get_employers(self):
        params = {'page': 10, 'per_page': 10, 'area': 113, 'only_with_vacancies': True}
        response = requests.get('https://api.hh.ru/employers', params).json()
        return response['items']

    def get_vacancies(self):
        vacancies = []
        for id in self.employers_id:
            params = {'employer_id': id, 'per_page': 5}
            response = requests.get('https://api.hh.ru/vacancies', params).json()['items']
            vacancies.extend(response)
        return vacancies
