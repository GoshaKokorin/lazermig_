import io
import random
from uuid import uuid4

from django.core.files.base import File
from PIL import Image, ImageDraw


MAX_IMAGE_WIDTH = 1280
MAX_IMAGE_HEIGHT = 720


def get_file_logo(width=150, height=70) -> File:
    """Принимает параметры ширины и высоты изображения. Возвращает объект File с расширением jpg."""
    assert width < MAX_IMAGE_WIDTH, f'максимальная ширина изображения {MAX_IMAGE_WIDTH}, задано {width}'
    assert height < MAX_IMAGE_HEIGHT, f'максимальная высота изображения {MAX_IMAGE_HEIGHT}, задано {height}'

    base_color = random.randint(200, 255)
    c_offset = random.randint(0, 40)
    rgb = (
        base_color - c_offset,
        base_color - c_offset,
        base_color - c_offset,
    )
    file = Image.new('RGB', (width, height), rgb)

    draw = ImageDraw.Draw(file)
    for i in range(random.randint(3, 10)):
        w1 = random.randint(0, width)
        h1 = random.randint(0, height)
        w2 = random.randint(0, width)
        h2 = random.randint(0, height)
        points = ((w1, h1), (w2, h2))
        base_fig_color = random.randint(150, 200)
        color_offset = random.randint(30, 80)
        fill_color = (
            base_fig_color - color_offset,
            base_fig_color - color_offset,
            base_fig_color - color_offset,
        )
        if random.randint(0, 5) > 4:
            draw.line(points, fill=fill_color, width=10)

    io_file = io.BytesIO()
    file.save(io_file, format='JPEG')
    file.seek(0)
    file_name = f'{uuid4()}.jpg'
    return File(io_file, name=file_name)