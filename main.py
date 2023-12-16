from conf import get_model_config
from conf.setup import INIT_PROMPT

chat = get_model_config().start_chat()
response = chat.send_message(INIT_PROMPT)
print(response.text)


def ask_question(prompt: str):
    response = chat.send_message(prompt)
    print(response.text)


def main():
    while True:
        user_input = input()

        if user_input.lower() == "stop":
            print("Existing NARVIS..")
            break

        # Do something with the input
        ask_question(user_input)


if __name__ == '__main__':
    main()
