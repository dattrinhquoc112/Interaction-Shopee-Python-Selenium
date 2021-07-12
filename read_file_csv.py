import csv


def content_csv(filePath):
    content = []
    try:
        with open(filePath, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                content.append(row)
    except:
        print("error: read_file_csv")
    return content
