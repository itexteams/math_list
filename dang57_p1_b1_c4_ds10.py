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


def bt_dang57_p1_b1_c4_ds10(self):
            #Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các hệ số để bài toán phong phú
                A = random.randint(5, 9)   # Hệ số của m trong căn (Ví dụ: 7)
                B = random.randint(1, 5)   # Hệ số tự do trong căn (Ví dụ: 1)
                C = random.randint(2, 2)   # Hệ số của x trong căn (Mặc định: 2)
                K = random.randint(2, 2)   # Hệ số của m ở mẫu (Mặc định: 2)
                p = -1                     # Đầu mút trái của đoạn
                q = 1                      # Đầu mút phải của đoạn

                # Tính toán điều kiện của m
                # Điều kiện 1: m >= (C*q - B)/A
                m_min_val = Rational(C*q - B, A)

                # Điều kiện 2: m < p/K hoặc m > q/K
                m_ex_low = Rational(p, K)
                m_ex_high = Rational(q, K)

                # Tìm các giá trị nguyên âm m thỏa mãn (duyệt trong khoảng từ -20 đến -1)
                ds_m_nguyen_am = []
                for m_val in range(-20, 0):
                    cond1 = (m_val >= m_min_val)
                    cond2 = (m_val < m_ex_low or m_val > m_ex_high)
                    if cond1 and cond2:
                        ds_m_nguyen_am.append(m_val)

                kq_dung = len(ds_m_nguyen_am)

                # --- Bước 4: Điều chỉnh phương án sai ---
                # Tạo danh sách đáp án, đảm bảo không trùng với đáp án đúng
                s_options = {0, 1, 2, 3, 4, 5}
                if kq_dung in s_options:
                    s_options.remove(kq_dung)

                wrong_choices = random.sample(list(s_options), 3)

                # --- Bước 2: Viết lại nội dung theo mẫu ---
                # Câu hỏi
                noidungcauhoi = (r'''Cho hàm số $y = \frac{2}{x - %sm} + \sqrt{%sm + %s - %sx}$. Có bao nhiêu giá trị nguyên âm của tham số $m$ để tập xác định của hàm số chứa đoạn $[%s; %s]$?'''
                                 % (latex(K) if K != 1 else "", latex(A), latex(B), latex(C), latex(p), latex(q)))

                # Các đáp án
                da_d = r'\True $%s$' % kq_dung
                da_s1 = r'$%s$' % wrong_choices[0]
                da_s2 = r'$%s$' % wrong_choices[1]
                da_s3 = r'$%s$' % wrong_choices[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Hàm số xác định khi và chỉ khi:
            $\begin{cases} x - %sm \neq 0 \\ %sm + %s - %sx \geq 0 \end{cases} \Leftrightarrow \begin{cases} x \neq %sm \\ x \leq \frac{%sm + %s}{%s} \end{cases}$. \\
            Để tập xác định của hàm số chứa đoạn $[%s; %s]$ thì ta phải có: \\
            $\begin{cases} \frac{%sm + %s}{%s} \geq %s \\ %sm \notin [%s; %s] \end{cases} \Leftrightarrow \begin{cases} %sm + %s \geq %s \\ \left[\begin{smallmatrix} %sm < %s \\ %sm > %s \end{smallmatrix}\right. \end{cases} \Leftrightarrow \begin{cases} m \geq %s \\ \left[\begin{smallmatrix} m < %s \\ m > %s \end{smallmatrix}\right. \end{cases}$. \\
            ''' % (K, A, B, C, K, A, B, C, p, q, A, B, C, q, K, p, q, A, B, C*q, K, p, K, q, latex(m_min_val), latex(m_ex_low), latex(m_ex_high)))

                if kq_dung == 0:
                    loigiai += r"Kết hợp lại ta thấy không có giá trị nguyên âm nào của $m$ thỏa mãn."
                else:
                    loigiai += r"Các giá trị nguyên âm thỏa mãn là $m \in \{%s\}$, có $%s$ giá trị." % (", ".join(map(str, ds_m_nguyen_am)), kq_dung)

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

