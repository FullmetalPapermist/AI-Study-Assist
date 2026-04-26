def summarise_notes(query_engine):
    print("\nHow would you like the summary?")
    print("1. Short summary")
    print("2. Bullet points")
    print("3. Detailed explanation")

    choice = input("Choose: ")

    if choice == "1":
        prompt = "Summarise the notes in 3 concise sentences."
    elif choice == "2":
        prompt = "Summarise the notes in 5 clear bullet points."
    elif choice == "3":
        prompt = "Provide a detailed but clear summary of the notes."
    else:
        print("Invalid choice.")
        return

    try:
        print("querying engine...")
        response = query_engine.query(prompt)
        print("\nSummary:\n", response)
    except Exception as e:
        print("Error generating summary:", e)