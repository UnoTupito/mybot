import json


def save():
    with open('companies.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(comp_book, ensure_ascii=False))
    print('All changes saved')


def load():
    with open('companies.json', 'r', encoding='utf-8') as file:
        got_comp_book = json.load(file)
    return got_comp_book


def add_comp():
    name = (input('Enter company\'s name: ')).title()
    person = input('Enter contact persons\'s name: ')
    phone = input('Enter the phone number: ')
    result = input('Enter the negotiation\'s result: ')
    comp_book[name] = [person, phone, result]
    print('The following information is added:')
    print('Company: ' + name + '    info: ', end='')
    print(comp_book.get(name))
    print()


def show_companies():
    for x in comp_book.keys():
        print(x)


def del_company():
    done = False
    while not done:
        comp_del = (input("What company do you want to delete? Enter the name.\n")).title()
        if comp_del in comp_book.keys():
            comp_book.pop(comp_del)
            print('The company is now deleted from the list')
            done = True
        else:
            print('I didn\'t find this company. Try one more time? Enter \'No\' to cancel')
            answer = (input('')).title()
            if answer == 'No':
                done = True


def show_one():
    done = False
    while not done:
        comp_show = (input("What company do you want to see? Enter the name.\n")).title()
        if comp_show in comp_book.keys():
            print('Company: ' + comp_show + '    info: ', end='')
            print(comp_book.get(comp_show))
            done = True
        else:
            print('I didn\'t find this company. Try one more time? Enter \'No\' to cancel')
            answer = (input('')).title()
            if answer == 'No':
                done = True


def change_company():
    done = False
    while not done:
        comp_change = (input("What company do you want to change? Enter the name.\n")).title()
        if comp_change in comp_book.keys():
            finished = False
            while not finished:
                answers = ['1', '2', '3']
                print("What do you want to change?")
                print('1 - change contact person\'s name\n2 - change contact phone number\n3 - change negotiation result')
                change = input()
                if change in answers:
                    if change == '1':
                        print('Enter new name:')
                        comp_book[comp_change][int(change)-1] = input()
                    elif change == '2':
                        print('Enter new phone number:')
                        comp_book[comp_change][int(change)-1] = input()
                    else:
                        print('Enter new negotiation result:')
                        comp_book[comp_change][int(change)-1] = input()
                    print('The information changed successfully.')
                    print('Company: ' + comp_change + '    info: ', end='')
                    print(comp_book.get(comp_change))
                    finished = True
                else:
                    print('You should enter only 1, 2 or 3. Try one more time? Enter \'No\' to cancel')
                    answer = (input('')).title()
                    if answer == 'No':
                        finished = True
            done = True
        else:
            print('I didn\'t find this company. Try one more time? Enter \'No\' to cancel')
            answer = (input('')).title()
            if answer == 'No':
                done = True


com_list = \
    'Available commands:\n' \
    '/start\n'\
    '/add - add a new company\n'\
    '/change - change company info\n'\
    '/showall - show all companies\n' \
    '/showone - show information about a company\n' \
    '/del - delete a company from the list\n' \
    '/stop - stop the bot'

try:
    comp_book = load()
except:
    comp_book = \
        {
            'Apple': ['Tim Cook', '987234673', 'negotiations in progress'],
            'Meta': ['Mark Zukerberg', '973459823', 'agreed']
        }


while True:
    # print(com_list)
    com = input('What do you want to do?\nTo read available commands use /help\n')
    if com == '/start':
        print('Welcome!')
    elif com == '/add':
        print('Let\'s add a company')
        add_comp()
        save()
    elif com == '/change':
        change_company()
        save()
    elif com == '/showall':
        show_companies()
    elif com == '/showone':
        show_one()
    elif com == '/del':
        del_company()
        save()
    elif com == '/help':
        print(com_list)
    elif com == '/stop':
        print('Thank you for working with me. See you later!')
        break
    else:
        'I don\'t know this command, try one more time.'
