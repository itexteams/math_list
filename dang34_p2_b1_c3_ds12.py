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


def bt_dang34_p2_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến Sympy
            t = symbols('t')

            p0 = random.choice([300, 400, 500, 600])
            dp1 = random.choice([50, 100, 150, 200])
            p1 = p0 + dp1
            t_calc = random.randint(5, 9)

            k_val = Rational(3 * dp1, 2)
            he_so_truoc_t = Rational(2 * k_val, 3) # Chính là dp1

            # Biểu thức P(t)
            expr_P = he_so_truoc_t * sqrt(t**3) + p0

            # Tính giá trị tại t_calc
            val_at_t = float(he_so_truoc_t * (t_calc**(1.5)) + p0)
            val_round = round(val_at_t)

            # --- BƯỚC 2: VIẾT LẠI THEO MẪU CODE PYTHON ---

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Một quần thể vi khuẩn ban đầu gồm $%s$ vi khuẩn, sau đó bắt đầu tăng trưởng. Gọi $P(t)$ là số lượng vi khuẩn của quần thể đó tại thời điểm $t$ (ngày), $(0 \le t \le 10)$. Tốc độ tăng trưởng của quần thể được cho bởi hàm số $P'(t)=k\sqrt{t}$, trong đó $k$ là hằng số. Sau $1$ ngày, số lượng vi khuẩn đã tăng lên thành $%s$ con.''' 
                            % (latex(p0), latex(p1)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                # --- Nhận biết: Về nguyên hàm cơ bản ---
                nb_da_d = r'\True Hàm số $P(t)$ là một nguyên hàm của hàm số $f(t)=k\sqrt{t}$'
                nb_da_s = r'Hàm số $P(t)$ là một đạo hàm của hàm số $f(t)=k\sqrt{t}$'
                nb_da = random.choice([nb_da_d, nb_da_s])

                # --- Thông hiểu: Tìm hằng số C ---
                th_da_d = r'\True Hằng số tự do khi tìm nguyên hàm $P(t)$ là $C=%s$' % latex(p0)
                th_da_s = r'Hằng số tự do khi tìm nguyên hàm $P(t)$ là $C=%s$' % latex(p1)
                th_da = random.choice([th_da_d, th_da_s])

                # --- Vận dụng: Tìm hằng số k và công thức P(t) ---
                vd_da_d = r'\True Công thức của hàm số là $P(t) = %s\sqrt{t^3} + %s$' % (latex(he_so_truoc_t), latex(p0))
                vd_da_s = r'Công thức của hàm số là $P(t) = %s\sqrt{t} + %s$' % (latex(k_val), latex(p0))
                vd_da = random.choice([vd_da_d, vd_da_s])

                # --- Vận dụng cao: Tính giá trị cụ thể ---
                vdc_da_d = r'\True Số lượng vi khuẩn sau $%s$ ngày xấp xỉ $%s$ con' % (t_calc, val_round)
                vdc_da_s = r'Số lượng vi khuẩn sau $%s$ ngày xấp xỉ $%s$ con' % (t_calc, val_round + random.randint(10, 50))
                vdc_da = random.choice([vdc_da_d, vdc_da_s])

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Nội dung lời giải chi tiết
            loigiai_tonghop = [
                'Ta có $P(t) = \\int k\\sqrt{t} \\text{d}t = \\frac{2k}{3}t^{\\frac{3}{2}} + C$. Do đó $P(t)$ là nguyên hàm của $P\'(t)$.',
                r'Vì $P(0) = %s \Rightarrow C = %s$.' % (latex(p0), latex(p0)),
                r'Sau 1 ngày $P(1) = %s \Rightarrow \frac{2k}{3}\cdot 1^{\frac{3}{2}} + %s = %s \Rightarrow k = %s$. \\ Vậy $P(t) = %s\sqrt{t^3} + %s$.' % (latex(p1), latex(p0), latex(p1), latex(k_val), latex(he_so_truoc_t), latex(p0)),
                r'Sau $%s$ ngày: $P(%s) = %s\sqrt{%s^3} + %s \approx %s$.' % (t_calc, t_calc, latex(he_so_truoc_t), t_calc, latex(p0), val_round)
            ]

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + answers[0] + '}\n'
                '{' + answers[1] + '}\n'
                '{' + answers[2] + '}\n'
                '{' + answers[3] + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_tonghop[0] + '\n'
                '\\item ' + loigiai_tonghop[1] + '\n'
                '\\item ' + loigiai_tonghop[2] + '\n'
                '\\item ' + loigiai_tonghop[3] + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

