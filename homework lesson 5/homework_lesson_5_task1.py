from datetime import datetime

newspapers = {
    'The Moscow Times': 'Wednesday, October 2, 2002',
    'The Guardian': 'Friday, 11.10.13',
    'Daily News': 'Thursday, 18 August 1977'}

for newspaper in newspapers:
    if newspaper == 'The Moscow Times':
        print(datetime.strptime(newspapers[newspaper], '%A, %B %d, %Y').date())
    elif newspaper == 'The Guardian':
        print(datetime.strptime(newspapers[newspaper], '%A, %d.%m.%y').date())
    elif newspaper == 'Daily News':
        print(datetime.strptime(newspapers[newspaper], '%A, %d %B %Y').date())
