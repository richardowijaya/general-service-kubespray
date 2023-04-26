import pytest
from starlette.testclient import TestClient
from main import app
import os

folder_path = "controllers"
data = []
datas = []
def extract_prefix(controller_name):
    words = []
    start = 0
    for i in range(1, len(controller_name)):
        if controller_name[i].isupper():
            words.append(controller_name[start:i].lower())
            start = i
    words.append(controller_name[start:].lower())
    return '-'.join(words)


for filename in os.listdir(folder_path):
    if filename.endswith("Controller.py"):  
        controller_name = os.path.splitext(filename)[0]
        text = extract_prefix(controller_name)
        text = text.replace("-controller", "")
        data.append(text)
        datas.append(text+'s')

# @pytest.mark.parametrize("datas", datas)
# def test_get_all(datas):
#     client = TestClient(app)
#     response = client.get(f"/api/general/get-{datas}")
#     assert response.status_code == 200
                                                            
# @pytest.mark.parametrize("data", data)
# def test_get_by_id(data):
#     client = TestClient(app)
#     response = client.get(f"/api/general/get-{data}/1")
#     assert response.status_code == 200

# @pytest.mark.parametrize("data", data)
# def test_delete_data(data):
#     client = TestClient(app)
#     response = client.delete(f"/api/general/delete-{data}/1")
#     assert response.status_code == 202

# @pytest.mark.parametrize("data",data)
# def test_patch_by_id(data):
#     client = TestClient(app)
#     response = client.patch(f"/api/general/active-{data}/1")
#     assert response.status_code == 202