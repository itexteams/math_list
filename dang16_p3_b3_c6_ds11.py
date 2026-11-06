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


def bt_dang16_p3_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các xác suất sao cho a > b và tổng a+b < 1 (để đảm bảo tính thực tế của bài toán nếu cần)
                a_val = random.choice([0.5, 0.6, 0.7, 0.8])
                b_val = random.choice([0.2, 0.3, 0.4])
                while a_val <= b_val:
                    a_val = random.choice([0.5, 0.6, 0.7, 0.8])
                    b_val = random.choice([0.2, 0.3, 0.4])

                c_val = random.choice([0.6, 0.7, 0.8, 0.9])

                # Random hệ số m, n cho biểu thức ma + nb
                m_val = random.choice([2, 3, 4, 5])
                n_val = random.choice([2, 3, 4, 5])

                # Tính toán các giá trị của bài toán
                p_all = round(a_val * b_val * c_val, 4)
                p_none = round((1 - a_val) * (1 - b_val) * (1 - c_val), 4)
                p_at_least_one = round(1 - p_none, 4)

                ab_val = round(a_val * b_val, 4)
                ab_none = round((1 - a_val) * (1 - b_val), 4)
                sum_ab = round(a_val + b_val, 4)
                minus_c = round(1 - c_val, 4)

                kq = round(m_val * a_val + n_val * b_val, 4)

                # Hàm chuyển đổi số thập phân: dùng dấu phẩy và xóa số 0 thừa
                def f_dec(num):
                    return f"{num:g}".replace('.', ',')

                c_str = f_dec(c_val)
                p_all_str = f_dec(p_all)
                p_at_least_one_str = f_dec(p_at_least_one)
                p_none_str = f_dec(p_none)
                ab_val_str = f_dec(ab_val)
                ab_none_str = f_dec(ab_none)
                sum_ab_str = f_dec(sum_ab)
                minus_c_str = f_dec(minus_c)
                a_str = f_dec(a_val)
                b_str = f_dec(b_val)
                kq_str = f_dec(kq)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên không trùng với đáp án đúng
                variations = [
                    round(n_val * a_val + m_val * b_val, 4),
                    round(m_val * a_val - n_val * b_val, 4),
                    round(m_val * b_val + n_val * a_val, 4),
                    round(kq + 0.2, 4),
                    round(kq - 0.2, 4),
                    round(kq + 1, 4),
                    round(kq - 1, 4)
                ]
                unique_vars = []
                for v in variations:
                    if v != kq and v > 0 and v not in unique_vars:
                        unique_vars.append(v)

                while len(unique_vars) < 3:
                    v = round(kq + random.choice([-0.4, 0.4, -0.6, 0.6]), 4)
                    if v != kq and v > 0 and v not in unique_vars:
                        unique_vars.append(v)

                random.shuffle(unique_vars)
                s = ['$%s$'%(f_dec(unique_vars[0])),
                     '$%s$'%(f_dec(unique_vars[1])),
                     '$%s$'%(f_dec(unique_vars[2]))]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một công ty xây dựng đấu thầu ba dự án $X, Y, Z$. Xác suất để ba dự án $X, Y$ và $Z$ trúng thầu tương ứng là $a; b$ và $%s$ $\\left(a>b\\right)$. Biết rằng xác suất để ít nhất một trong ba dự án trúng thầu là $%s$ và xác suất để cả ba dự án đều trúng thầu là $%s$. Giả sử việc trúng thầu của ba dự án $X, Y$ và $Z$ là độc lập. Giá trị $%sa + %sb$ bằng bao nhiêu?'''
                                 %(c_str, p_at_least_one_str, p_all_str, m_val, n_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $A, B, C$ lần lượt là các biến cố dự án $X, Y, Z$ trúng thầu. \\\\
                Theo giả thiết, ta có $P\\left(A\\right)=a, P\\left(B\\right)=b, P\\left(C\\right)=%s$. \\\\
                Vì $A, B, C$ là các biến cố độc lập nên ta có: \\\\
                Xác suất cả ba dự án đều trúng thầu là: \\\\
                $P\\left(A \\cap B \\cap C\\right) = P\\left(A\\right) \\cdot P\\left(B\\right) \\cdot P\\left(C\\right) = a \\cdot b \\cdot %s = %s \\Rightarrow ab = %s$. \\\\
                Xác suất ít nhất một dự án trúng thầu là: \\\\
                $1 - P\\left(\\overline{A}\\right) \\cdot P\\left(\\overline{B}\\right) \\cdot P\\left(\\overline{C}\\right) = 1 - \\left(1-a\\right)\\left(1-b\\right)\\left(1-%s\\right) = %s$. \\\\
                $\\Rightarrow \\left(1-a\\right)\\left(1-b\\right) \\cdot %s = 1 - %s = %s \\Rightarrow \\left(1-a\\right)\\left(1-b\\right) = %s$. \\\\
                $\\Rightarrow 1 - \\left(a+b\\right) + ab = %s \\Rightarrow a+b = 1 + %s - %s = %s$. \\\\
                Ta có hệ phương trình: $\\begin{cases} a+b = %s \\\\ ab = %s \\end{cases}$. \\\\
                Do đó $a, b$ là nghiệm của phương trình: $t^2 - %st + %s = 0$. \\\\
                Giải phương trình ta được $t = %s$ hoặc $t = %s$. \\\\
                Vì $a > b$ nên ta chọn $a = %s, b = %s$. \\\\
                Vậy $%sa + %sb = %s \\cdot %s + %s \\cdot %s = %s$.'''
                           %(c_str,
                             c_str, p_all_str, ab_val_str,
                             c_str, p_at_least_one_str,
                             minus_c_str, p_at_least_one_str, p_none_str, ab_none_str,
                             ab_none_str, ab_val_str, ab_none_str, sum_ab_str,
                             sum_ab_str, ab_val_str,
                             sum_ab_str, ab_val_str,
                             a_str, b_str,
                             a_str, b_str,
                             m_val, n_val, m_val, a_str, n_val, b_str, kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content  

