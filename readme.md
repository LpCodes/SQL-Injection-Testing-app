# ⚠️ SQL Injection Testing Tool

This tool is designed to test a given URL for SQL injection vulnerabilities. It uses a list of common SQL injection payloads to inject into the URL and checks if the response contains any SQL errors or vulnerabilities. The tool is intended for educational purposes and ethical security testing.

## 📝 Disclaimer

This tool is intended for **educational purposes and ethical security testing only**. Do not use it to attack websites without proper authorization. Unauthorized testing may violate local laws and could result in legal consequences. The author assumes no responsibility for any misuse or damage caused by this tool. Use responsibly and with proper authorization.

---

## 🚀 Features

- Tests for SQL injection vulnerabilities using a comprehensive list of payloads.
- Detects common SQL error messages in responses.
- Supports customizable timeout and delay between requests.
- Verbose mode for detailed debugging output.
- Randomized User-Agent headers to avoid detection.
- Interactive mode to pause and continue testing.

---

## 🛠️ Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required dependencies by running the following command:
   ```bash
   pip install requests
   ```

---

## 🖥️ Usage

Run the tool by passing the target URL as an argument. Additional options are available for customization.

### Basic Usage
```bash
python app.py "http://example.com/vulnerable_page.php?id="
```

### Advanced Usage
```bash
python app.py "http://example.com/vulnerable_page.php?id=" --timeout 10 --delay 1 --verbose
```

### Command-Line Options
| Option          | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `url`           | The target URL to test for SQL injection vulnerabilities.                   |
| `-t`, `--timeout`| Request timeout in seconds (default: 5).                                   |
| `-d`, `--delay`  | Delay between requests in seconds (default: 0.5).                          |
| `-v`, `--verbose`| Enable verbose output for detailed debugging.                              |

---

## 💻 Example

### Testing a URL
```bash
python app.py "http://example.com/vulnerable_page.php?id="
```

### Output
```
2023-10-15 12:34:56,789 - INFO - Testing payload: ' OR 1=1--
2023-10-15 12:34:57,123 - WARNING - Vulnerable to SQL injection with payload: ' OR 1=1--
Continue testing? (y/n): y
2023-10-15 12:34:57,456 - INFO - Testing payload: ' OR '1'='1
2023-10-15 12:34:57,789 - INFO - No vulnerabilities detected.
```

---

## ⚠️ Notes

- This tool is a **basic example** and may not cover all possible SQL injection scenarios. It is important to use it responsibly and with proper authorization.
- Always replace `"http://example.com/vulnerable_page.php?id="` with the actual URL you want to test.
- Be cautious when testing production systems. Use this tool only in environments where you have explicit permission to conduct security testing.

---

## 🤝 Contributing

Contributions are welcome! If you would like to contribute to this repository, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and ensure they are well-documented and thoroughly tested.
4. Submit a pull request with a clear description of your changes.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by various open-source security tools and educational resources.


