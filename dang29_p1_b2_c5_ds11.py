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


def bt_dang29_p1_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo các thông số ngẫu nhiên
                # k là cơ số (ví dụ: 2, 3, 5)
                k = random.choice([2, 3, 5])
                # m là số mũ của k trong biểu thức k^m (ví dụ: 9 = 3^2 -> m=2)
                m = random.randint(2, 4)
                # n là số mũ của k ở cơ số vế phải (ví dụ: 9 = 3^2 -> n=2)
                n = random.randint(2, 3)

                k_m = k**m # Giá trị k^m (ví dụ 9, 27, 4, 8...)
                k_n = k**n # Giá trị k^n (ví dụ 4, 9, 25...)

                # Hệ số của phương trình: n*a + (n*m)*b = 1
                he_so_a = n
                he_so_b = n * m
                ket_qua = 1

                # 2. Tạo đáp án đúng
                da_dung_str = f"{he_so_a}a + {he_so_b}b = {ket_qua}"
                da_d = r'\True $' + da_dung_str + '$'

                # 3. Tạo các phương án sai (nhiễu)
                # Đảm bảo các phương án sai không trùng đáp án đúng
                s = []
                # Nhiễu 1: Đổi dấu
                s.append(f"${he_so_a}a - {he_so_b}b = {ket_qua}$")
                # Nhiễu 2: Hoán vị hệ số
                if he_so_a != he_so_b:
                    s.append(f"${he_so_b}a + {he_so_a}b = {ket_qua}$")
                # Nhiễu 3: Thay đổi kết quả vế phải
                s.append(f"${he_so_a}a + {he_so_b}b = {n}$")
                s.append(f"${he_so_a}a + {he_so_b}b = {m}$")
                s.append(f"$a + {m}b = {n}$")

                # Lọc trùng và loại đáp án đúng nếu lỡ trùng
                s = list(set([x for x in s if x != f"${da_dung_str}$"]))
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # 4. Nội dung câu hỏi
                noidungcauhoi = (r'Xét các số thực $a$ và $b$ thỏa mãn $\log_{%s} \left( %s^a \cdot %s^b \right) = \log_{%s} %s$. Mệnh đề nào dưới đây đúng?'
                                 % (k, k, k_m, k_n, k))

                # 5. Nội dung lời giải
                loigiai = (r'''Ta có:
                            $$\log_{%s} \left( %s^a \cdot %s^b \right) = \log_{%s} %s \Leftrightarrow \log_{%s} \left( %s^a \cdot %s^{%sb} \right) = \log_{%s^{%s}} %s$$
                            $$\Leftrightarrow \log_{%s} %s^{a + %sb} = \log_{%s} %s^{\frac{1}{%s}}$$
                            $$\Leftrightarrow a + %sb = \frac{1}{%s} \Leftrightarrow %sa + %sb = 1.$$'''
                           % (k, k, k_m, k_n, k, k, k, k, m, k, n, k,
                              k, k, m, k, k, n,
                              m, n, he_so_a, he_so_b))

            # 6. Xuất câu trắc nghiệm theo định dạng LaTeX
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

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

