from locale import locale_alias
import dropbox
import os
class TransferData:
    def __init__(self, access_token): 
         self.access_token = access_token
    def upload_file(self):
        dbx = dropbox.Dropbox(self.access_token)
        file_from = str(input("Enter the file path"))
        local_path = ""
        file_to = ""
        for root, dirs, files in os.walk(file_from):
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode-WriteMode('overwrite'))
def main():
    uploadfilesobject = TransferData("sl.BLcBNB-R5r6k1MR1-ZF-Hg7nHfkbx7VpK_kDER9Kj3bSaN48wpR51h-McGFUdoPsCwZlnrj1QnKtYQGs_jh22bS1W7gV325-ooJUh3dh1BSKJmMVhqYGGiZLN5ORA5sFvu9s3Fc")
    uploadfilesobject.upload_file()
main()
print("File uploaded")

