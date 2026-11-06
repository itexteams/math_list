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


def bt_dang46_p1_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến danh sách dạng (ở đây chỉ có 1 dạng dựa trên ảnh)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                u = random.randint(1, 2)
                v = random.randint(1, 3)
                target_num = (7**u) * (5**v)

                m = 2 * u
                n = 2 * v
                p = 1
                q = 3

                # Bước 2: Random các hệ số c1, c2, c3, c4 trong biểu thức A = c1*m + c2*n + c3*p + c4*q
                # Trong ảnh gốc là: A = 1*m + 2*n + 3*p + 4*q
                coeffs = random.sample(range(1, 6), 4)
                c1, c2, c3, c4 = coeffs

                # Tính đáp án đúng
                kq_val = c1*m + c2*n + c3*p + c4*q
                da = '$%s$' % kq_val

                # Bước 3: Tạo các phương án nhiễu (không trùng với đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = kq_val + random.choice([-5, -3, -2, -1, 1, 2, 3, 5, 10])
                    if sai != kq_val and sai > 0:
                        s.add('$%s$' % sai)

                das_list = list(s)
                das1, das2, das3 = das_list[0], das_list[1], das_list[2]

                # Bước 4: Soạn nội dung câu hỏi
                # Biểu thức A dưới dạng text latex
                expr_a = ""
                parts = []
                if c1 == 1: parts.append("m")
                else: parts.append(f"{c1}m")
                if c2 == 1: parts.append("n")
                else: parts.append(f"{c2}n")
                if c3 == 1: parts.append("p")
                else: parts.append(f"{c3}p")
                if c4 == 1: parts.append("q")
                else: parts.append(f"{c4}q")
                expr_a = " + ".join(parts).replace("+ 1", "+ ")

                noidungcauhoi = (r'Cho $\log_{9} 5 = a; \log_{4} 7 = b; \log_{2} 3 = c$. Biết $\log_{24} %s = \frac{mb + nac}{pc + q}$. Giá trị $A = %s$ là'
                                 % (target_num, expr_a))

                # Bước 5: Soạn lời giải chi tiết (bám sát logic trong ảnh)
                loigiai = (r'''Ta có $\log_{24} %s = \log_{24} (7^{%s} \cdot 5^{%s}) = %s\log_{24} 7 + %s\log_{24} 5$. \\
                          Biến đổi các giả thiết: \\
                          $a = \log_{9} 5 = \frac{1}{2}\log_{3} 5 \Rightarrow \log_{3} 5 = 2a$. \\
                          $b = \log_{4} 7 = \frac{1}{2}\log_{2} 7 \Rightarrow \log_{2} 7 = 2b$. \\
                          $c = \log_{2} 3$. \\
                          Suy ra $\log_{2} 5 = \log_{2} 3 \cdot \log_{3} 5 = c \cdot 2a = 2ac$. \\
                          Khi đó: $\log_{24} %s = \frac{\log_{2} (7^{%s} \cdot 5^{%s})}{\log_{2} 24} = \frac{%s\log_{2} 7 + %s\log_{2} 5}{\log_{2} (2^3 \cdot 3)} = \frac{%s(2b) + %s(2ac)}{3 + c} = \frac{%sb + %sac}{c + 3}$. \\
                          Đối chiếu ta được: $m=%s, n=%s, p=%s, q=%s$. \\
                          Vậy $A = %s \cdot %s + %s \cdot %s + %s \cdot %s + %s \cdot %s = %s$.'''
                          % (target_num, u, v, u, v,
                             target_num, u, v, u, v, u, v, 2*u, 2*v,
                             m, n, p, q,
                             c1, m, c2, n, c3, p, c4, q, kq_val))

                # Đưa các đáp án vào danh sách và shuffle
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
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

