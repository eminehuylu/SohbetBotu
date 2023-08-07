def chatbot_response(user_input):
    greetings = ["merhaba", "selam", "hey", "naber"]
    goodbyes = ["görüşürüz", "hoşça kal", "bye", "iyi günler"]

    if user_input.lower() in greetings:
        return "Merhaba! Ben mini sohbet botu. Size nasıl yardımcı olabilirim?"

    if user_input.lower() in goodbyes:
        return "Görüşürüz! Başka bir zaman tekrar gelin."

    return "Üzgünüm, anlamadım. Daha fazla detay verir misiniz?"

def main():
    print("Mini Sohbet Botu - Çıkış yapmak için 'görüşürüz' yazın.")

    while True:
        user_input = input("Kullanıcı: ")
        if user_input.lower() == "görüşürüz":
            print("Sohbet botu: Görüşürüz! Başka bir zaman tekrar gelin.")
            break
        response = chatbot_response(user_input)
        print("Sohbet botu:", response)

if __name__ == "__main__":
    main()
