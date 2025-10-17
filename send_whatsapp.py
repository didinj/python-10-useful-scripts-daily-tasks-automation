import pywhatkit as kit

def send_whatsapp_message(phone_no, message, hour, minute):
    kit.sendwhatmsg(phone_no, message, hour, minute)
    print("💬 WhatsApp message scheduled successfully!")

# Example usage
# send_whatsapp_message("+1234567890", "Good morning! ☀️", 9, 30)
