import random

def main():
    print("\n🔮 Welcome to Ujjwal Jindal's Fortune Teller (21JE1003) 🔮\n")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            "You're on a roll — don’t stop now!",
            "Good vibes ahead. Keep riding that wave, Ujjwal!"
        ],
        "sad": [
            "It's okay to not be okay. Brighter days are coming.",
            "The clouds will clear soon. Hang in there."
        ],
        "neutral": [
            "Still waters run deep. Something surprising is coming.",
            "No chaos = more clarity. Use this moment."
        ],
        "stressed": [
            "Breathe in. Breathe out. You've got this.",
            "Stress means you care. Don’t forget to care for yourself too, Ujjwal."
        ]
    }

    if mood in fortunes:
        message = random.choice(fortunes[mood])
        print(f"\n✨ Your fortune: {message} ✨\n")
    else:
        print("\n😕 Hmm, I don’t know that mood. Try happy/sad/neutral/stressed.\n")

if __name__ == "__main__":
    main()
