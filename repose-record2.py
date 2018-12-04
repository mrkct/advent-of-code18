from datetime import datetime


GUARD_STARTS = 0
GUARD_WAKE_UP = 1
GUARD_SLEEPS = 2


def parse_line(line):
    timestamp = line[3: line.find(']')]
    dtime = datetime.strptime(timestamp, "%y-%m-%d %H:%M")
    
    event = line[line.find(']')+2:]
    event_type = ''
    guard_id = None
    if 'wakes up' in event:
        event_type = GUARD_WAKE_UP
    elif 'falls asleep' in event:
        event_type = GUARD_SLEEPS
    else:
        event_type = GUARD_STARTS
        guard_id = int(event[event.find('#')+1: event.find(' ', event.find('#'))])
    
    return dict(
        datetime=dtime,
        event_type=event_type,
        guard_id=guard_id
    )

def filter_records_by_guard_id(records, guard_id):
    filtered_records = []
    i = 0
    while i < len(records):
        g_id = records[i]['guard_id']
        i += 1
        while i < len(records) and records[i]['event_type'] != GUARD_STARTS:
            if g_id == guard_id:
                filtered_records.append(records[i])
            i += 1
    
    return filtered_records


def get_most_slept_minute(records, guard_id):
    guard_records = filter_records_by_guard_id(records, guard_id)
    minutes_slept = [0 for x in range(60)]
    i = 0
    while i < len(guard_records):
        min_from = int(guard_records[i]['datetime'].strftime('%M'))
        min_to = int(guard_records[i+1]['datetime'].strftime('%M'))
        for x in range(min_from, min_to):
            minutes_slept[x] += 1
        i += 2
    
    msm_index = 0   # most slept minute index
    for i in range(60):
        if minutes_slept[msm_index] < minutes_slept[i]:
            msm_index = i
    
    return (msm_index, minutes_slept[msm_index])


with open('repose-record-input.txt', 'r') as file:
    records = []
    guard_ids = set()
    for line in file:
        event = parse_line(line)
        records.append(event)
        if event['event_type'] == GUARD_STARTS:
            guard_ids.add(event['guard_id'])
    guard_ids = list(guard_ids)
    records.sort(key=lambda x: x['datetime'])

    most_slept_minute = get_most_slept_minute(records, guard_ids[0]) # ritorna tupla (minuto, volte_dormito)
    most_slept_gid = guard_ids[0]
    for gid in guard_ids:
        t = get_most_slept_minute(records, gid)
        if t[1] > most_slept_minute[1]:
            most_slept_minute = t
            most_slept_gid = gid
    
    print("{} x {} = {}".format(most_slept_minute[0], most_slept_gid, most_slept_minute[0] * most_slept_gid))