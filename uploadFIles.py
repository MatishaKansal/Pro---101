import dropbox as dbx;
import os;

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, files_from, file_to):
        local_path = os.getcwd()
        for root, dirs, files in os.walk(files_from):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))
        relative_path = os.path.realpath(local_path, files_from)
        dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=os.writeMode('overwrite'))

    def main() :
        access_token = "sl.AzfvW3oFYYtZj5L72zCzhq-rp6pWQAyzpbALI5F98BbVzHnYbIWBejZxaINh0_QJG_5DCRs9Tdo5-JG_1LBvIXYhsz22uQfuxZhfsUUbUFtA8kZCFZq-ArF1ARIFiSkHM9Zk45o"
        files_from = input("Location of the file  ")
        file_name =  input("Name of the file  ")
        file_to = "/Matisha Kansal/" + file_name

    main()