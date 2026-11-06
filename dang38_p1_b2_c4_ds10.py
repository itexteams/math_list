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


def bt_dang38_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x_sym = symbols('x')

            # Thiết lập tham số (Có thể dùng randint để random hoàn toàn)
            x_split = 2
            x_start = -1
            x_vertex = 1
            x_end = 4

            a = 1
            b = -2 # Để đỉnh là -b/2a = 1
            c = -8
            f1 = a*x_sym**2 + b*x_sym + c

            # Hàm bậc nhất f2 sao cho liên tục tại x=2
            y_split = f1.subs(x_sym, x_split) # -8
            d = 2
            e = y_split - d * x_split # -12
            f2 = d*x_sym + e

            # Tính các giá trị tại các điểm nút
            y_start = int(f1.subs(x_sym, x_start))   # -5
            y_vertex = int(f1.subs(x_sym, x_vertex)) # -9
            y_end = int(f2.subs(x_sym, x_end))       # -4

            M = max(y_start, y_vertex, y_end)
            m = min(y_start, y_vertex, y_end)
            kq_dung = M + m

            # Tạo danh sách đáp án
            s = set()
            while len(s) < 3:
                sai = kq_dung + random.choice([-2, -1, 1, 2, 5])
                if sai != kq_dung: s.add(sai)

            list_ans = [f'${kq_dung}$'] + [f'${val}$' for val in s]
            random.shuffle(list_ans)

            list_1 = []
            for ans in list_ans:
                if ans == f'${kq_dung}$':
                    list_1.append(f'\\True {ans}')
                else:
                    list_1.append(ans)

            # Nội dung câu hỏi
            noidungcauhoi = (f"Cho hàm số $y = \\begin{{cases}} {latex(f1)} & \\text{{khi }} x \\le {x_split} \\\\ {latex(f2)} & \\text{{khi }} x > {x_split} \\end{{cases}}$. "
                             f"Gọi $M, m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số khi $x \\in [{x_start}; {x_end}]$. "
                             f"Tính $M + m$.")

            # Bảng biến thiên sử dụng gói tkz-tab chuẩn
            loigiai = (f"Ta có bảng biến thiên của hàm số trên đoạn $[{x_start}; {x_end}]$:\n"
                       f"\\begin{{center}}\n"
                       f"\\begin{{tikzpicture}}\n"
                       f"    \\tkzTabInit[lgt=1.2, espcl=2.5]{{$x$ /1, $y$ /2}}{{{x_start}, {x_vertex}, {x_split}, {x_end}}}\n"
                       f"    \\tkzTabVar{{+/ {y_start}, -/ {y_vertex}, R/, +/ {y_end}}}\n"
                       f"    \\tkzTabVal{{2}}{{4}}{{0.5}}{{{x_split}}}{{{y_split}}}\n" # Chèn giá trị tại điểm gãy x=2
                       f"\\end{{tikzpicture}}\n"
                       f"\\end{{center}}\n"
                       f"Dựa vào bảng biến thiên, ta có $M = {M}, m = {m}$.\\\\\n"
                       f"Vậy $M + m = {M} + ({m}) = {kq_dung}$.")

            # Xuất nội dung
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

