from telethon.sync import TelegramClient
import time
import random
from config import api_id, api_hash, phone_number, target_group

fun_facts = [
    "The $FUN token is revolutionizing the gaming industry with $FUN rewards and $FUN staking options.",
    "$FUN is the currency of choice for decentralized casinos. Use $FUN, earn $FUN, live $FUN!",
    "With $FUN, fast and secure blockchain gaming becomes a reality. HODL $FUN and play!",
    "Don't miss out on $FUN! The $FUN token is your gateway to decentralized entertainment.",
    "$FUN enables real-time transactions, community rewards, and seamless gaming. Bet with $FUN!",
    "Explore Web3 with $FUN — from gaming to DeFi, $FUN powers it all.",
    "$FUN is the ultimate gaming token. Use $FUN to play, stake, and earn across multiple platforms.",
    "More and more games are integrating $FUN every day. Join the $FUN movement now!",
    "Every time you play with $FUN, you're building the future of gaming. Earn, stake, and share $FUN.",
    "The $FUN token is all about speed, security, and gaming rewards. Stack your $FUN now!"
]

def generate_message():
    message = ' '.join(random.sample(fun_facts, 3))
    while message.count("$FUN") < 5 or len(message.split()) < 30:
        message += ' ' + random.choice(fun_facts)
    return message

def main():
    sent_messages = set()

    with TelegramClient('fun_session', api_id, api_hash) as client:
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            code = input("Enter the code received via Telegram: ")
            client.sign_in(phone_number, code)

        print(f"Logged in as {phone_number}. Sending messages to {target_group}...\n")

        while True:
            message = generate_message()
            if message not in sent_messages:
                try:
                    client.send_message(target_group, message)
                    print(f"[SENT] {message}\n")
                    sent_messages.add(message)
                except Exception as e:
                    print(f"[ERROR] Failed to send message: {e}")
            else:
                print("[SKIP] Duplicate message.")

            sleep_time = random.randint(120, 180)
            print(f"Sleeping for {sleep_time} seconds...\n")
            time.sleep(sleep_time)

if __name__ == "__main__":
    main()
