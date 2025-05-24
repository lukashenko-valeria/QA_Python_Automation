def calc_minutes(time_str):
    if 'h' in time_str:
        hour_list = time_str.split('h')
        return int(hour_list[0]) * 60
    elif 'm' in time_str:
        minute_list = time_str.split('m')
        return int(minute_list[0])
    elif 's' in time_str:
        second_list = time_str.split('s')
        return int(second_list[0]) // 60
    return 0

time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = time.replace(' ', ',').split(',')

minutes_sum = 0
for time_item in time_list:
    minutes_sum += calc_minutes(time_item)
print(minutes_sum)
