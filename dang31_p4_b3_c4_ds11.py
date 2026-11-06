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


def bt_dang31_p4_b3_c4_ds11(self):
            # Khai báo biến
             # --- Khởi tạo các biến ký hiệu ---
            a, b, x = symbols('a b x')

            # --- Bước 1: Random các giá trị để tạo đề bài ---
            # Đảm bảo x1 < x2 và các giá trị nguyên để bài toán đẹp
            x1 = random.randint(-8, -2)   # Tương ứng -5 trong đề
            x2 = random.randint(5, 12)    # Tương ứng 10 trong đề
            c = random.randint(10, 20)    # Tương ứng 17 trong đề
            d = random.randint(5, 15)     # Tương ứng 10 trong đề

            # --- Bước 2: Giải hệ phương trình tìm a, b ---
            # Tại x1: x1**2 + a*x1 + b = x1 + c
            eq1 = Eq(x1*a + b, x1 + c - x1**2)
            # Tại x2: a*x2 + b + d = x2 + c
            eq2 = Eq(x2*a + b, x2 + c - d)

            sol = solve((eq1, eq2), (a, b))
            val_a = sol[a]
            val_b = sol[b]
            kq_val = val_a + val_b # Giá trị a + b

            # Chuyển sang latex để hiển thị
            latex_a = latex(val_a)
            latex_b = latex(val_b)
            latex_kq = latex(kq_val)

            # --- Bước 3: Tạo các phương án nhiễu ---
            # Tạo danh sách đáp án đúng và sai
            da_dung = '$%s$' % latex_kq
            s = []
            while len(s) < 3:
                nhieu = kq_val + random.choice([-2, -1, 1, 2, 3, sp.Rational(1,2), -sp.Rational(1,2)])
                nhieu_str = '$%s$' % latex(nhieu)
                if nhieu_str != da_dung and nhieu_str not in s:
                    s.append(nhieu_str)

            da_s1, da_s2, da_s3 = s

            # --- Bước 4: Soạn nội dung câu hỏi và lời giải ---
            noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} x^2 + ax + b & \text{khi } x < %s \\ x + %s & \text{khi } %s \le x \le %s \\ ax + b + %s & \text{khi } x > %s \end{cases}$ liên tục trên $\mathbb{R}$. Tính $a + b$.'''
                             % (latex(x1), latex(c), latex(x1), latex(x2), latex(d), latex(x2)))

            # Tính toán các bước cho lời giải
            f_x1 = x1 + c
            f_x2 = x2 + c
            lim_trai_x1 = x1**2 # phần hằng số của x^2
            he_so_a_x1 = x1
            lim_phai_x2 = d # phần hằng số cộng thêm

            loigiai = (r'''Hàm số liên tục trên $(-\infty; %s)$, $(%s; %s)$ và $(%s; +\infty)$. \\
                       Để hàm số liên tục trên $\mathbb{R}$ thì hàm số phải liên tục tại $x = %s$ và $x = %s$. \\
                       Ta có: $f(%s) = %s$; $f(%s) = %s$. \\
                       $\lim_{x \to %s^-} f(x) = \lim_{x \to %s^-} (x^2 + ax + b) = %s + %sa + b$. \\
                       $\lim_{x \to %s^+} f(x) = \lim_{x \to %s^+} (ax + b + %s) = %sa + b + %s$. \\
                       Hàm số liên tục tại $x = %s$ và $x = %s$ khi: \\
                       $\begin{cases} %sa + b + %s = %s \\ %sa + b + %s = %s \end{cases} \Leftrightarrow \begin{cases} %sa + b = %s \\ %sa + b = %s \end{cases} \Leftrightarrow \begin{cases} a = %s \\ b = %s \end{cases}$ \\
                       Vậy $a + b = %s$.'''
                       % (latex(x1), latex(x1), latex(x2), latex(x2), 
                          latex(x1), latex(x2),
                          latex(x1), latex(f_x1), latex(x2), latex(f_x2),
                          latex(x1), latex(x1), latex(x1**2), latex(x1),
                          latex(x2), latex(x2), latex(d), latex(x2), latex(d),
                          latex(x1), latex(x2),
                          latex(x1), latex(x1**2), latex(f_x1), latex(x2), latex(d), latex(f_x2),
                          latex(x1), latex(f_x1 - x1**2), latex(x2), latex(f_x2 - d),
                          latex_a, latex_b, latex_kq))

            # --- Bước 5: Xuất định dạng EX ---
            list_1 = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

