# Mailcsv

This project uses Python to send personalized emails from a CSV file with Name and Email columns using the Mailgun API.

## Prerequisites

Before running the program, make sure you have the following:

1. **Kali Linux** (or any Linux-based system) not tested in windows or mac
2. **Python 3.x** installed
3. A **Mailgun account**:
   - Sign up for a free Mailgun account at https://www.mailgun.com/.
   - Create a domain and get your Mailgun API key and domain.
4. A **CSV file** containing two columns: `Name` and `Email`.

### Example CSV format:

```csv
Name,Email
```

## Setting up the environment

1. Clone this repository or copy the `email.py` script to your system.
2. Install the necessary Python dependencies by running:

   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install requests
   ```

3. Create a CSV file (e.g., `emails.csv`) in the same directory with the following structure:

```csv
Name,Email
Name,name@example.com
```

## Usage

1. Open the `email.py` script and replace the following placeholders:
   - `MAILGUN_DOMAIN`: Your Mailgun domain (e.g., `sandboxxxxx.mailgun.org`).
   - `MAILGUN_API_KEY`: Your Mailgun API key.
   - `email@mailgun.org`: The email you registered with Mailgun.

2. To send emails to all addresses in the CSV file, run the following command:

   ```bash
   python3 mail.py
   ```

3. The program will log the status of each email, indicating whether it was successfully sent or if there was an error.

## Error Handling

- The script automatically skips any row with missing `Name` or `Email` values.
- If an error occurs during the email sending process, the error is logged and the script moves on to the next recipient.

## License

Use it responsibly
