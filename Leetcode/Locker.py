# Complete the function below.
#import Queue
def  check_log_history(events):
    queue = []
    for i in range(len(events)):
        if 'ACQUIRE' == events[i][0]:
            queue.append(events[i][1])
            continue
        elif 'RELEASE' == events[i][0] and queue.popleft()== events[i][1]:
            queue.popleft()
            continue
        print queue
    return 0


print check_log_history([(ACQUIRE,364),
ACQUIRE 84,
RELEASE 84,
RELEASE 364
])
