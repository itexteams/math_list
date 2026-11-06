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


def bt_dang37_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Ngẫu nhiên hóa tên hàm số và các điểm mốc trên trục hoành
                list_funcs = [('f', 'g')]
                f_name, g_name = random.choice(list_funcs)

                list_limits = [('a', 'm', 'b')]
                l1, l2, l3 = random.choice(list_limits)

                # Đáp án đúng (B2: Viết lại y hệt nội dung hình ảnh nhưng thay dx bằng \text{d}x)
                # S = tích phân từ l1 đến l2 của |f(x)| + tích phân từ l2 đến l3 của |g(x)|
                kq_str = r'\int_{%s}^{%s} |%s(x)| \text{d}x + \int_{%s}^{%s} |%s(x)| \text{d}x' % (l1, l2, f_name, l2, l3, g_name)

                du = ['$%s$' % kq_str]
                da = random.choice(du)

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = [
                    r'$\int_{%s}^{%s} (%s(x) + %s(x)) \text{d}x$' % (l1, l3, f_name, g_name),
                    r'$\int_{%s}^{%s} |%s(x) - %s(x)| \text{d}x$' % (l1, l3, f_name, g_name),
                    r'$\int_{%s}^{%s} %s(x) \text{d}x + \int_{%s}^{%s} %s(x) \text{d}x$' % (l1, l2, f_name, l2, l3, g_name),
                    r'$\int_{%s}^{%s} |%s(x)| \text{d}x - \int_{%s}^{%s} |%s(x)| \text{d}x$' % (l1, l2, f_name, l2, l3, g_name),
                    r'$\int_{%s}^{%s} |%s(x)| \text{d}x + \int_{%s}^{%s} |%s(x)| \text{d}x$' % (l1, l2, g_name, l2, l3, f_name),
                    r'$\int_{%s}^{%s} |%s(x) + %s(x)| \text{d}x$' % (l1, l3, f_name, g_name)
                ]

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Cho $S$ là diện tích phần hình phẳng được tô màu như hình vẽ (biết đồ thị gồm hai nhánh của hàm số $%s(x)$ trên đoạn $[%s;%s]$ và $%s(x)$ trên đoạn $[%s;%s]$). Khi đó biểu thức tính diện tích $S$ là}
                                 {		\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            			\draw    (56.4,152.7) -- (284.7,152.7) ;
            			\draw [shift={(286.7,152.7)}, rotate = 180] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            			\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (128.5,72.4) -- (198.5,72.4) -- (198.5,152.4) -- (128.5,152.4) -- cycle ;
            			\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (181.63,45.22) .. controls (178.04,59.87) and (156.14,77.79) .. (126.42,88.93) .. controls (100.93,98.49) and (76.5,100.5) .. (62.28,95.41) -- cycle ;
            			\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (257.24,96.14) .. controls (248.98,110.41) and (215.26,106.8) .. (181.73,88.01) .. controls (157.98,74.71) and (140.67,57.35) .. (135.38,43.2) -- cycle ;
            			\draw  [draw opacity=0] (182.49,40.87) .. controls (183.19,56.27) and (158.83,76.98) .. (124.72,89.03) .. controls (95.4,99.4) and (67.66,100.27) .. (54.65,92.42) -- (114.72,60.75) -- cycle ; \draw   (182.49,40.87) .. controls (183.19,56.27) and (158.83,76.98) .. (124.72,89.03) .. controls (95.4,99.4) and (67.66,100.27) .. (54.65,92.42) ;  
            			\draw    (81.02,171.1) -- (80.63,28.7) ;
            			\draw [shift={(80.62,26.7)}, rotate = 89.84] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            			\draw  [draw opacity=0] (256.21,99.02) .. controls (245.2,109.81) and (213.53,105.45) .. (181.8,88.06) .. controls (154.53,73.11) and (135.4,53.01) .. (132.57,38.08) -- (196.22,61.75) -- cycle ; \draw   (256.21,99.02) .. controls (245.2,109.81) and (213.53,105.45) .. (181.8,88.06) .. controls (154.53,73.11) and (135.4,53.01) .. (132.57,38.08) ;  
            			\draw  [dash pattern={on 4.5pt off 4.5pt}]  (158.2,72.4) -- (159.2,152.4) ;
            			\draw  [dash pattern={on 4.5pt off 4.5pt}]  (158.2,72.4) -- (81.2,72.9) ;
            			\draw (59.4,157.5) node [anchor=north west][inner sep=0.75pt]    {$O$};
            			\draw (266.17,129.03) node [anchor=north west][inner sep=0.75pt]    {$x$};
            			\draw (83.6,15.1) node [anchor=north west][inner sep=0.75pt]    {$y$};
            			\draw (120.5,157.5) node [anchor=north west][inner sep=0.75pt]    {$a$};
            			\draw (191,157.5) node [anchor=north west][inner sep=0.75pt]    {$b$};
            			\draw (187.5,24) node [anchor=north west][inner sep=0.75pt]    {$y=f( x)$};
            			\draw (219,72) node [anchor=north west][inner sep=0.75pt]    {$y=g( x)$};
            			\draw (63.5,61) node [anchor=north west][inner sep=0.75pt]    {$n$};
            			\draw (149,158.5) node [anchor=north west][inner sep=0.75pt]    {$m$};
            		\end{tikzpicture}}'''
                                 % (f_name, l1, l2, g_name, l2, l3))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'Dựa vào hình vẽ, diện tích hình phẳng $S$ là tổng diện tích của hai phần: '
                           r'\\ Phần 1 giới hạn bởi đồ thị $%s(x)$ từ $%s$ đến $%s$: $S_1 = \int_{%s}^{%s} |%s(x)| \text{d}x$. '
                           r'\\ Phần 2 giới hạn bởi đồ thị $%s(x)$ từ $%s$ đến $%s$: $S_2 = \int_{%s}^{%s} |%s(x)| \text{d}x$. '
                           r'\\ Vậy $S = S_1 + S_2 = %s$.'
                           % (f_name, l1, l2, l1, l2, f_name, g_name, l2, l3, l2, l3, g_name, kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

