from datetime import datetime, timedelta


def check_plane_time(arrival_time: str, actual_time: str):
  arrival_time_datetime = datetime.strptime(arrival_time, '%H:%M')
  actual_time_datetime = datetime.strptime(actual_time, '%H:%M')
  delta = arrival_time_datetime - actual_time_datetime
  data = timedelta(minutes=0)
  
  if delta > timedelta(minutes=0):
    return f'Самолет прилетел раньше на {timedelta(minutes=0) + delta} минут'
  elif delta == timedelta(minutes=0):
    return f'Самолет прилетел вовремя'
  else:
    return f'Самолет опаздывает на {timedelta(minutes=0) - delta} минут'



arrival_plane_time = '14:40'

actual_plane_time = '14:30'

arrival_plane_time = '14:40'

actual_plane_time = '14:30'

arrival_plane_time = '14:40'

actual_plane_time = '14:30'

# arrival_plane_time = input() # Плановое время

# actual_plane_time = input()  # Фактическое время


print(check_plane_time('14:40', '14:30'))
print()
print(check_plane_time('14:40', '15:10'))
print()
print(check_plane_time('14:40', '14:40'))
