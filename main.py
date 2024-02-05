import string, random, sys, os.path

def key_gen(length: int) -> str:
    letters = string.ascii_letters + string.digits
    key = (''.join(random.choice(letters) for _ in range(length)))
    return key

def check_key(key: str) -> str:
    # check if key in file
    with open('db.txt', 'r') as f:
        stuff = f.readlines()
    for part in stuff:
        file_key, file_url = part.strip('\n').split(' :: ')
        if key == file_key:
            return file_url
        else:
            return 
    
def write_to_file(key: str, url: str) -> None:
    with open('db.txt', 'a') as f:
        f.write(f'{key} | {url}\n')

def file_exists() -> None:
    if os.path.exists('./db.txt'):
        return
    else:
        create_file()
        print("New file created")

def create_file() -> None:
    with open('db.txt', 'x') as f:
        f.close()

if __name__ == "__main__":
    arg = sys.argv[1:]
    file_exists()
    if arg[0] == '-o':
        # url = check_key(key)
        print("nto ok")
    else:
        print("ok")