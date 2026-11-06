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


def bt_dang36_p1_b3_c3_ds12(self):
            # Khai báo biến
            # B1 & B3: Nghiên cứu đề bài và thiết lập tham số ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Danh sách các bộ ký hiệu để random
                list_functions = [('f', 'g')]
                list_bounds = [('a', 'b')]

                # Chọn ngẫu nhiên bộ ký hiệu
                f_name, g_name = random.choice(list_functions)
                low, high = random.choice(list_bounds)

                # B2: Viết lại bài toán theo mẫu
                # Đáp án đúng
                da_dung = r'S=\int_{%s}^{%s} |%s(x) - %s(x)| \text{d}x' % (low, high, f_name, g_name)

                # Tạo danh sách các phương án sai (B4: Đảm bảo không trùng đáp án đúng)
                s = [
                    r'S=\int_{%s}^{%s} (%s(x) - %s(x)) \text{d}x' % (low, high, f_name, g_name), # Thiếu trị tuyệt đối
                    r'S=\int_{%s}^{%s} |%s(x) + %s(x)| \text{d}x' % (low, high, f_name, g_name), # Sai dấu cộng
                    r'S=\pi \int_{%s}^{%s} |%s(x) - %s(x)| \text{d}x' % (low, high, f_name, g_name), # Thừa pi
                    r'S=\pi \int_{%s}^{%s} [%s(x) - %s(x)]^2 \text{d}x' % (low, high, f_name, g_name), # Nhầm sang thể tích
                    r'S=\int_{%s}^{%s} |%s(x)| \text{d}x - \int_{%s}^{%s} |%s(x)| \text{d}x' % (low, high, f_name, low, high, g_name)
                ]

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Nội dung câu hỏi
                noidungcauhoi = (r'''\immini{Cho các hàm số $y = %s(x)$, $y = %s(x)$ liên tục trên đoạn [$%s;%s$]. 
                                 Khi đó, diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y = %s(x)$, $y = %s(x)$ 
                                 và hai đường thẳng $x = %s, x = %s$ là}
                                 {		\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            			\draw    (198.4,149.2) -- (393.73,149.2) ;
            			\draw [shift={(395.73,149.2)}, rotate = 180] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            			\draw    (221.52,161.6) -- (221.13,19.2) ;
            			\draw [shift={(221.12,17.2)}, rotate = 89.84] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            			\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (240,89.89) .. controls (240,71.41) and (266.21,56.44) .. (298.53,56.44) .. controls (330.86,56.44) and (357.07,71.41) .. (357.07,89.89) .. controls (357.07,108.36) and (330.86,123.33) .. (298.53,123.33) .. controls (266.21,123.33) and (240,108.36) .. (240,89.89) -- cycle ;
            			\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (254.15,111.69) .. controls (245.33,105.84) and (240,98.22) .. (240,89.89) .. controls (240,81.65) and (245.21,74.1) .. (253.86,68.27) -- cycle ; 
            			\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (339.43,65.96) .. controls (350.31,72.03) and (357.07,80.51) .. (357.07,89.89) .. controls (357.07,99.15) and (350.47,107.54) .. (339.81,113.6) -- cycle ; 
            			\draw    (254.8,37.07) -- (254.8,160.27) ;
            			\draw    (338.93,37.6) -- (338.93,160.8) ;
            			\draw  [draw opacity=0] (228.19,90.46) .. controls (242.29,70.12) and (268.54,56.44) .. (298.6,56.44) .. controls (330.89,56.44) and (358.79,72.22) .. (371.95,95.11) -- (298.6,124.79) -- cycle ; \draw   (228.19,90.46) .. controls (242.29,70.12) and (268.54,56.44) .. (298.6,56.44) .. controls (330.89,56.44) and (358.79,72.22) .. (371.95,95.11) ;  
            			\draw  [draw opacity=0] (359.05,100.57) .. controls (344.09,114.42) and (322.4,123.1) .. (298.28,123.02) .. controls (273.59,122.93) and (251.5,113.68) .. (236.62,99.14) -- (298.52,55.05) -- cycle ; \draw   (359.05,100.57) .. controls (344.09,114.42) and (322.4,123.1) .. (298.28,123.02) .. controls (273.59,122.93) and (251.5,113.68) .. (236.62,99.14) ;  
            			\draw (202.4,153) node [anchor=north west][inner sep=0.75pt]    {$O$};
            			\draw (378.67,133) node [anchor=north west][inner sep=0.75pt]    {$x$};
            			\draw (225.6,11.6) node [anchor=north west][inner sep=0.75pt]    {$y$};
            			\draw (238,152) node [anchor=north west][inner sep=0.75pt]    {$a$};
            			\draw (341.5,153) node [anchor=north west][inner sep=0.75pt]    {$b$};
            			\draw (262.5,28.5) node [anchor=north west][inner sep=0.75pt]    {$y=f( x)$};
            			\draw (265.5,123) node [anchor=north west][inner sep=0.75pt]    {$y=g( x)$};
            		\end{tikzpicture}}'''
                                 % (f_name, g_name, low, high, f_name, g_name, low, high))

                # Các đáp án
                da_d = ('\\True $' + da_dung + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'Theo công thức tính diện tích hình phẳng giới hạn bởi hai đồ thị hàm số '
                           r'$y = %s(x)$, $y = %s(x)$ và hai đường thẳng $x = %s, x = %s$, '
                           r'diện tích $S$ được tính bởi công thức: '
                           r'$S = \int_{%s}^{%s} |%s(x) - %s(x)| \text{d}x$.'
                           % (f_name, g_name, low, high, low, high, f_name, g_name))

            # Xuất câu trắc nghiệm theo đúng định dạng
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

