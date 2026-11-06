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


def bt_dang13_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khởi tạo biến ký hiệu
            x = symbols('x')


            k = random.choice([4, 8, 12, 16, 20])
            a_val = k // 4

            c_val = random.randint(1, 8)        # Tung độ tại điểm cắt trục tung (C)
            m_minus_1 = random.randint(4, 15)   # Giá trị của cụm (m-1)
            m_val = m_minus_1 + 1               # Giá trị của m

            # Tính f(2) = a*(2^4) - 2*(m-1) + C
            f_2_val = a_val * 16 - 2 * m_minus_1 + c_val

            # Các hệ số của f(x) = ax^4 + bx + c
            b_val = -m_minus_1
            tong = a_val + b_val + c_val

            # Hàm hỗ trợ định dạng số thập phân dấu phẩy
            def format_vn(number):
                return str(number).replace('.', ',')

            # --- BƯỚC 2: TẠO ĐÁP ÁN TRẮC NGHIỆM ---
            da = '$%s$' % format_vn(tong)
            s_list = []
            while len(s_list) < 3:
                sai = tong + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                if sai not in s_list and sai != tong:
                    s_list.append(sai)

            da_d = '\\True ' + str(da)
            list_1 = [da_d, '$%s$'%format_vn(s_list[0]), '$%s$'%format_vn(s_list[1]), '$%s$'%format_vn(s_list[2])]
            random.shuffle(list_1)

            # --- BƯỚC 3: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
            # Chuyển đổi dx thành \text{d}x theo yêu cầu
            noidungcauhoi = (r'''Cho hàm số $y = f(x)$ có $f'(x) = %sx^3 - m + 1$, $f(2) = %s$ và có đồ thị của hàm số $y = f(x)$ cắt trục tung tại điểm có tung độ bằng $%s$. Tìm được $f(x) = ax^4 + bx + c$ với $a, b, c \in \mathbb{Z}$. Tổng $a + b + c$ bằng bao nhiêu?''' 
                            % (latex(k), latex(f_2_val), latex(c_val)))

            # Xử lý hiển thị hệ số a (ẩn số 1 nếu a=1)
            a_display = latex(Rational(k, 4)) if a_val != 1 else ""

            loigiai = (r'''Ta có: $f(x) = \int f'(x)\text{d}x = %sx^4 - (m-1)x + C$. \\
            Từ giả thiết, ta có: \\\\
            $\begin{cases} f(0) = %s \\ f(2) = %s \end{cases} 
            \Leftrightarrow \begin{cases} C = %s \\ %s \cdot 16 - (m-1) \cdot 2 + C = %s \end{cases} 
            \Leftrightarrow \begin{cases} C = %s \\ m-1 = %s \end{cases} 
            \Leftrightarrow \begin{cases} C = %s \\ m = %s \end{cases}$. \\
            Do đó: $f(x) = %sx^4 - %sx + %s \Rightarrow \begin{cases} a = %s \\ b = %s \\ c = %s \end{cases} \Rightarrow a + b + c = %s$.''' 
                      % (a_display, 
                         latex(c_val), latex(f_2_val), 
                         latex(c_val), latex(a_val), latex(f_2_val), 
                         latex(c_val), latex(m_minus_1), 
                         latex(c_val), latex(m_val), 
                         a_display, latex(m_minus_1), latex(c_val), 
                         latex(a_val), latex(b_val), latex(c_val), latex(tong)))
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(tong))

            # --- BƯỚC 4: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

