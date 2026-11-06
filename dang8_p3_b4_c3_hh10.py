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


def bt_dang8_p3_b4_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1 & 3: Nghiên cứu đề bài và tìm cách random
                # a, b là các thông số của phương trình hypebol x^2/a^2 - y^2/b^2 = 1
                # h_tower là chiều cao tháp
                # Ở đề bài gốc: a=30, b=40, h_tower=120
                a_val = random.choice([15, 30, 45, 60])
                b_val = random.choice([20, 40, 60, 80])
                h_tower = random.choice([90, 120, 150, 180])

                # Tính toán OH và OK dựa trên điều kiện OH = 1/2 OK và OH + OK = h_tower
                # => OH = 1/3 * h_tower, OK = 2/3 * h_tower
                oh_val = Rational(h_tower, 3)
                ok_val = 2 * oh_val

                # Tính bán kính nóc (r1) tại y = oh_val: x^2/a^2 - oh^2/b^2 = 1 => x^2 = a^2 * (1 + oh^2/b^2)
                r1_sq = (a_val**2) * (1 + Rational(oh_val**2, b_val**2))
                r1_val = sqrt(r1_sq)

                # Tính bán kính đáy (r2) tại y = ok_val
                r2_sq = (a_val**2) * (1 + Rational(ok_val**2, b_val**2))     
                r2_val = sqrt(r2_sq)

                # Chuyển sang số thập phân và làm tròn 2 chữ số (hoặc giữ nguyên căn thức tùy ý)
                # Ở đây ta sẽ làm tròn để giống thực tế bài toán kỹ thuật
                kq_noc_num = round(float(r1_val), 0)
                kq_day_num = round(float(r2_val), 0)

                # Định dạng dấu phẩy cho số thập phân
                kq_noc = str(kq_noc_num).replace('.', ',')
                kq_day = str(kq_day_num).replace('.', ',')

                # Đáp án đúng
                da_dung = '$r_{nóc} \\approx %s$ m; $r_{đáy} \\approx %s$ m' % (kq_noc, kq_day)

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                du = [da_dung]
                da = du[0]

                s = [
                    '$r_{nóc} \\approx %s$ m; $r_{đáy} \\approx %s$ m' % (str(round(kq_noc_num + 5.5, 2)).replace('.', ','), str(round(kq_day_num + 10.2, 2)).replace('.', ',')),
                    '$r_{nóc} \\approx %s$ m; $r_{đáy} \\approx %s$ m' % (str(round(kq_noc_num - 3.1, 2)).replace('.', ','), str(round(kq_day_num - 5.4, 2)).replace('.', ',')),
                    '$r_{nóc} \\approx %s$ m; $r_{đáy} \\approx %s$ m' % (str(round(kq_noc_num + 2.8, 2)).replace('.', ','), str(round(kq_day_num - 2.1, 2)).replace('.', ',')),
                    '$r_{nóc} \\approx %s$ m; $r_{đáy} \\approx %s$ m' % (str(round(kq_noc_num * 1.2, 2)).replace('.', ','), str(round(kq_day_num * 1.1, 2)).replace('.', ',')),
                ]

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (103.36,188.4) -- (146.9,169.85) -- (286.21,169.85) -- (325.33,188.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 101; green, 186; blue, 15 }  ,fill opacity=1 ] (126.76,183.2) -- (151.42,169.9) -- (282.04,169.9) -- (303.53,183.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 189; green, 187; blue, 187 }  ,fill opacity=1 ] (154.31,170.4) .. controls (154.31,164.88) and (181.11,160.41) .. (214.16,160.41) .. controls (247.22,160.41) and (274.02,164.88) .. (274.02,170.4) .. controls (274.02,175.92) and (247.22,180.39) .. (214.16,180.39) .. controls (181.11,180.39) and (154.31,175.92) .. (154.31,170.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 192; green, 193; blue, 190 }  ,fill opacity=1 ] (155.1,55.7) -- (273.1,55.7) -- (273.1,170.41) -- (155.1,170.41) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (272.97,30.41) .. controls (226.8,77.42) and (227.15,124.08) .. (274.02,170.4) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (154.31,170.39) .. controls (201.32,123.96) and (201.54,77.3) .. (154.99,30.4) ;
            	\draw  [fill={rgb, 255:red, 183; green, 180; blue, 180 }  ,fill opacity=1 ] (175.6,55.61) .. controls (175.6,52.46) and (193,49.91) .. (214.47,49.91) .. controls (235.95,49.91) and (253.35,52.46) .. (253.35,55.61) .. controls (253.35,58.75) and (235.95,61.3) .. (214.47,61.3) .. controls (193,61.3) and (175.6,58.75) .. (175.6,55.61) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (169.74,173.31) .. controls (197.47,140.37) and (203.35,103.9) .. (187.38,63.9) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.41 ] (200.08,137.06) -- (223.34,175.67) -- (180.4,172.68) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 30; green, 28; blue, 28 }  ,fill opacity=0.17 ] (227.46,89.9) -- (207.93,66.67) -- (240.54,62.52) -- cycle ;
            	\draw  [draw opacity=0] (264.57,61.39) .. controls (253.94,63.93) and (236.62,65.59) .. (217.05,65.59) .. controls (195.62,65.59) and (176.87,63.6) .. (166.67,60.64) -- (217.05,55.5) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (264.57,61.39) .. controls (253.94,63.93) and (236.62,65.59) .. (217.05,65.59) .. controls (195.62,65.59) and (176.87,63.6) .. (166.67,60.64) ;  
            	\draw  [draw opacity=0] (268.79,76.02) .. controls (258.95,80.35) and (239.47,83.3) .. (217.05,83.3) .. controls (193.05,83.3) and (172.41,79.92) .. (163.38,75.09) -- (217.05,69.61) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (268.79,76.02) .. controls (258.95,80.35) and (239.47,83.3) .. (217.05,83.3) .. controls (193.05,83.3) and (172.41,79.92) .. (163.38,75.09) ;   
            	\draw  [draw opacity=0] (262.07,88.89) .. controls (251.44,91.43) and (234.12,93.09) .. (214.55,93.09) .. controls (193.12,93.09) and (174.37,91.1) .. (164.17,88.14) -- (214.55,83) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (262.07,88.89) .. controls (251.44,91.43) and (234.12,93.09) .. (214.55,93.09) .. controls (193.12,93.09) and (174.37,91.1) .. (164.17,88.14) ;  
            	\draw  [draw opacity=0] (263.07,99.89) .. controls (252.44,102.43) and (235.12,104.09) .. (215.55,104.09) .. controls (194.12,104.09) and (175.37,102.1) .. (165.17,99.14) -- (215.55,94) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (263.07,99.89) .. controls (252.44,102.43) and (235.12,104.09) .. (215.55,104.09) .. controls (194.12,104.09) and (175.37,102.1) .. (165.17,99.14) ;  
            	\draw  [draw opacity=0] (267.58,165.45) .. controls (257.54,168.52) and (238.45,170.59) .. (216.55,170.59) .. controls (192.38,170.59) and (171.63,168.07) .. (162.69,164.46) -- (216.55,160.5) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (267.58,165.45) .. controls (257.54,168.52) and (238.45,170.59) .. (216.55,170.59) .. controls (192.38,170.59) and (171.63,168.07) .. (162.69,164.46) ;  
            	\draw  [draw opacity=0] (269.08,154.95) .. controls (259.04,158.02) and (239.95,160.09) .. (218.05,160.09) .. controls (193.88,160.09) and (173.13,157.57) .. (164.19,153.96) -- (218.05,150) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (269.08,154.95) .. controls (259.04,158.02) and (239.95,160.09) .. (218.05,160.09) .. controls (193.88,160.09) and (173.13,157.57) .. (164.19,153.96) ;  
            	\draw  [draw opacity=0] (270.58,143.45) .. controls (260.54,146.52) and (241.45,148.59) .. (219.55,148.59) .. controls (195.38,148.59) and (174.63,146.07) .. (165.69,142.46) -- (219.55,138.5) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (270.58,143.45) .. controls (260.54,146.52) and (241.45,148.59) .. (219.55,148.59) .. controls (195.38,148.59) and (174.63,146.07) .. (165.69,142.46) ;  
            	\draw  [draw opacity=0] (267.58,130.95) .. controls (257.54,134.02) and (238.45,136.09) .. (216.55,136.09) .. controls (192.38,136.09) and (171.63,133.57) .. (162.69,129.96) -- (216.55,126) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (267.58,130.95) .. controls (257.54,134.02) and (238.45,136.09) .. (216.55,136.09) .. controls (192.38,136.09) and (171.63,133.57) .. (162.69,129.96) ;   
            	\draw  [draw opacity=0] (267.08,120.45) .. controls (257.04,123.52) and (237.95,125.59) .. (216.05,125.59) .. controls (191.88,125.59) and (171.13,123.07) .. (162.19,119.46) -- (216.05,115.5) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (267.08,120.45) .. controls (257.04,123.52) and (237.95,125.59) .. (216.05,125.59) .. controls (191.88,125.59) and (171.13,123.07) .. (162.19,119.46) ;  
            	\draw  [draw opacity=0] (265.13,109.36) .. controls (255.09,112.42) and (236,114.49) .. (214.1,114.49) .. controls (189.93,114.49) and (169.18,111.97) .. (160.24,108.37) -- (214.1,104.41) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (265.13,109.36) .. controls (255.09,112.42) and (236,114.49) .. (214.1,114.49) .. controls (189.93,114.49) and (169.18,111.97) .. (160.24,108.37) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.33 ] (217.58,53.28) .. controls (232.39,53.42) and (243.9,54.41) .. (243.9,55.61) .. controls (243.9,56.9) and (230.59,57.94) .. (214.17,57.94) .. controls (212.09,57.94) and (210.07,57.93) .. (208.11,57.89) -- cycle ;
            	\draw  [draw opacity=0][line width=4.5]  (273.64,167.91) .. controls (272.1,173.25) and (246.51,177.49) .. (215.16,177.49) .. controls (183.8,177.49) and (158.2,173.24) .. (156.69,167.9) -- (215.16,167.4) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.4 ][line width=4.5]  (273.64,167.91) .. controls (272.1,173.25) and (246.51,177.49) .. (215.16,177.49) .. controls (183.8,177.49) and (158.2,173.24) .. (156.69,167.9) ;  
            	\draw  [draw opacity=0][line width=3.75]  (254.78,60.3) .. controls (244.16,62.89) and (229.38,64.5) .. (213.04,64.5) .. controls (196.39,64.5) and (181.37,62.83) .. (170.71,60.16) -- (213.04,50.46) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ][line width=3.75]  (254.78,60.3) .. controls (244.16,62.89) and (229.38,64.5) .. (213.04,64.5) .. controls (196.39,64.5) and (181.37,62.83) .. (170.71,60.16) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (254.87,55.83) .. controls (251.26,52.66) and (250.91,47.16) .. (254.08,43.55) -- (275.33,19.36) .. controls (278.5,15.75) and (284,15.4) .. (287.61,18.57) -- (287.61,18.57) .. controls (291.22,21.74) and (291.57,27.24) .. (288.4,30.85) -- (267.15,55.04) .. controls (263.98,58.65) and (258.48,59) .. (254.87,55.83) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (140.46,19.96) .. controls (144.01,16.71) and (149.51,16.96) .. (152.76,20.51) -- (174.48,44.28) .. controls (177.72,47.83) and (177.47,53.33) .. (173.92,56.57) -- (173.92,56.57) .. controls (170.38,59.81) and (164.87,59.56) .. (161.63,56.02) -- (139.91,32.25) .. controls (136.67,28.7) and (136.92,23.2) .. (140.46,19.96) -- cycle ;
            	\draw  [draw opacity=0] (265.91,66.72) .. controls (256.07,71.05) and (236.59,73.99) .. (214.17,73.99) .. controls (190.17,73.99) and (169.53,70.62) .. (160.5,65.78) -- (214.17,60.3) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ] (265.91,66.72) .. controls (256.07,71.05) and (236.59,73.99) .. (214.17,73.99) .. controls (190.17,73.99) and (169.53,70.62) .. (160.5,65.78) ;  
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (214.17,55.61) -- (214.16,170.4) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (239.1,104.16) -- (189.1,104.66) ;
            	\draw   (213.27,55.51) .. controls (213.27,55.01) and (213.67,54.61) .. (214.17,54.61) .. controls (214.67,54.61) and (215.07,55.01) .. (215.07,55.51) .. controls (215.07,56) and (214.67,56.41) .. (214.17,56.41) .. controls (213.67,56.41) and (213.27,56) .. (213.27,55.51) -- cycle ;
            	\draw   (213.2,104.41) .. controls (213.2,103.91) and (213.6,103.51) .. (214.1,103.51) .. controls (214.6,103.51) and (215,103.91) .. (215,104.41) .. controls (215,104.9) and (214.6,105.31) .. (214.1,105.31) .. controls (213.6,105.31) and (213.2,104.9) .. (213.2,104.41) -- cycle ;
            	\draw   (213.27,170.51) .. controls (213.27,170.01) and (213.67,169.61) .. (214.17,169.61) .. controls (214.67,169.61) and (215.07,170.01) .. (215.07,170.51) .. controls (215.07,171) and (214.67,171.41) .. (214.17,171.41) .. controls (213.67,171.41) and (213.27,171) .. (213.27,170.51) -- cycle ;
            	\draw (215.55,94) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (214.5,33) node [anchor=north west][inner sep=0.75pt]    {$H$};
            	\draw (216.55,160.5) node [anchor=north west][inner sep=0.75pt]    {$K$};
            \end{tikzpicture}'''

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Một tháp làm mát ở một nhà máy có mặt cắt là một hypebol có phương trình $\\frac{x^2}{%s^2} - \\frac{y^2}{%s^2} = 1$. Cho biết chiều cao của tháp là $%s$ m và khoảng cách $OH$ từ tâm đối xứng đến nóc tháp bằng một nửa khoảng cách $OK$ từ tâm đối xứng đến đáy. Bán kính đường tròn đáy của tháp bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).}{%s}'''
                                 %(latex(a_val), latex(b_val), latex(h_tower),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Lời giải chi tiết
                loigiai = ('''Chọn hệ trục tọa độ sao cho tâm đối xứng của hypebol trùng với gốc tọa độ $O\\left(0; 0\\right)$, trục thực nằm trên trục $Ox$. \\\\
                             Gọi chiều cao tháp là $h = %s$ m. \\\\
                             Theo đề bài, ta có $OH + OK = h$ và $OH = \\frac{1}{2} OK$. \\\\
                             Suy ra $OH = \\frac{1}{3} h = \\frac{1}{3} \\cdot %s = %s$ m và $OK = \\frac{2}{3} h = \\frac{2}{3} \\cdot %s = %s$ m. \\\\
                             Vì nóc tháp và đáy tháp nằm ở hai phía đối với tâm đối xứng $O$, nên nếu chọn nóc ở phía trên thì tọa độ $y$ của nóc là $y_H = %s$ và tọa độ $y$ của đáy là $y_K = -%s$. \\\\
                             Bán kính đường tròn nóc tháp $r$ là giá trị $x > 0$ ứng với $y = %s$: \\\\
                             $\\frac{x^2}{%s^2} - \\frac{%s^2}{%s^2} = 1 \\Rightarrow x^2 = %s^2 \\cdot \\left(1 + \\frac{%s^2}{%s^2}\\right) = %s \\Rightarrow x = %s \\approx %s$ m. \\\\
                             Bán kính đường tròn đáy tháp $R$ là giá trị $x > 0$ ứng với $y = -%s$: \\\\
                             $\\frac{x^2}{%s^2} - \\frac{\\left(-%s\\right)^2}{%s^2} = 1 \\Rightarrow x^2 = %s^2 \\cdot \\left(1 + \\frac{%s^2}{%s^2}\\right) = %s \\Rightarrow x = %s \\approx %s$ m. \\\\
                             Vậy bán kính đáy tháp khoảng $%s$ m.'''
                          %(latex(h_tower), latex(h_tower), latex(oh_val), latex(h_tower), latex(ok_val),
                            latex(oh_val), latex(ok_val),
                            latex(oh_val), latex(a_val), latex(oh_val), latex(b_val), latex(a_val), latex(oh_val), latex(b_val), latex(r1_sq), latex(r1_val), kq_noc,
                            latex(ok_val), latex(a_val), latex(ok_val), latex(b_val), latex(a_val), latex(ok_val), latex(b_val), latex(r2_sq), latex(r2_val), kq_day,
                            kq_day))
                dapan='\\shortans[0]{$%s$}\n'%(str(kq_day))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace(',0$', '$')
            return content 

