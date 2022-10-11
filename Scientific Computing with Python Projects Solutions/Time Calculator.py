def add_time(start, duration, week_day=None):
    days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
            4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    # print(day_number)
    if start.split()[1] == 'PM':
        time = start.split()[0].split(':')
        time[0] = int(time[0])+12
    else:
        time = start.split()[0].split(':')
    start_in_minutes = int(time[0])*60+int(time[1])
    duration = duration.split(':')
    duration_in_minutes = int(duration[0])*60+int(duration[1])
    total_time = start_in_minutes+duration_in_minutes
    total_hours = total_time//60
    # print(total_hours)
    total_minutes = total_time % 60
    if len(str(total_minutes)) == 1:
        total_minutes = f'0{total_minutes}'
    new_time = None
    if week_day:
        for k, v in days.items():
            if v == week_day.title():
                day_number = k
        if total_hours > 12 and total_hours < 24:
            total_hours -= 12
            total_minutes = f'{total_minutes} PM'
            new_time = (f'{total_hours}:{total_minutes}, {days[day_number]}')
        elif total_hours < 12:
            if int(total_minutes) > 0:
                total_minutes = f'{total_minutes} AM'
            else:
                total_minutes = f'{total_minutes} AM'
            new_time = (f'{total_hours}:{total_minutes}, {days[day_number]}')
        elif total_hours == 12:
            if int(total_minutes) > 0:
                total_minutes = f'{total_minutes} PM'
            else:
                total_minutes = f'{total_minutes} PM'
            new_time = (f'{total_hours}:{total_minutes}, {days[day_number]}')
        elif total_hours >= 24:
            
            day_count = total_hours//24
            day_number += total_hours//24
            total_hours -= total_hours//24*24

            total_minutes = f'{total_minutes} AM'
            if day_count == 1:
                new_time = (
                    f'{total_hours}:{total_minutes}, {days[day_number]} (next day)')
            elif day_number == 7:
                new_time = (
                    f'{total_hours}:{total_minutes}, {days[day_number]} (next day)')
            elif day_number > 7:
                new_time = (
                    f'{total_hours}:{total_minutes}, {days[day_count//7-1]} ({day_count} days later)')
            else:
                if 'AM' in total_minutes and total_hours == 0:
                    print(day_count)
                    total_hours = 12
                new_time = (
                    f'{total_hours}:{total_minutes}, {days[day_number]} ({day_count} days later)')

    else:
        if total_hours > 12 and total_hours < 24:
            total_hours -= 12
            total_minutes = f'{total_minutes} PM'
            new_time = (f'{total_hours}:{total_minutes}')
        elif total_hours < 12:
            if int(total_minutes) > 0:
                total_minutes = f'{total_minutes} AM'
            else:
                total_minutes = f'{total_minutes} AM'
            new_time = (f'{total_hours}:{total_minutes}')
        elif total_hours == 12:
            if int(total_minutes) > 0:
                total_minutes = f'{total_minutes} PM'
            else:
                total_minutes = f'{total_minutes} PM'
            new_time = (f'{total_hours}:{total_minutes}')
        elif total_hours >= 24:

            day_number = total_hours//24
            total_hours -= total_hours//24*24
            total_minutes = f'{total_minutes} AM'
            print(total_hours, total_minutes, day_number)
            if day_number == 1:
                new_time = (
                    f'{total_hours}:{total_minutes} (next day)')

            elif day_number > 7:
                
                new_time = (
                    f'{total_hours}:{total_minutes} ({day_number} days later)')
            else:
                if 'AM' in total_minutes and total_hours == 0:
                    total_hours = 12
                new_time = (
                    f'{total_hours}:{total_minutes} ({day_number} days later)')
    print(new_time)


add_time("8:16 PM", "466:02", "tuesday")
