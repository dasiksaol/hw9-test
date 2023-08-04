from binary_con import binary_con
from pyfiglet import *
from art import *
from termcolor import colored
# pip install pyfiglet
# pip install termcolor
# pip install art

run = True
manual = False
loop = False
# font = [default, digital, isometric1]

# ascii_banner = figlet_format("Binary Conversion", font = "digital")
ascii_banner = figlet_format("Aupp")
print(colored((ascii_banner), "red"))
ascii_banner = figlet_format("Binary")
print(colored((ascii_banner), "green"))
ascii_banner = figlet_format("Conversion")
print(colored((ascii_banner), "blue"))
# print(FigletFont.getFonts())

# Art = text2art("101", font='block', chr_ignore=True) 
# print(Art)
print(colored("""
╔══════════════════════════════════════════════════════════════╗ 
║      ʕ•ᴥ•ʔ  Welcome to the Aupp Binary Converter  ʕ•ᴥ•ʔ      ║
╚══════════════════════════════════════════════════════════════╝""",'red', attrs=['bold', 'underline'], on_color='on_yellow'))
Tutorial = input("""Do you wish to read the tutorial? (y/n)
                    Input Here >>> """)

if Tutorial == "y":
    manual = True

while manual:
    
    ascii_banner = figlet_format("    User Manual")
    print(colored((ascii_banner), "green"))
    print(colored(""" 
╔══════════════════════════════════════════════════════════════╗ 
║                                                              ║
║         ༼ つ ◕_◕ ༽つ Operation (Opt):                        ║
║                                                              ║
║          - Input The Operation                               ║
║          - For Decimal to Binary, type (db)                  ║
║          - For Binary to Decimal, type (bd)                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
page 1/2""", "yellow"))

    input()
    print(colored(""" 
╔══════════════════════════════════════════════════════════════╗ 
║                                                              ║
║                ʕっ•ᴥ•ʔっ Number                              ║
║        - Input The Number You Want to Convert                ║
║        - Press Enter & Voila!!!                              ║
║       ** Please Only Input Number (Decimal/Binary)           ║                            
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
page 2/2""", "yellow"))

    print(colored(""" 
┬────────────────⇌••⇋────────────────┬
        Press Enter to Continue       
┴────────────────⇌••⇋────────────────┴
""",
"red"))
    input()
    break
    
while run:
    print("\n")
    print("Input Operation")
    opt = input("༼ つ ╹ ╹ ༽つ ")
    print("\n")
    if opt not in ["db", "bd"]:
        print(colored("100101010101001010010101111111010100101010000010101001010110010101", "red"))
        print(colored("100101010101001010010101000001010100101010000010101001010110010101", "red"))

        error = figlet_format(f"Error: Invalid Operator")
        print(colored(error, "red"))

        print(colored("100101010101001010010101111111010100101010000010101001010110010101", "red"))
        print(colored("100101010101001010010101000001010100101010000010101001010110010101", "red"))
    else:
        run = False
        print("Input Number You Wish to convert")
        value = input("༼ つ ╹ ╹ ༽つ ")
        print("\n")
        try: 
            int(value)
        except ValueError:
            print(colored("100101010101001010010101111111010100101010000010101001010110010101", "red"))
            print(colored("100101010101001010010101000001010100101010000010101001010110010101", "red"))

            error = figlet_format(f"Error: Invalid Input")
            print(colored(error, "red"))

            print(colored("100101010101001010010101111111010100101010000010101001010110010101", "red"))
            print(colored("100101010101001010010101000001010100101010000010101001010110010101", "red"))

        else:
            result = binary_con(opt, int(value))
            print("\n")
            print(colored("100101010101001010010101111111010100101010000010101001010110010101", "cyan"))
            print(colored("100101010101001010010101000001010100101010000010101001010110010101", "cyan"))

            
            ascii_banner = figlet_format(f"Opt = {str(opt)}")
            print(colored((ascii_banner), "green"))
            ascii_banner = figlet_format(f"Input = {str(value)}")
            print(colored((ascii_banner), "green"))
            ascii_banner = figlet_format(f"Result = {str(result)}")
            print(colored((ascii_banner), "green"))


            print(colored("100101010101001010010101001101010100101010000010101001010110010101", "cyan"))
            print(colored("100101010101001010010101000001010100101010000010101001010110010101", "cyan"))
        loop = True
        print(colored(""" 
┬────────────────⇌••⇋────────────────┬
        Press Enter to Continue       
┴────────────────⇌••⇋────────────────┴
""",
"red"))
    input()
    while loop:
        print("Restart APP? (y/n)")
        next = input("༼ つ ╹ ╹ ༽つ ")
        if next == "y":
            manual = False
            run = True
            break
        elif next == "n":
            manual = False
            thank = figlet_format("Thank You")
            print(thank)
            break
        else: 
            print("Please type y or n")
