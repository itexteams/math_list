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


def bt_dang49_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # Khai báo danh sách dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: TẠO DỮ LIỆU NGẪU NHIÊN ---
                # A_coeff là hệ số A trong đề bài (chọn 2, 4, 6)
                A_coeff = random.choice([2, 4, 6]) 
                A_half = A_coeff // 2

                # f(1) = 1/v_val
                v_val = random.randint(3, 6) 
                while v_val <= A_half:
                    v_val += 1

                C_val = v_val - A_half
                b_val = random.randint(2, 3) # Đoạn [1; b_val]

                # --- BƯỚC 2: TÍNH TOÁN KẾT QUẢ ---
                m_min = Rational(1, v_val)
                M_max = Rational(b_val**3, A_half * b_val**2 + C_val)

                # Kết quả chính xác dưới dạng phân số
                ket_qua_exact = M_max - m_min

                # Làm tròn đến hàng phần chục (0.1)
                kq_float = float(ket_qua_exact)
                kq_rounded = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Định dạng hiển thị (thay dấu . thành ,)
                da_dung = '$%s$' % str(kq_rounded).replace('.', ',')

                # --- BƯỚC 3: TẠO CÁC PHƯƠNG ÁN SAI ---
                s = []
                offsets = [0.5, 1.0, -0.3, 0.2, -0.5, 0.8]
                random.shuffle(offsets)

                for offset in offsets:
                    sai_val = float(kq_rounded) + offset
                    # Làm tròn phương án sai để đồng nhất định dạng
                    sai_rounded = Decimal(str(sai_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    str_sai = '$%s$' % str(sai_rounded).replace('.', ',')

                    if str_sai != da_dung and str_sai not in s:
                        s.append(str_sai)
                        if len(s) == 3: break

                das1, das2, das3 = s[0], s[1], s[2]

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
                noidungcauhoi = (
                    'Cho hàm số $y=f(x)$ liên tục trên $(0;+\\infty)$ thỏa mãn $%s x \\cdot f(x) - x^2 \\cdot f\'(x) = %s f^2(x)$, với '
                    '$f(x) \\neq 0, \\forall x \\in (0;+\\infty)$ và $f(1)=\\frac{1}{%s}$. Gọi $M, m$ lần lượt là giá trị lớn nhất, giá trị nhỏ nhất của hàm số '
                    '$y=f(x)$ trên đoạn $[1;%s]$. Giá trị $M-m$ làm tròn đến hàng phần chục bằng bao nhiêu?'
                    % (3, latex(A_coeff), latex(v_val), latex(b_val))
                )

                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                loigiai = (
                    '''Ta có: $3x \\cdot f(x) - x^2 \\cdot f'(x) = %s f^2(x) \\Rightarrow 3x^2 \\cdot f(x) - x^3 \\cdot f'(x) = %s x \\cdot f^2(x)$ \\\\
                    $\\Rightarrow \\frac{3x^2 \\cdot f(x) - x^3 \\cdot f'(x)}{f^2(x)} = %s x \\Rightarrow \\left( \\frac{x^3}{f(x)} \\right)' = %s x$ \\\\
                    $\\Rightarrow \\frac{x^3}{f(x)} = \\int %s x dx = %s x^2 + C$. \\\\
                    Mà $f(1) = \\frac{1}{%s} \\Rightarrow \\frac{1^3}{1/%s} = %s(1)^2 + C \\Rightarrow %s = %s + C \\Rightarrow C = %s$. \\\\
                    Suy ra $f(x) = \\frac{x^3}{%s x^2 + %s}$. \\\\
                    Xét $f'(x) = \\frac{x^4 + 6x^2 \\cdot %s}{(%s x^2 + %s)^2} > 0, \\forall x \\in [1;%s]$. \\\\
                    Hàm số đồng biến trên $[1;%s]$, do đó: \\\\
                    $m = f(1) = \\frac{1}{%s}$, $M = f(%s) = \\frac{%s^3}{%s \\cdot %s^2 + %s} = %s$. \\\\
                    Vậy $M - m = %s - %s = %s \\approx %s$.'''
                    % (latex(A_coeff), latex(A_coeff), latex(A_coeff), latex(A_coeff), 
                       latex(A_coeff), latex(A_half),
                       latex(v_val), latex(v_val), latex(A_half), latex(v_val), latex(A_half), latex(C_val),
                       latex(A_half), latex(C_val), latex(C_val), latex(A_half), latex(C_val), latex(b_val),
                       latex(b_val), latex(v_val), latex(b_val), latex(b_val), latex(A_half), latex(b_val), latex(C_val), latex(M_max),
                       latex(M_max), latex(m_min), latex(ket_qua_exact), str(kq_rounded).replace('.', ','))
                )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(str(kq_rounded).replace('.', ',')) 

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

