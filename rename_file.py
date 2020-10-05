import os
from os.path import isfile, join
from variable import catalog_dir


bad_chars = ['§']
only_files = os.listdir(catalog_dir)


def change_date_format(bad_format_of_date):
    """Изменяет формат даты в названии звонка"""
    split_bad_date_format = bad_format_of_date.split('-')
    return '{}-{}-{}'.format(split_bad_date_format[2], split_bad_date_format[1], split_bad_date_format[0])


def return_name_from_contactlist(list_of_name_parts):
    """Преобразует список из частей имени в строку"""
    name_to_string = ''
    for part in list_of_name_parts:
        if part == list_of_name_parts[-1]:
            name_to_string += '{}'.format(part)
        else:
            name_to_string += '{} '.format(part)
    return name_to_string


def rename_file_with_good_name(old_name, caller_name, date_of_call, time_of_call):
    os.rename(os.path.join(catalog_dir + old_name),
              os.path.join(catalog_dir + '{} {} {}'.format(caller_name, date_of_call, time_of_call)))


def final_name_for_file(name_of_file):
    """На вход принимает файл.
        Разбивает имя на части. Если длина списка элементов имени равна 3-м и не начинается с '§',
        то меняет имя в нужный формат.
        Иначе заменяет нукдобное имя на нужное"""
    list_of_elements = name_of_file.split(' ')
    name = list_of_elements[:-2]
    date_of_call = change_date_format(list_of_elements[-2])
    time_of_call = list_of_elements[-1]
    if name[0][0] in bad_chars:
        name = 'From Contacts'
        rename_file_with_good_name(name_of_file, name, date_of_call, time_of_call)
    else:
        name = return_name_from_contactlist(name)
        rename_file_with_good_name(name_of_file, name, date_of_call, time_of_call)


for file in only_files:
    if isfile(join(catalog_dir, file)):
        final_name_for_file(file)
