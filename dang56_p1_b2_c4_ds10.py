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


def bt_dang56_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số 
                x_sym = random.randint(1, 5) 
                c_val = random.randint(-5, 5)

                # Đảm bảo xm không trùng x_sym và không bằng 0
                xm = random.choice([i for i in range(-6, 7) if i != x_sym and i != 0])
                ym = random.randint(-10, 10)

                a, b, c = symbols('a b c')

                # Giải tìm hệ số
                # Từ x = -b/2a => b = -2*a*x_sym
                # Từ đi qua M(xm, ym) => a*xm^2 + b*xm + c_val = ym
                mau_so = (xm**2 - 2 * x_sym * xm)
                if mau_so == 0: mau_so = 1 # Bảo vệ chia cho 0

                a_val = Rational(ym - c_val, mau_so)
                b_val = -2 * a_val * x_sym
                c_final = c_val

                def format_poly(a_v, b_v, c_v):
                    # Hàm format đa thức đẹp mắt
                    res = f"{latex(a_v)}x^2"
                    if b_v > 0: res += f" + {latex(b_v)}x"
                    elif b_v < 0: res += f" {latex(b_v)}x"

                    if c_v > 0: res += f" + {latex(c_v)}"
                    elif c_v < 0: res += f" {latex(c_v)}"
                    return res

                kq_dung = f"$y = {format_poly(a_val, b_val, c_final)}$"

                # TẠO ĐÁP ÁN SAI: Dùng vòng lặp để đảm bảo luôn đủ 3 đáp án khác biệt
                s = set()
                while len(s) < 3:
                    # Tạo biến thể bằng cách thay đổi nhẹ các hệ số
                    a_sai = a_val + random.choice([-1, 1, 2, Rational(1, 2)])
                    b_sai = b_val + random.choice([-2, 2, 3])
                    c_sai = c_final + random.choice([-1, 1, -2])

                    tmp = f"$y = {format_poly(a_sai, b_sai, c_sai)}$"
                    if tmp != kq_dung:
                        s.add(tmp)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = (f"Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó có trục đối xứng là đường thẳng "
                                 f"$x = {x_sym}$, đi qua điểm $M({xm};{ym})$ và cắt trục tung tại điểm có tung độ bằng ${c_val}$?")

                # Các đáp án
                da_d = '\\True ' + kq_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = (f"Vì $(P)$ có trục đối xứng là đường thẳng $x = {x_sym}$ nên $-\\frac{{b}}{{2a}} = {x_sym} \\Leftrightarrow b = {-2*x_sym}a$. (1) \\\\\n"
                           f"Hơn nữa $(P)$ qua $M({xm};{ym})$ nên ta có ${ym} = a({xm})^2 + b({xm}) + c \\Leftrightarrow {ym} = {xm**2}a {'+' if xm*(-2*x_sym) >= 0 else ''} {xm*(-2*x_sym)}a + c$. (2) \\\\\n"
                           f"Lại có $(P)$ cắt trục tung tại điểm có tung độ bằng ${c_val}$ nên ${c_val} = a \\cdot 0^2 + b \\cdot 0 + c \\Leftrightarrow c = {c_val}$. (3) \\\\\n"
                           f"Từ (1), (2) và (3) ta có hệ: $\\begin{{cases}} b = {-2*x_sym}a \\\\ {xm**2}a {'+' if xm*(-2*x_sym) >= 0 else ''} {xm*(-2*x_sym)}a + {c_val} = {ym} \\\\ c = {c_val} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} a = {latex(a_val)} \\\\ b = {latex(b_val)} \\\\ c = {c_val} \\end{{cases}}$. \\\\\n"
                           f"Vậy $(P):$ {kq_dung}.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

