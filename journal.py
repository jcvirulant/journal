from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    # content
    db.create('journal.db', safe=True)
    db.create_tables(Entry, safe=True)
    )
    # timestamp

    class Meta:
        database = db


menu = OrderedDict([
    ('a', add_entry)
])


def initialize():
    """Initialize the App"""


def menu_loop():
    """Show the menu"""


def add_entry():
    """Add an entry."""


def view_entries():
    """View previous entries."""
    print('d) delete entry')


    next_action = input('Action: [Nqd] ').lower().strip()
    if next_action == input()


def delete_entry(entry):
    """Delete an entry."""
    if input('Are you sure? [yN] ').lower() == 'y':
        entry.delete_instance()


if __name__ == '__main__':
    initialize()
    menu_loop()