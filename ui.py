import os
from pathlib import Path
from typing import Optional
from InquirerPy import inquirer
from colorama import init, Fore, Style
from config import SUPPORTED_FORMATS, FormatSpec
import warnings
warnings.filterwarnings("ignore")

import sys
from pathlib import Path

init(autoreset=True)

def show_header():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + Style.BRIGHT + "====================================")
    print(Fore.CYAN + Style.BRIGHT + "           Katt-Converter           ")
    print(Fore.CYAN + Style.BRIGHT + "====================================" + Style.RESET_ALL)

def select_format() -> Optional[FormatSpec]:
    show_header()
    choices = [spec.name for spec in SUPPORTED_FORMATS.values()]
    choices.append("Exit")
    
    selection = inquirer.select(
        message="Select target output format (Use ↑/↓ arrows & Enter):",
        choices=choices,
        pointer=">"
    ).execute()

    if selection == "Exit":
        return None
    
    for spec in SUPPORTED_FORMATS.values():
        if spec.name == selection:
            return spec
            
    return None

def prompt_source_folder() -> Optional[Path]:
    while True:
        show_header()
        path_str = inquirer.text(
            message="Enter the source folder path (or press Enter to go back):"
        ).execute().strip().strip('"')

        if not path_str:
            return None

        path = Path(path_str)
        if path.exists() and path.is_dir():
            return path
        
        print(Fore.RED + "\n[!] Invalid directory. Press Enter to retry.")
        input()

def render_result(filename: str, target_name: str, status: str, detail: str = ""):
    if status == "SUCCESS":
        mark = Fore.GREEN + "✓" + Style.RESET_ALL
        print(f" {mark} {filename} → {target_name}")
    elif status == "SKIPPED":
        mark = Fore.YELLOW + "↷" + Style.RESET_ALL
        print(f" {mark} {filename} → SKIPPED ({detail})")
    else:
        mark = Fore.RED + "✗" + Style.RESET_ALL
        print(f" {mark} {filename} → FAILED ({detail})")