# omd.py
# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        "Утка-маляр взяла зонт ☂️ и гордо зашагала к бару. "
        "Дождь начался ровно в тот момент, когда она дошла до перекрёстка. "
        "Но зонт спас положение — утка пришла сухой и довольной 🦆✨"
    )


def step2_no_umbrella():
    print(
        "Утка-маляр решила, что зонт ей ни к чему. "
        "Первые пару шагов всё было прекрасно, "
        "но внезапно небо затянули тучи и пошёл ливень 🌧️. "
        "До бара утка добралась мокрая, но всё равно счастливая 🦆🍺"
    )


if __name__ == '__main__':
    step1()
