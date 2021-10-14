import csv
from operator import is_not
from functools import partial

class Parser():

    @staticmethod
    def get_data() -> list:

        firstname_male = []
        firstname_female = []
        surname_male = []
        surname_female = []
        patronymic = []
        with open('flaskapp/engine/data/data_for_generation.csv') as f:
            data_from_file = csv.DictReader(f, delimiter=',')
            for line in data_from_file:
                if line['firstname_male'] != None and line['firstname_male'] != '':
                    firstname_male.append(line['firstname_male'].rstrip())
                if line['firstname_female'] != None and line['firstname_female'] != '':
                    firstname_female.append(line['firstname_female'].rstrip())
                if line['surname_male'] != None and line['surname_male'] != '':
                    surname_male.append(line['surname_male'].rstrip())
                if line['surname_female'] != None and line['surname_female'] != '':
                    surname_female.append(line['surname_female'].rstrip())
                if line['patronymic'] != None and line['patronymic'] != '':
                    patronymic.append(line['patronymic'].rstrip())    
        return [
            firstname_male, firstname_female,
            surname_male, surname_female, patronymic
        ]

    # @staticmethod
    # def get_data(gender: str):

    #     if gender == 'male':
    #         with open('flaskapp/engine/data/firstname_male.txt', 'r') as f:
    #             firstname = [firstname.rstrip() for firstname in f]
    #         with open('flaskapp/engine/data/surname_male.txt', 'r') as f:
    #             surname = [surname.rstrip() for surname in f]
    #     elif gender == 'female':
    #         with open('flaskapp/engine/data/firstname_female.txt', 'r') as f:
    #             firstname = [firstname.rstrip() for firstname in f]
    #         with open('flaskapp/engine/data/surname_female.txt', 'r') as f:
    #             surname = [surname.rstrip() for surname in f]

    #     with open('flaskapp/engine/data/patronymic.txt', 'r') as f:
    #         patronymic = [patronymic.rstrip() for patronymic in f]

    #     return [surname, firstname, patronymic]
