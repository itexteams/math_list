import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang57_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tổng số cầu thủ (từ 11 đến 25 cầu thủ)
                n = random.randint(11, 25)

                # Tính số phần tử không gian mẫu (Chỉnh hợp chập 3 của n)
                omega = n * (n - 1) * (n - 2)

                # Số kết quả thuận lợi luôn là 2 (dựa theo việc liệt kê các hoán vị không có điểm bất động của 3 người)
                k = 2

                # Tính xác suất và rút gọn phân số a/b
                P = Rational(k, omega)
                a = P.p
                b = P.q

                # Kết quả cần tìm b - a
                kq = b - a

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo danh sách các đáp án sai (đảm bảo không trùng với đáp án đúng và luôn dương)
                s_raw = [kq + 1, kq - 1, kq + 2, kq - 2, kq + 10, kq - 10, b + a, b]
                s_unique = list(set([x for x in s_raw if x != kq and x > 0]))
                random.shuffle(s_unique)

                s = ['$%s$'%(latex(s_unique[0])),
                     '$%s$'%(latex(s_unique[1])),
                     '$%s$'%(latex(s_unique[2])),
                     '$%s$'%(latex(s_unique[3])),
                     '$%s$'%(latex(s_unique[4]))]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.45 ] (185.88,194.32) .. controls (185.88,186.95) and (210.53,180.97) .. (240.94,180.97) .. controls (271.35,180.97) and (296,186.95) .. (296,194.32) .. controls (296,201.69) and (271.35,207.66) .. (240.94,207.66) .. controls (210.53,207.66) and (185.88,201.69) .. (185.88,194.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.45 ] (203.88,192.05) .. controls (203.88,185.94) and (220.47,180.97) .. (240.94,180.97) .. controls (261.41,180.97) and (278,185.94) .. (278,192.05) .. controls (278,198.17) and (261.41,203.13) .. (240.94,203.13) .. controls (220.47,203.13) and (203.88,198.17) .. (203.88,192.05) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.11 ][fill={rgb, 255:red, 225; green, 222; blue, 222 }  ,fill opacity=1 ] (174.3,134.65) .. controls (174.3,98.61) and (203.51,69.4) .. (239.55,69.4) .. controls (275.59,69.4) and (304.8,98.61) .. (304.8,134.65) .. controls (304.8,170.69) and (275.59,199.9) .. (239.55,199.9) .. controls (203.51,199.9) and (174.3,170.69) .. (174.3,134.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.37 ] (177.8,127.65) .. controls (177.8,96.03) and (203.43,70.4) .. (235.05,70.4) .. controls (266.67,70.4) and (292.3,96.03) .. (292.3,127.65) .. controls (292.3,159.27) and (266.67,184.9) .. (235.05,184.9) .. controls (203.43,184.9) and (177.8,159.27) .. (177.8,127.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.37 ] (188.3,112.4) .. controls (188.3,89.2) and (207.1,70.4) .. (230.3,70.4) .. controls (253.5,70.4) and (272.3,89.2) .. (272.3,112.4) .. controls (272.3,135.6) and (253.5,154.4) .. (230.3,154.4) .. controls (207.1,154.4) and (188.3,135.6) .. (188.3,112.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (238.1,102.9) -- (266.1,121.4) -- (255.6,151.9) -- (221.1,152.4) -- (212.6,120.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (219.6,72.4) .. controls (223.6,69.9) and (240.45,65.65) .. (259.95,72.65) .. controls (261.9,76.15) and (261.05,74.15) .. (262.53,78.89) .. controls (240.7,81.65) and (261.7,78.9) .. (239.55,81.65) .. controls (231.05,79.9) and (230.05,79.9) .. (217.05,78.65) .. controls (219.05,72.9) and (217.55,78.4) .. (219.6,72.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (188.95,92.9) .. controls (196.2,93.15) and (188.7,92.65) .. (196.2,92.9) .. controls (190.7,114.4) and (196.2,92.65) .. (190.45,114.9) .. controls (179.2,137.15) and (189.95,115.4) .. (179.45,137.4) .. controls (179.45,136.9) and (174.2,133.65) .. (174.2,132.9) .. controls (174.95,117.15) and (176.45,110.65) .. (188.95,92.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (186.2,160.9) .. controls (197.95,167.4) and (196.45,167.4) .. (208.95,172.4) .. controls (217.45,182.4) and (219.95,185.4) .. (225.45,190.4) .. controls (221.7,193.9) and (222.7,192.9) .. (218.45,196.4) .. controls (205.2,192.9) and (189.45,179.9) .. (183.7,168.65) .. controls (185.2,164.4) and (184.2,166.4) .. (186.2,160.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (271.9,171.15) .. controls (289.25,163.9) and (281.7,166.65) .. (294.35,160.4) .. controls (296.35,167.9) and (296.4,166.4) .. (296.15,167.4) .. controls (289.5,183.9) and (270.5,193.65) .. (262.9,195.65) .. controls (256.9,191.65) and (260.1,193.15) .. (255.1,189.9) .. controls (269.1,174.15) and (264.9,180.15) .. (271.9,171.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (282.85,91.4) .. controls (289.85,92.65) and (282.85,91.4) .. (289.9,92.35) .. controls (303.1,111.65) and (302.6,118.15) .. (304.85,131.15) .. controls (299.35,135.65) and (303.35,132.65) .. (299.1,135.15) .. controls (293.85,125.65) and (297.35,132.15) .. (287.35,113.9) .. controls (285.6,103.9) and (284.6,100.15) .. (282.85,91.4) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (239.55,81.65) -- (238.1,102.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (262.53,78.89) -- (282.85,91.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (217.05,78.65) -- (196.2,92.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (287.35,113.9) -- (266.1,121.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (190.45,114.9) -- (212.6,120.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (178.95,136.15) -- (186.2,160.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (221.1,152.4) -- (208.95,172.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (271.9,171.15) -- (255.6,151.9) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.15 ]   (294.35,160.4) -- (299.1,135.15) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.12 ]   (225.45,190.4) -- (255.1,189.9) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.79 ] (239.55,81.65) -- (238.1,102.9) -- (213.95,120.9) -- (190.45,114.9) -- (213.2,119.15) -- (235.95,102.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (239.55,81.65) -- (241.2,101.9) -- (256.7,115.15) -- (238.1,102.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (284.95,103.9) -- (287.35,113.9) -- (266.1,121.4) -- (284.7,112.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (238.35,152.15) -- (222.2,154.9) -- (212.95,166.15) -- (221.1,152.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (180.95,144.15) -- (178.2,137.9) -- (175.95,134.9) -- (179.45,137.4) -- cycle ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (217.05,77.65) -- (194.7,93.15) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.77 ] (238.45,103.9) -- (228.95,113.4) -- (225.7,115.9) -- (215.45,121.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.77 ] (194.2,94.9) -- (189.7,112.15) -- (189.45,107.65) -- (192.2,96.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.77 ] (230.7,76.9) -- (233.7,78.9) -- (219.7,77.65) -- (223.7,76.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (300.2,113.15) -- (303.7,128.9) -- (300.95,130.65) -- (298.45,115.65) -- (291.95,98.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (292.7,167.9) -- (294.2,168.9) -- (287.7,178.4) -- (276.45,188.15) -- (262.9,195.65) -- (257.7,189.9) -- (272.45,183.9) -- (281.7,177.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (222.7,190.4) -- (217.95,194.9) -- (204.95,188.65) -- (193.95,180.15) -- (185.45,170.4) -- (186.2,166.2) -- (196.45,175.4) -- (206.7,182.4) -- cycle ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (185.5,162.9) -- (179.45,137.4) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (271.38,172.53) -- (255.6,151.9) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (272.9,171.15) -- (255.6,151.9) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.71 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ]   (262.53,78.89) -- (285,91.65) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.08 ] (179.8,119.6) .. controls (179.8,95.3) and (205.99,75.6) .. (238.3,75.6) .. controls (270.61,75.6) and (296.8,95.3) .. (296.8,119.6) .. controls (296.8,143.9) and (270.61,163.6) .. (238.3,163.6) .. controls (205.99,163.6) and (179.8,143.9) .. (179.8,119.6) -- cycle ;
            \end{tikzpicture}'''

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Trong một trận đấu để gây quỹ từ thiện, cả Messi, Ronaldo và Maguire đều có mặt trong đội hình xuất phát của một đội bóng. Huấn luyện viên quan tâm đến 3 vị trí trên sân là thủ môn, tiền vệ phòng ngự, tiền đạo cắm, mỗi vị trí cần duy nhất một cầu thủ đảm nhiệm. Đây là trận đấu mà yếu tố chuyên môn không được đặt nặng nên huấn luyện viên sử dụng máy tính để chọn ngẫu nhiên ra 3 cầu thủ từ $%s$ cầu thủ trong đội hình xuất phát đảm nhiệm 3 vị trí kể trên. Biết rằng Messi không thích làm thủ môn, Ronaldo thì không thích đá tiền vệ phòng ngự, còn Maguire thì không thích đá vị trí tiền đạo cắm. Xác suất để cả Messi, Ronaldo và Maguire đều hài lòng sau khi 3 vị trí này được máy tính lựa chọn bằng $\frac{a}{b}$ (trong đó hai số dương $a, b$ là nguyên tố cùng nhau); hiệu $b - a$ bằng bao nhiêu?}{%s}'''
                                 %(latex(n),hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Không gian mẫu là số cách chọn ra 3 cầu thủ từ $%s$ cầu thủ và phân công vào 3 vị trí phân biệt. \\\\
                         Số phần tử của không gian mẫu là: $n\\left(\\Omega\\right) = A_{%s}^3 = %s$. \\\\
                         Gọi biến cố $X$: "Cả Messi, Ronaldo và Maguire đều được chọn và đều hài lòng với vị trí của mình". \\\\
                         Để biến cố $X$ xảy ra, 3 người được chọn bắt buộc phải là Messi, Ronaldo và Maguire. \\\\
                         Gọi 3 vị trí thủ môn, tiền vệ phòng ngự, tiền đạo cắm lần lượt là $V_1, V_2, V_3$. \\\\
                         Có $3! = 6$ cách xếp 3 người vào 3 vị trí. Ta xét các ràng buộc: \\\\
                         - Messi không thích làm thủ môn (không xếp vào $V_1$). \\\\
                         - Ronaldo không thích đá tiền vệ phòng ngự (không xếp vào $V_2$). \\\\
                         - Maguire không thích đá vị trí tiền đạo cắm (không xếp vào $V_3$). \\\\
                         Bằng cách liệt kê, chỉ có $2$ trường hợp xếp thoả mãn yêu cầu là: \\\\
                         + Trường hợp 1: Ronaldo làm thủ môn ($V_1$), Maguire đá tiền vệ phòng ngự ($V_2$), Messi đá tiền đạo cắm ($V_3$). \\\\
                         + Trường hợp 2: Maguire làm thủ môn ($V_1$), Messi đá tiền vệ phòng ngự ($V_2$), Ronaldo đá tiền đạo cắm ($V_3$). \\\\
                         Do đó, số kết quả thuận lợi cho biến cố $X$ là: $n\\left(X\\right) = 2$. \\\\
                         Xác suất cần tìm là: $P = \\frac{n\\left(X\\right)}{n\\left(\\Omega\\right)} = \\frac{2}{%s} = \\frac{%s}{%s}$. \\\\
                         Suy ra $a = %s, b = %s$. Vậy hiệu $b - a = %s - %s = %s$.'''
                         %(latex(n), latex(n), latex(omega),
                           latex(omega), latex(a), latex(b),
                           latex(a), latex(b), latex(b), latex(a), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

