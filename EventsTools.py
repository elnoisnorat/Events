'''
EventsTools.py
'''
import pickle, pprint
import calendar
import datetime
from getpass import _raw_input


class Events:
    def __init__(self, name, date, time, status):
        self.name = name
        self.date = date
        self.time = time
        self.status = status
    
    def set_name(self, name):
        self.name = name
        
    def set_date(self, date):
        self.date = date
        
    def set_time(self, time):
        self.time = time
        
    def set_status(self, status):
        self.status = status
        
    def get_name(self):
        return self.name
        
    def get_date(self):
        return self.date
        
    def get_time(self):
        return self.time
        
    def get_status(self):
        return self.status    


#username = 'guest'
username = ''
username = _raw_input('Enter a username: ')
try:
    userfile = open(username+'.pkl', 'rb')
    try:
        eventsList = pickle.load(userfile)
    except EOFError:
        eventsList = []
except FileNotFoundError:
    userfile = open(username+'.pkl', 'wb')
    eventsList = []
    
userfile.close()



def add(event, date, time):
    now = datetime.datetime.now()
    if event == None :
        event = 'Untitled event'
    if date == None:
        date = []
        date.append(str(now.day)+'/'+str(now.month)+'/'+str(now.year))
    #else: # check if valid date
    if time == None:
        time = []
        time.append(str(now.hour)+':'+str(now.minute))
    #else: # check if valid time
    

    ev = Events(event, date, time, ' ')
    eventsList.append(ev)   
    savefile = open(username+'.pkl', 'wb')
    pickle.dump(eventsList, savefile)
    savefile.close()
    
def remove(event):
    if event == None :
        print('remove: Invalid operation. Must enter event name ')
        return

    for e in eventsList:
        if e.get_name() == event:
            eventsList.remove(e)
            savefile = open(username+'.pkl', 'wb')
            pickle.dump(eventsList, savefile)
            savefile.close()
            
    
    
def edit(event, date, time):    
    if event == None :
        print('edit: Invalid operation. Must enter event name')
        return

    now = datetime.datetime.now()
    if date == None:
        date = []
        date.append(str(now.day)+'/'+str(now.month)+'/'+str(now.year))
    if time == None:
        time = []
        time.append(str(now.hour)+':'+str(now.minute))

    for e in eventsList:
        if e.get_name() == event:
            e.set_date(date)
            e.set_time(time)
            savefile = open(username+'.pkl', 'wb')
            pickle.dump(eventsList, savefile)
            savefile.close()
            
#or VIEW
def available(event, date, time):
    res = ''
    if event == None and date !=None:
        res = res + '-------------------Events with date '+date+':-----------------\n'
        for e in eventsList:
            if e.get_date() == date:       
                res = res +'----- '+ str(e.get_date()) +'----\n'
                res = res +' '+ e.get_name() +' '
                res = res +' ('+ str(e.get_time())+') '
                res = res +' -  '+ e.get_status()+'\n'
    
    elif event == None and time !=None:
        res = res + '-------------------Events with time '+time+':-----------------\n'
        for e in eventsList:
            if e.get_time() == time:
                res = res +'----- '+ str(e.get_date()) +'----\n'
                res = res +' '+ e.get_name() +' '
                res = res +' ('+ str(e.get_time())+') '
                res = res +' -  '+ e.get_status()+'\n'

    elif event == None :
        res = res + '-------------------All Events:-----------------\n'
        for e in eventsList:
            res = res +'----- '+ str(e.get_date()) +'----\n'
            res = res +' '+ e.get_name() +' '
            res = res +' ('+ str(e.get_time())+') '
            res = res +' - '+ e.get_status()+'\n'
    else:
        res = res + '-------------------Events with name '+event+':-----------------\n'
        for e in eventsList:
            if e.get_name() == event:
                res = res +'----- '+ str(e.get_date()) +'----\n'
                res = res +' '+ e.get_name() +' '
                res = res +' ('+ str(e.get_time())+') '
                res = res +' -  '+ e.get_status()+'\n'
                
    return res

    
def mark(event, status):
    if event == None :
        print('mark: Invalid operation. Must enter event name ')
        return

    if status == None:
        status = 'Done'

    for e in eventsList:
        if e.get_name() == event:
            e.set_status(status)
            savefile = open(username+'.pkl', 'wb')
            pickle.dump(eventsList, savefile)
            savefile.close()
            
            
        
     
