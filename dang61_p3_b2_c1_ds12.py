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


def bt_dang61_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số của bài toán: (Đỉnh H, cách trục x1, độ cao y1, thanh ngang h)
                # Đảm bảo bài toán ra số tương đối đẹp và thực tế
                params = [(15, 5, 10, 3), (12, 4, 8, 2), (18, 6, 12, 4), (20, 5, 15, 5), (16, 4, 12, 4)]
                H, x1, y1, h = random.choice(params)

                # Tính toán các hệ số
                # Phương trình parabol: y = a*x^2 + H. Đi qua (x1, y1) => a*x1^2 + H = y1 => a = (y1 - H) / x1^2
                a_val = Rational(y1 - H, x1**2)

                # Chiều cao h(x) = y - h = a*x^2 + H - h
                C = H - h

                # Diện tích S(x) = 2x * h(x) = 2*a*x^3 + 2*C*x
                a2 = 2 * a_val
                C2 = 2 * C

                # Đạo hàm S'(x) = 6*a*x^2 + 2*C. Cho S'(x) = 0 => x^2 = -2C / 6a = -C / 3a
                a6 = 6 * a_val
                x_sq = Rational(-C2, a6)
                x_opt = sqrt(x_sq)

                # Diện tích Max
                max_area = a2 * (x_opt**3) + C2 * x_opt

                # Làm tròn đến hàng đơn vị
                max_area_float = float(max_area)
                kq_rounded = round(max_area_float)
                kq_str = str(kq_rounded)

                # Các đáp án trắc nghiệm (Tạo phương án nguyên)
                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
                options_val = [
                    kq_rounded + 1, 
                    kq_rounded - 1, 
                    kq_rounded + 2, 
                    kq_rounded - 2, 
                    kq_rounded + 3
                ]
                random.shuffle(options_val)

                s = ['$%s$' % (str(opt)) for opt in options_val[:3]]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Một bảo tàng khoa học muốn lắp đặt một cửa sổ trang trí lớn hình parabol trên bức tường phía tây của tòa nhà. Cửa sổ này có đỉnh cao nhất cách sàn nhà $%s$ mét. Một điểm trên khung cửa sổ cách trục đối xứng cửa sổ $%s$ mét và có độ cao $%s$ mét so với sàn nhà. Bên trong khung cửa sổ, người thiết kế muốn đặt một tấm kính màu, hình chữ nhật với hai đỉnh trên của tấm kính nằm trên đường cong của khung cửa sổ và hai đỉnh dưới của tấm kính nằm trên một thanh ngang cố định cách sàn nhà $%s$ mét (song song với sàn nhà). Diện tích lớn nhất của tấm kính màu là bao nhiêu mét vuông? (Kết quả làm tròn đến hàng đơn vị).}
                                 {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                 	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 221 }  ,fill opacity=1 ] (178.43,32.86) -- (282.57,32.86) -- (282.57,223.92) -- (178.43,223.92) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 227; green, 224; blue, 219 }  ,fill opacity=1 ] (176.4,32.86) -- (284.6,32.86) -- (284.6,25.6) -- (176.4,25.6) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 228; green, 226; blue, 221 }  ,fill opacity=1 ] (179.38,32.86) -- (282.57,32.86) -- (282.57,222.94) -- (179.38,222.94) -- cycle ; \\draw  [color={rgb, 255:red, 207; green, 202; blue, 195 }  ,draw opacity=1 ] (179.38,32.86) -- (179.38,222.94)(184.38,32.86) -- (184.38,222.94)(189.38,32.86) -- (189.38,222.94)(194.38,32.86) -- (194.38,222.94)(199.38,32.86) -- (199.38,222.94)(204.38,32.86) -- (204.38,222.94)(209.38,32.86) -- (209.38,222.94)(214.38,32.86) -- (214.38,222.94)(219.38,32.86) -- (219.38,222.94)(224.38,32.86) -- (224.38,222.94)(229.38,32.86) -- (229.38,222.94)(234.38,32.86) -- (234.38,222.94)(239.38,32.86) -- (239.38,222.94)(244.38,32.86) -- (244.38,222.94)(249.38,32.86) -- (249.38,222.94)(254.38,32.86) -- (254.38,222.94)(259.38,32.86) -- (259.38,222.94)(264.38,32.86) -- (264.38,222.94)(269.38,32.86) -- (269.38,222.94)(274.38,32.86) -- (274.38,222.94)(279.38,32.86) -- (279.38,222.94) ; \\draw  [color={rgb, 255:red, 207; green, 202; blue, 195 }  ,draw opacity=1 ] (179.38,32.86) -- (282.57,32.86)(179.38,37.86) -- (282.57,37.86)(179.38,42.86) -- (282.57,42.86)(179.38,47.86) -- (282.57,47.86)(179.38,52.86) -- (282.57,52.86)(179.38,57.86) -- (282.57,57.86)(179.38,62.86) -- (282.57,62.86)(179.38,67.86) -- (282.57,67.86)(179.38,72.86) -- (282.57,72.86)(179.38,77.86) -- (282.57,77.86)(179.38,82.86) -- (282.57,82.86)(179.38,87.86) -- (282.57,87.86)(179.38,92.86) -- (282.57,92.86)(179.38,97.86) -- (282.57,97.86)(179.38,102.86) -- (282.57,102.86)(179.38,107.86) -- (282.57,107.86)(179.38,112.86) -- (282.57,112.86)(179.38,117.86) -- (282.57,117.86)(179.38,122.86) -- (282.57,122.86)(179.38,127.86) -- (282.57,127.86)(179.38,132.86) -- (282.57,132.86)(179.38,137.86) -- (282.57,137.86)(179.38,142.86) -- (282.57,142.86)(179.38,147.86) -- (282.57,147.86)(179.38,152.86) -- (282.57,152.86)(179.38,157.86) -- (282.57,157.86)(179.38,162.86) -- (282.57,162.86)(179.38,167.86) -- (282.57,167.86)(179.38,172.86) -- (282.57,172.86)(179.38,177.86) -- (282.57,177.86)(179.38,182.86) -- (282.57,182.86)(179.38,187.86) -- (282.57,187.86)(179.38,192.86) -- (282.57,192.86)(179.38,197.86) -- (282.57,197.86)(179.38,202.86) -- (282.57,202.86)(179.38,207.86) -- (282.57,207.86)(179.38,212.86) -- (282.57,212.86)(179.38,217.86) -- (282.57,217.86)(179.38,222.86) -- (282.57,222.86) ; \\draw  [color={rgb, 255:red, 207; green, 202; blue, 195 }  ,draw opacity=1 ]  ;
                                 	\\draw  [color={rgb, 255:red, 190; green, 184; blue, 175 }  ,draw opacity=1 ][line width=3]  (262.1,158.9) .. controls (241.03,20.63) and (219.97,20.63) .. (198.9,158.9) ;
                                 	\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 140; green, 236; blue, 237 }  ,fill opacity=1 ][line width=1.5]  (259.38,158.9) .. controls (240.13,24.18) and (220.87,24.18) .. (201.62,158.9) ;
                                 	\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 84; green, 154; blue, 237 }  ,fill opacity=1 ][line width=1.5]  (214.38,92.86) -- (247.92,92.86) -- (247.92,138.84) -- (214.38,138.84) -- cycle ;
                                 	\\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1.5]    (205.55,139.04) -- (256.75,138.64) ;
                                 	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 221 }  ,fill opacity=1 ] (156.28,162.66) -- (303.72,162.66) -- (303.72,226.6) -- (156.28,226.6) -- cycle ;
                                 	\\draw  [fill={rgb, 255:red, 237; green, 233; blue, 226 }  ,fill opacity=1 ] (153.4,166.86) -- (306.6,166.86) -- (306.6,159) -- (153.4,159) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 228; green, 226; blue, 221 }  ,fill opacity=1 ] (157.61,166.86) -- (303.72,166.86) -- (303.72,226.6) -- (157.61,226.6) -- cycle ; \\draw  [color={rgb, 255:red, 220; green, 216; blue, 208 }  ,draw opacity=1 ] (157.61,166.86) -- (157.61,226.6)(162.61,166.86) -- (162.61,226.6)(167.61,166.86) -- (167.61,226.6)(172.61,166.86) -- (172.61,226.6)(177.61,166.86) -- (177.61,226.6)(182.61,166.86) -- (182.61,226.6)(187.61,166.86) -- (187.61,226.6)(192.61,166.86) -- (192.61,226.6)(197.61,166.86) -- (197.61,226.6)(202.61,166.86) -- (202.61,226.6)(207.61,166.86) -- (207.61,226.6)(212.61,166.86) -- (212.61,226.6)(217.61,166.86) -- (217.61,226.6)(222.61,166.86) -- (222.61,226.6)(227.61,166.86) -- (227.61,226.6)(232.61,166.86) -- (232.61,226.6)(237.61,166.86) -- (237.61,226.6)(242.61,166.86) -- (242.61,226.6)(247.61,166.86) -- (247.61,226.6)(252.61,166.86) -- (252.61,226.6)(257.61,166.86) -- (257.61,226.6)(262.61,166.86) -- (262.61,226.6)(267.61,166.86) -- (267.61,226.6)(272.61,166.86) -- (272.61,226.6)(277.61,166.86) -- (277.61,226.6)(282.61,166.86) -- (282.61,226.6)(287.61,166.86) -- (287.61,226.6)(292.61,166.86) -- (292.61,226.6)(297.61,166.86) -- (297.61,226.6)(302.61,166.86) -- (302.61,226.6) ; \\draw  [color={rgb, 255:red, 220; green, 216; blue, 208 }  ,draw opacity=1 ] (157.61,166.86) -- (303.72,166.86)(157.61,171.86) -- (303.72,171.86)(157.61,176.86) -- (303.72,176.86)(157.61,181.86) -- (303.72,181.86)(157.61,186.86) -- (303.72,186.86)(157.61,191.86) -- (303.72,191.86)(157.61,196.86) -- (303.72,196.86)(157.61,201.86) -- (303.72,201.86)(157.61,206.86) -- (303.72,206.86)(157.61,211.86) -- (303.72,211.86)(157.61,216.86) -- (303.72,216.86)(157.61,221.86) -- (303.72,221.86) ; \\draw  [color={rgb, 255:red, 220; green, 216; blue, 208 }  ,draw opacity=1 ]  ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.32 ] (236.32,99.52) -- (235.92,111.52) -- (222.32,131.92) -- (227.12,117.52) -- (221.92,123.52) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.32 ] (244.38,108.46) -- (243.98,115.46) -- (230.38,135.86) -- (235.18,121.46) -- (230.5,128.99) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.14 ] (213.2,93.48) -- (246.75,93.48) -- (223.2,138.48) -- (215.55,138.22) -- cycle ;
                                 	\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (273.12,174.8) -- (287.12,174.8) -- (287.12,179.2) -- (273.12,179.2) -- cycle ;
                                 	\\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (254.61,174.66) -- (268.61,174.66) -- (268.61,179.06) -- (254.61,179.06) -- cycle ;
                                 	\\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1.5]    (229.38,92.86) -- (229.38,57.86) ;
                                 	\\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1.5]    (221.15,138.84) -- (221.32,158.4) ;
                                 	\\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1.5]    (240.95,139.24) -- (241.12,158.8) ;
                                 	\\end{tikzpicture}}'''
                                 % (latex(H), latex(x1), latex(y1), latex(h)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho trục $Ox$ nằm trên mặt sàn, trục $Oy$ chứa trục đối xứng của parabol và hướng lên trên. \\\\
                Khi đó đỉnh của parabol là $I(0; %s)$. Phương trình của parabol có dạng $y = ax^2 + %s$ (với $a < 0$). \\\\
                Vì điểm trên khung cửa sổ cách trục đối xứng $%s$ mét và có độ cao $%s$ mét nên parabol đi qua điểm $M(%s; %s)$. \\\\
                Thay tọa độ điểm $M$ vào phương trình parabol ta được: \\\\
                $a \\cdot %s^2 + %s = %s \\Leftrightarrow %s a = %s \\Leftrightarrow a = %s$. \\\\
                Suy ra phương trình parabol là $y = %s x^2 + %s$. \\\\
                Gọi kích thước của tấm kính hình chữ nhật là $2x$ (chiều rộng, với $x > 0$) và $y - %s$ (chiều cao). \\\\
                Vì hai đỉnh trên nằm trên parabol nên $y = %s x^2 + %s$. \\\\
                Chiều cao của tấm kính là: $h(x) = y - %s = (%s x^2 + %s) - %s = %s x^2 + %s$. \\\\
                Diện tích của tấm kính là: $S(x) = 2x \\cdot h(x) = 2x(%s x^2 + %s) = %s x^3 + %s x$ với $x > 0$. \\\\
                Đạo hàm: $S'(x) = %s x^2 + %s$. \\\\
                Cho $S'(x) = 0 \\Leftrightarrow %s x^2 + %s = 0 \\Leftrightarrow x^2 = %s \\Rightarrow x = %s$. \\\\
                Lập bảng biến thiên, ta thấy $S(x)$ đạt giá trị lớn nhất tại $x = %s$. \\\\
                Giá trị lớn nhất của diện tích là $S_{\\max} = %s \\approx %s$ (m$^2$).'''
                           % (
                              latex(H), latex(H),
                              latex(x1), latex(y1), latex(x1), latex(y1),
                              latex(x1), latex(H), latex(y1), latex(x1**2), latex(y1 - H), latex(a_val),
                              latex(a_val), latex(H),
                              latex(h),
                              latex(a_val), latex(H),
                              latex(h), latex(a_val), latex(H), latex(h), latex(a_val), latex(C),
                              latex(a_val), latex(C), latex(a2), latex(C2),
                              latex(a6), latex(C2),
                              latex(a6), latex(C2), latex(x_sq), latex(x_opt),
                              latex(x_opt),
                              latex(max_area), kq_str
                             ))

                dapan='\\shortans[0]{$%s$}\n'%(kq_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + dapan +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

