# Задача №1 unit-tests
# Напишите тесты на любые 3 задания из занятия
# «Коллекции данных» модуля «Основы языка программирования Python».
# Используйте своё решение домашнего задания.


import requests
import unittest
from unittest import TestCase
from main import get_name_mentors , get_top_name , get_max_duration_courses

# unittest


mentors_list = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python",
		   "Python-разработчик с нуля", "Frontend-разработчик с нуля"]

durations = [14, 20, 12, 20]



class TestGetName(TestCase):
    def test_get_name(self):
        expected = 'Адилет , Азамат , Александр , Алексей , Алена , Анатолий , Анна , Антон , Вадим , Валерий , Владимир , Денис , Дмитрий , Евгений , Елена , Иван , Илья , Кирилл , Константин , Максим , Михаил , Никита , Николай , Олег , Павел , Ринат , Роман , Сергей , Татьяна , Тимур , Филипп , Эдгар , Юрий'
        result = get_name_mentors(mentors_list)
        self.assertEqual(result, expected)

    def test_get_top3_name(self):
        expected = [['Александр', 10], ['Евгений', 5], ['Максим', 4]]
        result = get_top_name(mentors_list)
        self.assertEqual(result, expected)

    def test_get_max_duration_courses(self):
        expected = 'Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев), cамый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)'
        result = get_max_duration_courses(courses, durations)
        self.assertEqual(result, expected)





# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API.
# Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test
# на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов





# ЗАГРУЖАЕМ ФАЙЛ НА ЯНДЕКС-ДИСК



class YandexDisk:

	def __init__(self, token):
		self.token = token

	def get_headers(self):
		return {
			'Content-Type': 'application/json',
			'Authorization': f'OAuth {self.token}'
		}

	def get_files_list(self):
		files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
		params = {"limit": 99999}
		headers = self.get_headers()
		response = requests.get(files_url, headers=headers, params=params)
		return response.json()

	def _get_upload_link(self, disk_file_path):
		upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
		headers = self.get_headers()
		params = {"path": disk_file_path, "overwrite": True}
		response = requests.get(upload_url, headers=headers, params=params)
		return response.json()

	def upload_file_to_disk(self, disk_file_path, filename):
		data_link = self._get_upload_link(disk_file_path=disk_file_path)
		url = data_link.get("href")
		response = requests.put(url, data=open(filename, 'rb'))
		print(response.status_code)
		if response.status_code == 201:
			print("Файл успешно загружен")
		return response.status_code



	def get_list_names_files(self):
		'''Функция возвращает список названий
		 всех файлов на Яндекс-диске '''
		data = ya.get_files_list()
		# Избавимся от первого уровня вложенности файла:
		data_list = data["items"]
		# Список заголовков
		name_list = []
		for element in data_list:
			name_list.append(element['name'])

		return name_list




# ТЕСТИРОВАНИЕ
TOKEN = "..."
ya = YandexDisk(token=TOKEN)
my_file = 'file_for_homework'
file_on_ya_disk = 'tests_file.txt'

class TestYandexDisc(TestCase):
    def test_status_upload_file(self):
        '''Проверка на статуса
         "Файл загружен" '''
        expected = 201
        result = ya.upload_file_to_disk(file_on_ya_disk, my_file)
        self.assertEqual(result, expected)

    #Тест на ответ с ошибкой
    #Используем декоратор для пропуска провального теста
    @unittest.expectedFailure
    def test_fuls_status_upload_file(self):
        '''Проверка на статуса
         "Файл загружен" '''
        expected = 504
        result = ya.upload_file_to_disk(file_on_ya_disk, my_file)
        self.assertEqual(result, expected)

	# Проверяем , есть ли файл с нужным названием в списке файлов на Яндекс-диске
    def test_name_file_in_disk(self):
        a = file_on_ya_disk
        list1 = ya.get_list_names_files()
        self.assertIn(a,list1)


