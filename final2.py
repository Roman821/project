from PIL import Image, ImageFilter
import os
import matplotlib.pyplot as plt

class Filter:
    def apply_to_image(self, image):
        pass

class BrightFilter(Filter):
    def apply_to_image(self, image):
        return image.point(lambda i: i * 1.5)

class GreenChanger(Filter):
    def apply_to_image(self, image):
        r, g, b = image.split()
        g = g.point(lambda i: i * 1.5)
        return Image.merge('RGB', (r, g, b))

class SketchFilter(Filter):
    def apply_to_image(self, image):
        return image.filter(ImageFilter.FIND_EDGES)

class CharcoalFilter(Filter):
    def apply_to_image(self, image):
        return image.filter(ImageFilter.EMBOSS)

class OilFilter(Filter):
    def apply_to_image(self, image):
        return image.filter(ImageFilter.BLUR)

class WatercolorFilter(Filter):
    def apply_to_image(self, image):
        return image.filter(ImageFilter.SMOOTH_MORE)

class PastelFilter(Filter):
    def apply_to_image(self, image):
        return image.filter(ImageFilter.SMOOTH)

filters = {
    '1': {'name': 'BrightFilter', 'instance': BrightFilter()},
    '2': {'name': 'GreenChanger', 'instance': GreenChanger()},
    '3': {'name': 'Sketch', 'instance': SketchFilter()},
    '4': {'name': 'Charcoal', 'instance': CharcoalFilter()},
    '5': {'name': 'Oil', 'instance': OilFilter()},
    '6': {'name': 'Watercolor', 'instance': WatercolorFilter()},
    '7': {'name': 'Pastel', 'instance': PastelFilter()},
}

while True:
    print('Введите путь к файлу:')
    path = input()
    while not os.path.exists(path) or not path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        print('Файла не существует или это не изображение.')
        path = input()

    image = Image.open(path)

    print('Хотите увидеть изображение до обработки? (Да/Нет):')
    view_before = input()
    if view_before.lower() == 'да':
        plt.imshow(image)
        plt.show()

    print('Меню фильтров:')
    for key, value in filters.items():
        print(f'{key}: {value["name"]}')
    print('0: Выход')

    print('Выберите фильтр (или 0 для выхода):')
    choice = input()

    if choice == '0':
        break

    filter_instance = filters[choice]['instance']
    image = filter_instance.apply_to_image(image)

    print('Хотите увидеть изображение после обработки? (Да/Нет):')
    view_after = input()
    if view_after.lower() == 'да':
        plt.imshow(image)
        plt.show()

    print('Куда сохранить:')
    save_path = input()
    image.save(save_path)

    print('Ещё раз? (Да/Нет):')
    again = input()
    if again.lower() != 'да':
        break

print('До свидания!')