# Telegram $FUN Token Auto Messenger Bot

This script automatically sends messages about the `$FUN` token to a Telegram group every 2–3 minutes using Telethon.

---

## 🔧 Features

- Real Telegram client login using `api_id` and `api_hash`
- Sends a unique message with:
  - At least **30 words**
  - At least **5–6 times `$FUN`**
- Auto-login session saved to `fun_session.session`
- No message duplicates in a single run

---

## ⚙️ Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/telegram-fun-token-auto-messenger.git
cd telegram-fun-token-auto-messenger
