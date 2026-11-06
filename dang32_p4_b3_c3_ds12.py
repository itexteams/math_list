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


def bt_dang32_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random các thông số (R, AB sao cho d nguyên để bài toán đẹp)
                # Các bộ số Pitago: (3,4,5), (6,8,10), (5,12,13)
                bo_so = random.choice([
                    {'R': 5, 'd': 4, 'AB': 6},
                    {'R': 10, 'd': 8, 'AB': 12},
                    {'R': 13, 'd': 12, 'AB': 10},
                    {'R': 5, 'd': 3, 'AB': 8}
                ])

                r_val = bo_so['R']
                d_val = bo_so['d']
                ab_val = bo_so['AB']
                gia_tien = random.choice([100, 150, 200, 250, 300]) # nghìn đồng/m2

                # Bước 2: Tính toán diện tích bằng tích phân
                x_sym = symbols('x')
                f = sqrt(r_val**2 - x_sym**2)
                # Tính giá trị xấp xỉ của diện tích
                s_val_raw = 2 * integrate(f, (x_sym, -r_val, d_val)).evalf()
                s_val_rounded = round(float(s_val_raw), 2) # Làm tròn 2 chữ số như mẫu

                # Tính số tiền
                kq_num = int(s_val_rounded * gia_tien)

                # Đáp án đúng
                da_dung = '$%s$' % (kq_num)

                # Tạo các đáp án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_num + random.choice([-100, -50, 50, 100, 10, -10, 20, -20])
                    if sai != kq_num and sai > 0:
                        s.add('$%s$' % (sai))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một người có miếng đất hình tròn có bán kính bằng $%s \, m$. Người này tính trồng cây trên mảnh đất đó, biết mỗi mét vuông trồng cây thu hoạch được $%s$ nghìn. Tuy nhiên cần có một khoảng trống để dựng một cái chòi và để đồ dùng nên người này bớt lại một phần đất nhỏ không trồng cây (phần màu trắng như hình vẽ), trong đó $AB = %s \, m$. Tính số tiền thu hoạch.}
                                 {\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1] 
            			\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (73.7,146) .. controls (73.7,118.39) and (96.09,96) .. (123.7,96) .. controls (151.31,96) and (173.7,118.39) .. (173.7,146) .. controls (173.7,173.61) and (151.31,196) .. (123.7,196) .. controls (96.09,196) and (73.7,173.61) .. (73.7,146) -- cycle ;
            			\draw    (163.7,116) -- (163.7,176) ;
            			\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (163.72,176.62) .. controls (170.39,167.57) and (174.13,157.36) .. (174.13,146.57) .. controls (174.13,135.78) and (170.39,125.58) .. (163.73,116.53) -- cycle ;
            			\draw (160.33,97.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$A$};
            			\draw (159,178.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$B$};
            		\end{tikzpicture}}'''
                                 %(latex(r_val), latex(gia_tien), latex(ab_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Gắn trục tọa độ sao cho đường tròn có phương trình x^2 + y^2 = R^2
                # Khoảng cách từ tâm đến dây cung AB là d
                loigiai = (r'''\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            					\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (73.7,146) .. controls (73.7,118.39) and (96.09,96) .. (123.7,96) .. controls (151.31,96) and (173.7,118.39) .. (173.7,146) .. controls (173.7,173.61) and (151.31,196) .. (123.7,196) .. controls (96.09,196) and (73.7,173.61) .. (73.7,146) -- cycle ;
            					\draw    (163.7,116) -- (163.7,176) ;
            					\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (163.72,176.62) .. controls (170.39,167.57) and (174.13,157.36) .. (174.13,146.57) .. controls (174.13,135.78) and (170.39,125.58) .. (163.73,116.53) -- cycle ;
            					\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (173.7,146) .. controls (173.35,174.65) and (150.73,197.62) .. (123.14,197.34) .. controls (95.59,197.06) and (73.48,173.7) .. (73.64,145.11) -- cycle ;
            					\draw    (60.65,144.9) -- (195.9,146.38) ;
            					\draw [shift={(197.9,146.4)}, rotate = 180.63] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw    (124.65,207.4) -- (124.65,82.65) ;
            					\draw [shift={(124.65,80.65)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw (160.33,97.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$A$};
            					\draw (159,178.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$B$};
            					\draw (105.25,144.45) node [anchor=north west][inner sep=0.75pt]    {$O$};
            					\draw (180.25,147.8) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (105.5,72.9) node [anchor=north west][inner sep=0.75pt]    {$y$};
            				\end{tikzpicture}
            			\end{center}
                    Chọn hệ trục tọa độ $Oxy$ sao cho tâm hình tròn trùng với gốc tọa độ $O$. \\
                             Phương trình đường tròn là $x^2 + y^2 = %s^2 \Rightarrow y = \pm \sqrt{%s - x^2}$. \\
                             Khoảng cách từ tâm đến dây cung $AB$ là $d = \sqrt{%s^2 - (\frac{%s}{2})^2} = %s$. \\
                             Diện tích phần đất trồng cây là: \\
                             $S = 2\int_{-%s}^{%s} \sqrt{%s - x^2} \text{d}x \approx %s \, (m^2)$. \\
                             Vậy số tiền thu được là: $%s \cdot %s = %s$ nghìn đồng.'''
                          %(latex(r_val), latex(r_val**2), latex(r_val), latex(ab_val), latex(d_val),
                            latex(r_val), latex(d_val), latex(r_val**2), latex(str(s_val_rounded).replace('.',',')),
                            latex(str(s_val_rounded).replace('.',',')), latex(gia_tien), latex(kq_num)
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

