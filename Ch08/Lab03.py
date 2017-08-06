def check_password(password: str) -> str:
    if len(password) < 8:
        return "invalid password"

    if not password.isalnum():
        return "invalid password"

    count = 0
    for i in range(len(password)):
        if password[i].isdigit():
            count += 1
            if count == 2:
                return "valid password"

    return "invalid password"


if __name__ == '__main__':
    password = "asasd89sdfsd43"
    print("'{0}' : {1}".format(password, check_password(password)))

    password = "asasd89"
    print("'{0}' : {1}".format(password, check_password(password)))

    password = "asasdsdfsd"
    print("'{0}' : {1}".format(password, check_password(password)))
