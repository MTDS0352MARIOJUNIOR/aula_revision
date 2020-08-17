#data e horario atual
from datetime import date, time, datetime
d = datetime.now()
print(d.strftime('%d/%m/%Y'))
print(d.strftime('%A, %d %B, %y'))
