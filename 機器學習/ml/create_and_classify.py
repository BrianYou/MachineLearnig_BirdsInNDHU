import pandas as pd
import os
import shutil

# 讀取CSV檔案
csv_file = 'Data/label-base.csv'
data = pd.read_csv(csv_file)

# 假設鳥類名稱在 'bird_name' 欄位，檔案名稱在 'file_name' 欄位
bird_names = data['EngName'].unique()

# 建立資料夾
for bird in bird_names:
    folder_path = os.path.join('Data/ClassifyRawData', bird)
    os.makedirs(folder_path, exist_ok=True)
    print(f'Created folder: {folder_path}')

# 複製檔案到相應資料夾
for index, row in data.iterrows():
    bird_name = row['EngName']
    file_name = row['RawFileName']
    source_file_path = os.path.join('Data/RawData', file_name)
    destination_folder_path = os.path.join('Data/ClassifyRawData', bird_name)
    destination_file_path = os.path.join(destination_folder_path, file_name)
    
    if os.path.isfile(source_file_path):
        shutil.copy2(source_file_path, destination_file_path)
        print(f'Copied {file_name} to {destination_folder_path}')
    else:
        print(f'File {file_name} does not exist in source directory')