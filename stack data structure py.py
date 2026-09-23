#copy paste delete show_all_items delete_all clipboard paste_all



class stack():
    def __init__(self ):
        self.items = []

    def copy_text(self):
        text = input('write anything that you want to copy:\n')
        self.items.append(str(text))

        print(F'{self.items} HAS BEEN COPIED')

    def paste(self):
        if self.items :
            print(self.items[-1])
        else :
            print('nothing to copy')

    def delete(self):
        if not self.items:
            print('list is empty')
            return
        print('all your items that you copied :')
        for i , item in enumerate(self.items , 1):
            print(f'{i}. {item}')

        choice = input('which one you want to delete ? ')

        if not choice.isdigit():
            print('invalid input')
            return

        c = int(choice)
        if c < 1 or c > len(self.items):
            print('invalid number')
            return

        dlt = self.items.pop(c-1)
        print(f'item has been deleted : {dlt}')

    def show_all(self):
        if self.items :
            for i ,  itm in enumerate(self.items ,  1):
                print(f'{i}.{itm}')
        else : 
            print('no item in the list ')

    def delete_all(self):
        choice = input('you sure?[y/n] ').lower()
        if choice == 'y' :
            self.items.clear()
            print(f'all items are deleted ')
            return
        if choice == 'n' :
            return
        if choice != 'n' and choice != 'y' :
            print('ivalid ')
            return

    def paste_all (self):
        if not self.items :
            print('no item')
            return
        if self.items :
            print(*self.items, sep=', ')
            return

    def clipboard(self):
        if not self.items :
            print('nothing to show')
            return

        for i , item in enumerate(self.items , 1) :
            print(f'{i}. {item}')

        paste = input('\n which one you want to paste ?')
        
        if not paste.isdigit():
            print('invalid')
            return
        paste = int(paste)
        
        if paste < 1 or paste > len(self.items) :
            print('invalid')
            return
        
        print(self.items[paste-1])


clas = stack()

def answer_s (a , clas ):
    
    if a == 1 :
        clas.copy_text()
    elif a == 2:
        clas.paste()
    elif a == 3:
        clas.delete()
    elif a == 4:
        clas.show_all()
    elif a == 5:
        clas.delete_all()
    elif a == 6:
        clas.clipboard()
    elif a == 7:
        clas.paste_all()


while  True :
    print('what do you want to do ?\n \n1.copy\n2.paste\n3.delete\n4.show_all_items\n5.delete_all\n6.clipboardl\n7.paste_all\n8.exit')
    answer = int(input("answer : " ))
    if answer < 1 or answer > 8 :
        print('invalid')
        continue
    elif answer == 8 :
         print('the work has been finished')
         break
    else :
        answer_s(answer ,clas )
        
        
