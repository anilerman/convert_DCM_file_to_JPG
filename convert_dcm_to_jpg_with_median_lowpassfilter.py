import os
import pydicom
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter, median_filter

def apply_low_pass_filter(image_array):
    # Düşük Geçiren Filtre (Gaussian Filtre) uygula
    low_pass_filtered_image = gaussian_filter(image_array, sigma=1)
    return low_pass_filtered_image

def apply_median_filter(image_array):
    # Median Filtre uygula
    median_filtered_image = median_filter(image_array, size=3)
    return median_filtered_image

def dicom_to_jpg_with_filters(dicom_path, jpg_path):
    # DICOM dosyasını aç
    dicom_dataset = pydicom.dcmread(dicom_path)

    # DICOM görüntüsünü numpy dizisine çevir
    pixel_array = dicom_dataset.pixel_array

    # Düşük Geçiren Filtre uygula
    low_pass_filtered_image = apply_low_pass_filter(pixel_array)

    # Median Filtre uygula
    median_filtered_image = apply_median_filter(low_pass_filtered_image)

    # Numpy dizisini uygun formata dönüştür
    final_image = median_filtered_image.astype(np.uint8)

    # Numpy dizisini PIL Image nesnesine çevir
    image = Image.fromarray(final_image)

    # JPG olarak kaydet
    image.save(jpg_path, 'JPEG')

def convert_folder_dcm_to_jpg_with_filters(folder_path):
    # Klasördeki tüm dosyaları al
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.dcm')]

    # Her bir DICOM dosyasını JPG'ye dönüştür ve filtreler uygula
    for dicom_file in file_list:
        dicom_path = os.path.join(folder_path, dicom_file)
        jpg_file = os.path.splitext(dicom_file)[0] + '_filtered.jpg'
        jpg_path = os.path.join(folder_path, jpg_file)

        dicom_to_jpg_with_filters(dicom_path, jpg_path)
        print(f"{dicom_file} dönüştürüldü ve filtreler uygulandı -> {jpg_file}")

# Klasördeki DICOM dosyalarını JPG'ye dönüştür ve filtreler uygula
convert_folder_dcm_to_jpg_with_filters('E:\\ÖNEMLİ DOSYALAR\\DERS\\HTW Saar\\SS2023\\Medical Imaging\\Brain Scann Dokuments\\HTW_02\\Portrait\\matlab')
