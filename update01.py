import pandas as pd
import webbrowser
import time
import sys

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\rOpening in {i} seconds...")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rOpening now!          \n")
    sys.stdout.flush()

def open_links_in_sets(links, num_links_to_open):
    for link in links[:num_links_to_open]:
        countdown_timer(10)  # Countdown for 10 seconds before each link opens
        webbrowser.open(link)

def get_num_links():
    while True:
        try:
            num = int(input("How many links do you want to open?: "))
            if num > 0:
                return num
            else:
                print("Please enter a valid number (greater than 0).")
        except ValueError:
            print("Please enter a valid number.")

print("Instagram Unfollowing Code ---JETROCK HACKS--- \n")

filename = input('Enter your Excel File Name: ')

df = pd.read_excel(f'Json_files/{filename}.xlsx')

username_column = 'username'
df['insta_url'] = 'https://www.instagram.com/' + df[username_column]

links_to_open = df['insta_url'].tolist()

step = 50
start = 0

while True:
    open_more = input("Do you want to open more links? (yes/no): ").lower()
    if open_more == 'yes':
        num_links = get_num_links()
        links_subset = links_to_open[start:start + step]
        open_links_in_sets(links_subset, num_links)
        start += step
    else:
        break
