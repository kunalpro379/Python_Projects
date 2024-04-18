import asyncio
import random
import sqlite3

# Function to connect users
async def connect_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    while True:
        cursor.execute("SELECT chat_id, gender FROM users WHERE connected_partner IS NULL")
        rows = cursor.fetchall()
        
        for chat_id, gender in rows:
            partner_gender = 'female' if gender == 'male' else 'male'
            cursor.execute("SELECT chat_id FROM users WHERE gender=? AND chat_id!=? AND connected_partner IS NULL ORDER BY RANDOM() LIMIT 1", (partner_gender, chat_id))
            partner = cursor.fetchone()
            if partner:
                partner_id = partner[0]
                cursor.execute("UPDATE users SET connected_partner=? WHERE chat_id=?", (partner_id, chat_id))
                cursor.execute("UPDATE users SET connected_partner=? WHERE chat_id=?", (chat_id, partner_id))
                conn.commit()
                print(f"Users {chat_id} and {partner_id} connected.")
            else:
                print(f"No match found for user {chat_id}.")
        
        await asyncio.sleep(1)

# Start the connection handler
async def main():
    await connect_users()

if __name__ == "__main__":
    asyncio.run(main())
