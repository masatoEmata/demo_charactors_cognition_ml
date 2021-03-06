# Based on: https://qiita.com/Cyber_Hacnosuke/items/c121cfd1945a3174bc84

import cv2
import glob
import pickle
import os
from google.colab.patches import cv2_imshow

ETL_TYPE = 'ETL8G'
IM_DIR = f"/content/sample_data/{ETL_TYPE}/img"
# IM_DIR = f"./dataset/{ETL_TYPE}"
IM_SIZE = 32
SAVE_FILE = IM_DIR + f"/{ETL_TYPE}.pickle"


def im_formatter(file_path):
  img = cv2.imread(file_path)
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img = cv2.resize(img_gray, (IM_SIZE, IM_SIZE))
  return img


def get_file_paths(dir_name):
  dir_path = f'{IM_DIR}/{dir_name}'
  return glob.glob(dir_path + "/*")


result = []
dir_names = os.listdir(IM_DIR)
for dir_name in dir_names:
#   print('############################################')
#   print(dir_name)
  is_character_name = len(dir_name) == 1
  if is_character_name:
    file_paths = get_file_paths(dir_name)
    for file_path in file_paths:
      img = im_formatter(file_path)
      cv2_imshow(img)
      result.append([dir_name, img])

pickle.dump(result, open(SAVE_FILE, "wb"))
