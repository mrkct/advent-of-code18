import string

def get_job_time(job):
    return 60 + 1 + string.ascii_uppercase.index(job)


requirements = {}
with open('the-sum-of-its-parts-input.txt', 'r') as file: # 
    for line in file:
        required_letter, letter = line[5:6], line[36:37] # easy parsing
        if letter not in requirements:
            requirements[letter] = []
        if required_letter not in requirements: # to handle the first letter, that only appears as required
            requirements[required_letter] = []
        requirements[letter].append(required_letter)

workers = [dict(job=None, time=0) for _ in range(5)]
time_passed = 0

while requirements:
    # we assign jobs to workers who are free right now
    for j in requirements:
        # if a job can be done now
        if requirements[j] == []:
            # and there is no other worker doing it right now
            someone_doingit = False
            for w in workers:
                if w["job"] == j:
                    someone_doingit = True
                    break
            if not someone_doingit:
                # we search for a free worker
                for i in range(len(workers)):
                    if workers[i]["time"] == 0:
                        # we found it, we assign the job to him and break the cycle
                        # because we dont want to assign the same job to other free workers
                        workers[i]["job"] = j
                        workers[i]["time"] = get_job_time(j)
                        break
    for i in range(len(workers)):
        # we decrement the time counter for the workers
        workers[i]["time"] = max(0, workers[i]["time"] - 1)
        # the worker has completed his job. we remove it from the list
        if workers[i]["time"] == 0:
            job = workers[i]["job"]
            if job in requirements:
                del requirements[job]
            for j in requirements:
                if job in requirements[j]:
                    requirements[j].remove(job)
    time_passed += 1


print("Time passed: {}".format(time_passed))