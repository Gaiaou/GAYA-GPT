import os
from services.api_services import APIServices
from dotenv import load_dotenv
from colorama import init, Fore, Style, Back
import time
from datetime import datetime
import textwrap

# Initialize colorama
init()

class GayaTerminal:
    def __init__(self):
        self.api = APIServices()

    def loading_animation(self):
        chars = "░▒▓█"
        for _ in range(2):
            for char in chars:
                print(f"\r{Fore.GREEN}[*] Establishing neural connection {char}", end="")
                time.sleep(0.2)
        print(f"\r{' ' * 50}\r", end="")

    def print_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        banner = f"""{Fore.CYAN}
         ██████╗  █████╗ ██╗ █████╗     ██████╗ ██████╗ ████████╗
        ██╔════╝ ██╔══██╗██║██╔══██╗    ██╔════╝ ██╔══██╗╚══██╔══╝
        ██║  ███╗███████║██║███████║    ██║  ███╗██████╔╝   ██║   
        ██║   ██║██╔══██║██║██╔══██║    ██║   ██║██╔═══╝    ██║   
        ╚██████╔╝██║  ██║██║██║  ██║    ╚██████╔╝██║        ██║   
         ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝        ╚═╝   
        {Style.RESET_ALL}"""
        
        print(banner)
        print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}║{Style.RESET_ALL}        {Fore.WHITE}GAYA - Advanced AI Intelligence System{Style.RESET_ALL}        {Fore.MAGENTA}║{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}Creator:{Style.RESET_ALL} @YOUNES")
        print(f"{Fore.YELLOW}Version:{Style.RESET_ALL} 1.0.0 | {Fore.MAGENTA}Codename:{Style.RESET_ALL} GAYA\n")
        self.print_menu()

    def print_menu(self):
        print(f"{Fore.MAGENTA}[*] Available Commands:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}├──[1]{Style.RESET_ALL} {Fore.WHITE}ask <question>{Style.RESET_ALL} - Engage with GAYA AI")
        print(f"{Fore.GREEN}├──[2]{Style.RESET_ALL} {Fore.WHITE}clear{Style.RESET_ALL} - Clear terminal")
        print(f"{Fore.GREEN}└──[3]{Style.RESET_ALL} {Fore.WHITE}exit{Style.RESET_ALL} - Terminate session")

    def format_hacker_response(self, response):
        now = datetime.now().strftime("%H:%M:%S")
        
        print(f"\n{Fore.MAGENTA}╔══════════════════════ GAYA RESPONSE ══════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}║ {Fore.GREEN}[TIME]{Style.RESET_ALL} {now}                                            {Fore.MAGENTA}║{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}║ {Fore.GREEN}[STATUS]{Style.RESET_ALL} Connection Secure | Encryption: Enabled        {Fore.MAGENTA}║{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}╠════════════════════════════════════════════════════════════╣{Style.RESET_ALL}")
        
        wrapper = textwrap.TextWrapper(width=60, break_long_words=False, replace_whitespace=False)
        lines = response.split('\n')
        
        for line in lines:
            if line.strip():
                wrapped = wrapper.wrap(line)
                for wrapped_line in wrapped:
                    print(f"{Fore.MAGENTA}║ {Style.RESET_ALL}{wrapped_line:<60}{Fore.MAGENTA}║{Style.RESET_ALL}")
            else:
                print(f"{Fore.MAGENTA}║ {' ' * 60}║{Style.RESET_ALL}")
        
        print(f"{Fore.MAGENTA}╠════════════════════════ SYSTEM INFO ═════════════════════════╣{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}║ {Fore.GREEN}[CPU]{Style.RESET_ALL} Neural Core | {Fore.GREEN}[MEM]{Style.RESET_ALL} 512TB Quantum Cache        {Fore.MAGENTA}║{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}╚════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")

    def run(self):
        self.print_banner()

        while True:
            try:
                command = input(f"\n{Fore.MAGENTA}┌──({Fore.RED}GAYA{Fore.MAGENTA}㉿{Fore.GREEN}AI{Fore.MAGENTA})-[{Fore.WHITE}~/core{Fore.MAGENTA}]\n└─{Style.BRIGHT}$ {Style.RESET_ALL}").strip()
                
                if command.lower() == 'exit':
                    print(f"\n{Fore.YELLOW}[!] Initiating shutdown sequence...")
                    time.sleep(0.5)
                    print(f"[!] Clearing quantum pathways...")
                    time.sleep(0.5)
                    print(f"[!] GAYA offline...{Style.RESET_ALL}")
                    break
                    
                if command.lower() == 'clear':
                    self.print_banner()
                    continue

                elif command.lower().startswith('ask '):
                    question = command[4:]
                    print(f"\n{Fore.MAGENTA}[*] Establishing quantum link...{Style.RESET_ALL}")
                    self.loading_animation()
                    response = self.api.mistral_query(question)
                    self.format_hacker_response(response)

                else:
                    print(f"\n{Fore.RED}[!] Invalid command. Check syntax and try again.{Style.RESET_ALL}")

            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}[!] Emergency shutdown initiated...{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"\n{Fore.RED}[!] Critical error: {str(e)}{Style.RESET_ALL}")

def main():
    load_dotenv()
    terminal = GayaTerminal()
    terminal.run()

if __name__ == "__main__":
    main()
    
