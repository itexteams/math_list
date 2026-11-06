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


def bt_dang44_p1_b2_c3_ds12(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                a_val = random.randint(-2, 0)
                fa_val = 0

                b_val = random.randint(2, 4)
                fb_val = random.randint(-2, -1)


                phan_x2 = Rational(b_val**2 - a_val**2, 2)
                phan_f = fb_val - fa_val
                kq_sym = phan_x2 + phan_f

                # Định dạng đáp án đúng
                if kq_sym.is_integer:
                    da_dung = str(kq_sym)
                else:
                    da_dung = latex(kq_sym)


                s_list = []
                while len(s_list) < 3:
                    nhieu = kq_sym + random.choice([-2, -1, 1, 2, Rational(3,2), -Rational(1,2)])
                    val_str = str(nhieu) if nhieu.is_integer else latex(nhieu)
                    if val_str != da_dung and val_str not in s_list:
                        s_list.append(val_str)

                # --- TÍNH TOÁN THÔNG SỐ ĐỒ THỊ ĐỂ ĐI QUA ĐIỂM CHO TRƯỚC ---
                # Ta chọn hàm f(x) = k*(x - root_L)*(x - a)*(x - root_R)
                # Để đồ thị giống hình: root_L < a < b < root_R và k > 0
                root_L = a_val - 2
                root_R = b_val + 1.5
                # k = fb / [(b - root_L)*(b - a)*(b - root_R)]
                mau_so = (b_val - root_L) * (b_val - a_val) * (b_val - root_R)
                k_val = float(fb_val) / mau_so

                # --- TẠO MÃ TIKZ ---
                tikz_code = r"""\begin{center} \scalebox{0.6}{ 
            \begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (-4,0) -- (6,0) node[below] {$x$};
                \draw[->] (0,-4) -- (0,4) node[left] {$y$};
                \draw (0,0) node[below left] {$O$};
                \begin{scope}
                    \clip (-3.5,-3.5) rectangle (5.5,3.8);
                    \draw[thick, blue, smooth, samples=100, domain=-3.5:5.5] 
                        plot (\x, {%f*(\x-(%f))*(\x-(%f))*(\x-(%f))}); 
                \end{scope}
                \draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
                \fill (%s,0) circle (1.5pt) node[above left] {$%s$};
                \fill (%s,%s) circle (1.5pt);
                \node at (%s, 0.3) {$%s$};
                \node at (-0.4, %s) {$%s$};
                \node at (3, 2.5) {$y=f(x)$};
            \end{tikzpicture} }
            \end{center}""" % (k_val, root_L, a_val, root_R, 
                   b_val, b_val, fb_val, fb_val, 
                   a_val, a_val, b_val, fb_val, 
                   b_val, b_val, fb_val, fb_val)

                # --- B2: NỘI DUNG CÂU HỎI ---
                text_cauhoi = (r"Cho hàm số $y = f(x)$ có đồ thị như hình vẽ sau. Tích phân $I = \int_{%s}^{%s} [x + f'(x)] dx$ bằng" 
                               % (latex(a_val), latex(b_val)))

                noidungcauhoi = text_cauhoi + tikz_code

                # Nội dung lời giải
                loigiai = (r"Dựa vào đồ thị, ta thấy $f(%s) = %s$ và $f(%s) = %s$.\\"
                           r"Ta có: $I = \int_{%s}^{%s} x \text{d}x + \int_{%s}^{%s} f'(x) \text{d} x$\\"
                           r"$= \left[ \frac{x^2}{2} + f(x) \right]_{%s}^{%s}$\\"
                           r"$= \left( \frac{%s^2}{2} + f(%s) \right) - \left( \frac{(%s)^2}{2} + f(%s) \right)$\\"
                           r"$= \left( \frac{%s}{2} + (%s) \right) - \left( \frac{%s}{2} + %s \right) = %s$."
                           % (latex(a_val), latex(fa_val), latex(b_val), latex(fb_val),
                              latex(a_val), latex(b_val), latex(a_val), latex(b_val),
                              latex(a_val), latex(b_val),
                              latex(b_val), latex(b_val), latex(a_val), latex(a_val),
                              latex(b_val**2), latex(fb_val), latex(a_val**2), latex(fa_val), da_dung))

                # Xử lý các đáp án trắc nghiệm
                da_d = r'\True $%s$' % da_dung
                list_1 = [da_d] + [r'$%s$' % s for s in s_list]
                random.shuffle(list_1)

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

