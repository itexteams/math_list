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


def bt_dang18_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Random tâm I(x1, y1) và I'(x2, y2)
                x1, y1 = random.randint(-3, 3), random.randint(-3, 3)
                x2, y2 = random.randint(-3, 3), random.randint(-3, 3)

                # Đảm bảo hai tâm không trùng nhau
                while x1 == x2 and y1 == y2:
                    x2, y2 = random.randint(-3, 3), random.randint(-3, 3)

                # Random bán kính R1, R2 (số nguyên dương cho đẹp)
                r1 = random.randint(3, 6)
                r2 = random.randint(3, 6)

                # Tính khoảng cách II'
                dist_sq = (x2 - x1)**2 + (y2 - y1)**2
                dist = sqrt(dist_sq)

                # Tính các hệ số khai triển đường tròn: x^2 + y^2 - 2ax - 2by + c = 0
                # c = a^2 + b^2 - R^2
                c1 = x1**2 + y1**2 - r1**2
                c2 = x2**2 + y2**2 - r2**2

                # Hàm xử lý dấu cho phương trình (hiển thị - - thành +, + - thành -)
                def fmt_eq(val, var):
                    coeff = -2 * val
                    if coeff > 0: return f"+{coeff}{var}"
                    elif coeff < 0: return f"{coeff}{var}"
                    else: return ""

                def fmt_c(val):
                    if val > 0: return f"+{val}"
                    elif val < 0: return f"{val}"
                    else: return ""

                eq1_str = f"x^2 + y^2 {fmt_eq(x1, 'x')} {fmt_eq(y1, 'y')} {fmt_c(c1)} = 0"
                eq2_str = f"x^2 + y^2 {fmt_eq(x2, 'x')} {fmt_eq(y2, 'y')} {fmt_c(c2)} = 0"

                # Xác định vị trí tương đối
                diff_r = abs(r1 - r2)
                sum_r = r1 + r2

                if diff_r < dist < sum_r:
                    vi_tri = "cắt nhau tại hai điểm phân biệt"
                elif dist == sum_r:
                    vi_tri = "tiếp xúc ngoài nhau"
                elif dist == diff_r and dist != 0:
                    vi_tri = "tiếp xúc trong nhau"
                elif dist > sum_r:
                    vi_tri = "ngoài nhau"
                else:
                    vi_tri = "đựng nhau"

                # --- B2: Viết lại đề bài và lời giải ---
                noidungcauhoi = (f"Trong mặt phẳng tọa độ $Oxy$, cho hai đường tròn $(C): {eq1_str}$ và $(C'): {eq2_str}$. Khi đó vị trí tương đối của hai đường tròn là")

                da_d = f"\\True {vi_tri}"

                # Các đáp án nhiễu
                options = ["cắt nhau tại hai điểm phân biệt", "tiếp xúc ngoài nhau", "tiếp xúc trong nhau", "ngoài nhau", "đựng nhau"]
                if vi_tri in options: options.remove(vi_tri)
                random.shuffle(options)

                da_s1 = options[0]
                da_s2 = options[1]
                da_s3 = options[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Đường tròn $(C)$ có tâm $I({x1}; {y1})$ và bán kính $R={r1}$.\\\\ "
                           f"Đường tròn $(C')$ có tâm $I'({x2}; {y2})$ và bán kính $R'={r2}$.\\\\ "
                           f"Ta có $II' = \\sqrt{{({x2}-{x1})^2 + ({y2}-{y1})^2}} = {latex(dist)}$.\\\\ "
                           f"Vì $|R-R'| = {abs(r1-r2)}$ và $R+R' = {r1+r2}$.\\\\ "
                           f"Dễ thấy các giá trị thỏa mãn điều kiện để hai đường tròn {vi_tri}.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--','+')
            return content

