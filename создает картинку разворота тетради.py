import PIL.Image as Image
from PIL import ImageDraw

type = 'lines'

# Создание картинки шириной 3320px на 2339px
img = Image.new('RGB', (3320, 2339), color=(255, 255, 255))

# Начерчивание линии для рисования
draw = ImageDraw.Draw(img)

# Рисование горизонтальных линий
for i in range(55, img.height, 55):
    draw.line((0, i, img.width, i), fill=(0, 0, 255), width=1)

if type == 'cells':
    # Рисование вертикальных линий
    for i in range(55, img.width, 55):
        draw.line((i, 0, i, img.height), fill=(0, 0, 255), width=1)

# Сохранение картинки в файл
img.save(f'./img/{type}.png')
