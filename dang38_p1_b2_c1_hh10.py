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


def bt_dang38_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị
                valid = False
                while not valid:
                    # Chọn độ dài AC (b) và BC (a)
                    AC_val = random.randint(3, 8)
                    BC_val = random.randint(4, 9)

                    # Tạo phân số cos(A+B) = -cosC
                    den = random.choice([3, 4, 5, 6, 8, 9])
                    num = random.randint(1, den - 1)

                    # Chọn dấu cho cos(A+B) (thường là âm để góc C nhọn, nhưng cứ random)
                    sign = random.choice([-1, 1])
                    cos_A_plus_B = Rational(sign * num, den)
                    cos_C = -cos_A_plus_B

                    # Tính cạnh c = AB theo định lý cosin: c^2 = a^2 + b^2 - 2ab*cosC
                    AB_sq = AC_val**2 + BC_val**2 - 2 * AC_val * BC_val * cos_C

                    if AB_sq > 0:
                        AB = simplify(sqrt(AB_sq))
                        # Kiểm tra bất đẳng thức tam giác
                        AB_float = float(AB)
                        if (AB_float + AC_val > BC_val) and (AC_val + BC_val > AB_float) and (BC_val + AB_float > AC_val):
                            valid = True

                kq = latex(AB)

                # Tạo các phương án sai (distractors)
                # Sai lầm 1: Nhầm dấu của cosC (cho cosC = cos(A+B) thay vì -cos(A+B))
                fake1_sq = AC_val**2 + BC_val**2 - 2 * AC_val * BC_val * cos_A_plus_B
                fake1 = simplify(sqrt(fake1_sq)) if fake1_sq > 0 else simplify(sqrt(AC_val**2 + BC_val**2 + 5))

                # Sai lầm 2: Áp dụng Pytago (bỏ qua phần -2ab*cosC)
                fake2 = simplify(sqrt(AC_val**2 + BC_val**2))

                # Sai lầm 3: Quên lấy căn bậc hai hoặc tính sai
                fake3_sq = AC_val**2 + BC_val**2 + 2 * AC_val * BC_val * cos_C # Sai dấu trong định lý cosin
                fake3 = simplify(sqrt(fake3_sq)) if fake3_sq > 0 else simplify(sqrt(AC_val**2 + BC_val**2 + 7))

                s_cands = [fake1, fake2, fake3]
                unique_s_cands = []
                for cand in s_cands:
                    if cand != AB and cand not in unique_s_cands:
                        unique_s_cands.append(cand)

                # Đảm bảo đủ 3 phương án sai
                while len(unique_s_cands) < 3:
                    bogus = simplify(sqrt(AB_sq + random.choice([-4, -2, 2, 4, 6])))
                    if bogus > 0 and bogus != AB and bogus not in unique_s_cands:
                        unique_s_cands.append(bogus)

                random.shuffle(unique_s_cands)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % (latex(unique_s_cands[0])),
                    '$%s$' % (latex(unique_s_cands[1])),
                    '$%s$' % (latex(unique_s_cands[2]))
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Tam giác $ABC$ có $\\cos(A+B)=%s, AC=%s, BC=%s$. Cạnh $AB$ bằng'
                                 % (latex(cos_A_plus_B), AC_val, BC_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Tính thành phần 2*AC*BC
                term_2ab = 2 * AC_val * BC_val
                term_mul = simplify(term_2ab * cos_C)

                loigiai = ('Trong tam giác $ABC$, ta có $A + B + C = 180^\\circ \\Rightarrow A + B = 180^\\circ - C$.\\\\ \n'
                           'Suy ra $\\cos(A+B) = \\cos(180^\\circ - C) = -\\cos C$.\\\\ \n'
                           'Do đó $\\cos C = -\\cos(A+B) = -\\left(%s\\right) = %s$.\\\\ \n'
                           'Áp dụng định lí côsin trong tam giác $ABC$, ta có:\\\\ \n'
                           '$AB^2 = AC^2 + BC^2 - 2 \\cdot AC \\cdot BC \\cdot \\cos C$\\\\ \n'
                           '$\\Rightarrow AB^2 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\left(%s\\right) = %s + %s - %s = %s$.\\\\ \n'
                           'Vậy $AB = %s$.'
                           % (latex(cos_A_plus_B), latex(cos_C),
                              AC_val, BC_val, AC_val, BC_val, latex(cos_C), AC_val**2, BC_val**2, latex(term_mul), latex(AB_sq),
                              kq))

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

