import os
import re
import chardet
from typing import Optional
from colorama import Fore, Style, init, Back
import sys

class Colors:
    init(autoreset=True)
    HEADER = Fore.MAGENTA
    BG_HEADER = Style.BRIGHT + Back.BLACK
    BLUE = Fore.BLUE
    GREEN = Fore.GREEN
    WARNING = Fore.YELLOW
    YELLOW = Fore.YELLOW
    FAIL = Fore.RED
    WHITE = Fore.WHITE
    ENDC = Style.RESET_ALL

class SearchFile:
    def __init__(self, file_path: str, pattern: str, quiet: bool = False):
        self.file_path = file_path
        self.pattern = pattern
        self.quiet = quiet
        self.pattern_lower = pattern.lower()

    def _process_file(self) -> bool:
        try:
            with open(self.file_path, 'rb') as f:
                result = chardet.detect(f.read())
                encoding = result['encoding']

            with open(self.file_path, 'r', encoding=encoding) as f:
                content = f.read().lower()
                pattern_lower = self.pattern.lower()
                if pattern_lower in content:
                    lines = content.split('\n')
                    match_found = False
                    for i, line in enumerate(lines, start=1):
                        if pattern_lower in line:
                            if not match_found:
                                self._handle_text_result()
                                match_found = True
                            colored_line = line.replace(pattern_lower, f"{Colors.GREEN}{pattern_lower}{Colors.ENDC}")
                            self._print_result(i, colored_line)

                    return match_found  # Found a case-insensitive text match

        except (UnicodeDecodeError, LookupError):
            if self._search_binary_file():
                if not self.quiet:
                    print(f"{Colors.WARNING}Binary match found: {self.file_path}{Colors.ENDC}")
                return True
        return False

    def _handle_text_result(self) -> None:
        if not self.quiet:
            print(f"{Colors.YELLOW}Match found at: {Colors.BG_HEADER} {self.file_path}{Colors.ENDC}")

    def _search_binary_file(self) -> bool:
        if not self.quiet:
            with open(self.file_path, 'rb') as f:
                chunk = f.read(4096)
                while chunk:
                    if self.pattern.encode() in chunk:
                        return True
                    chunk = f.read(4096)
        return False

    def _print_result(self, line_number: int, line: str) -> None:
        colored_line = line.replace(self.pattern_lower, f"{Colors.BG_HEADER}{self.pattern_lower}{Colors.ENDC}")
        if not self.quiet:
            print(f"{Colors.HEADER}In line {line_number}:{Colors.ENDC}", colored_line)
        
class FileSearch:
    def __init__(self, quiet: bool = False):
        self.quiet = quiet

    def FindString(self, root_dir: str, pattern: str) -> bool:
        found_any = False  # Track if any matches are found
        for root, _, files in os.walk(root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                search_file = SearchFile(file_path, pattern, quiet=self.quiet)  # Pass quiet parameter here
                try:
                    if search_file._process_file():
                        found_any = True  # Set the flag to True if a match is found
                except (UnicodeDecodeError, PermissionError) as e:
                    print(f"Error processing {file_path}: {e}")

        return found_any  # Return the flag indicating whether any matches were found
