'''
EventsTools.py
'''
import pickle
import calendar 
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


username = ''
username = _raw_input('Enter a username: ')
with open('Users.txt') as usersfile:
    for e in usersfile:
        if username in e:#ok
            output = open(username+'.txt', 'r')
        else:#crea nuevo
            print('Crear nuevo....')


eventsList =  []
eventsList.append(eventsList)


pickle.dump(Events, output)
pickle.dump(eventsList, output)

output.close()

ev = Events()

def add(event, date, time):
    
    if event == None :
        event = 'Untitled event'
    if date == None:
        date = date.today() 
    
    if  calendar.weekday(date[0] + date[1], date[3] + date[4], date[6] +date[7]) != None:   #check if valid date? no se si funciona esto
        ev = Events(event, date, time, None)
        eventsList.append(ev)
    else:
        print('Invalid date')
   
   
    
def remove(event):
    if eventsList.__getattribute__(event) != None :
        eventsList.remove(event)
    else:
        print('Event is not in the list')
    
    
def edit(event, date, time):    
    eventsList.__getattribute__(event).set_date(date)
    eventsList.__getattribute__(event).set_time(time)

def view(event, date, time):
    res = ''
    if date != None:
        res = res +'----- '+ eventsList.__getattribute__(event).get_date() +' -----\n'
    if event != None :
        res = res + event
    if time != None:
        res = res +' ('+ eventsList.__getattribute__(event).get_time() +') '
    
    res = res +' - :'+ eventsList.__getattribute__(event).get_status()
    return res

    
def mark(event, status):
    eventsList.__getattribute__(event).set_status(status) 
    # or eventsList.__getattribute__(event).set_status('Done')
