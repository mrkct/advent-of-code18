from datetime import datetime

# Beware: This is terrible

GUARD_WAKE_UP = 'wakes up'
GUARD_SLEEPS = 'falls asleep'
GUARD_STARTS = 'begins shift'

def parse_line(line):
    timestamp = line[3: line.find(']')]
    dtime = datetime.strptime(timestamp, "%y-%m-%d %H:%M")
    date, time = timestamp.split(' ')
    year, month, day = date.split('-')
    hour, minute = time.split(':')

    
    event = line[line.find(']')+2:]
    event_type = ''
    guard_id = None
    if GUARD_WAKE_UP in event:
        event_type = GUARD_WAKE_UP
    elif GUARD_SLEEPS in event:
        event_type = GUARD_SLEEPS
    else:
        event_type = GUARD_STARTS
        guard_id = int(event[event.find('#')+1: event.find(' ', event.find('#'))])
    
    return dict(
        year=int(year),
        month=int(month),
        day=int(day),
        hour=int(hour),
        minute=int(minute),
        datetime=dtime,
        event_type=event_type,
        guard_id=guard_id
    )

def time_difference(datetime1, datetime2):
    m1 = int(datetime1.timestamp() / 60)
    m2 = int(datetime2.timestamp() / 60)

    return abs(m1-m2)

with open('repose-record-input.txt', 'r') as file:
    records = []
    guard_ids = set()
    for line in file:
        event = parse_line(line)
        records.append(event)
        if event['event_type'] == GUARD_STARTS:
            guard_ids.add(event['guard_id'])
    guard_ids = list(guard_ids)
    records.sort(key=lambda x: (x['year'], x['month'], x['day'], x['hour'], x['minute']))

    i = 0
    sleeping_times = {}
    while i < len(records):
        g_id = records[i]['guard_id']
        if g_id not in sleeping_times:
            sleeping_times[g_id] = 0
        i += 1
        while i < len(records) and records[i]['event_type'] != GUARD_STARTS:
            sleeping_times[g_id] += time_difference(records[i]['datetime'], records[i+1]['datetime'])
            i += 2

    most_sleep_guard = guard_ids[0]
    for gid in guard_ids:
        if sleeping_times[gid] > sleeping_times[most_sleep_guard]:
            most_sleep_guard = gid
    
    sleepy_guard_records = []
    work_days = {}
    i = 0
    while i < len(records):
        g_id = records[i]['guard_id']
        i += 1
        while i < len(records) and records[i]['event_type'] != GUARD_STARTS:
            if g_id == most_sleep_guard:
                sleepy_guard_records.append(records[i])
                datekey = records[i]['datetime'].strftime('%y-%m-%d')
                if datekey not in work_days:
                    work_days[datekey] = ['.' for minute in range(60)]
            i += 1
    
    i = 0
    while i < len(sleepy_guard_records):
        min_from = int(sleepy_guard_records[i]['datetime'].strftime('%M'))
        min_to = int(sleepy_guard_records[i+1]['datetime'].strftime('%M'))
        keydate = sleepy_guard_records[i]['datetime'].strftime('%y-%m-%d')
        for x in range(min_from, min_to):
            work_days[keydate][x] = '#'
        i += 2


    for date in work_days:
        print(date, end='  ')
        for i in range(len(work_days[date])):
            print(work_days[date][i], end='')
        print("")
    

    column_sleep = [0 for x in range(60)]
    for date in work_days:
        for x in range(60):
            if work_days[date][x] == '#':
                column_sleep[x] += 1
    
    max_min = 0
    for i in range(60):
        if column_sleep[i] > column_sleep[max_min]:
            max_min = i
    print("Best time to attack is at minute {}. The guard {} slept {} times at this minute".format(max_min, most_sleep_guard, column_sleep[max_min]))
    print("The code is {} x {} = {}".format(most_sleep_guard, max_min, int(most_sleep_guard) * max_min))