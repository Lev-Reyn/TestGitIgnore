"""https://fixmypc.ru/post/vstavka-teksta-i-izobrazheniia-v-kartinku-s-python-pillow-pil/ - статья"""
from PIL import Image, ImageDraw, ImageFont


for i in range(1, 5):
    file = open(f'/Users/levreyn/Yandex.Disk.localized/python otr/телеграм бот/BOT_test_tasks/data_for_test_task/task_text/{i}.txt')
    text = file.read()
    im = Image.new('RGB', (1600, 100 + 50 * text.count('\n')), color=('#10ffc5'))
    font = ImageFont.truetype(
        '/Users/levreyn/Yandex.Disk.localized/python otr/создание изображений/шрифты/5/ofont.ru_RussianPunk.ttf',
        size=40)  # добавляем шрифт
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (20, 50),
        text=text,
        font=font,
        fill=('#1C0606')
    )
    # Откроет изображение в новом окне
    # im.show()
    im.save(f'photos/test{i}.png')
