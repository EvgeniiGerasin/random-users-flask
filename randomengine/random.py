from randomengine.parser import Parser
from randomengine.loginandpassword import DataAuth

import random
import time


class RandomUserData():

    def __init__(
        self,
        start_date: str = None,
        stop_date: str = None
    ) -> None:
        """Methods for radom data

        Args:
            start_date: %d%m%Y
            stop_date: %d%m%Y
        """
        self.start_date = start_date
        self.stop_date = stop_date

    def full_random(self) -> list:
        """The method returns random data of a male/female's
        full name and date of birth. 
        Example: list -> 
        ['surname', 'fistname', 'patranymic', 'date of birth']
        """
        random_date = self.formation_date(self.start_date, self.stop_date)
        gender = random.choice(['male', 'female'])
        surname = random.choice(Parser.get_data(gender=gender)[0])
        firstname = random.choice(Parser.get_data(gender=gender)[1])
        patranymic = random.choice(Parser.get_data(gender=gender)[2])
        if gender == 'male':
            patranymic = patranymic + 'ич'
        else:
            patranymic = patranymic + 'на'
        date_birth = random_date
        username = DataAuth().username(surname)
        password = DataAuth().password(firstname)
        return [surname, firstname, patranymic, date_birth, username, password]

    def formation_date(self, start_date: str, stop_date: str) -> str:

        if start_date:
            start = start_date
        else:
            start = '01.01.1990'
        if stop_date:
            stop = stop_date
        else:
            stop = '01.01.2010'

        date_start_sec = time.mktime(time.strptime(start, '%d.%m.%Y'))
        date_stop_sec = time.mktime(time.strptime(stop, '%d.%m.%Y'))
        random_data_sec = random.randint(
            0, date_stop_sec - date_start_sec
        ) + date_start_sec
        return time.strftime('%d.%m.%Y', time.localtime(random_data_sec))
