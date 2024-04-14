import Note

def write_note(array):
    file = open("Notes.csv", 'w', encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close


def read_note():
    try:
        array = []
        file = open("Notes.csv", "r+", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for i in notes:
            split_i = i.split(';')
            note = Note.Note(
                id = split_i[0], title = split_i[1], body = split_i[2], date = split_i[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array