def to_do_list():
    print('Welcome to To-Do App 💓\n')

    tasks = []

    while True:
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Remove Task')
        print('4. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter a task to add: ')
            tasks.append(task)

        elif choice == "2":
            print('\nTasks: ')

            if not tasks:
                print('No tasks yet. 👀')
            else:
                for index,task in enumerate(tasks,start=1):
                    print(index,task)

        elif choice =='3':
            num = int(input('Enter the task number to remove: '))

            if 1<=num <=len(tasks):
                tasks.pop(num-1)
                print('Task removed ✅')
            else:
                print('INVALID TASK NUMBER! 👎')

        elif choice =="4":
            break

        else:
            print('INVALID CHOICE. 🔴')
            print('\n')

to_do_list()