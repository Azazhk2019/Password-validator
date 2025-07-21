while True:
        user_password = input("Enter your password (type 'exit' to quit): ")
        if user_password.lower() == "exit":
            print("Exiting...")
            break
        password_length = len(user_password)
        uppercase_characters = 0
        digit_count = 0
        has_space = False

        for chars in user_password:
            if chars.isupper():
                uppercase_characters = uppercase_characters +1
            if chars.isdigit():
                digit_count = digit_count + 1
            if chars == " ":
                has_space = True

        if password_length >=8 and uppercase_characters > 0 and digit_count > 0 and has_space == False:
            print("Password Accepted")
            break
        else:
            print("Password Rejected!")        


