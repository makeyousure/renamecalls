import os
from os.path import isfile, join
from variable import catalog_dir


only_files = os.listdir(catalog_dir)


def create_new_folder(file_of_record):
    checked_file_date = file_of_record.split(' ')
    split_date_to_list = checked_file_date[-2].split('-')
    get_year = split_date_to_list[-1]
    get_month = split_date_to_list[-2]
    path_for_move = '{}{}/{}/'.format(catalog_dir, get_year, get_month) + file_of_record

    if os.path.isdir(catalog_dir+get_year):
        if os.path.isdir('{}{}/{}'.format(catalog_dir, get_year, get_month)):
            os.replace(catalog_dir + file_of_record, path_for_move)
        else:
            os.mkdir('{}{}/{}'.format(catalog_dir, get_year, get_month))
            os.replace(catalog_dir + file_of_record, path_for_move)
    else:
        os.mkdir('{}{}'.format(catalog_dir, get_year))
        os.mkdir('{}{}/{}'.format(catalog_dir, get_year, get_month))
        os.replace(catalog_dir + file_of_record, path_for_move)


for file in only_files:
    if isfile(join(catalog_dir, file)):
        if os.stat(catalog_dir+file).st_size <= 45000:
            os.remove(catalog_dir+file)
        else:
            create_new_folder(file)
