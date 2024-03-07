filename = input("File name: ")

filename = filename.lower().strip()



match filename:
    case filename.endswith(".gif"):
        print("image/gif")
    case filename.endswith(".jpg" | ".jpeg"):
        print("image/jpeg")
    case filename.endswith(".png"):
        print("image/png")
    case filename.endswith(".pdf"):
        print("application/pdf")
    case filename.endswith(".txt"):
        print("text/plain")
    case filename.endswith(".zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")
