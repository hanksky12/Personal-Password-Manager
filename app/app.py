from utils.file import File


def run():
    try:
        file = File()
        while True:
            command = input("\n\n請輸入新指令代號new command code：\n"
                            "1.=>insert\n"
                            "2.=>update\n"
                            "3.=>delete\n"
                            "4.=>reset_password\n"
                            "5.=>exit\n")
            if command == "1":
                file.insert()
            elif command == "2":
                file.update()
            elif command == "3":
                file.delete()
            elif command == "4":
                file.reset_password()
            elif command == "5":
                exit()
            else:
                print("Invalid command:", command)
    except IndexError:
        print("Please input command")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
