import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pprint import pprint
from baiduspider import BaiduSpider
import requests
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(572, 413)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 331, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(370, 80, 171, 211))
        
        img = QImage('./images/init.png')
        size = QSize(170, 210)
        pixImg = QPixmap.fromImage(img.scaled(size, Qt.IgnoreAspectRatio))
        self.label_3.setPixmap(pixImg)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 80, 171, 31))
        self.textEdit.setObjectName("textEdit")
        # self.textEdit.setText("请输入待查询关键词")
        s = '<b style="color:#575757;font-size:13px">{}</b>'.format("请输入待查询关键词")
        self.textEdit.setText(s)
        
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 111, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 80, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 140, 331, 151))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 320, 331, 78))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(370, 320, 171, 78))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(370, 290, 111, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Web Keyword IR System"))
        self.label.setText(_translate("Form", "Web  Keyword  IR  System"))
        self.label_2.setText(_translate("Form", "Information Retrieval Final Project, 51255901138, 舒翔"))
        self.label_4.setText(_translate("Form", "More Infos:"))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_5.setText(_translate("Form", "Results: "))
        self.label_6.setText(_translate("Form", "Logs:  "))
        self.label_7.setText(_translate("Form", "Keyword: "))
    
    def search(self):
        
        # get keyword and print logs
        keyword = self.textEdit.toPlainText()
        t = time.strftime('%H:%M:%S', time.localtime(time.time()))
        self.textEdit_4.append(str(t)+"\nKeyword: {}".format(keyword))
        self.textEdit_4.append("------------------------")
        
        # get baike knowledge
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit_2.setFont(font)
        result_baike = BaiduSpider().search_baike(keyword)
        self.textEdit_2.setText(str(result_baike[0].des))
        s = '<a href="{}" style="color:#3232CD;font-size:15px"><b>{}</b></a>'.format(result_baike[0].url, "详细信息")
        self.textEdit_2.append(s)
        
        # get a random picture
        result_pic = BaiduSpider().search_pic(keyword, pn=random.randint(1, 5))
        pic_link = result_pic.results[random.randint(0, 10)].url
        res2 = requests.request(url=pic_link, method='get')
        print(res2.cookies)
        content=res2.content
        with open('./images/f.jpg','wb') as f:
            f.write(content)
        img = QImage('./images/f.jpg')
        size = QSize(170, 210)
        pixImg = QPixmap.fromImage(img.scaled(size, Qt.IgnoreAspectRatio))
        self.label_3.setPixmap(pixImg)
        
        # get more informations
        self.textEdit_3.clear()
        result_more = BaiduSpider().search_zhidao(keyword).plain
        for i in range(5):
            # self.textEdit_3.append("- " + result_more[i]['title'])
            # self.textEdit_3.append(result_more[i]['url'])
            s = '<a href="{}" style="color:#3232CD;font-size:15px;font-family:Microsoft YaHei"><b>{}</b></a>'.format(result_more[i]['url'], result_more[i]['title'])
            self.textEdit_3.append("- "+s)

if __name__=="__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QMainWindow()
    ui=Ui_Form()    
    ui.setupUi(widget)
    widget.show()
    
    sys.exit(app.exec_())

