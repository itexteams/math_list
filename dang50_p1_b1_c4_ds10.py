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


def bt_dang50_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Xét mẫu số x^2 - px + q = 0
                # Để có 2 nghiệm phân biệt: Delta = p^2 - 4q > 0
                p = random.randint(2, 6)
                q = random.randint(-3, 4)
                while (p**2 - 4*q <= 0) or q == 0: # Đảm bảo delta dương và tích ab khác 0 để bài toán hay hơn
                    p = random.randint(2, 6)
                    q = random.randint(-3, 4)

                # Random tử số x^2 + mx + n (không ảnh hưởng đến a, b nhưng làm đề phong phú)
                m = random.randint(-9, 9)
                n = random.randint(-9, 9)

                # Hệ số k trong biểu thức Q = a^3 + b^3 - k*ab
                k = random.randint(2, 6)

                # Tính toán giá trị đúng theo Vi-et
                # a + b = p, a * b = q
                S = p
                P = q
                # Q = a^3 + b^3 - k*ab = (a+b)^3 - 3ab(a+b) - k*ab
                kq_val = S**3 - 3*P*S - k*P

                # --- B4: Điều chỉnh các phương án sai ---
                da = '$%s$' % latex(kq_val)

                s_vals = []
                # Tạo các phương án sai quanh đáp án đúng
                offsets = [-10, -5, 5, 10, 2, -2, 7, -7]
                random.shuffle(offsets)
                for off in offsets:
                    wrong_val = kq_val + off
                    if wrong_val != kq_val:
                        s_vals.append('$%s$' % latex(wrong_val))
                    if len(s_vals) >= 3:
                        break

                das1 = s_vals[0]
                das2 = s_vals[1]
                das3 = s_vals[2]

                # --- B2: Viết lại bài toán theo mẫu code ---
                # Câu hỏi
                # Thiết lập đa thức mẫu số để hiển thị latex
                mau_so = x**2 - p*x + q
                tu_so = x**2 + m*x + n

                noidungcauhoi = (r'''Hàm số $y = \frac{%s}{%s}$ có tập xác định $D = \mathbb{R} \setminus \{a; b\}; a \neq b$. Giá trị biểu thức $Q = a^3 + b^3 - %sab$ bằng'''
                                 %(latex(tu_so), latex(mau_so), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=(r'''Hàm số $y = \frac{%s}{%s}$ xác định khi: $%s \neq 0$. \\
                         Gọi $a, b$ là $2$ nghiệm của phương trình $%s = 0$. \\
                         Theo Vi-et có $\begin{cases} a+b = %s \\ a.b = %s \end{cases}$. \\
                         Có $Q = a^3 + b^3 - %sab = (a+b)^3 - 3ab(a+b) - %sab$ \\
                         $= %s^3 - 3 \cdot %s \cdot %s - %s \cdot %s = %s$. \\
                         Vậy $Q = %s$.'''
                         %(latex(tu_so), latex(mau_so), latex(mau_so),
                           latex(mau_so), latex(S), latex(P),
                           latex(k), latex(k),
                           latex(S), latex(P), latex(S), latex(k), latex(P), latex(kq_val),
                           latex(kq_val)
                         ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

