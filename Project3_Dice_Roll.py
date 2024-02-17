import random
from colorama import Fore


x = [f"{Fore.RED}1", f"{Fore.BLUE}2", f"{Fore.RED}3", f"{Fore.BLUE}4", f"{Fore.RED}5", f"{Fore.BLUE}6"]
y = int(input("Baraye tas andakhtan adade 1 ra wared konid: "))
if y == 1:
    random = random.choice(x)
    print(random)
