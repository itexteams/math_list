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


def bt_dang21_p3_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Khai báo danh sách dạng (ở đây chỉ có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Để có lời giải giống ảnh (phân tích được nhân tử), ta chọn trước 1 nghiệm nguyên k
                # Phương trình có dạng: x^3 + ax^2 + d = 0 (với d = b - c)
                # Ta chọn a và k, sau đó tính d sao cho x = k là nghiệm: k^3 + a*k^2 + d = 0 => d = -k^3 - a*k^2

                a = random.randint(-5, 5)
                if a == 0: a = -3 # Tránh trường hợp quá đơn giản

                k = random.randint(-3, 3)
                if k == 0: k = 1

                d = -k**3 - a*k**2

                # Chọn b ngẫu nhiên, từ đó suy ra c (tung độ đề bài hỏi)
                b = random.randint(-5, 5)
                c = b - d

                # Hàm số ban đầu: y = x^3 + ax^2 + b
                f_x = x**3 + a*x**2 + b

                # Phương trình tương đương: x^3 + ax^2 + d = 0
                # Phân tích nhân tử: (x - k)(x^2 + (a+k)x + k(a+k)) = 0
                b_quad = a + k
                c_quad = k * (a + k)
                quad_expr = x**2 + b_quad*x + c_quad

                # Tìm tập nghiệm để đếm số điểm
                roots = solve(x**3 + a*x**2 + d, x)
                # Lọc nghiệm thực và lấy duy nhất (set)
                real_roots = [r for r in roots if r.is_real]
                unique_roots = list(set(real_roots))
                kq_count = len(unique_roots)

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                da_dung = str(kq_count)
                s_options = ['0', '1', '2', '3', '4']
                if da_dung in s_options:
                    s_options.remove(da_dung)

                random.shuffle(s_options)
                das1 = s_options[0]
                das2 = s_options[1]
                das3 = s_options[2]

                # B2: Viết lại đề bài và lời giải theo mẫu
                # Câu hỏi
                noidungcauhoi = (r'Cho hàm số $y = %s$. Có bao nhiêu điểm trên đồ thị hàm số có tung độ bằng $%s$?'
                                 % (latex(f_x), latex(c)))

                # Các đáp án
                da_d = r'\True ' + da_dung
                da_s1 = das1
                da_s2 = das2
                da_s3 = das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt cấu trúc trong ảnh)
                # Giải phương trình bậc 2 để trình bày nghiệm
                quad_roots = solve(quad_expr, x)

                # Định dạng hiển thị nghiệm x = ...
                if len(quad_roots) == 2:
                    if quad_roots[0].is_Integer and quad_roots[1].is_Integer:
                        str_roots = f"x = {latex(quad_roots[0])}, x = {latex(quad_roots[1])}"
                    else:
                        # Trường hợp nghiệm căn thức như trong ảnh 1 +/- sqrt(3)
                        str_roots = f"x = {latex(quad_roots[0])}, x = {latex(quad_roots[1])}"
                elif len(quad_roots) == 1:
                    str_roots = f"x = {latex(quad_roots[0])}"
                else:
                    str_roots = "vô nghiệm"

                loigiai = (r'''$y = %s \Rightarrow %s = %s$ \\
                             $\Leftrightarrow %s = 0$ \\
                             $\Leftrightarrow (x - %s)(%s) = 0$ \\
                             $\Leftrightarrow \left[\begin{aligned} & x - %s = 0 \\ & %s = 0 \end{aligned}\right. \Leftrightarrow \left[\begin{aligned} & x = %s \\ & %s \end{aligned}\right.$ \\
                             Vậy có %s điểm trên đồ thị hàm số có tung độ bằng $%s$.'''
                           % (latex(c), latex(f_x), latex(c),
                              latex(x**3 + a*x**2 + d),
                              latex(k), latex(quad_expr),
                              latex(k), latex(quad_expr), latex(k), str_roots,
                              da_dung, latex(c)
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(da_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


