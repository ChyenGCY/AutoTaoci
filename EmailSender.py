import smtplib, ssl
from email.mime.text import MIMEText


class EmailSender:
    def __init__(self, sender_email, sender_password, recipient_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email

    def send_email(self, subject, message):
        """Sends an email with the given subject and message."""

        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = self.sender_email
        msg["To"] = self.recipient_email

        # Create a secure SSL context
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP("smtp.kth.se", 587)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, sender_password)
            server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print("Error sending email:", e)


# Example usage:
if __name__ == "__main__":
    # sender_email = input("Enter your email address: ")
    # sender_password = input("Enter your email password: ")
    sender_email = ""
    sender_password = ""
    recipient_email = ""

    sender = EmailSender(sender_email, sender_password, recipient_email)

    # subject = input("Enter the email subject: ")
    # message = input("Enter the email message: ")
    subject = "Test Email"
    message = "This is a test email sent from Python."

    sender.send_email(subject, message)
