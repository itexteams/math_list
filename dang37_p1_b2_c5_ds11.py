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


def bt_dang37_p1_b2_c5_ds11(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các số nguyên tố để bài toán luôn đẹp và có nghĩa
                n = random.choice([2, 3, 5])        # Cơ số trung gian (trong hình là 3)
                m = random.choice([x for x in [2, 3, 5] if x != n]) # Thừa số chung (trong hình là 2)
                p = random.choice([7, 11, 13, 17])  # Số nguyên tố còn lại (trong hình là 7)
                k = random.randint(2, 4)            # Số mũ (trong hình là 3)

                # Các giá trị xuất hiện trong đề bài
                base_M = m * n                      # Cơ số của M (m*n = 6)
                arg_M = (m**k) * p                  # Số dưới dấu log của M (2^3 * 7 = 56)

                # Đáp án đúng dựa trên biến đổi: a=k, b=k, c=1
                ans_a, ans_b, ans_c = k, k, 1
                da_dung_str = f"a={ans_a}, b={ans_b}, c={ans_c}"

                # Bước 4: Tạo các phương án sai
                s = [
                    f"a={ans_a}, b={ans_a}, c={ans_a}",
                    f"a={ans_a}, b={ans_c}, c={ans_a}",
                    f"a={ans_c}, b={ans_a}, c={ans_a}",
                    f"a={ans_a}, b={ans_b}, c={ans_b+1}",
                    f"a={ans_a+1}, b={ans_b}, c={ans_c}",
                ]
                s = list(set([x for x in s if x != da_dung_str])) # Loại bỏ trùng lặp
                random.shuffle(s)

                das1, das2, das3 = s[0], s[1], s[2]

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r"Đặt $M = \log_{%s} %s, N = a + \frac{\log_{%s} %s - b}{\log_{%s} %s + c}$ với $a, b, c \in \mathbb{R}$. Bộ số $a, b, c$ nào dưới đây để có $M = N$?"
                                 % (latex(base_M), latex(arg_M), n, p, n, m))

                # --- NỘI DUNG LỜI GIẢI (Sử dụng f-string để tránh lỗi đếm %s) ---
                # Chuẩn bị các thành phần nhỏ để ghép vào lời giải cho sạch sẽ
                log_n_m = fr"\log_{{{n}}} {m}"
                log_n_p = fr"\log_{{{n}}} {p}"

                loigiai = (fr"""Ta có:
            $M = \log_{{{base_M}}} {arg_M} = \frac{{\log_{{{n}}} {arg_M}}}{{\log_{{{n}}} {base_M}}} = \frac{{\log_{{{n}}} ({m}^{k} \cdot {p})}}{{1 + {log_n_m}}} = \frac{{{k}{log_n_m} + {log_n_p}}}{{1 + {log_n_m}}}$
            $= \frac{{{k}(1 + {log_n_m}) + {log_n_p} - {k}}}{{1 + {log_n_m}}} = {k} + \frac{{{log_n_p} - {k}}}{{{log_n_m} + 1}}$.
            Vậy $M = N \Leftrightarrow \begin{{cases}} a = {ans_a} \\ b = {ans_b} \\ c = {ans_c} \end{{cases}}$.""")

                # Các đáp án trắc nghiệm
                da_d = f"\\True ${da_dung_str}$"
                list_1 = [da_d, f"${das1}$", f"${das2}$", f"${das3}$"]
                random.shuffle(list_1)

            # --- XUẤT CÂU TRẮC NGHIỆM ---
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

