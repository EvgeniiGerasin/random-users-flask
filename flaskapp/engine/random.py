from flaskapp.engine.parser import Parser
from flaskapp.engine.loginandpassword import DataAuth

import random
import time
import csv


class RandomUserData():

    def __init__(
        self,
        start_date: str = None,
        stop_date: str = None,
        gender: str = None,
        number: str = None,
    ) -> None:
        """Methods for radom data

        Args:
            start_date: %d%m%Y
            stop_date: %d%m%Y
        """
        self.start_date = start_date
        self.stop_date = stop_date
        self.gender = gender
        self.number = number

    def full_random_user(self) -> dir:
        """The method returns random data of a male/female's
        full name,date of birth, isername and password
        Example: dic -> 
        {'gender': , 'surname': , 'fistname': , 'patranymic': , 'date of birth': ,
        'username': , 'password':}
        """
        random_date = self._formation_date()
        gender = random.choice(['male', 'female'])
        patranymic = random.choice(Parser.get_data()[4])
        if gender == 'male':
            patranymic = patranymic + 'ич'
            surname = random.choice(Parser.get_data()[2])
            firstname = random.choice(Parser.get_data()[0])
        else:
            patranymic = patranymic + 'на'
            surname = random.choice(Parser.get_data()[3])
            firstname = random.choice(Parser.get_data()[1])
        date_birth = random_date
        username = DataAuth().username(surname)
        password = DataAuth().password(firstname)
        return {
            'gender': gender,
            'surname': surname,
            'firstname': firstname,
            'patranymic': patranymic,
            'date_birth': date_birth,
            'username': username,
            'password': password
        }

    def castom_random_user(self) -> dir:
        """The method returns random data of a male/female's
        full name,date of birth, isername and password
        Example: dic -> 
        {'gender': , 'surname': , 'fistname': , 'patranymic': , 'date of birth': ,
        'username': , 'password':}
        """
        gender = self.gender
        if gender == 'random':
            gender = random.choice(['male', 'female'])
        random_date = self._formation_date(self.start_date, self.stop_date)
        patranymic = random.choice(Parser.get_data()[4])
        if gender == 'male':
            patranymic = patranymic + 'ич'
            surname = random.choice(Parser.get_data()[2])
            firstname = random.choice(Parser.get_data()[0])
        else:
            patranymic = patranymic + 'на'
            surname = random.choice(Parser.get_data()[3])
            firstname = random.choice(Parser.get_data()[1])
        date_birth = random_date
        username = DataAuth().username(surname)
        password = DataAuth().password(firstname)
        return {
            'gender': gender,
            'surname': surname,
            'firstname': firstname,
            'patranymic': patranymic,
            'date_birth': date_birth,
            'username': username,
            'password': password
        }

    def _formation_date(
        self,
        start_date: str = None,
        stop_date: str = None
    ) -> str:

        if start_date:
            start = start_date
        else:
            start = '1990-01-01'
        if stop_date:
            stop = stop_date
        else:
            stop = '2010-01-01'

        date_start_sec = time.mktime(time.strptime(start, '%Y-%m-%d'))
        date_stop_sec = time.mktime(time.strptime(stop, '%Y-%m-%d'))
        random_data_sec = random.randint(
            0, date_stop_sec - date_start_sec
        ) + date_start_sec
        return time.strftime('%d.%m.%Y', time.localtime(random_data_sec))

    def generate_csv_users(self, number):

        with open('flaskapp/engine/csv/data_users.csv', 'w') as f:
            fields_names = [
                'gender', 'surname', 'firstname', 'patranymic',
                'date_birth', 'username', 'password',
            ]
            writer = csv.DictWriter(f, fieldnames=fields_names)
            writer.writeheader()
            for _ in range(0, number):
                data_one_user = self.castom_random_user()
                writer.writerow(
                    {
                        'gender': data_one_user['gender'],
                        'surname': data_one_user['surname'],
                        'firstname': data_one_user['firstname'],
                        'patranymic': data_one_user['patranymic'],
                        'date_birth': data_one_user['date_birth'],
                        'username': data_one_user['username'],
                        'password': data_one_user['password'],
                    }
                )

    def get_user(self):

        data_for_create = Parser.get_data()

        output_data = []

        if self.number and self.number != '':
            number = self.number
        else:
            number = 1
        for _ in range(0, number):
            patranymic = random.choice(Parser.get_data()[4])
            random_date = self._formation_date(
                self.start_date,
                self.stop_date
            )
            # service gender
            gender = self.gender
            if gender == 'random' or gender == '' or gender == None:
                gender = random.choice(['male', 'female'])
            if gender == 'male':
                patranymic = patranymic + 'ич'
                surname = random.choice(data_for_create[2])
                firstname = random.choice(data_for_create[0])
            elif gender == 'female':
                patranymic = patranymic + 'на'
                surname = random.choice(data_for_create[3])
                firstname = random.choice(data_for_create[1])
            date_birth = random_date
            username = DataAuth().username(surname)
            password = DataAuth().password(firstname)

            output_data.append(
                {
                    'gender': gender,
                    'surname': surname,
                    'firstname': firstname,
                    'patranymic': patranymic,
                    'date_birth': date_birth,
                    'username': username,
                    'password': password
                }
            )
        return output_data
