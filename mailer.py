import yagmail
import csv

# Function to send emails using yagmail
def send_emails_from_csv(csv_file, yagmail_user, yagmail_password):
    failed_emails = []

    # Ask user for the email subject and content template
    subject_template = input("Enter the email subject (use {name} to include the recipient's name): ")
    content_template = input("Enter the email content (use {name} to include the recipient's name): ")

    with yagmail.SMTP(yagmail_user, yagmail_password) as yag:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                email = row['email']
                name = row['name']

                # Personalize the email content
                subject = subject_template.format(name=name)
                contents = content_template.format(name=name)

                # Send the email
                try:
                    yag.send(to=email, subject=subject, contents=[contents])
                    print(f"Email sent to {name} at {email}")
                except Exception as e:
                    print(f"Failed to send email to {name} at {email}. Error: {e}")
                    failed_emails.append({'email': email, 'name': name, 'error': str(e)})

    # Display failed email attempts
    if failed_emails:
        print("\nFailed to send the following emails:")
        for entry in failed_emails:
            print(f"Email: {entry['email']}, Name: {entry['name']}, Error: {entry['error']}")

# Yagmail user credentials
YAGMAIL_USER = 's.abhaysastha@gmail.com'
YAGMAIL_APP_PASSWORD = 'tigveghwvxswxuxx'  # Not the plain password

# Path to the CSV file
CSV_FILE_PATH = 'emails.csv'

# Call the function to send emails from the CSV file
send_emails_from_csv(CSV_FILE_PATH, YAGMAIL_USER, YAGMAIL_APP_PASSWORD)
