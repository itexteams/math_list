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


def bt_dang45_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Chọn bộ số Pitago để mẫu số đẹp (nguyên)
                A, B = random.choice([(3, 4), (6, 8), (5, 12), (8, 15)])
                x0, y0 = random.randint(-5, 5), random.randint(-5, 5)
                R = random.randint(1, 5)

                # 2. Tính toán các hệ số phương trình đường tròn
                a_coeff = -2 * x0
                b_coeff = -2 * y0
                c_circle = x0**2 + y0**2 - R**2

                # 3. Tính toán tham số m cho 2 vị trí tiếp tuyến
                dist_val = int(R * sqrt(A**2 + B**2))
                inside_abs = A * x0 + B * y0
                m1, m2 = -inside_abs + dist_val, -inside_abs - dist_val

                # 4. CHỌN Delta trùng với m2 để loại m2
                c_delta = m2 

                # 5. HÀM BỔ TRỢ: Xử lý dấu
                def get_s(val):
                    if val > 0: return f"+ {val}"
                    if val < 0: return f"- {abs(val)}"
                    return ""

                # 6. CHUẨN BỊ CHUỖI TRƯỚC (Để f-string sạch sẽ)
                s_m1 = get_s(m1)
                s_m2 = get_s(m2)
                s_a = get_s(a_coeff)
                s_b = get_s(b_coeff)
                s_c = get_s(c_circle)
                s_cd = get_s(c_delta)

                s_circle = f"x^2 + y^2 {s_a}x {s_b}y {s_c} = 0".replace(" 1x", " x").replace(" -1x", " -x").replace("+ 0x", "").replace("+ 0y", "")

                noidungcauhoi = (f"Trong mặt phẳng tọa độ $(Oxy)$, cho đường tròn $(C): {s_circle}$. "
                                 f"Phương trình đường tiếp tuyến với $(C)$ song song với đường thẳng $\\Delta : {A}x + {B}y {s_cd} = 0$ là")

                # 7. NỘI DUNG LỜI GIẢI - FIX LỖI NGOẶC NHỌN TẠI ĐÂY
                # Lưu ý: Các lệnh LaTeX như \text{}, \frac{}, \sqrt{}, \begin{} phải dùng {{ }}
                loigiai = (f"Đường tròn $(C)$ có tâm $I({x0}; {y0})$ và bán kính $R = {R}$.\\\\ "
                           f"Gọi $d$ là tiếp tuyến cần tìm. Vì $d // \\Delta$ nên $d$ có dạng: ${A}x + {B}y + m = 0$ ($m \\neq {c_delta}$).\\\\ "
                           f"$d$ là tiếp tuyến của $(C) \\Leftrightarrow d(I, d) = R$\\\\ "
                           f"$\\Leftrightarrow \\frac{{|{A} \\cdot ({x0}) + {B} \\cdot ({y0}) + m|}}{{\\sqrt{{{A}^2 + {B}^2}}}} = {R}$ "
                           f"$\\Leftrightarrow \\frac{{|{inside_abs} + m|}}{{{int(sqrt(A**2 + B**2))}}} = {R}$\\\\ "
                           f"$\\Leftrightarrow |{inside_abs} + m| = {dist_val} \\Leftrightarrow \\left[\\begin{{aligned}} & m = {m1} \\text{{ (nhận)}} \\\\ & m = {m2} \\text{{ (loại vì trùng }} \\Delta) \\end{{aligned}}\\right.$\\\\ "
                           f"Vậy có 1 tiếp tuyến cần tìm là: ${A}x + {B}y {s_m1} = 0$.")

                # 8. CÁC ĐÁP ÁN TRẮC NGHIỆM
                da_dung = f"${A}x + {B}y {s_m1} = 0$"
                da_sai1 = f"${A}x + {B}y {get_s(m1+2)} = 0$"
                da_sai2 = f"${A}x + {B}y {get_s(m1-2)} = 0$"
                da_sai3 = f"${A}x + {B}y {s_m2} = 0$" 

                list_1 = ['\\True ' + da_dung, da_sai1, da_sai2, da_sai3]
                random.shuffle(list_1)

            # 9. XUẤT KẾT QUẢ
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

