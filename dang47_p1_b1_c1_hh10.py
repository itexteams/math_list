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


def bt_dang47_p1_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các nghiệm cho phương trình bậc 2 của cos(alpha)
                # Nghiệm dương (nhận): p1/q1 với 0 < p1 < q1
                # Nghiệm âm (loại): -p2/q2 với p2, q2 > 0
                while True:
                    q1 = random.randint(2, 5)
                    p1 = random.randint(1, q1 - 1)
                    g1 = math.gcd(p1, q1)
                    p1 //= g1
                    q1 //= g1

                    q2 = random.randint(2, 5)
                    p2 = random.randint(1, q2 - 1)
                    g2 = math.gcd(p2, q2)
                    p2 //= g2
                    q2 //= g2

                    # Tạo hệ số cho phương trình a*cos^2(a) + b*cos(a) + c = 0
                    a = q1 * q2
                    b = p2 * q1 - p1 * q2
                    c = - p1 * p2

                    # Hạn chế trường hợp khuyết b để giống mẫu nhất
                    if b != 0:
                        break

                # Hàm tạo chuỗi hiển thị phương trình đẹp (xử lý dấu cộng/trừ)
                def format_eq(a, b, c):
                    res = f"{a}\\cos^2 \\alpha"
                    if b == 1:
                        res += " + \\cos \\alpha"
                    elif b == -1:
                        res += " - \\cos \\alpha"
                    elif b > 0:
                        res += f" + {b}\\cos \\alpha"
                    elif b < 0:
                        res += f" - {abs(b)}\\cos \\alpha"

                    if c > 0:
                        res += f" + {c}"
                    elif c < 0:
                        res += f" - {abs(c)}"
                    return res + " = 0"

                def format_t_eq(a, b, c):
                    res = f"{a}t^2"
                    if b == 1:
                        res += " + t"
                    elif b == -1:
                        res += " - t"
                    elif b > 0:
                        res += f" + {b}t"
                    elif b < 0:
                        res += f" - {abs(b)}t"

                    if c > 0:
                        res += f" + {c}"
                    elif c < 0:
                        res += f" - {abs(c)}"
                    return res + " = 0"

                pt_str = format_eq(a, b, c)
                t_pt_str = format_t_eq(a, b, c)

                # Tính các giá trị lượng giác
                cos_val = Rational(p1, q1)
                cos_sq = cos_val**2
                sin_sq = 1 - cos_sq
                tan_sq = sin_sq / cos_sq

                # Kết quả của biểu thức P
                P_val = simplify(tan_sq + sin_sq)

                # Đáp án đúng
                du = ['$%s$' % latex(P_val)]
                da = du[0]

                # Tạo các phương án sai (nhiễu)
                cot_sq = cos_sq / sin_sq
                w1 = simplify(1 / P_val)              # Nghịch đảo
                w2 = simplify(tan_sq - sin_sq)        # Nhầm dấu
                w3 = simplify(cot_sq + cos_sq)        # Nhầm hàm
                w4 = simplify(P_val * Rational(1, 2)) # Sai hệ số

                choices = [w1, w2, w3, w4]
                s_set = set()
                for cand in choices:
                    cand_str = '$%s$' % latex(cand)
                    if cand != P_val and cand_str != da:
                        s_set.add(cand_str)

                # Bổ sung ngẫu nhiên nếu các nhiễu bị trùng và chưa đủ 3 đáp án sai
                count = 1
                while len(s_set) < 3:
                    fake = P_val + Rational(count, 3)
                    fake_str = '$%s$' % latex(fake)
                    if fake != P_val and fake_str != da and fake_str not in s_set:
                        s_set.add(fake_str)
                    count += 1

                s = list(s_set)
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Cho $%s$, $0^\\circ < \\alpha < 90^\\circ$. Giá trị của biểu thức $P = \\tan^2 \\alpha + \\sin^2 \\alpha$ bằng' % pt_str)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Hiển thị cấu trúc điều kiện nghiệm
                root_str = "\\begin{array}{l} t = %s \\text{ (nhận)} \\\\ t = %s \\text{ (loại)} \\end{array}" % (latex(Rational(p1, q1)), latex(Rational(-p2, q2)))

                # Nội dung lời giải chi tiết
                loigiai = ('''Phương trình: $%s$. \\\\
                              Đặt $t = \\cos \\alpha$. Vì $0^\\circ < \\alpha < 90^\\circ$ nên $0 < t < 1$. \\\\
                              Phương trình trở thành: $%s$ \\\\
                              $\\Leftrightarrow \\left[ %s \\right.$. \\\\
                              Suy ra $\\cos \\alpha = %s \\Rightarrow \\cos^2 \\alpha = %s$. \\\\
                              Ta có $\\sin^2 \\alpha = 1 - \\cos^2 \\alpha = 1 - %s = %s$. \\\\
                              Và $\\tan^2 \\alpha = \\frac{\\sin^2 \\alpha}{\\cos^2 \\alpha} = \\frac{%s}{%s} = %s$. \\\\
                              Vậy $P = \\tan^2 \\alpha + \\sin^2 \\alpha = %s + %s = %s$.'''
                           % (pt_str, t_pt_str, root_str,
                              latex(cos_val), latex(cos_sq),
                              latex(cos_sq), latex(sin_sq),
                              latex(sin_sq), latex(cos_sq), latex(tan_sq),
                              latex(tan_sq), latex(sin_sq), latex(P_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

