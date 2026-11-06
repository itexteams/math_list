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


def bt_dang24_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                ti_le = random.choice([49.9, 49.99, 49.999])

                if ti_le == 49.9:
                    kq = 3
                    tl_str = "49,9"
                    p = "49,9"
                elif ti_le == 49.99:
                    kq = 4
                    tl_str = "49,99"
                    p = "49,99"
                else:
                    kq = 5
                    tl_str = "49,999"
                    p = "49,999"

                #Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)
                s = ['$%s$'%(kq+1),
                     '$%s$'%(kq+2),
                     '$%s$'%(kq-1),
                     '$%s$'%(kq-2),
                    ]

                if du[0] in s:
                    s.remove(du[0])

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''\\immini{Với hình vuông $A_1B_1C_1D_1$ như hình vẽ bên, cách tô màu như phần màu cam được gọi là cách tô màu "đẹp". Một nhà thiết kế tiến hành tô màu cho một hình vuông như hình bên, theo quy trình sau: \\\\
                1. Bước 1: Tô màu "đẹp" cho hình vuông $A_1B_1C_1D_1$. \\\\
                2. Bước 2: Tô màu "đẹp" cho hình vuông $A_2B_2C_2D_2$ là hình vuông ở chính giữa khi chia hình vuông $A_1B_1C_1D_1$ thành $9$ phần bằng nhau như hình vẽ. \\\\
                3. Bước 3: Tô màu "đẹp" cho hình vuông $A_3B_3C_3D_3$ là hình vuông ở chính giữa khi chia hình vuông $A_2B_2C_2D_2$ thành $9$ phần bằng nhau. Cứ tiếp tục như vậy. \\\\
                Hỏi cần ít nhất bao nhiêu bước để tổng diện tích phần được tô màu chiếm $%s\\%%$?}
                                 {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (145,146.9) -- (128.3,146.9) -- (127.8,128.7) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (109.8,112.4) -- (93.1,112.4) -- (92.6,94.2) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (108.9,130.2) -- (128.1,130.2) -- (128.1,149.4) -- (108.9,149.4) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (92.4,130.9) -- (108.9,130.9) -- (108.9,147.4) -- (92.4,147.4) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (91.3,112.4) -- (109.8,112.4) -- (109.8,130.9) -- (91.3,130.9) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (198,200.6) -- (144.8,200.6) -- (144.8,147.4) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (92.6,94.2) -- (39.4,94.2) -- (39.4,41) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (92.25,147.4) -- (145.45,147.4) -- (145.45,200.6) -- (92.25,200.6) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (39.4,147.4) -- (92.6,147.4) -- (92.6,200.6) -- (39.4,200.6) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (39.4,94.2) -- (92.6,94.2) -- (92.6,147.4) -- (39.4,147.4) -- cycle ;
            	\\draw  [line width=1]  (39.4,41) -- (199,41) -- (199,200.6) -- (39.4,200.6) -- cycle ;
            	\\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (92.6,41.9) -- (92.6,200.4) ;
            	\\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (145.8,40.4) -- (145.8,200.9) ;
            	\\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (38.6,94.2) -- (199.6,94.2) ;
            	\\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (40.6,147.4) -- (199.1,147.4) ;
            	\\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (128.3,94.4) -- (128.3,146.9) ;
            	\\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (109.8,94.9) -- (109.8,147.4) ;
            	\\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (146.6,112.4) -- (93.1,112.4) ;
            	\\draw [line width=1]  [dash pattern={on 1.69pt off 2.76pt}]  (145.6,129.9) -- (92.1,129.9) ;
            	\\draw  [line width=1]  (92.6,94.2) -- (145.8,94.2) -- (145.8,147.4) -- (92.6,147.4) -- cycle ;
            \\end{tikzpicture}}'''
                                 %(tl_str))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Gọi diện tích hình vuông $A_1B_1C_1D_1$ là $S$. \\\\
                Diện tích phần tô màu ở bước 1 là $S_1 = \\frac{1}{2}S - \\frac{1}{2} \\cdot \\frac{S}{9} = \\frac{4}{9}S$. \\\\
                Diện tích hình vuông $A_2B_2C_2D_2$ là $\\frac{S}{9}$. \\\\
                Diện tích phần tô màu ở bước 2 là $S_2 = \\frac{4}{9} \\cdot \\frac{S}{9} = \\frac{4}{9^2}S$. \\\\
                Tương tự, diện tích phần tô màu ở bước $n$ là $S_n = \\frac{4}{9^n}S$. \\\\
                Tổng diện tích phần được tô màu sau $n$ bước là: \\\\
                $T_n = S_1 + S_2 + \\dots + S_n = \\frac{4}{9}S \\cdot \\frac{1 - \\left(\\frac{1}{9}\\right)^n}{1 - \\frac{1}{9}} = \\frac{S}{2} \\left[1 - \\left(\\frac{1}{9}\\right)^n\\right]$. \\\\
                Yêu cầu bài toán tương đương với: \\\\
                $T_n > %s\\%% \\cdot S \\Leftrightarrow \\frac{1}{2} \\left[1 - \\left(\\frac{1}{9}\\right)^n\\right] > \\frac{%s}{100} \\Leftrightarrow \\left(\\frac{1}{9}\\right)^n < 1 - \\frac{2 \\cdot %s}{100}$. \\\\
                Giải bất phương trình trên, ta tìm được giá trị nhỏ nhất của $n$ là $n = %s$. \\\\
                Vậy cần ít nhất $%s$ bước.'''
                         %(tl_str, p, p, kq, kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

