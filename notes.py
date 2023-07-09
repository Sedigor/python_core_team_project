from datetime import datetime
import os
import pickle



def open_notes():
    file_name = 'Notes.bin'
    if os.path.exists(file_name):
        with open(file_name, "rb") as fh:
            notes = pickle.load(fh)
    else:
        notes = {}
    return notes

def serch_max_id(notes):
    max_id = 0
    for i in notes:
        if i > max_id:
            max_id = i
    return max_id

def write_notes(notes):
    file_name = 'Notes.bin'
    with open(file_name, "wb") as fh:
        pickle.dump(notes, fh)


def new_record():
    notes = open_notes()
    max_id = serch_max_id(notes)
    print('Введіть текст:')
    text = input()

    if len(text)<2:
        return

    print('Ключеве слово:') 
    tag = input()
    rec = [datetime.now(), text]
    if len(tag)>0:
   
        rec.append(tag)
    max_id += 1

    notes.update({max_id:rec})
    write_notes(notes)
    print('Запис внесено.\n')


    
def print_records(notes, n_notes = 3, num_record=0 ):
    print('\n\n\n')
    n=n_notes
    if num_record > 0:
        notes = {num_record: notes[num_record]}
    for id, text in notes.items():
        if n == 0:
            print('\nНатисніть <Enter> для продовження')
            input()
            n = n_notes
        len_id = len(str(id))
        print(f"Запис {id} від {text[0].strftime('%d.%m.%Y, %M:%I')}"+'-'*(50-len_id))
        print(text[1])
        if len(text)>2:
            tag = 'Ключове слово: '+ text[2]
            print(' '*(78 - len(tag)) + tag)
        print()
        n -= 1
 
        

    
    

def view_records():
    notes = open_notes()
    print_records(notes)


def search_record():
    notes = open_notes()
    search_notes = {}
    search_text = input('Введіть фразу для пошуку:')
    for id, text in notes.items():
        if search_text in notes[id][1]:
            search_notes.update({id:notes[id]})
    if search_notes:
        print_records(search_notes)
    else:
        print( '\n Запис із такою фразою не знайдено. \n')


def search_tag():
    notes = open_notes()
    search_notes = {}
    search_text = input('Введіть ключеве слово для пошуку:')
    for id, text in notes.items():
        if len(notes[id]) > 2 and search_text in notes[id][2]:
            search_notes.update({id:notes[id]})
    if search_notes:
        print_records(search_notes)
    else:
        print( '\n Запис із таким ключевим словом не знайдено. \n')

def edit_record():
    notes = open_notes()
    id_edit = input('Введіть номер запису для редагування:')
    try:
        id_edit = int(id_edit)
    except:
        print(f'\n{id_edit} не є номером запису!\n')
        return
    try:
        notes[id_edit]
    except:
        print( '\n Запис із таким номером не знайдено. \n')
        return
    search_notes = {id_edit:notes[id_edit]}
    print_records(search_notes)

    print('Введіть новий текст:')
    text = input()    

    if len(text)<2:
        return

    print('Ключеве слово:') 
    tag = input()
    rec = [datetime.now(), text]
    if len(tag)>0:
         rec.append(tag)

    notes[id_edit] = rec
    write_notes(notes)
    print('Зміни внесено.\n')

def remuve_record():
    notes = open_notes()
    id_edit = input('Введіть номер запису для видалення:')
    try:
        id_edit = int(id_edit)
    except:
        print(f'\n{id_edit} не є номером запису!\n')
        return
    try:
        notes[id_edit]
    except:
        print( '\n Запис із таким номером не знайдено. \n')
        return
       
    search_notes = {id_edit:notes[id_edit]}
    print_records(search_notes)
    k = input('Видалити поточний запис? (<Т> Так / інше - Ні?)')
    if k == 'т' or k == 'Т' or k == 'n' or k ==  'N':
        notes.pop(id_edit)
        write_notes(notes)
        print('Запис видалено.\n')
   
        






if __name__ == "__main__":

    notes = {}
    max_nunber = 1
    file_name = 'Notes.bin'




    while True:
        print("Робота із нотатками:")
        print("<Н> - новий запис, <З> - перегляд всіх записів, <П> - пошук в записах, <Т> - пошук за ключевим словом,")
        choice = input( "<Р> - редагувати запис, <В> - видалити запис, інше - вихід.")
        if choice == 'н' or choice == 'Н' or choice == 'y' or choice == 'Y':
            new_record()
        elif choice == 'з' or choice == 'З'  or choice == 'p' or choice == 'P':
            view_records()
        elif choice == 'п' or choice == 'П' or choice == 'g' or choice == 'G':
            search_record()
        elif choice == 'т' or choice == 'Т' or choice == 'n' or choice == 'N':
            search_tag()
        elif choice == 'р' or choice == 'Р' or choice == 'H' or choice == 'h':
            edit_record()
        elif choice == 'в' or choice == 'В' or choice == 'd' or choice == 'D':
            remuve_record()
        else:
            
            break









