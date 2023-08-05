from binary_con import binary_con
from pyfiglet import *
import time
from termcolor import colored
from colorama import Fore
# pip install pyfiglet
# pip install termcolor
# pip install 

## clear screen function (flipping page)
def clear_screen():
    print("\033c", end="")
    
run = True
manual = False
loop = False
# font = [default, digital, isometric1]

## Logo
ascii_banner = figlet_format("Aupp")
print(colored((ascii_banner), "red"))
ascii_banner = figlet_format("Binary")
print(colored((ascii_banner), "green"))
ascii_banner = figlet_format("Conversion")
print(colored((ascii_banner), "blue"))
    # print(FigletFont.getFonts())

## Intro (Input to continue)
print(colored("""
╔══════════════════════════════════════════════════════════════╗ 
║      ʕ•ᴥ•ʔ  Welcome to the Aupp Binary Converter  ʕ•ᴥ•ʔ      ║
╚══════════════════════════════════════════════════════════════╝""",'red', attrs=['bold', 'underline'], on_color='on_yellow'))
Tutorial = input("""          Do you wish to read the tutorial? (y/n)
          Input Here >>> """)

if Tutorial == "y":
    manual = True

## if input "n" or anything else = no show manual 
## user manual / Tutorial (input/enter to continue/flip page) + (clear screen of intro)
while manual:
    clear_screen()
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
    print(colored(""" 
┬────────────────⇌••⇋────────────────┬
        Press Enter to Continue       
┴────────────────⇌••⇋────────────────┴
""",
"red"))
    input()
    clear_screen()
    ascii_banner = figlet_format("    User Manual")
    print(colored((ascii_banner), "green"))
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

## converter 
## clear screen after each conversion
## input/enter to continue

while run:
    clear_screen()
    converter = figlet_format("   Converter")
    print(colored((converter), "green"))
    print("\n")
    print(colored("Input Operation \n", "yellow", attrs= ["bold"]))
    opt = input("༼ つ ╹ ╹ ༽つ ")
    print("\n")
    if opt not in ["db", "bd"]:
        print(colored("100101010101001010010101111111010100101010000010101001010110010101", "red"))
        print(colored("100101010101001010010101000001010100101010000010101001010110010101", "red"))

        error = figlet_format(f"Error: Invalid Operator")
        print(colored(error, "red"))

        print(colored("100101010101001010010101111111010100101010000010101001010110010101", "red"))
        print(colored("100101010101001010010101000001010100101010000010101001010110010101", "red"))
        print(colored(""" 
┬────────────────⇌••⇋────────────────┬
        Press Enter to Continue       
┴────────────────⇌••⇋────────────────┴
""",
"cyan"))
        input()
        loop = False
    else:
        run = False
        print(colored("Input Number You Wish to convert \n", "yellow", attrs= ["bold"]))
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
            print(colored(""" 
┬────────────────⇌••⇋────────────────┬
        Press Enter to Continue       
┴────────────────⇌••⇋────────────────┴
""",
"cyan"))
            input()
            run = True
            loop = False

        else:
            result = binary_con(opt, int(value))
            print("\n")
            if result == "Error: Invalid Number":
                print(colored("100101010101001010010101111111010100101010000010101001010110010101", "red"))
                print(colored("100101010101001010010101000001010100101010000010101001010110010101", "red"))

                error = figlet_format("Error: Invalid Number")
                print(colored(error, "red"))

                print(colored("100101010101001010010101111111010100101010000010101001010110010101", "red"))
                print(colored("100101010101001010010101000001010100101010000010101001010110010101", "red"))
                print(colored(""" 
    ┬────────────────⇌••⇋────────────────┬
            Press Enter to Continue       
    ┴────────────────⇌••⇋────────────────┴
    """,
    "cyan"))
                input()
                run = True
                loop = False
            else: 
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
            
                print(colored(""" 
        ┬────────────────⇌••⇋────────────────┬
                Press Enter to Continue       
        ┴────────────────⇌••⇋────────────────┴
        """,
        "red"))
                input()
                loop = True

    while loop:
        print(colored("Restart APP? (y/n) \n", "yellow", attrs= ["bold"]))
        next = input("༼ つ ╹ ╹ ༽つ ")
        if next == "y":
            clear_screen()
            manual = False
            run = True
            break
        elif next == "n":
            clear_screen()
            manual = False
        
            bye = figlet_format("Thank You")
            penguin = """
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡛⠇⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⣀⡜⡇
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⡿⠟⠛⣷⠇
⠀⠀⠀⠀⣠⣶⣿⠿⠻⢿⣿⣿⣿⠷⢤⡀⠀⠀⢸⠉⠁⠰⡹⠀
⠀⠀⠀⣼⣿⡟⠀⠀⠀⠀⠙⣿⠃⠀⠀⠱⡄⢀⡇⠀⠀⣦⠇⠀
⠀⠀⢰⣿⣿⠀⠰⠾⠷⠠⣴⣟⣲⠔⠿⠓⢳⡼⠀⠀⢰⡸⠀⠀
⠀⠀⣸⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣶⡦⠃⠀⠀
⠀⠀⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡯⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀
⢠⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀
⠈⠿⣿⣿⣿⣿⣿⣄⣀⡀⠀⠀⠀⠀⠀⣀⣾⡛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠛⠿⠥⢄⡬⠵⠐⠒⠂⠉⠋⠉⠁⠀⠀⠀⠀⠀⠀
            """
            y_axis = 0
            direction = 1
            for i in range(40):
                clear_screen()
                print('\n' * y_axis + Fore.GREEN + bye + penguin)
                time.sleep(0.09)
                y_axis += direction
                if y_axis == 0 or y_axis == 10:
                    direction *= -1
            break
        else: 
            print("Please type y or n")
