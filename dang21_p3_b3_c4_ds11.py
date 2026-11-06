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


def bt_dang21_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            def generate_fixed_sign_question():
                # B3: Random điểm chia x0 (có thể âm hoặc dương)
                x0 = random.randint(-5, 5)
                while x0 == 0: x0 = random.randint(-5, 5) # Tránh x0 = 0 để thấy rõ việc xử lý dấu

                m = random.randint(2, 5)
                k = random.randint(1, 5)

                # Tính toán giá trị
                limit_right = x0**2 + k
                a_correct = limit_right - m * x0

                # Tạo biểu thức tử số và mẫu số
                # Sử dụng sympy để tự động tối ưu dấu: x - (-2) sẽ thành x + 2
                mau_so_expr = x - x0
                tu_so_expr = expand((x - x0) * (x**2 + k))

                # Chuyển sang chuỗi latex (sympy tự xử lý x - (-2) thành x + 2)
                str_mau_so = latex(mau_so_expr)
                str_tu_so = latex(tu_so_expr)
                str_x0 = latex(x0)

                # Xử lý phần hiển thị m*x0 + a để tránh + -
                mx0 = m * x0
                phan_tu_tu_do = f"{mx0} + a" if mx0 >= 0 else f"{mx0} + a" 
                # Nếu muốn đẹp hơn có thể dùng: f"({mx0}) + a"

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (r"Giá trị của $a$ để hàm số liên tục trên $\mathbb{R}$ bằng bao nhiêu? "
                                 r"$f(x) = \begin{cases} %sx + a & \text{khi } x \le %s \\ \frac{%s}{%s} & \text{khi } x > %s \end{cases}$."
                                 % (latex(m), str_x0, str_tu_so, str_mau_so, str_x0))

                # --- Đáp án ---
                da_dung = f"$a = {a_correct}$"
                s = set()
                while len(s) < 3:
                    sai = a_correct + random.choice([-2, -1, 1, 2, 5])
                    if sai != a_correct: s.add(f"$a = {sai}$")

                list_1 = [r"\True " + da_dung] + list(s)
                random.shuffle(list_1)

                # --- Lời giải (Xử lý triệt để dấu) ---
                # Sử dụng hàm latex của sympy trực tiếp lên biểu thức (x - x0) 
                # để nó tự biến x - (-2) thành x + 2
                nhan_tu_rut_gon = latex(x - x0) 

                loigiai = (r"Khi $x < %s$ thì $f(x) = %sx + a$ là hàm đa thức nên liên tục trên $(-\infty; %s)$.\\"
                           r"Khi $x > %s$ thì $f(x) = \frac{%s}{%s}$ liên tục trên $(%s; +\infty)$.\\"
                           r"Xét tính liên tục tại $x = %s$:\\"
                           r"+ $f(%s) = %s(%s) + a = %s + a$.\\"
                           r"+ $\lim_{x \to %s^-} f(x) = %s + a$.\\"
                           r"+ $\lim_{x \to %s^+} f(x) = \lim_{x \to %s^+} \frac{(%s)(x^2 + %s)}{%s} = \lim_{x \to %s^+} (x^2 + %s) = %s$.\\"
                           r"Hàm số liên tục trên $\mathbb{R} \Leftrightarrow$ liên tục tại $x = %s$\\"
                           r"$\Leftrightarrow %s + a = %s \Leftrightarrow a = %s$."
                           % (str_x0, latex(m), str_x0,
                              str_x0, str_tu_so, str_mau_so, str_x0,
                              str_x0,
                              str_x0, latex(m), str_x0, latex(mx0),
                              str_x0, latex(mx0),
                              str_x0, str_x0, nhan_tu_rut_gon, latex(k), str_mau_so, str_x0, latex(k), latex(limit_right),
                              str_x0,
                              latex(mx0), latex(limit_right), latex(a_correct)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a_correct))

                return noidungcauhoi, list_1, loigiai, dapan

            # Thực thi và in kết quả
            noidung, d_an, giai, dapan = generate_fixed_sign_question()
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidung + dapan+'\n'
                       '\\loigiai{' + giai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content   

