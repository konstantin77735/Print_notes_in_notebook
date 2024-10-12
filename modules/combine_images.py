import os
import re
from PIL import Image, ImageDraw, ImageFont

def combine_images(input_dir, output_dir, image_width, image_height, empty_dir):
    possesed_files=[]
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
   
    # Получаем список файлов в указанной директории
    files = sorted(os.listdir(input_dir), key=lambda x: int(re.search(r'\d+', x).group()))
    
    # Проходим по каждому второму файлу (четным индексам)
    for i in range(0, len(files), 1):
        #print(f'итерация: {i}, possesed files:')
        #print(possesed_files)
        #print('_____')
        
        #Если мы эти файлы обрабатывали, то скипаем
        #Пример: объединили 1ю и 3ю, 2ю и 4ю, дальше 3ю пропустили, 4ю пропустили, пошли ДАЛЬШЕ объединять 5 и 7, потом 6 и 8...
        if files[i] in possesed_files or files[i+2] in possesed_files:
            continue
        
        # Открываем текущие два изображения
        img1 = Image.open(os.path.join(input_dir, files[i])) #файл который сейчас обрабатываем. Допустим, 1.png
        img2 = None
        
        if i == len(files) - 1:
            #print(f'i: {i}')
            
            if i % 2 != 0:
                
                img2 = Image.open(os.path.join(empty_dir)) #тогда это: 3.png
        else:             
            img2 = Image.open(os.path.join(input_dir, files[i + 2])) #тогда это: 3.png
            

            
        # Создаем новое изображение, горизонтально объединяя текущие два
        new_img = Image.new('RGBA', ( image_width , max(img1.height, img2.height)))

        # Проверяем, нужно ли перевернуть изображения на 180 градусов
        if i % 4 == 0:  # Для первой страницы (i=0, 4, 8, ...)
            img1 = img1.rotate(180)
        if i % 4 == 1:  # Для четвертой страницы (i=2, 6, 10, ...)
            img2 = img2.rotate(180)

        new_img.paste(img1, (0, 0), img1.convert('RGBA'))
                           
        new_img.paste(img2, ( int(image_width/2)+5, 0), img2.convert('RGBA'))



        # Создаем еще одно новое изображение, объединяя текущее с фоновым
        final_img = Image.new('RGBA', (new_img.width, max(new_img.height, image_height)))
        final_img.paste(new_img, (0, 0))


        # Сохраняем полученное изображение
        final_img.save(os.path.join(output_dir, f'{i+1}-{i+3}.png'))
              
        possesed_files += [files[i], files[i+2]]
        

    print("Изображения успешно объединены!") 
    