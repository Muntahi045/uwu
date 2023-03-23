import os
os.system("clear")

print("""\033[1;35m ──────────▄▄▄▄▄▄▄▄▄───────────
────────▄█████████████▄────────
█████──█████████████████──█████
▐████▌─▀███▄───────▄███▀─▐████▌
─█████▄──▀███▄───▄███▀──▄█████─
─▐██▀███▄──▀███▄███▀──▄███▀██▌─
──███▄▀███▄──▀███▀──▄███▀▄███──
──▐█▄▀█▄▀███─▄─▀─▄─███▀▄█▀▄█▌──
───███▄▀█▄██─██▄██─██▄█▀▄███───
────▀███▄▀██─█████─██▀▄███▀────
───█▄─▀█████─█████─█████▀─▄█───
───███────────███────────███───
───███▄────▄█─███─█▄────▄███───
───█████─▄███─███─███▄─█████───
───█████─████─███─████─█████───
───█████─████─███─████─█████───
───█████─████─███─████─█████───
───█████─████▄▄▄▄▄████─█████───
────▀███─█████████████─███▀────
──────▀█─███─▄▄▄▄▄─███─█▀──────
─────────▀█▌▐█████▌▐█▀─────────
────────────███████────────────
 
\033[1;31m             by @O7ZXZ   
             TEAM SECURITY
the Booster https://t.me/protection17
the Booster https://t.me/mosLord777

""")
print('\033[1;36m~~~')
print("\033[1;32m >> install  Termux: 1")


print('\033[1;36m~~~')
print("\033[0;31m >> install Nmap: 2 ")


print('\033[1;36m~~~')
print(" \033[0;35m >> install Sqlmap 3 ")

print('\033[1;36m~~~')
print("\033[1;36m >> install ledear_hacking: 4 ")

print('\033[1;36m~~~')
print("\033[0;33m >> install Zphisher: 5")

print('\033[1;36m~~~')
print("\033[0;35m >> install Metasploit: 6")


print('\033[1;36m~~~')
print( " \033[0;33m >> Red_hawk: 7")

print('\033[1;36m~~~')
print("\033[0;31m >> install Seeker: 8")


print('\033[1;36m~~~~~~~~~')
o = input("--->> ")

if o == '1' :
	os.system("  pkg update -y pkg upgrade -y pkg install python -y pkg install python2 -y pkg install python2-dev -y pkg install python3 -y pkg install java -y  pkg install fish -y pkg install ruby -y pkg install help -y pkg install git -y pkg install host -y pkg install php -y pkg install perl -y pkg install nmap -y pkg install bash -y pkg install clang -y pkg install nano -y pkg install w3m -y pkg install havij -y pkg install hydra -y pkg install figlet -y pkg install cowsay -y pkg install curl -y  pkg install tar -y pkg install zip -y pkg install unzip -y pkg install tor -y pkg install google -y  pkg install sudo -y  pkg install wget -y pkg install wireshark -y pkg install wgetrc -y  pkg install wcalc -y pkg install bmon -y pkg install vpn -y pkg install unrar -y pkg install toilet -y pkg install proot -y pkg install net-tools -y pkg install golang -ypkg install chroot -y termux-chroot -y pkg install macchanger -y pkg install openssl -y pkg install cmatrix -y pkg install openssh -y pkg install wireshark -y termux-setup-storage -y pkg install macchanger -y apt update && apt upgrade -y ")
	

elif o == '2' :
	os.system("pkg install nmap")
	
if o == '3' :
	os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
	
if o == '4'  :
	os.system("git clone https://github.com/Ledear-Hacker/LEDEAR_HACKING")	

elif o == '5' :
	os.system("git clone --depth=1 https://github.com/htr-tech/zphisher.git")	
			
	
if o == '6' :
	os.system("pkg install bacula-fd")
	os.system("pkg install openjdk-17")
	os.system("pkg install openssl")
	os.system("pkg install wget")
	os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
	os.system("chmod +x metasploit.sh")
	os.system("./metasploit.sh")
	os.system("msfconsole")

elif o == "7" :
	os.system("https://github.com/Tuhinshubhra/RED_HAWK")
	
if o == "8" :
	os.system("git clone https://github.com/thewhiteh4t/seeker.git")			

print("y/n")
i = input("\033[0;32mwant start agen: ")

if i == 'y' :
	os.system("python3 muntahi-install.py")

elif i == 'n' :
	os.system("cd")


else:
	print("\033[0;31merorre")