question = (input("Hello! I hope you are having a good day. Are you ready to get your horoscope?\n "))

if question == 'Yes' or question == 'yes':
    month = (input("Yay! What is your birth month?\n"))

    if month == "july" or "July" or "august" or "August":
        day = (input("What is your day of birth?\n"))

elif question == 'No' or question == 'no':
    print("Boo!")
