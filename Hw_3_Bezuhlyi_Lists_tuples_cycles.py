notes = []

while True:
    command = input("Enter a command (add, earliest, latest, longest, shortest, exit): ")

    if command == "add":
        note = input("Enter a note: ")
        notes.append(note)
        print("Note added.")

    elif command == "earliest":
        if len(notes) == 0:
            print("No notes to display.")
        else:
            notes.sort(key=lambda x: x.lower())
            print("Notes (oldest to newest):")
            for note in notes:
                print("- " + note)

    elif command == "latest":
        if len(notes) == 0:
            print("No notes to display.")
        else:
            notes.sort(key=lambda x: x.lower(), reverse=True)
            print("Notes (newest to oldest):")
            for note in notes:
                print("- " + note)

    elif command == "longest":
        if len(notes) == 0:
            print("No notes to display.")
        else:
            notes.sort(key=lambda x: len(x), reverse=True)
            print("Notes (longest to shortest):")
            for note in notes:
                print("- " + note)

    elif command == "shortest":
        if len(notes) == 0:
            print("No notes to display.")
        else:
            notes.sort(key=lambda x: len(x))
            print("Notes (shortest to longest):")
            for note in notes:
                print("- " + note)

    elif command == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid command.")




