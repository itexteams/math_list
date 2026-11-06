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


def bt_dang27_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- BƯỚC 1: RANDOM HỆ SỐ ---
                # Tử số: A*n^3 + B*n^2 + C
                A = randint(2, 9) # Hệ số n^3 tử số (dương để dễ nhìn)
                B = randint(1, 9) * random.choice([-1, 1]) # Hệ số n^2
                C = randint(1, 9) * random.choice([-1, 1]) # Hằng số tử

                # Mẫu số: a*n^3 + D
                # Chọn trước giá trị tham số 'a' (kết quả cần tìm)
                val_a = randint(2, 10) 
                # Đảm bảo a khác A để phân số không bằng 1 (cho bài toán hay hơn)
                while val_a == A:
                    val_a = randint(2, 10)

                D = randint(1, 9) * random.choice([-1, 1]) # Hằng số mẫu

                # Giá trị giới hạn L = A/a
                L = Rational(A, val_a)

                # Tính kết quả yêu cầu: P = a - a^2
                ket_qua = val_a - val_a**2

                # --- BƯỚC 2: TẠO CÁC ĐÁP ÁN NHIỄU ---
                # Đáp án đúng
                kq = ket_qua

                # Tạo nhiễu
                # Nhiễu 1: Tính nhầm dấu a + a^2
                w1 = val_a + val_a**2
                # Nhiễu 2: Tính ngược a^2 - a
                w2 = val_a**2 - val_a
                # Nhiễu 3: Sai lệch đơn vị hoặc tính sai a
                w3 = kq + randint(1, 5)*random.choice([-1, 1])

                # Đảm bảo các đáp án khác nhau
                list_w = [w1, w2, w3]
                if len(set(list_w)) < 3 or kq in list_w:
                    w1 = kq + 1
                    w2 = kq - 1
                    w3 = kq - 2

                du = ['$%s$'%(latex(kq))]
                da = random.choice(du)

                s = ['$%s$'%(latex(w1)),
                     '$%s$'%(latex(w2)),
                     '$%s$'%(latex(w3))]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- BƯỚC 3: XÂY DỰNG NỘI DUNG LATEX ---

                # Hàm phụ trợ để hiển thị đa thức đẹp (xử lý dấu cộng trừ)
                def poly_str(coef_n2, coef_const):
                    s_n2 = ("+ " if coef_n2 > 0 else "- ") + latex(abs(coef_n2)) + "n^2"
                    s_c = ("+ " if coef_const > 0 else "- ") + latex(abs(coef_const))
                    return f"{s_n2} {s_c}"

                ts_str = f"{latex(A)}n^3 {poly_str(B, C)}" # Tử số
                ms_str = f"an^3 {'+ ' if D > 0 else '- '}{latex(abs(D))}" # Mẫu số

                # Câu hỏi
                noidungcauhoi = ('''Biết $\\lim_{n \\to +\\infty} \\frac{%s}{%s} = %s$ với $a$ là tham số. Khi đó $a - a^2$ bằng'''
                                 %(ts_str, ms_str, latex(L)))

                # Lời giải chi tiết
                loigiai = ('''Ta có $\\lim_{n \\to +\\infty} \\frac{%s}{%s} 
                = \\lim_{n \\to +\\infty} \\frac{n^3(%s + \\frac{%s}{n} %s \\frac{%s}{n^3})}{n^3(a %s \\frac{%s}{n^3})}$ 
                $= \\frac{%s}{a}$. \\\\
                Theo giả thiết: $\\frac{%s}{a} = %s \\Leftrightarrow a = %s$. \\\\
                Suy ra $a - a^2 = %s - (%s)^2 = %s$.'''
                %(ts_str, ms_str, 
                  latex(A), latex(B), "+" if C>0 else "-", latex(abs(C)),
                  "+" if D>0 else "-", latex(abs(D)),
                  latex(A),
                  latex(A), latex(L), latex(val_a),
                  latex(val_a), latex(val_a), latex(kq)
                  ))

                # --- BƯỚC 4: XUẤT OUTPUT ---
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

