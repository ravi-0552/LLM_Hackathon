import os


LOG_FILE = "recommendation_log.txt"


def confirm_recommendation(recommendation):
    """
    Human-in-the-loop confirmation.

    Options:
    1. Accept
    2. Reject
    3. Regenerate

    Returns:
        "accept"
        "reject"
        "regenerate"
    """

    print("\n" + "=" * 70)
    print("🤖 AI Recommendation")
    print("=" * 70)
    print(recommendation)
    print("=" * 70)

    while True:

        print("\nChoose an option:")
        print("1. Accept Recommendation")
        print("2. Reject Recommendation")
        print("3. Regenerate Recommendation")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        # -----------------------------
        # Accept
        # -----------------------------

        if choice == "1":

            with open(LOG_FILE, "a", encoding="utf-8") as file:

                file.write("=" * 80 + "\n")
                file.write(recommendation)
                file.write("\n\n")

            print("\n✅ Recommendation saved successfully.\n")

            return "accept"

        # -----------------------------
        # Reject
        # -----------------------------

        elif choice == "2":

            print("\n❌ Recommendation discarded.\n")

            return "reject"

        # -----------------------------
        # Regenerate
        # -----------------------------

        elif choice == "3":

            print("\n🔄 Regenerating recommendation...\n")

            return "regenerate"

        else:

            print("\nInvalid choice. Please enter 1, 2 or 3.\n")