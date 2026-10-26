# CS50 - File Extensions: prints the media type of a file based on its extension

# Ask for the file name, ignoring upper/lower case and extra spaces
filename = input("Name: ").lower().strip()

# Compare the end of the file name (last 4 or 5 characters) with each known extension
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
    # Any other extension (or no extension) gets the default type
    print("application/octet-stream")


