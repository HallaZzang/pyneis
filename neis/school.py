# coding: utf-8

import sys
import re
from bs4 import BeautifulSoup

from neis.meal import Menu, Meal

class School(object):
    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    @property
    def course(self):
        return self._course

    def __repr__(self):
        name = self.name.encode(sys.stdout.encoding or 'utf-8')
        return '<School: {}>'.format(name)

    def get_weekly_meals(self, year, month, day, type):
        """
        :params type: 1(breakfast), 2(lunch), 3(dinner)
        """

        data = {
            'schulCode': self.code,
            'schulCrseScCode': self.course,
            'schulKndScCode': '{:02}'.format(self.course)
        }

        data['schYmd'] = '{}.{:02}.{:02}'.format(year, month, day)
        data['schMmealScCode'] = type

        response = self._request_client.post('/sts_sci_md01_001.do', data)
        soup = BeautifulSoup(response.content)

        dates = []
        for col in soup.thead.find_all('th', scope='col'):
            dates.append(unicode(col.get_text(strip=True).split('(')[0]))

        meals = []
        cols = soup.tbody.find_all('tr')[1].find_all('td', 'textC')
        for idx, col in enumerate(cols):
            menus = []
            temp = col.get_text(strip=True, separator='||')
            if temp:
                for chunk in temp.split('||'):
                    text = re.sub(ur'[①-⑬]+', '', chunk)

                    match = re.search(ur'[①-⑬]+', chunk)
                    if match:
                        allergy = match.group(0)
                    else:
                        allergy = ''

                    menu = Menu()
                    menu._text = text
                    menu._allergy = allergy

                    menus.append(menu)

            meal = Meal()
            meal._date = dates[idx]
            meal._type = type
            meal._menus = menus

            meals.append(meal)

        return meals