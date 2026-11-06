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


def bt_dang36_p1_b3_c4_ds11(self):
            # Khai báo biến
            # --- THIẾT LẬP DỮ LIỆU ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn ngẫu nhiên k và m để tạo bài toán (m khác 0)
                k = random.randint(1, 5)
                m = random.randint(1, 6)
                while m == k: # Đảm bảo m khác k để biểu thức không quá đơn giản
                    m = random.randint(1, 6)

                # Tạo đa thức tử số: x(x-k)(x-m) = x^3 - (k+m)x^2 + kmx
                tu_so = expand(x*(x-k)*(x-m))
                mau_so_hien_thi = "x(x-%s)" % m if m > 0 else "x(x+%s)" % abs(m)

                # Tính toán giá trị a, b và T
                val_a = -k
                val_b = m - k
                kq_val = val_a**2 + val_b**2

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % kq_val

                # Tạo danh sách đáp án nhiễu
                s = set()
                while len(s) < 3:
                    nhieu = kq_val + random.choice([-2, -1, 1, 2, 3, 4, 5])
                    if nhieu >= 0 and nhieu != kq_val:
                        s.add('$%s$' % nhieu)

                list_nhieu = list(s)
                das1 = list_nhieu[0]
                das2 = list_nhieu[1]
                das3 = list_nhieu[2]

                # --- NỘI DUNG CÂU HỎI ---
                # Sử dụng latex(tu_so) để sympy tự in đẹp đa thức
                noidungcauhoi = (r'''Cho biết hàm số $f(x) = \begin{cases} \dfrac{%s}{%s} & \text{khi } x(x-%s) \neq 0 \\ a & \text{khi } x = 0 \\ b & \text{khi } x = %s \end{cases}$ liên tục trên $\mathbb{R}$. Giá trị của $T = a^2 + b^2$ bằng'''
                                 % (latex(tu_so), mau_so_hien_thi, m, m))

                # --- CÁC ĐÁP ÁN ---
                da_d = '\\True ' + str(da_dung)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI ---
                loigiai = (r'''Vì hàm số $f(x)$ liên tục trên $\mathbb{R}$ suy ra hàm số cũng liên tục tại $x = 0$ và $x = %s$. Do đó: \\
                           $\lim_{x \to 0} f(x) = \lim_{x \to 0} \dfrac{%s}{x(x-%s)} = \lim_{x \to 0} \dfrac{x(x-%s)(x-%s)}{x(x-%s)} = f(0) \Leftrightarrow \lim_{x \to 0} (x-%s) = a \Leftrightarrow a = %s$. \\
                           $\lim_{x \to %s} f(x) = \lim_{x \to %s} \dfrac{%s}{x(x-%s)} = \lim_{x \to %s} \dfrac{x(x-%s)(x-%s)}{x(x-%s)} = f(%s) \Leftrightarrow \lim_{x \to %s} (x-%s) = b \Leftrightarrow b = %s$. \\
                           Vậy $T = a^2 + b^2 = (%s)^2 + (%s)^2 = %s$.'''
                           % (m, latex(tu_so), m, k, m, m, k, val_a,
                              m, m, latex(tu_so), m, m, k, m, m, m, m, k, val_b,
                              val_a, val_b, kq_val))

            # --- XUẤT KẾT QUẢ ---
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

