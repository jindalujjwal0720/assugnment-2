def main():
    print("\n🔮 Welcome to Ujjwal Jindal's Fortune Teller (21JE1003) 🔮\n")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print("\n✨ Your fortune: Good vibes ahead. Keep riding that wave, Ujjwal! ✨\n")
    elif mood == "sad":
        print("\n✨ Your fortune: The clouds will clear soon. Hang in there. ✨\n")
    elif mood == "neutral":
        print("\n✨ Your fortune: Still waters run deep. Something surprising is coming. ✨\n")
    else:
        print("\n😕 Hmm, I don’t know that mood. Try happy/sad/neutral.\n")

if __name__ == "__main__":
    main()
