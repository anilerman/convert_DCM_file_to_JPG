import os
import imageio

def create_gif(folder_path, gif_path):
    # Klasördeki tüm JPG dosyalarını al
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

    # JPG dosyalarını sırala
    file_list.sort()

    # Gif için imageio Writer nesnesi oluştur
    gif_writer = imageio.get_writer(gif_path, duration=0.07)  # Duration: Her bir kare arasındaki süre (saniye)

    # Her bir JPG dosyasını GIF'e ekle
    for jpg_file in file_list:
        jpg_path = os.path.join(folder_path, jpg_file)
        image = imageio.imread(jpg_path)
        gif_writer.append_data(image)

    # Writer nesnesini kapat
    gif_writer.close()

# Klasördeki JPG dosyalarını kullanarak bir GIF oluştur ve belirli bir dosya yoluna kaydet
create_gif('E:\\ÖNEMLİ DOSYALAR\\DERS\\HTW Saar\\SS2023\\Medical Imaging\\Brain Scann Dokuments\\HTW_02\\Portrait\\matlab', 'E:\\ÖNEMLİ DOSYALAR\\DERS\\HTW Saar\\SS2023\\Medical Imaging\\Brain Scann Dokuments\\HTW_02\\Portrait\\output.gif')
