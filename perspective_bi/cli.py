import sys
from pathlib import Path
from .server import run_server

def main():
    if len(sys.argv) < 2:
        print("Usage: perspective-bi run <file.py>")
        sys.exit(1)
    
    command = sys.argv[1]
    if command == "run":
        if len(sys.argv) < 3:
            print("Error: Please specify a Python file to run")
            sys.exit(1)
        
        file_path = Path(sys.argv[2])
        if not file_path.exists():
            print(f"Error: File {file_path} does not exist")
            sys.exit(1)
            
        run_server(str(file_path))
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()