from dataclasses import dataclass
import json

from bs4 import BeautifulSoup


@dataclass
class Class:
    title: str
    subject: str
    code: str
    section: str
    hours: tuple[float, float]
    CRN: str
    term: str
    session: str
    instructor: str
    times: str
    location: str
    full: bool
    attribute: str

    def to_json(self) -> str:
        return json.dumps({
            'title': self.title,
            'subject': self.subject,
            'code': self.code,
            'section': self.section,
            'minHours': self.hours[0],
            'maxHours': self.hours[1],
            'CRN': self.CRN,
            'term': self.term,
            'session': self.session,
            'instructor': self.instructor,
            'times': None,
            'location': self.location,
            'full': self.full,
            'attribute': self.attribute,
        })


classes = []

for i in range(1, 26):
    with open(f'data/html/{i}.html') as file:
        html = ''.join(line for line in file)

    soup = BeautifulSoup(html, features='html.parser')

    data = [c.find_all('td') for c in soup.table.tbody.find_all('tr')]

    for class_ in data:
        title = class_[0].a.text
        subject = class_[1].text
        code = class_[2].text
        section = class_[3].text

        _hours = class_[4].text
        if ' TO ' in _hours:
            low, high = map(float, _hours.split(' TO '))
        elif ' OR ' in _hours:
            low, high = map(float, _hours.split(' OR '))
        else:
            low = high = float(_hours)
        hours = (low, high)

        CRN = class_[5].text
        term = class_[6].text
        session = class_[7].text
        instructor = class_[8].text
        times = 'TODO' # class_[9]
        campus = class_[10].text
        full = 'FULL' in class_[11].text
        attribute = class_[12].text

        classes.append(Class(title, subject, code, section, hours, CRN, term, session, instructor, times, campus, full, attribute))


with open('docs/classes.json', 'w') as file:
    file.write('[' + ','.join(c.to_json() for c in classes) + ']\n')
