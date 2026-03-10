import csv

def load_messages(path: str) -> list[dict]:
  messages = []
  with open(path, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        messages.append(row)
  return messages
     
if __name__ == "__main__":
  load_messages("./messages_data/messages.csv") 