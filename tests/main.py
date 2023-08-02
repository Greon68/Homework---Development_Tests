# ЗАДАЧА №1
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

def get_name_mentors(list_of_list):
    '''Функция получает на вход список списков имён и
    фамилий преподователей .
     Возвращает строку с уникальными именами из входящего списка '''
    # Добавим в общий список всех преподавателей со всех курсов
    all_list = []
    for m in list_of_list:
        all_list.extend(m)

    # Список только из имён
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    # Оставим только уникальные имена
    unique_names = list(set(all_names_list))
    # отсортируем имена в алфавитном порядке.
    all_names_sorted = sorted(unique_names)
    # Финишный список
    all_names_str = ' , '.join(all_names_sorted)
    return all_names_str

def get_top_name(data_list):
	'''Функция получает на вход список списков имён и
    фамилий людей . Возвращает список списков с тремя
     уникальными именами  и количесвом их повторений во входном списке'''
	all_data_list = []
	for el in data_list:
		all_data_list.extend(el)

	# Cоздаём полный список имен
	all_name_list = []
	for elem in all_data_list:
		all_name_list.append(elem.split()[0])
	# Cоздаём уникальных имён
	unique_names = list(set(all_name_list))
	# Cоздадим список количеств повторений уникальных имен
	count_name_list = []
	for name in unique_names:
		count_name = all_name_list.count(name)
		count_name_list.append([name, count_name])
	# Сортируем список по алфавиту
	count_name_list.sort(key=lambda x: x[1], reverse=True)
	# Выводим 3 первых элемента
	top_3_list = count_name_list[:3]
	return top_3_list





def get_max_duration_courses(list_of_courses ,list_of_durations):
	'''Функция получает на вход 2 списка - названия курсов и их продолжительность (по индексам) .
	Возвращает название и продолжительность самых длинных и самых коротких  курсов ,
	'''
	# В этот список будут добавляться словари-курсы
	courses_list = []
	for cours , duration  in zip (list_of_courses,list_of_durations):
		course_dict= {'Название курса':cours ,'Продолжительность':duration }
		courses_list.append(course_dict)
	# Сравнение длительности курсов , нахождение самого длинного и самого короткого
	min_dur_cours = min(durations)            # 12
	max_dur_cours = max(durations)            # 20

	# Определим списки самых коротких и самых длинных курсов
	duration_min_list = []    # Список курсов с минимальной длительностью обучения
	duration_max_list = []    # Список курсов с максимальной длительностью обучения
	for course in courses_list:
		if course['Продолжительность']== min_dur_cours:
			duration_min_list.append(course['Название курса'])
		if course['Продолжительность'] == max_dur_cours:
			duration_max_list.append(course['Название курса'])

	courses_min = ", ".join(str(a) for a in duration_min_list)
	courses_max = ", ".join(str(a) for a in duration_max_list)
	result = f'Самый короткий курс(ы): {courses_min} - {min_dur_cours} месяца(ев), cамый длинный курс(ы): {courses_max} - {max_dur_cours} месяца(ев)'
	return 	result


# Задание № 2
# Работа с Яндекс-диском

import requests
import unittest
from unittest import TestCase

# ЗАГРУЖАЕМ ФАЙЛ НА ЯНДЕКС-ДИСК

TOKEN = "..."


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
		# pprint (data_list)
		# Список заголовков
		name_list = []
		for element in data_list:
			name_list.append(element['name'])
		return name_list





if __name__ == '__main__':
	# Задание №1
	unic_name = get_name_mentors(mentors_list)
	print(unic_name)
	res = get_top_name(mentors_list)
	print(res)
	result = get_max_duration_courses(courses, durations)
	print(result)

	# Задание №2
	ya = YandexDisk(token=TOKEN)
	my_file = 'file_for_homework'
	file_on_ya_disk = 'tests_file.txt'
	# Загрузка нового файла на Яндекс-диск:
	ya.upload_file_to_disk(file_on_ya_disk, my_file)

	# Определим , имеется ли файл с нужным названием на Яндекс-диске :
	name_list = ya.get_list_names_files()

	print(len(name_list))
	if file_on_ya_disk in name_list:
		print('Файл обнаружен')
	else:
		print('Файл не найден')


























