# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.

import json
import datetime

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def list_notes():
    notes = load_notes()
    if notes:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело заметки: {note['body']}")
            print(f"Дата/время создания: {note['created_at']}")
            print(f"Дата/время последнего изменения: {note['updated_at']}")
            print('-' * 30)
    else:
        print("Нет заметок")

def add_note():
    notes = load_notes()
    note = {}
    note['id'] = len(notes) + 1
    note['title'] = input("Введите заголовок заметки: ")
    note['body'] = input("Введите тело заметки: ")
    now = datetime.datetime.now()
    note['created_at'] = now.strftime("%Y-%m-%d %H:%M:%S")
    note['updated_at'] = now.strftime("%Y-%m-%d %H:%M:%S")
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена")

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки, которую хотите изменить: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новое тело заметки: ")
            note['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка изменена")
            break
    else:
        print("Заметка не найдена")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена")
            break
    else:
        print("Заметка не найдена")

def menu():
    while True:
        print("\nМеню:")
        print("1. Список заметок")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        choice = input("Выберите пункт меню (1-5): ")
        if choice == '1':
            list_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Повторите попытку.")

menu()