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


def bt_dang30_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số góc và giá trị vế phải sao cho bài toán tường minh
                # Trong ảnh: sin(3x + pi/3) = -sqrt(3)/2
                a = random.choice([2, 3, 4]) # Hệ số của x

                # Chọn cặp giá trị góc alpha và giá trị lượng giác tương ứng
                list_val = [
                    ('-\\frac{\\sqrt{3}}{2}', -pi/3),
                    ('-\\frac{1}{2}', -pi/6),
                    ('-\\frac{\\sqrt{2}}{2}', -pi/4),
                    ('\\frac{1}{2}', pi/6),
                    ('\\frac{\\sqrt{2}}{2}', pi/4),
                    ('\\frac{\\sqrt{3}}{2}', pi/3)
                ]
                val_str, alpha = random.choice(list_val)

                # Tính toán số nghiệm thực tế trong khoảng (0, pi/2) để sinh ra đáp án đúng
                # Họ nghiệm 1: a*x + pi/3 = alpha + k*2*pi  => x = (alpha - pi/3)/a + k*2*pi/a
                # Họ nghiệm 2: a*x + pi/3 = pi - alpha + k*2*pi => x = (pi - alpha - pi/3)/a + k*2*pi/a

                sol_count = 0
                list_nghiem_1 = []
                list_nghiem_2 = []

                # Duyệt k trong khoảng hợp lý để đếm nghiệm chính xác
                for k in range(-5, 6):
                    x1 = (alpha - pi/3)/a + k*2*pi/a
                    if 0 < x1 < pi/2:
                        sol_count += 1
                        list_nghiem_1.append(k)

                    x2 = (pi - alpha - pi/3)/a + k*2*pi/a
                    if 0 < x2 < pi/2:
                        sol_count += 1
                        list_nghiem_2.append(k)

                kq = sol_count

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai không trùng với đáp án đúng
                s = []
                for i in [1, 2, 3, 4, 5]:
                    if i != kq:
                        s.append('$%s$' % i)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Phương trình $\\sin \\left( %sx+\\frac{\\pi}{3} \\right) = %s$ có bao nhiêu nghiệm thuộc khoảng $\\left( 0;\\frac{\\pi}{2} \\right)$?'''
                                 %(latex(a), val_str))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Xử lý chuỗi hiển thị bổ trợ cho lời giải chi tiết
                # Bước biến đổi họ nghiệm tổng quát
                # ax + pi/3 = alpha + k2pi  => x = (alpha - pi/3)/a + k 2pi/a
                h1_tu = alpha - pi/3
                h2_tu = pi - alpha - pi/3

                x1_bientan = latex(h1_tu / a).replace('/', '\\frac')
                x2_bientan = latex(h2_tu / a).replace('/', '\\frac')

                # Biện luận chi tiết từng trường hợp tương tự mẫu ảnh
                # TH1
                if len(list_nghiem_1) > 0:
                    k1_str = ", ".join([str(m) for m in list_nghiem_1])
                    th1_txt = ('''TH1: $x = %s + k\\frac{2\\pi}{%s} \\in \\left( 0;\\frac{\\pi}{2} \\right) \\Rightarrow k \\in \\{%s\\}$. Suy ra trường hợp này có nghiệm thỏa mãn.''' % (latex(h1_tu/a), latex(a), k1_str))
                else:
                    th1_txt = ('''TH1: $x = %s + k\\frac{2\\pi}{%s} \\in \\left( 0;\\frac{\\pi}{2} \\right)$. Trường hợp này không có giá trị $k$ nguyên nào thỏa mãn.''' % (latex(h1_tu/a), latex(a)))

                # TH2
                if len(list_nghiem_2) > 0:
                    k2_str = ", ".join([str(m) for m in list_nghiem_2])
                    th2_txt = ('''TH2: $x = %s + k\\frac{2\\pi}{%s} \\in \\left( 0;\\frac{\\pi}{2} \\right) \\Rightarrow k \\in \\{%s\\}$. Suy ra trường hợp này có nghiệm thỏa mãn.''' % (latex(h2_tu/a), latex(a), k2_str))
                else:
                    th2_txt = ('''TH2: $x = %s + k\\frac{2\\pi}{%s} \\in \\left( 0;\\frac{\\pi}{2} \\right)$. Trường hợp này không có giá trị $k$ nguyên nào thỏa mãn.''' % (latex(h2_tu/a), latex(a)))

                # Nội dung lời giải
                loigiai=('''Ta có $\\sin \\left( %sx+\\frac{\\pi}{3} \\right) = %s \\Leftrightarrow \\sin \\left( %sx+\\frac{\\pi}{3} \\right) = \\sin \\left( %s \\right)$ \\\\
                         $\\Leftrightarrow \\left[ \\begin{aligned} & %sx+\\frac{\\pi}{3} = %s+k2\\pi \\\\ & %sx+\\frac{\\pi}{3} = \\pi - \\left( %s \\right)+k2\\pi \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x = %s + k\\frac{2\\pi}{%s} \\\\ & x = %s + k\\frac{2\\pi}{%s} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})$. \\\\
                         +) %s \\\\
                         +) %s \\\\
                         Vậy phương trình chỉ có $%s$ nghiệm thuộc khoảng $\\left( 0;\\frac{\\pi}{2} \\right)$.'''
                        %(latex(a), val_str, latex(a), latex(alpha),
                          latex(a), latex(alpha), latex(a), latex(alpha), latex(h1_tu/a), latex(a), latex(h2_tu/a), latex(a),
                          th1_txt, th2_txt, latex(kq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

