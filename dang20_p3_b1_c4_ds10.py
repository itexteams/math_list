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


def bt_dang20_p3_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Ta có hàm số y = (x + b) / (x - a) = 1 + (a + b) / (x - a)
                # Đặt k = a + b. Số điểm nguyên phụ thuộc vào số ước của k.

                a = random.randint(-5, 5)
                if a == 0: a = 1 # Tránh mẫu là x

                # Chọn k sao cho có một lượng ước vừa phải (thường chọn k = 2, 3, 4, 5, 6)
                k = random.choice([2, 3, 4, 5, 6])
                b = k - a

                # Hàm số ban đầu
                f = (x + b) / (x - a)

                # Tìm các ước của k
                divisors = []
                for i in range(1, abs(k) + 1):
                    if k % i == 0:
                        divisors.append(i)
                        divisors.append(-i)
                divisors.sort(reverse=True) # Sắp xếp để trình bày giống mẫu

                # Đáp án đúng là số lượng ước
                kq = len(divisors)

                # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                da = '$%s$' % kq
                s = []
                for i in [2, 4, 6, 8, 10]:
                    if i != kq:
                        s.append('$%s$' % i)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu điểm có tọa độ nguyên thuộc đồ thị hàm số $y = %s$?'''
                                 % (latex(f)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Viết nội dung lời giải giống hệt cấu trúc trong ảnh
                # Tạo chuỗi các trường hợp x-a = ước
                cac_truong_hop = r'\left[\begin{aligned} '
                cac_ket_qua_x = r'\left[\begin{aligned} '

                ds_diem = []
                for d in divisors:
                    x_val = d + a
                    y_val = 1 + k // d
                    cac_truong_hop += f'x - {a} &= {d} \\\\ ' if a >= 0 else f'x + {abs(a)} &= {d} \\\\ '
                    cac_ket_qua_x += f'x &= {x_val} \\\\ '
                    ds_diem.append(f'({x_val}; {y_val})')

                cac_truong_hop += r'\end{aligned}\right.'
                cac_ket_qua_x += r'\end{aligned}\right.'

                string_diem = ", ".join([f"M_{i+1}{ds_diem[i]}" for i in range(len(ds_diem))])

                loigiai = ('''TXĐ: $D = \\mathbb{R} \\setminus \\{%s\\}$. \\\\
                             Ta có $y = %s = 1 + \\frac{%s}{x - %s}$. \\\\
                             Tung độ của một điểm thuộc đồ thị hàm số là số nguyên $\\Leftrightarrow \\frac{%s}{x - %s} \\in \\mathbb{Z}$. (1) \\\\
                             Vì hoành độ của điểm đó là số nguyên nên (1) $\\Leftrightarrow %s \\Leftrightarrow %s$. \\\\
                             Vậy các điểm thuộc đồ thị hàm số $y = %s$ có tọa độ nguyên là \\\\
                             $%s$. \\\\
                             Vậy có %s điểm có tọa độ nguyên thuộc đồ thị hàm số.'''
                           % (latex(a), latex(f), latex(k), latex(a),
                              latex(k), latex(a), cac_truong_hop, cac_ket_qua_x,
                              latex(f), string_diem, kq))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+')
            return content

