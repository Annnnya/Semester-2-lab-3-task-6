"""
simple notebook on python
"""

from datetime import date

class Note:
    """
    class for a single note in notebook
    """
    def __init__(self, memo='', tags=''):
        self.memo = memo
        self.tags = tags
        self.date = date.today()
    def match (self, search_filter: str):
        """
        checks if the note has tag by filter
        """
        if search_filter in self.tags:
            return True

class Notebook:
    """
    class for the notebook
    """
    def __init__(self):
        """
        creates empty notebook
        """
        self.notes = []
    def search(self, filtr:str) -> list:
        """
        searches notes by tags
        """
        res = []
        for note in self.notes:
            if note.match(filtr):
                res.append(note)
        return res
    def new_note(self, memo, tags=''):
        """
        creates new note in notebook
        """
        self.notes.append(Note(memo, tags))
    def modify_memo(self, note_id, memo):
        """
        modifies memo in the note
        """
        try:
            self.notes[note_id] = Note(memo, self.notes[note_id].tags)
            print('\nNote edited!\n')
        except IndexError:
            print('Wrong note id: memo with such id doesnt exist')
    def modify_tags(self, note_id, tags):
        """
        modifies tags in the note
        """
        try:
            self.notes[note_id] = Note(self.notes[note_id].memo, tags)
            print('\nNote edited!\n')
        except IndexError:
            print('Wrong note id: memo with such id doesnt exist')

class Menu:
    """
    class for object menu where everything happens
    """
    def __init__(self) -> None:
        """
        welcome message and notebook creation
        """
        print('''Welcome to the Notebook!

Type n or new note to create a note
Type em or edit memo to edit memo
Type et ot edit tags to edit tags
Type f or find to search the note by tags
Type sh or show to see your notes
Type exit to exit
Type h or help to see this message again
''')
        self.book = Notebook()
    def notebook_output(self, notes:list):
        """
        function for output of notes
        """
        for idx, note in enumerate(notes):
            print(f""" Note id: {idx}
 Memo:
{note.memo}
 Tags: {note.tags}
 Date of creation: {note.date}
""")
    def mainloop(self):
        """
        loop for work with the notebook
        """
        while True:
            action = input('>>> ')
            if action=='n' or action=='new note':
                print('Enter your memo (press enter twice to stop recording):\n')
                memo=''
                while True:
                    inp = input()
                    if inp != '':
                        memo = memo+inp+'\n'
                    else:
                        break
                memo = memo.strip()
                tags = input('Enter your tags:\n')
                self.book.new_note(memo, tags)
                print('\nNote saved!\n')
            elif action == 'em' or action == 'edit memo':
                idx = input('Enter memo id:\n')
                print('Enter your new memo (press enter twice to stop recording):\n')
                memo=''
                while True:
                    inp = input()
                    if inp != '':
                        memo = memo+inp+'\n'
                    else:
                        break
                memo.strip('\n')
                try:
                    self.book.modify_memo(int(idx), memo)
                except ValueError:
                    print('Id must be a number')
            elif action == 'et' or action == 'edit tags':
                idx = input('Enter memo id:\n')
                tag = input('Enter your new tags:\n')
                try:
                    self.book.modify_tags(int(idx), tag)
                except ValueError:
                    print('Id must be a number')
                except IndexError:
                    print('Wrong note id: memo with such id doesnt exist')
            elif action == 'f' or action == 'find':
                tags = input('Enter tag for search:\n')
                results = self.book.search(tags)
                if results != []:
                    print('Found notes:\n')
                    self.notebook_output(results)
                else:
                    print('No notes found :(')
            elif action == 'sh' or action == 'show':
                print('\nHere are your notes:\n')
                self.notebook_output(self.book.notes)
            elif action == 'exit':
                break
            elif action == 'h' or action == 'help':
                print("""
Type n or new note to create a note
Type em or edit memo to edit memo
Type et ot edit tags to edit tags
Type f or find to search the note by tags
Type sh or show to see your notes
Type exit to exit
""")
            else:
                print('Wrong input')

menu = Menu()
menu.mainloop()
