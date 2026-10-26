filename = input("Name: ").lower().strip()

if filename[-4:] == ".gif":
    print("image/gif")
elif filename[-4:] == ".jpg" or filename[-5:] == ".jpeg":
    print("image/jpeg")
elif filename[-4:] == ".png":
    print("image/png")
elif filename[-4:] == ".pdf":
    print("application/pdf")
elif filename[-4:] == ".txt":
    print("text/plain")
elif filename[-4:] == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")


