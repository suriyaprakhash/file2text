#  Copyright 2021 Suriya Prakhash Deenadayalan. All Rights Reserved.
#  Licensed under the Apache License, Version 2.0 (the "License"); You may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

import pytesseract
import filetype
from pdf2image import convert_from_path
import cv2
import os
from PIL import Image


def read_file_into_text(config):
    location_file = config['location']['file']
    location_img = config['location']['img']
    location_text = config['location']['text']
    poppler_path = config['poppler']['path']
    tesseract_path = config['tesseract']['path']
    support_filetype = config['support']['filetype']

    file_list = []

    # os.chdir(imglocation_src)
    for file in os.listdir(location_file):
        file_path = f"{location_file}\{file}"
        print(file_path)
        kind = filetype.guess(location_file + '/' + file)
        file_list.append(file_path)
        if kind != None and kind.mime == 'application/pdf':
            image_name_list = export_file_into_page_images(location_file, location_img, file, poppler_path)
            convert_images_to_text(location_img, location_text, image_name_list, tesseract_path)
        elif kind != None and (kind.mime == 'image/jpeg' or kind.mime == 'image/png'):
            image_name_list = []
            image_name_list.append(file)
            convert_images_to_text(location_file, location_text, image_name_list, tesseract_path)
        else:
            print('FileName: ' + file + ' not processed')
            print('Supports only ' + support_filetype + ' files or file type not found')

    return 'test--'


def export_file_into_page_images(location_file, location_img, file, poppler_path):
    pages = convert_from_path(pdf_path=location_file + file, poppler_path=poppler_path)
    i = 1
    image_name_list = []
    for page in pages:
        image_name = f"{file.replace('.', '_')}_" + str(i) + ".jpg"
        page.save(location_img + image_name, "JPEG")
        i = i + 1
        image_name_list.append(image_name)
    return image_name_list


def convert_images_to_text(location_img, location_text, image_name_list, tesseract_path):
    # img = Image.open(location_img + image_list[0])
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    for img_name in image_name_list:
        img = cv2.imread(location_img + img_name)
        print(img)
        result = pytesseract.image_to_string(img)
        text_file = open(location_text + img_name.replace('.', '_') + ".txt", "w")
        text_file.write(result)
        text_file.close()
