from os import access
import dropbox 

class TransferData :
    def __init__(self, access_token) :
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to) 

def main() :
    access_token = 'a70A5J8oMn0AAAAAAAAAAUpgiS85BJuVD8exvR7N9HxT_yrSzbvbsvi4GKigQ29L'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload the file to, including the file name: ") 

    transferData.upload_file(file_from, file_to)
    print("The file has been uploaded.") 

main() 