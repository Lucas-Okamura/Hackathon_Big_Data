import sys
import os.path
import requests


FILE_PATH = 'equipe_410685677.zip'
URL = 'https://hackathon-batalha-final.s3.amazonaws.com/'
POST_DATA = {
    'key': FILE_PATH,
    'AWSAccessKeyId': 'AKIA6HWHFK26FN543IED',
    'policy': 'eyJleHBpcmF0aW9uIjogIjIwMjAtMTEtMTZUMDI6NTk6MDBaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAiaGFja2F0aG9uLWJhdGFsaGEtZmluYWwifSwgeyJrZXkiOiAiZXF1aXBlXzQxMDY4NTY3Ny56aXAifV19',
    'signature': 'sX0qE3DLIJnJkDRMo90nSM9reX0='
}


def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        print('ERRO: Arquivo %s não encontrado.' % FILE_PATH)
        sys.exit(0)


def upload_file(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f)}
        http_response = requests.post(URL, data=POST_DATA, files=files)
    return http_response.status_code


if __name__ == '__main__':
    check_file_exists(FILE_PATH)
    status_code = upload_file(FILE_PATH)

    if status_code == 204:
        print('Arquivo submetido com sucesso!')
    else:
        print('Falha ao submeter o arquivo. HTTP Status Code %s' % status_code)
