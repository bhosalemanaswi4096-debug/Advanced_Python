
import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}\b'
    emails = re.findall(pattern, text)
    return emails

text = input("Enter a text: ")

result = find_emails(text)

print("Email addresses found:")
print(result)
