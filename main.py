from datetime import datetime


class Pet:
    '''
    pets have behaviors and attributes
    '''
    name = ''
    voice = ''
    interests = ()
    relationships = ()
    location = 0
    mental_state = 0
    current_action = ()

    names = (
        'Blep', 'Heart Snake', 'Hissy Snake', 'Yoshi', 'Arbok',
        'Ekans', 'Visaj', 'Testudo', 'Guard Snake',
        'British Snake', 'Snake', 'Hissy', 'Teeny Slither',
        'Slither Buddy', 'Cane Snake'
    )

    voices = {
        'English' : 1,
        'onomatopea' : 2,
        'Pokemon' : 3,
    }

    interests = (
        'security', 'music', 'technology', 'dance', 'sports',
        'personal hygiene'
    )

    ''' relationships
    blep and heart snake are dating
    blep and british snake are cousins
    teeny slither is slither buddy's child
    '''

    locations = (
        'Albany', 'Halfmoon', 'Great Britian', 'Brooklyn'
    )