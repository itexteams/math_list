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


def bt_dang38_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Random tọa độ các điểm chốt của đồ thị f'(x)
                x1 = random.randint(-3, -2)
                x2 = random.randint(0, 1)
                x3 = x2 + random.randint(1, 2)
                x4 = x3 + random.randint(1, 2)

                y1 = random.randint(1, 2)
                y2 = y1 + random.randint(1, 2)
                y4 = random.randint(1, y2 - 1)

                # Tính toán diện tích từng phần (S = tích phân f'(x))
                s1 = Rational((y1 + y2) * (x2 - x1), 2)
                s2 = Rational(y2 * (x3 - x2), 1)
                s3 = Rational((y2 + y4) * (x4 - x3), 2)

                kq_chinh_xac = s1 + s2 + s3

                # --- Tạo mã TikZ cho hình vẽ ---
                tikz_code = (r"""\begin{center}
            \begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (%s,0) -- (%s,0) node[below] {$x$};
                \draw[->] (0,-1) -- (0,%s) node[left] {$y$};
                \node at (0,0) [below left] {$O$};
                \draw[thick, color=blue] (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s);
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s) -- (0,%s) node[left] {$%s$};
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s) -- (0,%s) node[left] {$%s$};
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s);
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s) -- (0,%s) node[right] {$%s$};
            \end{tikzpicture}
            \end{center}""" % (latex(x1-1), latex(x4+1), latex(y2+1), 
                                latex(x1), latex(y1), latex(x2), latex(y2), latex(x3), latex(y2), latex(x4), latex(y4),
                                latex(x1), latex(x1), latex(x1), latex(y1), latex(y1), latex(y1),
                                latex(x2), latex(x2), latex(x2), latex(y2), latex(y2), latex(y2),
                                latex(x3), latex(x3), latex(x3), latex(y2),
                                latex(x4), latex(x4), latex(x4), latex(y4), latex(y4), latex(y4)))

                # --- B4: Điều chỉnh các phương án sai ---
                kq = latex(kq_chinh_xac)
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo danh sách các phương án nhiễu
                s = []
                offsets = [Rational(1, 2), 1, Rational(3, 2), 2, -1, Rational(-1, 2), Rational(5, 2)]
                random.shuffle(offsets)
                for off in offsets:
                    sai = kq_chinh_xac + off
                    if sai > 0 and sai != kq_chinh_xac:
                        s.append('$%s$' % (latex(sai)))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- Câu hỏi ---
                noidungcauhoi = ('''Cho hàm số $y = f(x)$ có đạo hàm liên tục trên đoạn $[%s;%s]$ và có đồ thị hàm số $y = f'(x)$ như hình vẽ bên dưới. Giá trị của biểu thức $H = f(%s) - f(%s)$ là
            %s''' % (latex(x1), latex(x4), latex(x4), latex(x1), tikz_code))

                # --- Các đáp án ---
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                loigiai = ('''Dựa vào định lý cơ bản của giải tích, ta có: \\\\
                             $H = f(%s) - f(%s) = \\int_{%s}^{%s} f'(x) \\text{d}x$. \\\\
                             Giá trị của tích phân này bằng diện tích hình phẳng giới hạn bởi đồ thị $y=f'(x)$ và trục hoành trên đoạn $[%s; %s]$. \\\\
                             Chia hình phẳng thành 3 phần: \\\\
                             + Diện tích hình thang $S_1$ trên đoạn $[%s; %s]: S_1 = \\frac{(%s + %s) \\cdot (%s - (%s))}{2} = %s$. \\\\
                             + Diện tích hình chữ nhật $S_2$ trên đoạn $[%s; %s]: S_2 = %s \\cdot (%s - %s) = %s$. \\\\
                             + Diện tích hình thang $S_3$ trên đoạn $[%s; %s]: S_3 = \\frac{(%s + %s) \\cdot (%s - %s)}{2} = %s$. \\\\
                             Vậy $H = S_1 + S_2 + S_3 = %s + %s + %s = %s$.''' 
                           % (latex(x4), latex(x1), latex(x1), latex(x4), 
                              latex(x1), latex(x4),
                              latex(x1), latex(x2), latex(y1), latex(y2), latex(x2), latex(x1), latex(s1),
                              latex(x2), latex(x3), latex(y2), latex(x3), latex(x2), latex(s2),
                              latex(x3), latex(x4), latex(y2), latex(y4), latex(x4), latex(x3), latex(s3),
                              latex(s1), latex(s2), latex(s3), latex(kq_chinh_xac)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

