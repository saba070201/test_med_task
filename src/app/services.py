import datetime 
def create_time_stamps():
    end_time = datetime.datetime(year=2023,month=11,day=11,hour=21,minute=0)
    start_time = datetime.datetime(year=2023,month=11,day=11,hour=9,minute=0)
    delta = datetime.timedelta(minutes=1)
    all_times = []
    while start_time <= end_time:
        all_times.append(start_time.strftime('%H:%M'))
        start_time= start_time+delta
    return all_times
def get_free(busy,all_):
    for i in all_:
        for j in busy:
            if i == j['start']:
                all_.insert(all_.index(i)+1,'busy')
                del all_[all_.index(i)+2:all_.index(j['stop'])]
 
    temp_list=[]
    free=[]
    i=0
    while i < len(all_):
        if len(temp_list)==31:
          
            free.append({'start':temp_list[0],'stop':[temp_list[-1]]})
            temp_list=[]
            i=i-1
          
        elif all_[i]=='busy':
            temp_list=[]
            i+=1
        else:
            temp_list.append(all_[i])
            i+=1
    return free

def get_openings():
    busy = [
    {'start' : '10:30',
    'stop' : '10:50'
    },
    {'start' : '18:40',
    'stop' : '18:50'
    },
    {'start' : '14:40',
    'stop' : '15:50'
    },
    {'start' : '16:40',
    'stop' : '17:20'
    },
    {'start' : '20:05',
    'stop' : '20:20'
    }
    ]
    l=create_time_stamps()
    RESULT=get_free(busy,l)
    return RESULT 