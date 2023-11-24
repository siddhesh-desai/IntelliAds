import pywhatkit as pwk

def send_whatsapp_message(to_whom, message):
    pwk.sendwhatmsg_instantly(to_whom, message,10)
    # pwk.sendwhatmsg_instantly("+919370554548", "Uth re, jhopu nako.",10)