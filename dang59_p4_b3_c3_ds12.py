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


def bt_dang59_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Khởi tạo danh sách dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random tham số. Chọn f(0) = a sao cho phương trình hoành độ có nghiệm đẹp
                # Các giá trị a chọn lọc: -1 (nghiệm -1,3), 2 (nghiệm 0,2), -6 (nghiệm -2,4)
                list_a = [-1, 2, -6, -13]
                a = random.choice(list_a)

                # Các thông số cố định theo cấu trúc hàm trong ảnh để đảm bảo f(x) = x^2 + a
                # f'(x) + 4x - 6x * e^{x^2 - f(x) + a} = 0
                f_0 = a
                val_minus_a = -a # dùng cho latex hiển thị f(x) - a

                # Tính toán kết quả thực tế bằng SymPy
                f_x = x**2 + a
                f_prime = 2*x
                f_double_prime = 2
                g_x = f_prime + f_double_prime

                # Tìm nghiệm phương trình hoành độ giao điểm: f(x) - g(x) = 0
                roots = solve(f_x - g_x, x)
                roots = sorted([sp.simplify(r) for r in roots])
                x1, x2 = roots[0], roots[1]

                # Tính diện tích S
                dt = integrate(Abs(f_x - g_x), (x, x1, x2))
                kq_str = latex(dt)

                # Đáp án đúng
                da = '$%s$' % (kq_str)

                # Tạo các đáp án nhiễu (không trùng đáp án đúng)
                s = []
                while len(s) < 6:
                    sai = dt + random.choice([Rational(1, 3), Rational(2, 3), 1, 2, Rational(4, 3), -1, Rational(-2, 3)])
                    if sai > 0:
                        sai_latex = '$%s$' % (latex(sai))
                        if sai_latex != da and sai_latex not in s:
                            s.append(sai_latex)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=f(x)$ có đạo hàm liên tục trên $\\mathbb{R}$ và thỏa mãn $f'(x)+4x-6x \\cdot e^{x^2-f(x)%s}=0, \\forall x \\in \\mathbb{R}$ và $f(0)=%s$. Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=f(x)$ và đồ thị hàm số $y=f'(x)+f''(x)$.'''
                                 % (latex(a if a < 0 else '+' + str(a)), latex(f_0)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng \text{d}x theo yêu cầu)
                loigiai = ('''Ta có $f'(x)+4x-6x \\cdot e^{x^2-f(x)%s}=0, \\forall x \\in \\mathbb{R}$ \\\\
                             $\\Leftrightarrow f'(x)+4x=6x \\cdot e^{x^2-f(x)%s} \\Leftrightarrow \\left[ f'(x)+4x \\right] e^{f(x)%s}=6x \\cdot e^{x^2}$ \\\\
                             $\\Leftrightarrow \\left[ f'(x)+4x \\right] e^{f(x)+2x^2%s}=6x \\cdot e^{3x^2} \\Leftrightarrow \\left[ e^{f(x)+2x^2%s} \\right]'=6x \\cdot e^{3x^2}$ \\\\
                             Suy ra $e^{f(x)+2x^2%s}=\\int 6x \\cdot e^{3x^2} \\text{d}x = e^{3x^2}+C$. \\\\
                             Vì $f(0)=%s$ nên suy ra $C=0$. \\\\
                             Vậy $f(x)=x^2%s$. \\\\
                             Do đó, ta có $f'(x)=2x, f''(x)=2$. \\\\
                             Xét phương trình $f(x)-\\left[ f'(x)+f''(x) \\right]=x^2-2x%s=0 \\Leftrightarrow \\left[ \\begin{aligned} &x=%s \\\\ &x=%s \\end{aligned} \\right.$ \\\\
                             Vậy $S=\\int_{%s}^{%s} \\left| f(x)-\\left[ f'(x)+f''(x) \\right] \\right| \\text{d}x = \\left| \\int_{%s}^{%s} (x^2-2x%s) \\text{d}x \\right| = %s$.'''
                           % (latex(a if a < 0 else '+' + str(a)), 
                              latex(a if a < 0 else '+' + str(a)), 
                              latex(-a if -a < 0 else '+' + str(-a)), 
                              latex(-a if -a < 0 else '+' + str(-a)), 
                              latex(-a if -a < 0 else '+' + str(-a)), 
                              latex(-a if -a < 0 else '+' + str(-a)), 
                              latex(f_0), 
                              latex(a if a < 0 else '+' + str(a)),
                              latex(a-2 if a-2 < 0 else '+' + str(a-2)),
                              latex(x1), latex(x2),
                              latex(x1), latex(x2),
                              latex(x1), latex(x2),
                              latex(a-2 if a-2 < 0 else '+' + str(a-2)),
                              kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

