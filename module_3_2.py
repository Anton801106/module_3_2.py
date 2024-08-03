#"Способы вызова функции"


def send_email(message, recipient, *, sender = "university.help@gmail.com"):

    if not ('@' in recipient and '@' in sender) and recipient.endswith('.com', '.ru', '.net') and sender.endswith(('.com', '.ru', '.net')):
        print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    else:
        print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>")
        if sender != "university.help@gmail.com":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender = 'university.help@gmail.com')

