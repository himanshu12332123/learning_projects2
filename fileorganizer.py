import os

def arrange_files(files,ext):
    files = [file for file in files if file.endswith(ext)]
    print(files)
    if not(os.path.exists("imagess")):
        os.mkdir("imagess")
    i = 1
    for file in files:
        os.rename(file,f"imagess/photo-{i + 6}{ext}")
        i += 1
    

if __name__ == "__main__":
    files = os.listdir()
    arrange_files(files,".jpg")