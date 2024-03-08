from search import search
from colorama import Fore, Style, init, Back
import sys
import os
import getpass

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


def main():
    search_pattern: Optional[str] = None
    root_directory: Optional[str] = None
    quiet: bool = False
    user = getpass.getuser()

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg.startswith("--text="):
            search_pattern = arg.split("=")[1]
        elif arg == "--text":
            i += 1
            if i < len(sys.argv):
                search_pattern = sys.argv[i]
            else:
                raise RuntimeError("Text cannot be empty")
        elif arg.startswith("--indir="):
            root_directory = arg.split("=")[1]
        elif arg == "--indir":
            i += 1
            if i < len(sys.argv):
                root_directory = sys.argv[i]
            else:
                raise RuntimeError("Directory cannot be empty")
        elif arg == "--quiet":
            quiet = True

        i += 1

    try:
        if root_directory and search_pattern:
            file_search = search.FileSearch(quiet=quiet)
            if os.path.isdir(root_directory):
                result = file_search.FindString(root_directory, search_pattern)
            elif os.path.isfile(root_directory):
                result = search.SearchFile(root_directory, search_pattern, quiet=quiet)._process_file()
            else:
                print(f"{Colors.FAIL}Error:{Colors.ENDC} '{root_directory}' is not a valid file or directory.")

            try:
                if result:  # Check the result of the search
                    sys.exit(0)
                else:
                    sys.exit(1)
            except NameError:
                print("Something went wrong.")
        else:
            print(f"Usage: python search-utils --indir=<directory> --text=<search_pattern> [--quiet]")
    except KeyboardInterrupt:
        print(f"{Colors.WARNING}Search interrupted by {user}!{Colors.ENDC}")

if __name__ == "__main__":
    
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Colors.WARNING}Search interrupted by {user}!{Colors.ENDC}")