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


def bt_dang41_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các tham số đảm bảo nghiệm luôn nguyên và bài toán có nghĩa
                t_1 = random.randint(2, 5) # Căn bậc hai của (A - x) tại điểm cực đại
                k = random.choice([3, 6])  # Hệ số của chi phí vận hành (đảm bảo k chia hết cho 3 để nghiệm nguyên)
                B = random.randint(5, 20)  # Chi phí cố định

                # Tính toán các hệ số dựa trên t_1 và k
                A = 3 * t_1**2 + 2 * k * t_1
                x_max = A - t_1**2

                B_plus_kA = B + k * A
                k2 = 2 * k
                k_3 = int(k2 / 3)
                A_3 = int(A / 3)
                t_2 = -k_3 - t_1
                abs_t_2 = abs(t_2)

                kq = x_max

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da= random.choice(du)

                # Tạo các phương án sai ngẫu nhiên, đảm bảo không trùng nhau và lớn hơn 0
                s = []
                while len(s) < 6:
                    sai = kq + random.choice([-10, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 10, 15, 20])
                    if sai > 0 and sai != kq and ('$%s$' % sai) not in s:
                        s.append('$%s$' % sai)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (185.4,77.4) .. controls (199.4,29.4) and (256.4,44.9) .. (261.9,66.4) .. controls (256.9,70.4) and (253.4,70.4) .. (248.09,73.61) .. controls (229.9,48.9) and (193.9,66.4) .. (198.4,95.4) .. controls (176.9,76.4) and (145.4,117.9) .. (182.4,131.9) .. controls (142.4,140.9) and (140.4,76.4) .. (185.4,77.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (151.2,119.5) .. controls (170.97,151.83) and (196.9,136.4) .. (217.4,106.4) .. controls (239.4,69.9) and (294.4,51.9) .. (299.9,108.4) .. controls (272.4,62.9) and (244.9,102.4) .. (224.4,129.4) .. controls (210.4,150.4) and (163.4,163.9) .. (151.2,119.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 63; green, 181; blue, 155 }  ,fill opacity=1 ] (261.9,66.4) .. controls (257.3,69.44) and (252.8,71.98) .. (248.6,74.27) .. controls (237.4,55.9) and (197.4,56.4) .. (198.4,95.4) .. controls (195.9,43.9) and (253.4,48.4) .. (261.9,66.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 63; green, 181; blue, 155 }  ,fill opacity=0.44 ] (185.4,77.4) .. controls (167.4,77.9) and (143.4,113.9) .. (182.4,131.9) .. controls (137.4,136.4) and (145.9,76.4) .. (185.4,77.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 56; green, 166; blue, 141 }  ,fill opacity=0.63 ] (151.2,119.5) .. controls (164.4,160.4) and (202.4,144.4) .. (225.4,112.9) .. controls (244.67,83.4) and (286.4,60.4) .. (299.9,108.4) .. controls (272.4,62.9) and (244.9,102.4) .. (224.4,129.4) .. controls (210.4,150.4) and (163.4,163.9) .. (151.2,119.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (272.36,124.55) .. controls (270.55,130.68) and (264.75,135.17) .. (257.87,135.17) .. controls (249.55,135.17) and (242.8,128.6) .. (242.8,120.49) .. controls (242.8,112.37) and (249.55,105.8) .. (257.87,105.8) .. controls (262.28,105.8) and (266.24,107.64) .. (269,110.58) -- (264.33,114.74) .. controls (262.72,113.08) and (260.42,112.05) .. (257.87,112.05) .. controls (253,112.05) and (249.05,115.83) .. (249.05,120.49) .. controls (249.05,125.14) and (253,128.92) .. (257.87,128.92) .. controls (261.88,128.92) and (265.27,126.36) .. (266.34,122.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (260.03,118.92) -- (272.39,118.92) -- (272.39,125.13) -- (260.03,125.13) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (274.71,119.41) -- (281.2,119.41) -- (281.2,134.85) -- (274.71,134.85) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ,even odd rule] (287.9,127.01) .. controls (287.9,125.35) and (289.34,124) .. (291.12,124) .. controls (292.9,124) and (294.34,125.35) .. (294.34,127.01) .. controls (294.34,128.67) and (292.9,130.02) .. (291.12,130.02) .. controls (289.34,130.02) and (287.9,128.67) .. (287.9,127.01)(282.82,127.01) .. controls (282.82,122.54) and (286.53,118.92) .. (291.12,118.92) .. controls (295.71,118.92) and (299.42,122.54) .. (299.42,127.01) .. controls (299.42,131.48) and (295.71,135.1) .. (291.12,135.1) .. controls (286.53,135.1) and (282.82,131.48) .. (282.82,127.01) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (296.18,119.29) -- (302.66,119.29) -- (302.66,138.06) -- (296.18,138.06) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (302.27,136.02) .. controls (302.17,137.18) and (301.86,138.34) .. (301.31,139.45) .. controls (298.86,144.45) and (292.68,146.55) .. (287.52,144.14) .. controls (284.72,142.84) and (282.79,140.48) .. (282,137.8) -- (287.24,136.38) .. controls (287.64,137.61) and (288.56,138.7) .. (289.88,139.32) .. controls (292.36,140.47) and (295.3,139.52) .. (296.44,137.19) .. controls (296.7,136.65) and (296.85,136.1) .. (296.89,135.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ,even odd rule] (309.67,127.01) .. controls (309.67,125.35) and (311.11,124) .. (312.89,124) .. controls (314.67,124) and (316.11,125.35) .. (316.11,127.01) .. controls (316.11,128.67) and (314.67,130.02) .. (312.89,130.02) .. controls (311.11,130.02) and (309.67,128.67) .. (309.67,127.01)(304.59,127.01) .. controls (304.59,122.54) and (308.3,118.92) .. (312.89,118.92) .. controls (317.47,118.92) and (321.19,122.54) .. (321.19,127.01) .. controls (321.19,131.48) and (317.47,135.1) .. (312.89,135.1) .. controls (308.3,135.1) and (304.59,131.48) .. (304.59,127.01) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (317.72,119.78) -- (324.2,119.78) -- (324.2,134.85) -- (317.72,134.85) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (357.92,129.24) .. controls (355.2,133.12) and (350.63,135.66) .. (345.45,135.66) .. controls (337.13,135.66) and (330.38,129.09) .. (330.38,120.98) .. controls (330.38,112.87) and (337.13,106.29) .. (345.45,106.29) .. controls (349.86,106.29) and (353.82,108.14) .. (356.58,111.07) -- (351.91,115.23) .. controls (350.3,113.58) and (348,112.54) .. (345.45,112.54) .. controls (340.58,112.54) and (336.63,116.32) .. (336.63,120.98) .. controls (336.63,125.64) and (340.58,129.41) .. (345.45,129.41) .. controls (348.46,129.41) and (351.11,127.98) .. (352.7,125.79) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (360.01,105.85) -- (366.5,105.85) -- (366.5,134.85) -- (360.01,134.85) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ,even odd rule] (373.96,127.5) .. controls (373.96,125.84) and (375.4,124.49) .. (377.18,124.49) .. controls (378.96,124.49) and (380.4,125.84) .. (380.4,127.5) .. controls (380.4,129.16) and (378.96,130.51) .. (377.18,130.51) .. controls (375.4,130.51) and (373.96,129.16) .. (373.96,127.5)(368.88,127.5) .. controls (368.88,123.03) and (372.59,119.41) .. (377.18,119.41) .. controls (381.77,119.41) and (385.48,123.03) .. (385.48,127.5) .. controls (385.48,131.97) and (381.77,135.59) .. (377.18,135.59) .. controls (372.59,135.59) and (368.88,131.97) .. (368.88,127.5) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ,even odd rule] (412.43,127.5) .. controls (412.43,125.84) and (413.87,124.49) .. (415.65,124.49) .. controls (417.43,124.49) and (418.88,125.84) .. (418.88,127.5) .. controls (418.88,129.16) and (417.43,130.51) .. (415.65,130.51) .. controls (413.87,130.51) and (412.43,129.16) .. (412.43,127.5)(407.35,127.5) .. controls (407.35,123.03) and (411.07,119.41) .. (415.65,119.41) .. controls (420.24,119.41) and (423.96,123.03) .. (423.96,127.5) .. controls (423.96,131.97) and (420.24,135.59) .. (415.65,135.59) .. controls (411.07,135.59) and (407.35,131.97) .. (407.35,127.5) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (421.02,105.85) -- (427.5,105.85) -- (427.5,134.85) -- (421.02,134.85) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (404.01,119.86) .. controls (405.27,121.29) and (406.11,123.11) .. (406.33,125.14) .. controls (406.91,130.42) and (403.06,135.15) .. (397.73,135.7) .. controls (392.41,136.26) and (387.62,132.43) .. (387.04,127.15) .. controls (386.72,124.29) and (387.71,121.6) .. (389.52,119.63) -- (394.14,123.84) .. controls (393.48,124.53) and (393.12,125.49) .. (393.23,126.5) .. controls (393.44,128.36) and (395.15,129.71) .. (397.05,129.51) .. controls (398.96,129.31) and (400.34,127.64) .. (400.14,125.78) .. controls (400.06,125.06) and (399.75,124.41) .. (399.29,123.91) -- cycle ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một công ty GigaCloud có mô hình số doanh nghiệp đăng ký theo giá cước $x$ là $S\left(x\right) = \sqrt{%s - x}$ (nghìn doanh nghiệp), $x < %s$ ($x$ tính bằng triệu đồng). Chi phí cố định: $%s$ tỉ đồng/tháng. Chi phí vận hành, bảo mật và bảo trì tăng theo bình phương số khách hàng: $C_v = %sS^2$ (tỉ đồng). Mức giá cước $x$ để lợi nhuận ròng hàng tháng lớn nhất bằng bao nhiêu?}{%s}'''
                                 % (latex(A), latex(A), latex(B), latex(k),hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('- Gọi doanh thu hàng tháng là $R\\left(x\\right)$. Vì $x$ tính bằng triệu đồng và $S\\left(x\\right)$ tính bằng nghìn doanh nghiệp nên doanh thu tính theo tỉ đồng là:\\\\\n'
                           '$R\\left(x\\right) = x \\cdot S\\left(x\\right) = x\\sqrt{%s - x}$.\\\\\n'
                           '- Tổng chi phí hàng tháng:\\\\\n'
                           '$C\\left(x\\right) = %s + %sS^2 = %s + %s\\left(%s - x\\right) = %s - %sx$.\\\\\n'
                           '- Lợi nhuận ròng:\\\\\n'
                           '$P\\left(x\\right) = R\\left(x\\right) - C\\left(x\\right) = x\\sqrt{%s - x} - \\left(%s - %sx\\right) = x\\sqrt{%s - x} + %sx - %s$.\\\\\n'
                           '- Đặt $t = \\sqrt{%s - x} > 0 \\Rightarrow x = %s - t^2$.\\\\\n'
                           'Khi đó: $P = \\left(%s - t^2\\right)t + %s\\left(%s - t^2\\right) - %s = -t^3 - %st^2 + %st - %s$.\\\\\n'
                           '- Xét đạo hàm theo $t$:\\\\\n'
                           '$P\'\\left(t\\right) = -3t^2 - %st + %s = -3\\left(t^2 + %st - %s\\right)$.\\\\\n'
                           '- Giải $P\'\\left(t\\right) = 0$:\\\\\n'
                           '$t^2 + %st - %s = 0 \\Rightarrow \\left(t - %s\\right)\\left(t + %s\\right) = 0 \\Rightarrow t = %s$ hoặc $t = %s$.\\\\\n'
                           'Vì $t = \\sqrt{%s - x} > 0$ nên nhận $t = %s$.\\\\\n'
                           '- Suy ra $x = %s - t^2 = %s - %s^2 = %s$.\\\\\n'
                           '- Nhận xét: Khi $t$ tăng qua $%s$, $P\'\\left(t\\right)$ đổi dấu từ dương sang âm (vì hệ số của $t^2$ trong $P\'\\left(t\\right)$ âm), nên $t = %s$ cho lợi nhuận lớn nhất.\\\\\n'
                           'Vậy GigaCloud nên niêm yết mức giá $x = %s$ triệu đồng/tháng.'
                           % (latex(A),
                              latex(B), latex(k), latex(B), latex(k), latex(A), latex(B_plus_kA), latex(k),
                              latex(A), latex(B_plus_kA), latex(k), latex(A), latex(k), latex(B_plus_kA),
                              latex(A), latex(A),
                              latex(A), latex(k), latex(A), latex(B_plus_kA), latex(k), latex(A), latex(B),
                              latex(k2), latex(A), latex(k_3), latex(A_3),
                              latex(k_3), latex(A_3), latex(t_1), latex(abs_t_2), latex(t_1), latex(t_2),
                              latex(A), latex(t_1),
                              latex(A), latex(A), latex(t_1), latex(x_max),
                              latex(t_1), latex(t_1),
                              latex(x_max)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(x_max))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

