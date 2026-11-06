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


def bt_dang55_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số để tạo bài toán mới (đảm bảo d < L)
                L_val = random.choice([2, 3, 4])
                d_val = random.choice([1, 2])
                if d_val >= L_val:
                    d_val = 1

                AB_val = 2 * L_val
                c1_val = random.choice([400, 500, 600]) # Chi phí sơn xanh (phần gạch chéo)
                c2_val = random.choice([200, 250, 300]) # Chi phí sơn trắng (phần còn lại)

                # Tính toán các hằng số theo sympy để hiển thị chính xác dưới dạng phân số
                a_val = Rational(-L_val - d_val, L_val**2)
                K_val = Rational(L_val**2, L_val + d_val)
                x0_val = Rational(d_val * L_val, L_val + d_val)

                # Chuyển đổi sang float để tính chính xác diện tích và làm tròn tiền
                K_float = float(K_val)
                x0_float = float(x0_val)
                d_float = float(d_val)
                L_float = float(L_val)

                # Tính S_1 + S_2 theo công thức tích phân chính xác đã được giải tích
                S1_plus_S2 = (L_float**2 - 0.5 * x0_float**2
                              + (4/3) * math.sqrt(K_float) * d_float * math.sqrt(d_float)
                              - (2/3) * math.sqrt(K_float) * (d_float - x0_float) * math.sqrt(d_float - x0_float)
                              - (2/3) * math.sqrt(K_float) * (d_float + L_float) * math.sqrt(d_float + L_float))

                A_float = 8 * S1_plus_S2
                Total_Area = 4 * L_float**2

                # Chi phí = (Diện tích trắng) * giá trắng + (Diện tích xanh) * giá xanh
                Cost = A_float * c2_val + (Total_Area - A_float) * c1_val

                # Làm tròn đến hàng đơn vị
                ans = math.floor(Cost + 0.5)
                while ans>9999:
                    L_val = random.choice([2, 3, 4])
                    d_val = random.choice([1, 2])
                    if d_val >= L_val:
                        d_val = 1

                    AB_val = 2 * L_val
                    c1_val = random.choice([400, 500, 600]) # Chi phí sơn xanh (phần gạch chéo)
                    c2_val = random.choice([200, 250, 300]) # Chi phí sơn trắng (phần còn lại)

                    # Tính toán các hằng số theo sympy để hiển thị chính xác dưới dạng phân số
                    a_val = Rational(-L_val - d_val, L_val**2)
                    K_val = Rational(L_val**2, L_val + d_val)
                    x0_val = Rational(d_val * L_val, L_val + d_val)

                    # Chuyển đổi sang float để tính chính xác diện tích và làm tròn tiền
                    K_float = float(K_val)
                    x0_float = float(x0_val)
                    d_float = float(d_val)
                    L_float = float(L_val)

                    # Tính S_1 + S_2 theo công thức tích phân chính xác đã được giải tích
                    S1_plus_S2 = (L_float**2 - 0.5 * x0_float**2
                                  + (4/3) * math.sqrt(K_float) * d_float * math.sqrt(d_float)
                                  - (2/3) * math.sqrt(K_float) * (d_float - x0_float) * math.sqrt(d_float - x0_float)
                                  - (2/3) * math.sqrt(K_float) * (d_float + L_float) * math.sqrt(d_float + L_float))

                    A_float = 8 * S1_plus_S2
                    Total_Area = 4 * L_float**2

                    # Chi phí = (Diện tích trắng) * giá trắng + (Diện tích xanh) * giá xanh
                    Cost = A_float * c2_val + (Total_Area - A_float) * c1_val

                    # Làm tròn đến hàng đơn vị
                    ans = math.floor(Cost + 0.5)
                # Các đáp án trắc nghiệm
                kq4 = ans
                du = ['$%s$'%(kq4)]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = ['$%s$'%(latex(kq4+105)).replace('.',','),
                     '$%s$'%(latex(kq4+218)).replace('.',','),
                     '$%s$'%(latex(kq4+33)).replace('.',','),
                     '$%s$'%(latex(kq4-124)).replace('.',','),
                     '$%s$'%(latex(kq4-25)).replace('.',','),
                     '$%s$'%(latex(kq4-311)).replace('.',','),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (106.2,225.96) .. controls (119.55,185.68) and (127.33,160.3) .. (141.82,134.46) .. controls (162.32,163.31) and (178.09,179.68) .. (201.06,190.81) .. controls (168.88,204.11) and (150.61,215.06) .. (106.2,225.96) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (291.56,225.96) .. controls (251.24,212.74) and (225.83,205.04) .. (199.94,190.63) .. controls (228.74,170.04) and (245.06,154.22) .. (256.11,131.21) .. controls (272.67,163.62) and (280.52,181.59) .. (291.56,225.96) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (293.2,42.04) .. controls (279.28,82.13) and (271.15,107.4) .. (256.29,133.03) .. controls (236.2,103.89) and (220.67,87.3) .. (197.85,75.85) .. controls (229.5,60.02) and (247.73,51.87) .. (293.2,42.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (106.2,40.6) .. controls (146.53,53.79) and (171.95,61.46) .. (197.85,75.85) .. controls (169.07,96.47) and (152.77,112.3) .. (141.74,135.32) .. controls (128.31,103.19) and (117.28,84.96) .. (106.2,40.6) -- cycle ;
            	\draw  [line width=1]  (106.2,40.6) -- (291.56,40.6) -- (291.56,225.96) -- (106.2,225.96) -- cycle ;
            	\draw [line width=1]    (106.2,40.6) .. controls (219.91,71.05) and (265.47,110.38) .. (291.56,225.96) ;
            	\draw [line width=1]    (291.56,225.96) .. controls (176.75,195.75) and (136.46,159.3) .. (106.2,40.6) ;
            	\draw [line width=1]    (106.2,225.96) .. controls (136.46,112.3) and (176.11,67.27) .. (291.56,40.6) ;
            	\draw [line width=1]    (291.56,40.6) .. controls (261.16,167.45) and (205.52,200.07) .. (106.2,225.96) ;
            	\draw  [line width=1]  (153.87,133.28) .. controls (153.87,108.42) and (174.02,88.27) .. (198.88,88.27) .. controls (223.74,88.27) and (243.89,108.42) .. (243.89,133.28) .. controls (243.89,158.14) and (223.74,178.29) .. (198.88,178.29) .. controls (174.02,178.29) and (153.87,158.14) .. (153.87,133.28) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (196.4,88.27) .. controls (196.4,87.59) and (196.95,87.03) .. (197.64,87.03) .. controls (198.33,87.03) and (198.88,87.59) .. (198.88,88.27) .. controls (198.88,88.96) and (198.33,89.51) .. (197.64,89.51) .. controls (196.95,89.51) and (196.4,88.96) .. (196.4,88.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (197.64,178.29) .. controls (197.64,177.61) and (198.2,177.05) .. (198.88,177.05) .. controls (199.57,177.05) and (200.12,177.61) .. (200.12,178.29) .. controls (200.12,178.98) and (199.57,179.53) .. (198.88,179.53) .. controls (198.2,179.53) and (197.64,178.98) .. (197.64,178.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (152.87,133.28) .. controls (152.87,132.6) and (153.43,132.04) .. (154.11,132.04) .. controls (154.8,132.04) and (155.36,132.6) .. (155.36,133.28) .. controls (155.36,133.97) and (154.8,134.52) .. (154.11,134.52) .. controls (153.43,134.52) and (152.87,133.97) .. (152.87,133.28) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (242.65,133.28) .. controls (242.65,132.6) and (243.21,132.04) .. (243.89,132.04) .. controls (244.58,132.04) and (245.13,132.6) .. (245.13,133.28) .. controls (245.13,133.97) and (244.58,134.52) .. (243.89,134.52) .. controls (243.21,134.52) and (242.65,133.97) .. (242.65,133.28) -- cycle ;
            	\draw (84.4,21.8) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (88.4,221.8) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (291.56,225.96) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (292.4,20.47) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\draw (190.15,87.22) node [anchor=north west][inner sep=0.75pt]    {$E$};
            	\draw (154.4,120.97) node [anchor=north west][inner sep=0.75pt]    {$F$};
            	\draw (190.98,155.63) node [anchor=north west][inner sep=0.75pt]    {$P$};
            	\draw (223.82,120.72) node [anchor=north west][inner sep=0.75pt]    {$Q$};
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Bác Tuấn trang trí bức tường hình vuông $ABCD$ có $AB = %sm$ như hình vẽ bằng cách sơn màu. Trong đó, bốn đường cong $AQB, APD, BEC, CFD$ đều là đường Parabol có các đỉnh lần lượt là $Q, P, E, F$. Biết rằng trục đối xứng của mỗi Parabol trùng với một trục đối xứng của hình vuông $ABCD$. Cho biết $OE = OF = OP = OQ = %sm$. Phần diện tích giới hạn bởi bốn đường Parabol nêu trên được sơn màu xanh với chi phí $%s$ nghìn đồng cho mỗi mét vuông. Phần diện tích còn lại của bức tường được sơn màu trắng với chi phí $%s$ nghìn đồng cho mỗi mét vuông. Tổng số tiền (đơn vị: nghìn đồng) bác Tuấn cần để hoàn thành việc sơn bức tường đó bằng bao nhiêu? (Kết quả làm tròn đến hàng đơn vị).}{%s}'''
                                 %(latex(AB_val), latex(d_val), latex(c1_val), latex(c2_val),hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gắn hệ trục tọa độ tại tâm $O$. Cạnh hình vuông bằng $%s$ nên các đỉnh là $\\left( \\pm %s; \\pm %s \\right)$.
                           \\begin{center}
                           	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                               	\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (198.88,133.28) .. controls (229.35,101.9) and (210.6,122.4) .. (230.6,100.65) .. controls (252.6,124.65) and (245.6,117.4) .. (256.2,131.9) .. controls (223.85,134.65) and (240.85,132.4) .. (198.88,133.28) -- cycle ;
                               	\\draw  [draw opacity=0][fill={rgb, 255:red, 232; green, 60; blue, 204 }  ,fill opacity=1 ] (291.56,225.96) .. controls (280.1,181.15) and (270.1,155.9) .. (256.2,131.9) .. controls (280.1,132.4) and (277.1,133.4) .. (291.6,132.15) .. controls (292.1,179.15) and (291.1,185.15) .. (291.56,225.96) -- cycle ;
                               	\\draw  [line width=1]  (106.2,40.6) -- (291.56,40.6) -- (291.56,225.96) -- (106.2,225.96) -- cycle ;
                               	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (106.2,40.6) .. controls (219.91,71.05) and (265.47,110.38) .. (291.56,225.96) ;
                               	\\draw [line width=1]    (291.56,225.96) .. controls (176.75,195.75) and (136.46,159.3) .. (106.2,40.6) ;
                               	\\draw [line width=1]    (106.2,225.96) .. controls (136.46,112.3) and (176.11,67.27) .. (291.56,40.6) ;
                               	\\draw [line width=1]    (291.56,40.6) .. controls (261.16,167.45) and (205.52,200.07) .. (106.2,225.96) ;
                               	\\draw  [line width=1]  (153.87,133.28) .. controls (153.87,108.42) and (174.02,88.27) .. (198.88,88.27) .. controls (223.74,88.27) and (243.89,108.42) .. (243.89,133.28) .. controls (243.89,158.14) and (223.74,178.29) .. (198.88,178.29) .. controls (174.02,178.29) and (153.87,158.14) .. (153.87,133.28) -- cycle ;
                               	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (196.4,88.27) .. controls (196.4,87.59) and (196.95,87.03) .. (197.64,87.03) .. controls (198.33,87.03) and (198.88,87.59) .. (198.88,88.27) .. controls (198.88,88.96) and (198.33,89.51) .. (197.64,89.51) .. controls (196.95,89.51) and (196.4,88.96) .. (196.4,88.27) -- cycle ;
                               	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (197.64,178.29) .. controls (197.64,177.61) and (198.2,177.05) .. (198.88,177.05) .. controls (199.57,177.05) and (200.12,177.61) .. (200.12,178.29) .. controls (200.12,178.98) and (199.57,179.53) .. (198.88,179.53) .. controls (198.2,179.53) and (197.64,178.98) .. (197.64,178.29) -- cycle ;
                               	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (152.87,133.28) .. controls (152.87,132.6) and (153.43,132.04) .. (154.11,132.04) .. controls (154.8,132.04) and (155.36,132.6) .. (155.36,133.28) .. controls (155.36,133.97) and (154.8,134.52) .. (154.11,134.52) .. controls (153.43,134.52) and (152.87,133.97) .. (152.87,133.28) -- cycle ;
                               	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (242.65,133.28) .. controls (242.65,132.6) and (243.21,132.04) .. (243.89,132.04) .. controls (244.58,132.04) and (245.13,132.6) .. (245.13,133.28) .. controls (245.13,133.97) and (244.58,134.52) .. (243.89,134.52) .. controls (243.21,134.52) and (242.65,133.97) .. (242.65,133.28) -- cycle ;
                               	\\draw [line width=1]    (87.2,134.4) -- (317.7,132.93) ;
                               	\\draw [shift={(321.7,132.9)}, rotate = 179.63] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                               	\\draw [line width=1]    (199.2,244.4) -- (197.73,17.4) ;
                               	\\draw [shift={(197.7,13.4)}, rotate = 89.63] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                               	\\draw [line width=1]    (198.88,133.28) -- (291.56,40.6) ;
                               	\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (106.2,225.96) .. controls (146,63.2) and (240.4,20.4) .. (291.56,225.96) ;
                               	\\draw (89,27) node [anchor=north west][inner sep=0.75pt]    {$A$};
                               	\\draw (88.4,221.8) node [anchor=north west][inner sep=0.75pt]    {$B$};
                               	\\draw (291.56,225.96) node [anchor=north west][inner sep=0.75pt]    {$C$};
                               	\\draw (292.4,25) node [anchor=north west][inner sep=0.75pt]    {$D$};
                               	\\draw (180.65,95) node [anchor=north west][inner sep=0.75pt]    {$E$};
                               	\\draw (156.4,112.47) node [anchor=north west][inner sep=0.75pt]    {$F$};
                               	\\draw (182.48,163) node [anchor=north west][inner sep=0.75pt]    {$P$};
                               	\\draw (221.82,131.22) node [anchor=north west][inner sep=0.75pt]    {$Q$};
                               	\\draw (183,135) node [anchor=north west][inner sep=0.75pt]    {$O$};
                               	\\draw (306.9,139) node [anchor=north west][inner sep=0.75pt]    {$x$};
                               	\\draw (179.9,13) node [anchor=north west][inner sep=0.75pt]    {$y$};
                               	\\draw (246.4,54.47) node [anchor=north west][inner sep=0.75pt]    {$d$};
                               	\\draw (123.4,163.97) node [anchor=north west][inner sep=0.75pt]    {$( P_{1})$};
                               	\\draw (217.65,111) node [anchor=north west][inner sep=0.75pt]    {$S_{1}$};
                               	\\draw (268.9,136) node [anchor=north west][inner sep=0.75pt]    {$S_{2}$};
                               \\end{tikzpicture}
                           \\end{center}
                             Parabol $\\left( P_1 \\right)$ qua $E\\left( 0; %s \\right)$ và $B\\left( %s; -%s \\right), C\\left( -%s; -%s \\right)$ có phương trình $y = ax^2 + %s$.\\\\
                             Thay $\\left( %s; -%s \\right)$ vào: $-%s = %s a + %s \\Rightarrow a = %s \\Rightarrow y = %s x^2 + %s \\Rightarrow x = \\pm \\sqrt{%s \\left( %s - y \\right)}$.\\\\
                             Phương trình hoành độ giao điểm của $\\left( P_1 \\right)$ và $d: y=x$ là: \\\\
                             $%s x^2 + %s = x \\Leftrightarrow %s x^2 - x + %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\Rightarrow y = %s \\\\ x = -%s \\end{array} \\right.$\\\\
                             Phần diện tích hình cánh hoa màu trắng (8 phần đối xứng).\\\\
                             $S_t = 8 \\left( S_1 + S_2 \\right) = 8 \\left\\{ \\int\\limits_0^{%s} \\left[ \\sqrt{%s \\left( %s - y \\right)} - y \\right] dy + \\int\\limits_{-%s}^0 \\left[ %s - \\sqrt{%s \\left( %s - y \\right)} \\right] dy \\right\\}$.\\\\
                             Tổng tiền $= A \\cdot %s + \\left( %s - A \\right) \\cdot %s \\approx %s$ nghìn đồng.'''
                             %(
                                 latex(AB_val), latex(L_val), latex(L_val),
                                 latex(d_val), latex(L_val), latex(L_val), latex(L_val), latex(L_val), latex(d_val),
                                 latex(L_val), latex(L_val), latex(L_val), latex(L_val**2), latex(d_val), latex(a_val), latex(a_val), latex(d_val), latex(K_val), latex(d_val),
                                 latex(a_val), latex(d_val), latex(a_val), latex(d_val), latex(x0_val), latex(x0_val), latex(L_val),
                                 latex(x0_val), latex(K_val), latex(d_val), latex(L_val), latex(L_val), latex(K_val), latex(d_val),
                                 latex(c2_val), latex(Total_Area), latex(c1_val), latex(ans)
                             ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(ans))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

