from sophy import Slackbot

def main():
    # Example: map the current script runner to their Slack email
    user_email = input("Enter your email to identify yourself: ")

    try:
        bot = Slackbot(user_email)
        bot.notify("Hello! Your script just ran successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
