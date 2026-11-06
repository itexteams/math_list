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


def bt_dang38_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tổng x^2 + y^2 = 2 * (số ở giữa)
                sum_sq = random.choice([1, 2, 3, 4])
                if sum_sq % 2 == 0:
                    u_tex = str(sum_sq // 2)
                else:
                    u_tex = "\\frac{%s}{2}" % sum_sq

                # Random hệ số của y^2
                b = random.choice([1, 2, 3])
                b_str = "" if b == 1 else str(b)

                # Random hệ số của xy
                a_opts = ["\\sqrt{3}", "\\sqrt{2}", "2", "3"]
                a_tex = random.choice(a_opts)

                # Biểu thức P
                if b == 1:
                    P_str = f"P = {a_tex}xy + y^2"
                else:
                    P_str = f"P = {a_tex}xy + {b}y^2"

                # Kết quả S = M + m
                ans_val = sum_sq * b

                da = f"${ans_val}$"

                # Tạo các phương án sai
                s_set = set()
                while len(s_set) < 3:
                    wrong = ans_val + random.choice([-2, -1, 1, 2, 3])
                    if wrong != ans_val and wrong > 0:
                        s_set.add(f"${wrong}$")

                s = list(s_set)
                # Thêm 1 phương án nhiễu dạng phân số giống đề bài gốc
                if random.random() < 0.5:
                    s[0] = "$\\frac{\\sqrt{3}}{2} - \\frac{1}{2}$"

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = f"Cho $x^2; {u_tex}; y^2$ theo thứ tự lập thành một cấp số cộng. Gọi $M, m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của biểu thức ${P_str}$. Tổng $S = M + m$ bằng"

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Thiết lập chuỗi công thức cho lời giải dựa trên biến R = sqrt(sum_sq)
                if sum_sq == 1:
                    sub_x = "\\cos \\alpha"
                    sub_y = "\\sin \\alpha"
                    step1 = f"{a_tex} \\cos \\alpha \\sin \\alpha + {b_str} \\sin^2 \\alpha"
                else:
                    sub_x = f"\\sqrt{{{sum_sq}}} \\cos \\alpha"
                    sub_y = f"\\sqrt{{{sum_sq}}} \\sin \\alpha"
                    step1 = f"{a_tex} ({sub_x}) ({sub_y}) + {b_str} ({sub_y})^2 = {sum_sq} \\cdot {a_tex} \\cos \\alpha \\sin \\alpha + {sum_sq * b} \\sin^2 \\alpha"

                a_term = a_tex if sum_sq == 1 else f"{sum_sq} \\cdot {a_tex}"
                fraction_A = f"\\frac{{{a_term}}}{{2}}"
                fraction_B = f"\\frac{{{sum_sq * b}}}{{2}}"

                # Nội dung lời giải
                loigiai = f'''Ta có $x^2; {u_tex}; y^2$ theo thứ tự lập thành một cấp số cộng nên: \\\\
            $x^2 + y^2 = 2 \\cdot {u_tex} = {sum_sq}$. \\\\
            Do đó, tồn tại góc $\\alpha$ sao cho $x = {sub_x}$ và $y = {sub_y}$. \\\\
            Thay vào biểu thức $P$, ta có: \\\\
            $P = {step1}$ \\\\
            $P = {fraction_A} \\sin 2\\alpha + {sum_sq * b} \\cdot \\frac{{1 - \\cos 2\\alpha}}{{2}}$ \\\\
            $P = {fraction_A} \\sin 2\\alpha - {fraction_B} \\cos 2\\alpha + {fraction_B}$. \\\\
            Biểu thức có dạng $P = A \\sin 2\\alpha + B \\cos 2\\alpha + C$ với $C = {fraction_B}$. \\\\
            Áp dụng điều kiện có nghiệm của phương trình lượng giác $A \\sin 2\\alpha + B \\cos 2\\alpha = P - C$, ta có: \\\\
            $(P - C)^2 \\le A^2 + B^2 \\Leftrightarrow C - \\sqrt{{A^2 + B^2}} \\le P \\le C + \\sqrt{{A^2 + B^2}}$. \\\\
            Suy ra giá trị lớn nhất là $M = C + \\sqrt{{A^2 + B^2}}$ và giá trị nhỏ nhất là $m = C - \\sqrt{{A^2 + B^2}}$. \\\\
            Vậy tổng $S = M + m = 2C = 2 \\cdot {fraction_B} = {ans_val}$.'''

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

