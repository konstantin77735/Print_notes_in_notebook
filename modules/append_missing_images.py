import os
import re
from PIL import Image, ImageDraw, ImageFont
import shutil

def append_missing_images(output_dir, dirs, empty_image_path):
    # Проходим по каждой подпапке в output_dir
    for input_filename in os.listdir(output_dir):
        input_path = os.path.join(output_dir, input_filename.strip())
        
        if os.path.isdir(input_path):
            # Проходим по папкам 'without_lines' и 'with_lines'
            for subdir in dirs:
                subdir_path = os.path.join(input_path, subdir)
                subdir_path = subdir_path.replace('./', '')

                if os.path.exists(subdir_path):
                    files = os.listdir(subdir_path)
                    
                    #for file in files:
                       # print(file)
                    
                    if len(files) == 0:
                        # Если файлов нет, пропускаем
                        print(f"Папка {subdir_path} пуста, пропускаем.")
                        continue
                    
                    # Если файлов больше 0 и не делится на 4
                    if len(files) > 0 and len(files) % 4 != 0:
                        # Вычисляем, сколько раз нужно добавить empty.png
                        while len(files) % 4 != 0 or (len(files) // 4) % 2 != 0:
                            print(f"Количество файлов в {subdir_path}: {len(files)}. Не кратно 4 или частное нечетное. Добавляем изображение.")
                            
                            # Путь к изображению empty.png
                            empty_image_path = './img/cells_half.png'
                            # Имя для нового изображения
                            new_image_name = f'{len(files) + 1}.png'
                            # Путь для копирования нового изображения
                            new_image_path = os.path.join(subdir_path, new_image_name)
                            
                            # Копируем empty.png в папку
                            shutil.copy(empty_image_path, new_image_path)
                            
                            # Добавляем новое изображение в список файлов
                            files.append(new_image_name)
                            
                        print(f"Файлы в {subdir_path} теперь кратны 4 и имеют четное частное.")
    