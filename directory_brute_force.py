import requests

def brute_force_directories(url, wordlist):
    with open(wordlist, 'r') as file:
        for word in file:
            word = word.strip()
            test_url = f"{url}/{word}/"
            response = requests.get(test_url)
            if response.status_code == 200:
                print(f"Found directory: {test_url}")

target_url = "http://example.com"
wordlist_path = "directories.txt"
brute_force_directories(target_url, wordlist_path)
