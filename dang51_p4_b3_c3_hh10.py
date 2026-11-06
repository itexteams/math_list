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


def bt_dang51_p4_b3_c3_hh10(self):
            # Khai báo biến
            # --- Bước 3: Suy nghĩ tìm cách random bài toán ---
            def generate_problem():
                # Chọn tâm I và bán kính R^2 sao cho dễ ra nghiệm nguyên
                xI, yI = random.randint(-2, 2), random.randint(-2, 2)
                r2 = random.choice([5, 10, 13, 17, 25, 26, 29]) 

                # Tìm tập hợp các điểm nguyên trên đường tròn
                pts = []
                for x_val in range(xI - 6, xI + 7):
                    rem = r2 - (x_val - xI)**2
                    if rem >= 0:
                        sr = int(rem**0.5)
                        if sr * sr == rem:
                            pts.append((x_val, yI + sr))
                            if sr != 0:
                                pts.append((x_val, yI - sr))

                # Lọc điểm: Cần ít nhất 1 điểm x > 0 và 1 điểm x < 0
                pts_pos = [p for p in pts if p[0] > 0]
                pts_neg = [p for p in pts if p[0] < 0]

                if len(pts_pos) < 1 or len(pts_neg) < 1:
                    return generate_problem() # Thử lại nếu không đủ điều kiện

                A_pt = random.choice(pts_pos) # A hoành độ dương
                B_pt = random.choice(pts_neg) # B hoành độ âm

                xA, yA = A_pt
                xB, yB = B_pt

                # Viết phương trình đường thẳng d đi qua A và B
                dx = xB - xA
                dy = yB - yA
                a_l, b_l, c_l = dy, -dx, dx*yA - dy*xA

                # Rút gọn hệ số đường thẳng
                common = sp.gcd(sp.gcd(a_l, b_l), c_l)
                a_l //= common; b_l //= common; c_l //= common
                if a_l < 0 or (a_l == 0 and b_l < 0):
                    a_l, b_l, c_l = -a_l, -b_l, -c_l

                # Tọa độ C (đối xứng A qua I vì tam giác ABC vuông tại B)
                xC, yC = 2*xI - xA, 2*yI - yA
                c_const = xI**2 + yI**2 - r2

                # Định dạng chuỗi toán học
                def fmt(val, var, is_first=False):
                    if val == 0: return ""
                    sign = "+" if val > 0 else "-"
                    abs_v = abs(val)
                    res = f"{abs_v}{var}" if abs_v != 1 else var
                    if is_first:
                        return f"{'' if val > 0 else '-'}{res}"
                    return f" {sign} {res}"

                str_C = f"x^2 + y^2{fmt(-2*xI, 'x')}{fmt(-2*yI, 'y')} {'+' if c_const >= 0 else '-'} {abs(c_const)} = 0"
                str_d = f"{fmt(a_l, 'x', True)}{fmt(b_l, 'y')} {'+' if c_l >= 0 else '-'} {abs(c_l)} = 0"

                # Làm sạch chuỗi (xử lý +- và hệ số 0)
                str_C = str_C.replace("+ 0x", "").replace("- 0x", "").replace("+ 0y", "").replace("- 0y", "").replace("  ", " ")
                str_d = str_d.replace("+ 0x", "").replace("- 0x", "").replace("+ 0y", "").replace("- 0y", "").replace("  ", " ")

                noidungcauhoi = (f"Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường thẳng $d: {str_d}$ "
                                 f"và đường tròn $(C): {str_C}$. Các giao điểm $A, B$ "
                                 f"của đường tròn $(C)$ và đường thẳng $d$, biết $A$ có hoành độ dương và $B$ có hoành độ âm. "
                                 f"Tìm tọa độ điểm $C$ thuộc $(C)$ sao cho tam giác $ABC$ vuông ở $B$.")

                loigiai = (f"Đường tròn $(C)$ có tâm $I({xI};{yI})$, bán kính $R = \\sqrt{{{r2}}}$. \\\\\n"
                           f"Tọa độ giao điểm của $A$ và $B$ là nghiệm của hệ: \\\\\n"
                           f"$\\begin{{cases}} {str_C} \\\\ {str_d} \\end{{cases}} \\Leftrightarrow "
                           f"\\left[\\begin{{aligned}} &x = {xA}, y = {yA} \\\\ &x = {xB}, y = {yB} \\end{{aligned}}\\right.$. \\\\\n"
                           f"Do $A$ có hoành độ dương và $B$ có hoành độ âm nên ta chọn $A({xA};{yA}), B({xB};{yB})$. \\\\\n"
                           f"Vì $\\triangle ABC$ vuông tại $B$ nên $AC$ là đường kính đường tròn $(C)$. \\\\\n"
                           f"Khi đó $C$ đối xứng với $A$ qua tâm $I$, suy ra $C({xC};{yC})$.")

                # Đáp án trắc nghiệm
                da_d = f"\\True $C({xC};{yC})$"
                list_1 = [da_d, f"$C({xB};{yB})$", f"$C({-xC};{yC})$", f"$C({yC};{xC})$"]
                random.shuffle(list_1)

                return noidungcauhoi, list_1, loigiai

            noidungcauhoi, list_1, loigiai = generate_problem()

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

