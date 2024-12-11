from os import system
import sys

arguments = sys.argv

# eftory {target_type} {target_output} {needed parameters ...} [optional parameters ...]
system("clear")
print("\33[1;33m", end="")
print(r"""

          _____                    _____                _____                   _______                   _____                _____          
         /\    \                  /\    \              /\    \                 /::\    \                 /\    \              |\    \         
        /::\    \                /::\    \            /::\    \               /::::\    \               /::\    \             |:\____\        
       /::::\    \              /::::\    \           \:::\    \             /::::::\    \             /::::\    \            |::|   |        
      /::::::\    \            /::::::\    \           \:::\    \           /::::::::\    \           /::::::\    \           |::|   |        
     /:::/\:::\    \          /:::/\:::\    \           \:::\    \         /:::/~~\:::\    \         /:::/\:::\    \          |::|   |        
    /:::/__\:::\    \        /:::/__\:::\    \           \:::\    \       /:::/    \:::\    \       /:::/__\:::\    \         |::|   |        
   /::::\   \:::\    \      /::::\   \:::\    \          /::::\    \     /:::/    / \:::\    \     /::::\   \:::\    \        |::|   |        
  /::::::\   \:::\    \    /::::::\   \:::\    \        /::::::\    \   /:::/____/   \:::\____\   /::::::\   \:::\    \       |::|___|______  
 /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \ |:::|    |     |:::|    | /:::/\:::\   \:::\____\      /::::::::\    \ 
/:::/__\:::\   \:::\____\/:::/  \:::\   \:::\____\    /:::/  \:::\____\|:::|____|     |:::|    |/:::/  \:::\   \:::|    |    /::::::::::\____\
\:::\   \:::\   \::/    /\::/    \:::\   \::/    /   /:::/    \::/    / \:::\    \   /:::/    / \::/   |::::\  /:::|____|   /:::/~~~~/~~      
 \:::\   \:::\   \/____/  \/____/ \:::\   \/____/   /:::/    / \/____/   \:::\    \ /:::/    /   \/____|:::::\/:::/    /   /:::/    /         
  \:::\   \:::\    \               \:::\    \      /:::/    /             \:::\    /:::/    /          |:::::::::/    /   /:::/    /          
   \:::\   \:::\____\               \:::\____\    /:::/    /               \:::\__/:::/    /           |::|\::::/    /   /:::/    /           
    \:::\   \::/    /                \::/    /    \::/    /                 \::::::::/    /            |::| \::/____/    \::/    /            
     \:::\   \/____/                  \/____/      \/____/                   \::::::/    /             |::|  ~|           \/____/             
      \:::\    \                                                              \::::/    /              |::|   |                               
       \:::\____\                                                              \::/____/               \::|   |                               
        \::/    /                                                               ~~                      \:|   |                               
         \/____/                                                                                         \|___|
""")

TARGET_TYPES = ["backdoor", "ransomware", "wifideauth", "dos"]
NEEDED_PARAMETERS = [
    [],
    []
]
OPTIONAL_PARAMETERS = [
    [],
    ["recursive"]
]

if len(arguments) == 1:
	print("WELCOME TO EFTORY!")
	print("Format to use eftory:")
	print("eftory {target_type} {target_os} {target_output} {needed options ..} [-o {optional options ..}]")
	exit(0)

target_type = arguments[1]
target_os = arguments[2]
target_output = arguments[3]
parameters = "|".join(arguments).split("-o")
needed_parameters = parameters[0].split("|")[4:] # ["eftory", "ransomware", "./makan.py", "", "-o", "--recursive"] -> [""]
optional_parameters = parameters[1].split("|") if len(parameters) > 1 else [] # ["eftory", "ransomware", "./makan.py", "", "-o", "--recursive"] -> ["--recursive"]

if target_type not in TARGET_TYPES:
	print(f"\33[1;31mSorry.. '{target_type}' target type doesn't recognized!")
	exit(0)

print(f"\33[1;37m", end="")
print(f"+---------------------------------+")
print(f"|             SUMMARY             |")
print(f"+----------------+----------------+")
print(f"|1. Target Type  |\33[1;31m {target_type:<15}\33[1;37m|")
print(f"+----------------+----------------|")
print(f"|2. Target OS    | ", end="")
print('\33[1;34m' if target_os == 'windows' else ('\33[1;32m' if target_os == 'linux' else ''), end=f"{target_os:<15}\33[1;37m|\n")
print(f"+----------------+----------------|")
print(f"|3. Target Output| {target_output:<15}|")
print(f"+----------------+----------------|")
number = 4
if len(needed_parameters) > 0:
    print(f"|4. Parameters   | {','.join(needed_parameters):>15}|")
    print(f"+----------------+----------------|")
    number += 1
if len(optional_parameters) > 0:
    print(f"{number}. Optional     | {','.join(optional_parameters):>15}")
    print(f"+----------------+----------------|")

if input("Do you want to continue? [y/n]") == 'y':
    if target_type == "ransomware":
        recursive = "--recursive" in optional_parameters
else:
    print("aight dude take your time! :)")
        