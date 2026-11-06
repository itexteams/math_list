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


def bt_dang28_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random các hệ số
                # Để lời giải đẹp, ta chọn a chia hết cho 6, b chia hết cho 3
                a = randint(1, 4) * 6  
                b = randint(-3, 3) * 3
                if b == 0: b = 3
                c = randint(1, 5)
                k = randint(2, 5) # f(0) = f'(0) = k

                # Bước 2: Tính toán các giá trị
                # C1 = f(0)*f'(0) = k^2
                c1 = k**2
                # C2 = f(0)^2 = k^2
                c2 = k**2

                # Biểu thức f^2(1) = (a/6) + (b/3) + c + 2*C1 + C2
                ans_val = Rational(a, 6) + Rational(b, 3) + c + 2*c1 + c2
                kq = latex(ans_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da= random.choice(du)

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                offsets = [-2, -1, 1, 2, 3, 5, 10]
                random.shuffle(offsets)
                for offset in offsets:
                    sai_val = ans_val + offset
                    if sai_val != ans_val:
                        s.append('$%s$'%(latex(sai_val)))
                    if len(s) == 3: break

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Định dạng dấu cho hệ số b
                dau_b = '+' if b > 0 else ''
                noidungcauhoi = ('''Cho hàm số $f(x)$ thỏa mãn $[f'(x)]^2 + f(x) \\cdot f''(x) = %s x^2 %s %s x + %s, \\forall x \\in \\mathbb{R}$ và $f(0) = f'(0) = %s$. Tính giá trị của $[f(1)]^2$.'''
                                 %(latex(a), dau_b, latex(b), latex(c), latex(k)
                                 ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # g(x) = f(x)f'(x) = (a/3)x^3 + (b/2)x^2 + cx + C1
                # f^2(x) = (a/6)x^4 + (b/3)x^3 + cx^2 + 2*C1x + C2
                loigiai=('''Ta có $[f(x)f'(x)]' = [f'(x)]^2 + f(x)f''(x)$. \\\\
                         Do đó theo giả thiết ta được $[f(x)f'(x)]' = %s x^2 %s %s x + %s$. \\\\
                         Suy ra $f(x)f'(x) = %s x^3 %s %s x^2 + %s x + C_1$. \\\\
                         Hơn nữa $f(0) = f'(0) = %s$ suy ra $C_1 = %s \\cdot %s = %s$. \\\\
                         Tương tự vì $[f^2(x)]' = 2f(x)f'(x)$ nên $[f^2(x)]' = 2\\left( %s x^3 %s %s x^2 + %s x + %s \\right)$. \\\\
                         Suy ra $f^2(x) = \\int 2\\left( %s x^3 %s %s x^2 + %s x + %s \\right) \\text{d}x = %s x^4 %s %s x^3 + %s x^2 + %s x + C_2$. \\\\
                         Cũng vì $f(0) = %s$ suy ra $C_2 = %s^2 = %s$. \\\\
                         Do đó $f^2(x) = %s x^4 %s %s x^3 + %s x^2 + %s x + %s$. \\\\
                         Vậy $[f(1)]^2 = %s$.'''
                         %(latex(a), dau_b, latex(b), latex(c),
                           latex(Rational(a,3)), dau_b, latex(Rational(b,2)), latex(c),
                           latex(k), latex(k), latex(k), latex(c1),
                           latex(Rational(a,3)), dau_b, latex(Rational(b,2)), latex(c), latex(c1),
                           latex(Rational(a,3)), dau_b, latex(Rational(b,2)), latex(c), latex(c1),
                           latex(Rational(a,6)), dau_b, latex(Rational(b,3)), latex(c), latex(2*c1),
                           latex(k), latex(k), latex(c2),
                           latex(Rational(a,6)), dau_b, latex(Rational(b,3)), latex(c), latex(2*c1), latex(c2),
                           latex(ans_val)
                         ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

