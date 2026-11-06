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


def bt_dang18_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ cách random bài toán
                # Để hàm số y = (ax + b) / (cx + d) xác định và có đạo hàm đẹp
                # Chọn c, d sao cho x0 != -d/c
                c = 1
                d = random.choice([-3, -2, -1, 1, 2, 3])

                # Random tử số ax + b
                a = random.choice([-3, -2, -1, 1, 2, 3])
                b = random.choice([-3, -2, -1, 1, 2, 3])

                # Hoành độ tiếp điểm x0 (chọn x0 sao cho mẫu số khác 0)
                x0 = 0
                while (c * x0 + d) == 0:
                    x0 = random.randint(-2, 2)

                # Hàm số và đạo hàm
                f = (a*x + b) / (c*x + d)
                f_prime = diff(f, x)

                # Tính các giá trị tại x0
                y0 = f.subs(x, x0)
                k = f_prime.subs(x, x0) # Hệ số góc

                # Phương trình tiếp tuyến: y = k(x - x0) + y0
                # Rút gọn về dạng y = kx + m (với m = y0 - k*x0)
                m = y0 - k * x0

                # Tạo biểu thức để latex hiển thị đẹp
                tiep_tuyen = k*x + m
                pt_tt_str = f"y = {latex(tiep_tuyen)}"

                # Chú ý xử lý dấu +- bằng cách dùng latex(k*x + m) 
                # Sympy sẽ tự động xử lý -2x + -3 thành -2x - 3

                # Đáp án đúng
                da_dung = f"${pt_tt_str}$"

                # Các đáp án nhiễu
                s = [
                    f"$y = {latex(k)}x + {latex(m + random.randint(1, 3))}$",
                    f"$y = {latex(k)}x + {latex(m - random.randint(1, 3))}$",
                    f"$y = {latex(-k)}x + {latex(m)}$",
                    f"$y = {latex(k+1)}x + {latex(m)}$",
                    f"$y = {latex(k-1)}x + {latex(m-1)}$",
                ]

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi
                noidungcauhoi = (f"Phương trình tiếp tuyến của đồ thị hàm số $y = {latex(f)}$ "
                                 f"tại điểm có hoành độ $x = {latex(x0)}$ là")

                # Các đáp án
                da_d = '\\True ' + da_dung
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Tập xác định: $D = \\mathbb{{R}} \\setminus \\{{{latex(Rational(-d,c))}\\}}$."
                           f"\\\\ Đạo hàm: $y' = {latex(simplify(f_prime))}$."
                           f"\\\\ Với $x = {latex(x0)} \\Rightarrow y({latex(x0)}) = {latex(y0)}$ và $y'({latex(x0)}) = {latex(k)}$."
                           f"\\\\ Phương trình tiếp tuyến cần tìm là: $y = {latex(k)}(x - {latex(x0)}) + {latex(y0)}$"
                           f"\\\\ $\\Leftrightarrow {pt_tt_str}$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -','-').replace('+ +','+').replace('- -','+').replace('- +','-')
            return content

