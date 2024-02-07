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
        file_key, file_url = part.strip('\n').split(' | ')
        if key == file_key:
            return file_url
    return None
    
def check_url(url: str) -> str:
    # check if url in file
    with open('db.txt', 'r') as f:
        stuff = f.readlines()
    for part in stuff:
        file_key, file_url = part.strip('\n').split(" | ")
        if url == file_url:
            return file_key
    return None

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
    if len(arg) == 0:
        print("Incorrect Usage!\nun-shorten URL: main.py -o URL\nshorten URL:    main.py URL")
    elif arg[0] == '-o':
        # un-shorten URL
        if len(arg) == 1:
            print("No URL!")
        else:
            url = arg[1]
            key = check_key(url)
            if key == None:
                print("URL not in file")
            else:
                print(key)
    else:
        # shorten URL
        url = arg[0]
        test = check_url(url)
        if test != None:
            print(f"URL already exists:\n{test}")
        else:
            newkey = key_gen(10)
            write_to_file(newkey, url)
            print(f"URL shortened!\n{newkey}")