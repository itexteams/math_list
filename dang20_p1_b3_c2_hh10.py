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


def bt_dang20_p1_b3_c2_hh10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng phân số LaTeX rút gọn tối giản
            def format_frac(num, den):
                if den == 0:
                    return "Undefined"
                # Rút gọn phân số
                common_divisor = math.gcd(num, den)
                num = num // common_divisor
                den = den // common_divisor

                # Xử lý dấu
                if den < 0:
                    num = -num
                    den = -den

                if den == 1:
                    return str(num)
                elif num == 0:
                    return "0"
                else:
                    # Nếu âm thì đẩy dấu trừ ra trước phân số
                    if num < 0:
                        return "-\\frac{" + str(abs(num)) + "}{" + str(den) + "}"
                    else:
                        return "\\frac{" + str(num) + "}{" + str(den) + "}"

            # 1. Random hệ số a và b (đảm bảo a khác b và không quá lớn)
            a = random.randint(1, 7)
            b = random.randint(1, 7)
            while a == b:
                b = random.randint(1, 7)

            # 2. Tính các hệ số k
            # Đáp án đúng: k = b / (a+b)
            correct_k = format_frac(b, a + b)

            # Các đáp án nhiễu phổ biến
            distractor1 = format_frac(b, a)       # Sai lầm: lấy trực tiếp b/a
            distractor2 = format_frac(a, a + b)   # Sai lầm: nhầm hệ số a thành tử
            distractor3 = format_frac(a + b, b)   # Sai lầm: nghịch đảo đáp án đúng

            # Đảm bảo các đáp án nhiễu không bị trùng lặp bằng cách dùng set
            pool_distractors = list(set([distractor1, distractor2, distractor3]))
            # Nếu bị trùng (ít xảy ra với cách setup này), bổ sung thêm nhiễu tĩnh
            while len(pool_distractors) < 3:
                extra = format_frac(random.randint(1, 5), random.randint(2, 9))
                if extra != correct_k and extra not in pool_distractors:
                    pool_distractors.append(extra)

            # 3. Câu hỏi
            noidungcauhoi = f"Cho đoạn thẳng $AB$ và điểm $I$ sao cho ${a}\\overrightarrow{{AI}} = {b}\\overrightarrow{{IB}}$. Tìm $k$ biết $\\overrightarrow{{AI}} = k\\overrightarrow{{AB}}$"

            # 4. Các đáp án
            da_d = '\\True $k = ' + correct_k + '$'
            da_s1 = '$k = ' + pool_distractors[0] + '$'
            da_s2 = '$k = ' + pool_distractors[1] + '$'
            da_s3 = '$k = ' + pool_distractors[2] + '$'

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # 5. Nội dung lời giải tự động
            loigiai = (f"Ta có ${a}\\overrightarrow{{AI}} = {b}\\overrightarrow{{IB}} "
                       f"\\Leftrightarrow {a}\\overrightarrow{{AI}} = {b}\\left(\\overrightarrow{{AB}} - \\overrightarrow{{AI}}\\right)$ \\\\ "
                       f"$\\Leftrightarrow {a}\\overrightarrow{{AI}} = {b}\\overrightarrow{{AB}} - {b}\\overrightarrow{{AI}} "
                       f"\\Leftrightarrow ({a} + {b})\\overrightarrow{{AI}} = {b}\\overrightarrow{{AB}}$ \\\\ "
                       f"$\\Leftrightarrow {a+b}\\overrightarrow{{AI}} = {b}\\overrightarrow{{AB}} "
                       f"\\Leftrightarrow \\overrightarrow{{AI}} = {correct_k}\\overrightarrow{{AB}}$.\\\\ "
                       f"Vậy $k = {correct_k}$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

