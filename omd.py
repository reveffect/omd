# omd.py
# Anton Kulikov <antany.kulikov@gmail.com>

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
        "Но зонт спас положение — утка пришла сухой и взяла себе красное полусухое 🦆✨"
    )


def step2_no_umbrella():
    print(
        "Утка-маляр решила, что зонт ей ни к чему. "
        "Ливень шёл стеной 🌧️. "
        "Когда утка дошла до бара, все подумали, что она специально так сделала — "
        "оказывается, она просто покрасила себя водой 🎨🦆.
    )


if __name__ == '__main__':
    step1()
