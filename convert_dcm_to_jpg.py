import os
import pydicom
import numpy as np
from PIL import Image

def dicom_to_jpg(dicom_path, jpg_path):
    # DICOM dosyasını aç
    dicom_dataset = pydicom.dcmread(dicom_path)

    # DICOM görüntüsünü numpy dizisine çevir
    pixel_array = dicom_dataset.pixel_array

    # Numpy dizisini uygun formata dönüştür
    pixel_array = pixel_array.astype(np.uint8)

    # Numpy dizisini PIL Image nesnesine çevir
    image = Image.fromarray(pixel_array)

    # JPG olarak kaydet
    image.save(jpg_path, 'JPEG')

def convert_folder_dcm_to_jpg(folder_path):
    # Klasördeki tüm dosyaları al
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.dcm')]

    # Her bir DICOM dosyasını JPG'ye dönüştür
    for dicom_file in file_list:
        dicom_path = os.path.join(folder_path, dicom_file)
        jpg_file = os.path.splitext(dicom_file)[0] + '.jpg'
        jpg_path = os.path.join(folder_path, jpg_file)

        dicom_to_jpg(dicom_path, jpg_path)
        print(f"{dicom_file} dönüştürüldü -> {jpg_file}")

# Klasördeki DICOM dosyalarını JPG'ye dönüştür
convert_folder_dcm_to_jpg('E:\\ÖNEMLİ DOSYALAR\\DERS\\HTW Saar\\SS2023\\Medical Imaging\\Brain Scann Dokuments\\HTW_02\\Portrait\\matlab')
