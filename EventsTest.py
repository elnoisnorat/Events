import EventsTools
#TEST para nosotros.....   correr por secciones para q se pueda ver el cambio,
            #'comentar' los 'adds' despues de la primera vez

EventsTools.add('evento1', None, None)
EventsTools.add('evento2', '01/02/11', None)
EventsTools.add('evento3', '01/02/11', '00:12')
EventsTools.add(None, '01/02/11', '12:12')


#EventsTools.edit(None, None, None)
#EventsTools.edit('evento2', '00/00/00', None)
#EventsTools.edit('evento3', None, '12:12')
#EventsTools.edit(None, '01/02/11', '12:13')


#EventsTools.mark(None, None)
#EventsTools.mark('evento2', None)
#EventsTools.mark('evento3', 'terminado')
#EventsTools.mark('eventonuevo', 'nuevo')


#EventsTools.remove(None)
#EventsTools.remove('evento2')
#EventsTools.remove('eventoQueNoExiste')

ev = EventsTools.available(None, None, None)
print(ev)

#ev = EventsTools.available(None, None, '12:12')
#print(ev)
