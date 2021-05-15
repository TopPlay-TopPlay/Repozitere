#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QListWidget, QHBoxLayout, QFileDialog
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtGui import QPixmap
import os
from PIL import Image
from PIL.ImageQt import ImageQt # для перевода графики из Pillow в Qt
from PIL import ImageFilter
from PIL.ImageFilter import (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN, GaussianBlur, UnsharpMask)





def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result



def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)

    list123.clear()
    for filename in filenames:
        list123.addItem(filename)



class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None
        self.save_dir = 'Папка:'
    def loadImage(self, filename):
        self.filename = filename
        Image_path = os.path.join(workdir, filename)
        self.image = Image.open(Image_path)
    def showImage(self, path):
        kartinka.hide()
        pixmapimage = QPixmap(path)
        w, h = kartinka.width(), kartinka.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        kartinka.setPixmap(pixmapimage)
        kartinka.show()
    def saveImage(self):

        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur1(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur2(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur3(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)


def showChosenImage():
    if list123.currentRow() >= 0:
        filename = list123.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)




workimage = ImageProcessor()


workdir = ' '
app = QApplication([])
window = QWidget()
pb_left = QPushButton('Лево')
pb_right = QPushButton('Право')
pb_mirror = QPushButton('Зеркало')
pb_ch_b = QPushButton('Ч/Б')
pb_rezkost = QPushButton('Резкость')
pb_papka = QPushButton('Папка')
list123 = QListWidget()
kartinka = QLabel('Картинка')
layoutv1 = QVBoxLayout()
layoutv2 = QVBoxLayout()
layouth1 = QHBoxLayout()
layout_main = QHBoxLayout()
layouth1.addWidget(pb_left)
layouth1.addWidget(pb_right)
layouth1.addWidget(pb_mirror)
layouth1.addWidget(pb_rezkost)
layouth1.addWidget(pb_ch_b)
layoutv2.addWidget(kartinka)
layoutv2.addLayout(layouth1)
layoutv1.addWidget(pb_papka)
layoutv1.addWidget(list123)
layout_main.addLayout(layoutv1)
layout_main.addLayout(layoutv2)

list123.currentRowChanged.connect(showChosenImage)
pb_ch_b.clicked.connect(workimage.do_bw)
pb_left.clicked.connect(workimage.do_blur)
pb_right.clicked.connect(workimage.do_blur1)
pb_rezkost.clicked.connect(workimage.do_blur2)
pb_mirror.clicked.connect(workimage.do_blur3)

pb_papka.clicked.connect(showFilenamesList)




window.setLayout(layout_main)
window.show()
app.exec_()