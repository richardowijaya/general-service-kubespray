from fastapi import FastAPI, testclient
from main import app
import os

folder_path = "G:\My Drive\Python Learn\FastAPI\DMS_microservices_FASTAPI\controllers"  # Replace with your folder path
prefixes = []

for file_name in os.listdir(folder_path):
    if file_name.endswith("Controller.py"):  # Change the extension if needed
        prefix = file_name.replace("Controller.py", "")  # Change "Controller.py" with your file extension
        prefix = '-'.join([word.lower() for word in prefix.split()])
        prefixes.append(prefix)

print(prefixes)


def test_get_all():
    client = testclient(app)
    for i in prefixes:
        response = client.get(f'/{prefixes}/')