
# SQL Injection Testing app

This app tests a given URL for SQL injection vulnerabilities. It uses a list of common SQL injection payloads to inject into the URL and checks if the response contains any SQL errors or vulnerabilities.

## Disclaimer

This app is for educational and ethical purposes only. The author assumes no responsibility for any misuse or damage caused by this app. Use responsibly and with proper authorization.

## Usage

1. Make sure you have Python installed on your system.
2. Install the required dependencies by running the following command:
   ```
   pip install requests
   ```
3. Run the app by passing the URL as an argument:
   ```
   python app.py "http://example.com/vulnerable_page.php?id="
   ```

## Example

```bash
python app.py "http://example.com/vulnerable_page.php?id="
```

The app will test the provided URL for SQL injection and print the result.

## Note

This app is a basic example and may not cover all possible SQL injection scenarios. It's important to use it responsibly and with proper authorization.


Remember to replace `"http://example.com/vulnerable_page.php?id="` with the actual URL you want to test.