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


def bt_dang50_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Khai báo biến dạng bài
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM THÔNG SỐ ---
                x0 = random.randint(2, 5) # Điểm giới hạn

                # Thiết lập tử số: (x + m) - sqrt(nx + p) sao cho tử bằng 0 tại x0
                m = random.randint(1, 3)
                n = random.randint(1, 5)
                p = (x0 + m)**2 - n*x0
                tu_ngoai = x + m
                tu_trong = n*x + p

                # Thiết lập mẫu số: x - sqrt(kx + l) sao cho mẫu bằng 0 tại x0
                k = random.randint(1, 4)
                l = x0**2 - k*x0
                mau_ngoai = x
                mau_trong = k*x + l

                # --- BƯỚC 2: TÍNH TOÁN KẾT QUẢ ---
                f = (tu_ngoai - sqrt(tu_trong)) / (mau_ngoai - sqrt(mau_trong))
                L = limit(f, x, x0)

                # Ép kiểu về Rational để lấy tử và mẫu
                L_rational = Rational(L)
                a = sp.numer(L_rational)
                b = sp.denom(L_rational)
                kq_final = a - b

                # --- BƯỚC 3: CÁC ĐÁP ÁN TRẮC NGHIỆM ---
                da = '$%s$' % latex(kq_final)
                s = [
                    '$%s$' % latex(kq_final + 1),
                    '$%s$' % latex(kq_final - 1),
                    '$%s$' % latex(kq_final + 2),
                    '$%s$' % latex(kq_final - 2),
                    '$%s$' % latex(kq_final + 3),
                    '$%s$' % latex(kq_final * (-1))
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'Giới hạn $\lim_{x \to %s} \frac{%s - \sqrt{%s}}{%s - \sqrt{%s}} = \frac{a}{b}$, với $a,b \in \mathbb{Z}, b > 0$ và $\frac{a}{b}$ là phân số tối giản. Giá trị của $a-b$ là'
                                 % (latex(x0), latex(tu_ngoai), latex(tu_trong), latex(mau_ngoai), latex(mau_trong)))

                # --- BƯỚC 5: CHUẨN BỊ DỮ LIỆU CHO LỜI GIẢI ---
                tu_da_thuc = sp.expand(tu_ngoai**2 - tu_trong)
                mau_da_thuc = sp.expand(mau_ngoai**2 - mau_trong)

                # Rút gọn (x - x0)
                tu_rut_gon = sp.simplify(tu_da_thuc / (x - x0))
                mau_rut_gon = sp.simplify(mau_da_thuc / (x - x0))

                # Giá trị tại x0 để thay vào lời giải
                val_tu_lh = (tu_ngoai + sqrt(tu_trong)).subs(x, x0)
                val_mau_lh = (mau_ngoai + sqrt(mau_trong)).subs(x, x0)
                val_tu_rut = tu_rut_gon.subs(x, x0)
                val_mau_rut = mau_rut_gon.subs(x, x0)

                # --- BƯỚC 6: XÂY DỰNG LỜI GIẢI (Đếm chính xác %s) ---
                loigiai = (r'''Ta có
                $$\lim_{x \to %s} \frac{%s - \sqrt{%s}}{%s - \sqrt{%s}} = \lim_{x \to %s} \left[ \frac{%s + \sqrt{%s}}{%s + \sqrt{%s}} \cdot \frac{(%s)^2 - (%s)}{%s^2 - (%s)} \right]$$
                $$= \lim_{x \to %s} \left[ \frac{%s + \sqrt{%s}}{%s + \sqrt{%s}} \cdot \frac{%s}{%s} \right] = \frac{%s}{%s} \cdot \frac{%s}{%s} = \frac{%s}{%s}$$
                $\Rightarrow a=%s, b=%s \Rightarrow a-b=%s$.'''
                % (
                    latex(x0), latex(tu_ngoai), latex(tu_trong), latex(mau_ngoai), latex(mau_trong), # Dòng 1 (5 biến)
                    latex(x0), # Dòng 1 (1 biến)
                    latex(mau_ngoai), latex(mau_trong), latex(tu_ngoai), latex(tu_trong), # Liên hợp (4 biến)
                    latex(tu_ngoai), latex(tu_trong), latex(mau_ngoai), latex(mau_trong), # Bình phương (4 biến)
                    latex(x0), # Dòng 2 (1 biến)
                    latex(mau_ngoai), latex(mau_trong), latex(tu_ngoai), latex(tu_trong), # Liên hợp (4 biến)
                    latex(tu_da_thuc), latex(mau_da_thuc), # Đa thức rút gọn (2 biến)
                    latex(val_mau_lh), latex(val_tu_lh), # Giá trị liên hợp (2 biến)
                    latex(val_tu_rut), latex(val_mau_rut), # Giá trị phân thức (2 biến)
                    latex(a), latex(b), # Kết quả a/b (2 biến)
                    latex(a), latex(b), latex(kq_final) # Kết luận (3 biến)
                ))

                # Đưa các đáp án vào danh sách
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất kết quả theo format mẫu
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

