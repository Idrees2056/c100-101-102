import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A4DVteXX9uOiTx3RuhRVSVQEj488O2_P7F1aAPnOdnRwhj0jmRzKzmUn_FpD23g-yB0pWHOz4a7nPyiPQel-PUtkyYQkcbAwOcT6DrbSlUuw_F9Jk1SdMpEdbSI16JHk6K1YVg2utPE'
    transferData = TransferData(access_token)
    transferfile = input("enter the path of the file you want to upload")
    file_from = transferfile
    file_to = '/empty folder/'+transferfile  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
