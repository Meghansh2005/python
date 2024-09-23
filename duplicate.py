
def find_duplicate_emails(emails):
    seen = set()
    duplicates = set()
    for email in emails:
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)
    return duplicates

email_list = ["a@example.com", "b@example.com", "a@example.com", "c@example.com"]
duplicates = find_duplicate_emails(email_list)
print("Duplicate emails:", duplicates)
