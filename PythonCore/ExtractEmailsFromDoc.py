import re

def extract_emails_from_doc(doc_text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, doc_text)
    return emails

document = """
aaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
bbbbbbbbbbbbbbbbbbbbbbbbb
cccccccccccccccccccccccccckunaldp379@gmail.combbbbbbbbbbbbbbbbbbbb
aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
dddddddddddddddddddddddddddddddddd
"""

emails = extract_emails_from_doc(document)
print("Emails in the document are:")
for email in emails:
    print(email)
