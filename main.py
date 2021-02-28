#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import design
from PyQt5 import QtWidgets
import ZonaKino
import HDRezka

class PresentManager(QtWidgets.QMainWindow, design.Ui_MainWindow):
    @staticmethod
    def save_file(directory):
        os.replace("result.pptx", directory[0])
    
    def fill_list(self):
        print(self.lineEdit.text())
        
        if self.lineEdit.text() != "":
            if self.radioButton.isChecked() == True:
                self.film_list = HDRezka.HDRezka(str(self.lineEdit.text()))
            else:
                self.film_list = ZonaKino.ZonaFilms(str(self.lineEdit.text()))
    
            self.listWidget.clear()
            current_lst = self.film_list.search_results
       
            for i in range(len(current_lst)):
                self.listWidget.addItem(current_lst[i]["film_name"])
         
    def add_to_ppt(self):
        
        if self.listWidget.currentRow() != -1:
            ZonaKino.PresentationCreator(self.film_list, self.listWidget.currentRow())
        
    def browse_folder(self):
        if os.path.isfile("result.pptx"):
            directory = QtWidgets.QFileDialog.getSaveFileName(filter = "*.pptx")
            
            if (directory[0]!=""):
                if not (".pptx" in directory[0]): directory[0]+=".pptx"
                self.save_file(directory)
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.fill_list)
        self.pushButton_2.clicked.connect(self.add_to_ppt)
        self.pushButton_3.clicked.connect(self.browse_folder)
        #self.pushButton_3.clicked.connect(QApplication.quit())
    
    
 
        
        
       
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = PresentManager()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    
    
    
    
    
    
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()