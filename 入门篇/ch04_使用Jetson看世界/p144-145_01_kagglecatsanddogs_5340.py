# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第144-145页 (PDF第154页, PDF第155页)
# 上下文: 据集。 ／ 我们使用如下代码下载“ kagglecatsanddogs_5340.zip”并将其解压，准备猫狗分类数

import os
import zipfile
import requests

# 下载数据集
url = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"
data_dir = './kagglecatsanddogs_5340'
zip_path = './kagglecatsanddogs_5340.zip'

if not os.path.exists(zip_path):
    print("Downloading dataset...")
    response = requests.get(url, stream=True)
    with open(zip_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)
    print("Download complete.")

# 解压数据集
if not os.path.exists(data_dir):
    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    print("Extraction complete.")
