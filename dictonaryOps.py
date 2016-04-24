super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Pied Piper' : 'Thomas Peterson'}

print(super_villains['Fiddler'])

del super_villains['Fiddler']

print(super_villains)

super_villains['Pied Piper'] = 'Hartley Rathaway'

print(super_villains)

print(len(super_villains))

print(super_villains.get('Pied Piper'))

print(super_villains.keys())

print(super_villains.values())


#-----OUTPUT--------#
'''
Isaac Bowin
{'Pied Piper': 'Thomas Peterson', 'Captain Cold': 'Leonard Snart', 'Weather Wizard': 'Mark Mardon'}
{'Pied Piper': 'Hartley Rathaway', 'Captain Cold': 'Leonard Snart', 'Weather Wizard': 'Mark Mardon'}
3
Hartley Rathaway
dict_keys(['Pied Piper', 'Captain Cold', 'Weather Wizard'])
dict_values(['Hartley Rathaway', 'Leonard Snart', 'Mark Mardon'])
'''
