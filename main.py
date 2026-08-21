import sys
from pathlib import Path
from colorama import Fore, Style
from config import OUTPUT_FOLDER_NAME
from detector import is_audio_file
from converter import convert_audio
import ui

def process_folder(source_folder: Path, target_format):
    ui.show_header()
    output_folder = source_folder / OUTPUT_FOLDER_NAME
    output_folder.mkdir(exist_ok=True)

    print(Fore.YELLOW + f"Scanning folder: {source_folder}\n" + Style.RESET_ALL)
    
    all_files = [f for f in source_folder.iterdir() if f.is_file()]
    audio_files = []
    
    print("Detecting audio files...")
    for f in all_files:
        if is_audio_file(f):
            audio_files.append(f)

    if not audio_files:
        print(Fore.RED + "\nNo supported audio files found in the selected folder.")
        print("\nPress Enter to continue...")
        input()
        return

    ui.show_header()
    print(Fore.CYAN + f"Converting to {target_format.name}...")
    print("────────────────────────────────────")

    converted_count = 0
    skipped_count = 0
    failed_count = 0

    for file_path in audio_files:
        if file_path.suffix.lower().lstrip(".") == target_format.extension.lower():
            ui.render_result(file_path.name, f"{file_path.stem}.{target_format.extension}", "SKIPPED", "Already target format")
            skipped_count += 1
            continue

        success, msg, dest_path = convert_audio(file_path, output_folder, target_format)
        
        if success:
            converted_count += 1
            ui.render_result(file_path.name, dest_path.name, "SUCCESS")
        else:
            failed_count += 1
            ui.render_result(file_path.name, f"{file_path.stem}.{target_format.extension}", "FAILED", msg)

    print("────────────────────────────────────")
    print(Fore.GREEN + Style.BRIGHT + "Conversion complete!")
    print(f"\n{Fore.GREEN}{converted_count} converted{Style.RESET_ALL} | "
          f"{Fore.YELLOW}{skipped_count} skipped{Style.RESET_ALL} | "
          f"{Fore.RED}{failed_count} failed{Style.RESET_ALL}\n")

    print("Press Enter to return to main menu...")
    input()

def main():
    while True:
        target_format = ui.select_format()
        if not target_format:
            print(Fore.CYAN + "\nGoodbye!")
            sys.exit(0)

        source_folder = ui.prompt_source_folder()
        if source_folder:
            process_folder(source_folder, target_format)

if __name__ == "__main__":
    main()