import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m
import

 \033[1;32m.  /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$       
 \033[1;34m. /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/| $$_____/| $$__  $$      
 \033[1;32m.| $$  \__/| $$  \ $$| $$$$  /$$$$| $$      | $$      | $$  \ $$      
 \033[1;34m.|  $$$$$$ | $$$$$$$$| $$ $$/$$ $$| $$$$$   | $$$$$   | $$$$$$$/      
 \033[1;32m. \____  $$| $$__  $$| $$  $$$| $$| $$__/   | $$__/   | $$__  $$      
 \033[1;34m. /$$  \ $$| $$  | $$| $$\  $ | $$| $$      | $$      | $$  \ $$      
 \033[1;32m.|  $$$$$$/| $$  | $$| $$ \/  | $$| $$$$$$$$| $$$$$$$$| $$  | $$      
 \033[1;34m. \______/ |__/  |__/|__/     |__/|________/|________/|__/  |__/      
                                                                   
 \033[1;32m. /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$                             
 \033[1;36m.| $$$ | $$ /$$__  $$| $$__  $$| $$_____/                             
 \033[1;32m.| $$$$| $$| $$  \__/| $$  \ $$| $$                                   
 \033[1;36m.| $$ $$ $$|  $$$$$$ | $$  | $$| $$$$$                                
 \033[1;32m.| $$  $$$$ \____  $$| $$  | $$| $$__/                                
 \033[1;36m.| $$\  $$$ /$$  \ $$| $$  | $$| $$                                   
 \033[1;32m.| $$ \  $$|  $$$$$$/| $$$$$$$/| $$$$$$$$                             
 \033[1;36m.|__/  \__/ \______/ |_______/ |________/                             
  ╔═══════════════════Note═══════════════════╗                 
  【𝐊𝐇𝐔𝐍𝐈 𝐊𝐀 𝐉𝐈𝐉𝐀 𝐀𝐍𝐈𝐋 𝐁𝐑𝐀𝐍𝐃】
  ╚══════════════════════════════════════════╝
\033[1;92m.Author    :  𝐊𝐇𝐔𝐍𝐈 𝐊𝐀 𝐉𝐈𝐉𝐀 𝐀𝐍𝐈𝐋 𝐈𝐍𝐒𝐈𝐃𝐄|
\033[1;31m.Brother  : 𝐀𝐍𝐈𝐋 𝐈𝐍𝐒𝐈𝐃𝐄 | 𝐀𝐘𝐀𝐍𝐒𝐇 𝐇𝐄𝐑𝐄   |
 \033[1;36mGithub    : 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐗𝐇𝐔𝐓 𝐊𝐎 𝐂𝐇𝐈𝐑𝐍𝐄 𝐖𝐀𝐋𝐀 𝐓𝐎𝐎𝐋     |
 \033[1;32m.Facebook  :𝐊𝐇𝐔𝐍𝐈 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐆𝐀𝐍𝐃 𝐊𝐈 𝐍𝐀𝐒 𝐅𝐀𝐃𝐍𝐄 𝐖𝐀𝐋𝐀 𝐀𝐍𝐈𝐋 𝐇𝐄𝐑𝐄
 \033[1;34mTool Name : 𝐒𝐀𝐈𝐌 𝐊 𝐀𝐋𝐋 𝐏𝐈𝐋𝐄 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐎 𝐗𝐇𝐎𝐃𝐍𝐄 𝐖𝐀𝐋𝐀 𝐀𝐒𝐇𝐈𝐐 𝐀𝐍𝐈𝐋   |
 \033[1;36mType type : 𝐊𝐇𝐔𝐍𝐈 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐎 𝐗𝐇𝐎𝐃𝐍𝐄 𝐊 𝐋𝐈𝐘𝐄 𝐅𝐑𝐄𝐄 𝐇𝐄 𝐓𝐎𝐎𝐋 |
  ───────────────────────────────────────────────────────
   𖣘︎𖣘︎𖣘︎𖣘︎𖣘︎︻╦デ╤━╼【★𝐀𝐍𝐈𝐋 𝐓𝐎𝐎𝐋 𝐎𝐖𝐍𝐀𝐑★】╾━╤デ╦︻𖣘︎𖣘︎𖣘︎𖣘︎𖣘︎
 ───────────────────────────────────────────────────────
\033[1;32m【𝐊𝐇𝐔𝐍𝐈 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐗𝐇𝐔𝐓 𝐌𝐄 𝐔𝐍𝐆𝐋𝐈 𝐃𝐀𝐋 𝐁𝐀𝐇𝐎𝐓 𝐓𝐄𝐉 𝐂𝐇𝐋𝐄𝐆𝐀】
 \033[1;36m       𖣘︎𖣘︎𖣘︎【𝐊𝐇𝐔𝐍𝐈 𝐊𝐀 𝐃𝐀𝐃 𝐀𝐍𝐈𝐋 𝐈𝐍𝐒𝐈𝐃𝐄】𖣘︎𖣘︎𖣘︎""" )

def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;32m[√]𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐗𝐇𝐔𝐓 𝐌𝐄 𝐏𝐔𝐑𝐀 𝐋𝐀𝐍𝐃 𝐂𝐇𝐋𝐀 𝐆𝐘𝐀】  {} of Convo\033[1;35m {} \033[1;33msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;32m  - Time: {}".format(current_time))
                else:
                    print("\033[1;32m[x] MESSEGE FAIL HO GYA BHOSDI KE TOKAN SAHI DAL  {} of Convo \033[1;34m{} with Token \033[1;36m{}: \n\033[1;36m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;33m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;35m[!] An error occurred: {}".format(e))
def main():	
    print(logo)   
    print(' \033[1;31m[•] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐃𝐃 𝐊𝐈 𝐗𝐇𝐔𝐓 𝐌𝐄 𝐓𝐎𝐎𝐊𝐄𝐍 𝐅𝐈𝐋𝐄 𝐃𝐀𝐋➼')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;36m[•] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐎 𝐊𝐇𝐀 𝐂𝐇𝐎𝐃𝐍𝐀 𝐈𝐃 𝐃𝐀𝐋➼ ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[•] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊 𝐒3 𝐍𝐈𝐊𝐀𝐋 𝐊𝐀𝐑 𝐅𝐈𝐋𝐄 𝐃𝐀𝐋 ➼')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[•] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊 𝐘𝐀𝐑𝐎 𝐊𝐀 𝐍𝐀𝐌𝐄 𝐃𝐀𝐋➼')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;34m[•] 𝐒𝐀𝐈𝐌 𝐊𝐈 𝐁𝐇𝐄𝐍 𝐊𝐎 𝐊𝐈𝐓𝐍𝐈 𝐒𝐏𝐄𝐄𝐃 𝐒𝐄 𝐂𝐇𝐎𝐃𝐍𝐀 𝐇𝐄➼' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()