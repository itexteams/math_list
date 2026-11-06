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


def bt_dang12_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: SUY NGHĨ TÌM CÁCH RANDOM ---
                # f(x) = m1*a*x^2 + n1*b*x + k  khi x <= x0
                # f(x) = m2*a*x + n2*b         khi x > x0
                # Tại x = x0: m1*a*x0^2 + n1*b*x0 + k = m2*a*x0 + n2*b
                # => (m1*x0^2 - m2*x0)a + (n1*x0 - n2)b = -k

                x0 = random.randint(1, 9) # Có thể random x0 nếu muốn phức tạp hơn
                m1 = random.randint(1, 9)
                n1 = random.randint(1, 9)
                k = random.randint(-10, 10)
                if k == 0: k = -5 # Tránh trường hợp bằng 0 quá đơn giản

                m2 = m1 + random.randint(1, 9)
                n2 = n1 + random.randint(1, 9)

                # Tính toán các hệ số cho biểu thức P = Aa + Bb
                A = m1 * (x0**2) - m2 * x0
                B = n1 * x0 - n2
                kq_val = -k

                # Tạo chuỗi latex cho biểu thức P
                char_A = "" if A == 1 else ("-" if A == -1 else str(A))
                char_B = "+" if B > 0 else "-"
                val_B = abs(B)
                char_B_str = f"{char_B} {val_B}" if val_B != 1 else char_B

                bieu_thuc_P = f"P = {char_A}a {char_B_str}b"

                # Các đáp án
                kq = kq_val
                du = [f'${latex(kq)}$']
                da = random.choice(du)

                # Tạo đáp án nhiễu
                s = [
                    f'${latex(kq + random.randint(1, 5))}$',
                    f'${latex(kq - random.randint(1, 5))}$',
                    f'${latex(-kq)}$',
                    f'${latex(k)}$',
                    f'${latex(kq + 2)}$',
                    f'${latex(kq - 2)}$'
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # --- NỘI DUNG CÂU HỎI ---
                # f1 = m1*a*x^2 + n1*b*x + k
                # f2 = m2*a*x + n2*b
                part1 = f"{'' if m1==1 else m1}ax^2 {'+' if n1>0 else ''}{'' if n1==1 else n1}bx {k:+}"
                part2 = f"{m2}ax {'+' if n2>0 else ''}{'' if n2==1 else n2}b"

                noidungcauhoi = (f"Biết hàm số $f(x) = \\begin{{cases}} {part1} & \\text{{khi }} x \\le {x0} \\\\ {part2} & \\text{{khi }} x > {x0} \\end{{cases}}$ "
                                 f"liên tục tại $x = {x0}$. Giá trị của biểu thức ${bieu_thuc_P}$ bằng bao nhiêu?")

                # --- NỘI DUNG LỜI GIẢI ---
                loigiai = (f"Ta có: $\\lim_{{x \\to {x0}^-}} f(x) = f({x0}) = {m1}a({x0})^2 + {n1}b({x0}) {k:+} = {m1*x0**2}a + {n1*x0}b {k:+}$.\\\\ "
                           f"$\\lim_{{x \\to {x0}^+}} f(x) = \\lim_{{x \\to {x0}^+}} ({part2}) = {m2*x0}a {n2:+}b$.\\\\ "
                           f"Do hàm số liên tục tại $x = {x0}$ nên: \\\\ "
                           f"${m1*x0**2}a + {n1*x0}b {k:+} = {m2*x0}a {n2:+}b \\Rightarrow ({m1*x0**2} - {m2*x0})a + ({n1*x0} - {n2})b = {-k} \\Rightarrow {bieu_thuc_P.replace('P = ', '')} = {kq}$.")
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
                # Xuất câu trắc nghiệm
                da_d = f"\\True {da}"
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+ '\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content   

