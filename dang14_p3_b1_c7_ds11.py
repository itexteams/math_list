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


def bt_dang14_p3_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến và logic ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các giá trị sao cho (n-m)/k là một số chính phương s^2
                # f(x) = (x + m)/(x + n) -> f'(x) = (n - m)/(x + n)^2
                k = randint(1, 4) # Hệ số góc tiếp tuyến
                s = randint(1, 3) # Khoảng cách từ x0 đến tiệm cận đứng
                diff = k * (s**2) # n - m = k*s^2

                n = randint(1, 5)
                m = n - diff

                # Hàm số f(x) = (x + m)/(x + n)
                f = (x + m)/(x + n)
                f_der = diff / (x + n)**2

                # Giải f'(x) = k => (x + n)^2 = s^2 => x = -n + s hoặc x = -n - s
                x_sol1 = -n + s
                x_sol2 = -n - s

                # Chọn hoành độ âm
                points = [val for val in [x_sol1, x_sol2] if val < 0]
                if not points: # Phòng hờ trường hợp không có số âm (dù logic trên thường tạo ra số âm)
                    x0 = x_sol2
                else:
                    x0 = random.choice(points)

                y0 = f.subs(x, x0)

                # Phương trình tiếp tuyến y = k(x - x0) + y0 = kx - k*x0 + y0
                # y = ax + b
                a = k
                b = y0 - k * x0

                # Giá trị T = a^2 * b
                T = (a**2) * b

                # Hệ số góc đường thẳng Delta (vuông góc với tiếp tuyến)
                # k * k_delta = -1 => k_delta = -1/k
                k_delta = Rational(-1, k)
                p = randint(1, 10) # Hệ số tự do của Delta

                # Kết quả đúng
                kq = int(T)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = du[0]

                # Tạo các phương án sai
                s_list = []
                while len(s_list) < 3:
                    sai = kq + randint(-15, 15)
                    if sai != kq and sai not in s_list:
                        s_list.append(sai)

                das1 = '$%s$' % (latex(s_list[0]))
                das2 = '$%s$' % (latex(s_list[1]))
                das3 = '$%s$' % (latex(s_list[2]))

                # Câu hỏi
                # Định dạng lại f(x) để giống mẫu (x-1)/(x+1)
                tu = x + m
                mau = x + n

                noidungcauhoi = ('''Cho hàm số $f\\left(x\\right) = \\frac{%s}{%s}$ có đồ thị $\\left(C\\right)$. Phương trình tiếp tuyến với $\\left(C\\right)$ vuông góc với đường thẳng $\\Delta: y = %sx + %s$ có dạng $y = ax + b$. Biết tọa độ tiếp điểm có hoành độ âm. Giá trị $T = a^2 \\cdot b$ bằng bao nhiêu?'''
                                 % (latex(tu), latex(mau), latex(k_delta), latex(p)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: $f'\\left(x\\right) = \\lim_{h \\to 0} \\frac{f\\left(x+h\\right)-f\\left(x\\right)}{h} = \\frac{%s}{\\left(x+%s\\right)^2}$.\\\\
                             Gọi $M\\left(x_0; \\frac{x_0%s}{x_0%s}\\right) \\in \\left(C\\right)$ là tọa độ tiếp điểm.\\\\
                             Hệ số góc của tiếp tuyến tại điểm $M \\in \\left(C\\right)$ là: $k = f'\\left(x_0\\right) = \\frac{%s}{\\left(x_0+%s\\right)^2}$.\\\\
                             Tiếp tuyến tại điểm $M \\in \\left(C\\right)$ vuông góc với đường thẳng $\\Delta: y = %sx + %s$ nên $k \\cdot \\left(%s\\right) = -1 \\Leftrightarrow k = %s$.\\\\
                             $\\Leftrightarrow \\frac{%s}{\\left(x_0+%s\\right)^2} = %s \\Leftrightarrow \\left(x_0+%s\\right)^2 = %s \\Leftrightarrow \\left[\\begin{aligned} & x_0 = %s \\\\ & x_0 = %s \\end{aligned}\\right. $.\\\\
                             Vì hoành độ tiếp điểm âm nên chọn $x_0 = %s \\Rightarrow M\\left(%s; %s\\right)$.\\\\
                             Phương trình tiếp tuyến tại $M\\left(%s; %s\\right)$ có dạng: $y = %s\\left(x - \\left(%s\\right)\\right) + %s \\Leftrightarrow y = %sx + %s$.\\\\
                             Suy ra $\\left\\{\\begin{aligned} & a = %s \\\\ & b = %s \\end{aligned}\\right. $.\\\\
                             Vậy $T = a^2 \\cdot b = %s^2 \\cdot %s = %s$.'''
                           % (latex(diff), latex(n), 
                              '+'+latex(m) if m > 0 else latex(m), '+'+latex(n) if n > 0 else latex(n),
                              latex(diff), latex(n),
                              latex(k_delta), latex(p), latex(k_delta), latex(k),
                              latex(diff), latex(n), latex(k), latex(n), latex(s**2),
                              latex(x_sol1), latex(x_sol2),
                              latex(x0), latex(x0), latex(y0),
                              latex(x0), latex(y0), latex(a), latex(x0), latex(y0), latex(a), latex(b),
                              latex(a), latex(b), latex(a), latex(b), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content      

