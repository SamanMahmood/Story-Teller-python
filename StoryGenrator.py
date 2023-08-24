import random

# Storing random data into lists to create story.
when = ['A long time ago', 'Yesterday', 'Before you were born',
        'In future', 'Before Thanos arrived', 'a few mintues', 'Today']
who = ['Saman', 'Maryum', 'Asma', 'Areej', 'Aimun',
       'Nawab', 'Batman', 'Superman', 'Captain Pakistan']
went = ['Dubai', 'Bahawalpur City', 'Lahor City', 'RYK City',
        'Bahawalnager City', 'Stark Tower', 'Bat Cave', 'Pakistan']
what = ['to eat a lot of cakes', 'to fight for justice',
        'to steal ice cream', 'to dance']

print(random.choice(when) + ', ' + random.choice(who) + ' went to ' +
      random.choice(went) + ' ' + random.choice(what) + '.')
