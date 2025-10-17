import smtplib
from email.message import EmailMessage

def send_email(sender, password, recipient, subject, body, attachment=None):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)
    if attachment:
        with open(attachment, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
    print("📧 Email sent successfully!")

# Example usage
# send_email("your@gmail.com", "yourpassword", "recipient@example.com", "Daily Report", "Here’s today’s report.", "report.pdf")
