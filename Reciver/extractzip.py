import zipfile
with zipfile.ZipFile("Rev.zip","r") as zip_ref:
    zip_ref.extractall("./")
