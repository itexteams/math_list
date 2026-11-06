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


def bt_dang36_p4_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài cạnh b, c và giá trị cos A
                valid = False
                while not valid:
                    b_val = random.randint(3, 10)
                    c_val = random.randint(3, 10)
                    den = random.choice([2, 3, 4, 5, 6])
                    num = random.randint(-den + 1, den - 1)
                    if num == 0:
                        continue
                    cos_A = Rational(num, den)

                    # Tính a^2 theo định lí cosin
                    a_sq = b_val**2 + c_val**2 - 2 * b_val * c_val * cos_A
                    if a_sq > 0:
                        a_val = simplify(sqrt(a_sq))
                        a_float = float(a_val)
                        # Kiểm tra bất đẳng thức tam giác
                        if (a_float + b_val > c_val) and (b_val + c_val > a_float) and (c_val + a_float > b_val):
                            valid = True

                kq = latex(a_val)

                # Tạo các phương án sai (distractors)
                # Sai lầm 1: Nhầm dấu trong định lí cosin
                fake1_sq = b_val**2 + c_val**2 + 2 * b_val * c_val * cos_A
                fake1 = simplify(sqrt(fake1_sq)) if fake1_sq > 0 else simplify(sqrt(b_val**2 + c_val**2 + 1))

                # Sai lầm 2: Nhầm công thức Pytago
                fake2 = simplify(sqrt(b_val**2 + c_val**2))

                # Sai lầm 3: Quên hệ số 2
                fake3_sq = b_val**2 + c_val**2 - b_val * c_val * cos_A
                fake3 = simplify(sqrt(fake3_sq)) if fake3_sq > 0 else simplify(sqrt(b_val**2 + c_val**2 + 2))

                s_cands = [fake1, fake2, fake3]
                unique_s_cands = []
                for cand in s_cands:
                    if cand != a_val and cand not in unique_s_cands:
                        unique_s_cands.append(cand)

                # Bổ sung đáp án nhiễu nếu bị trùng
                while len(unique_s_cands) < 3:
                    bogus = simplify(sqrt(a_sq + random.choice([-5, -3, -1, 1, 3, 5])))
                    if bogus > 0 and bogus != a_val and bogus not in unique_s_cands:
                        unique_s_cands.append(bogus)

                random.shuffle(unique_s_cands)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % (latex(unique_s_cands[0])),
                    '$%s$' % (latex(unique_s_cands[1])),
                    '$%s$' % (latex(unique_s_cands[2]))
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Cho $a; b; c$ là độ dài $3$ cạnh của tam giác $ABC$. Biết $b = %s; c = %s; \\cos A = %s$. Tính độ dài của $a$.'
                                 % (b_val, c_val, latex(cos_A)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                bc2_term = simplify(2 * b_val * c_val * cos_A)
                loigiai = ('Áp dụng định lí côsin trong tam giác $ABC$, ta có: \\\\ \n'
                           '$a^2 = b^2 + c^2 - 2bc \\cdot \\cos A$ \\\\ \n'
                           '$\\Rightarrow a^2 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\left(%s\\right)$ \\\\ \n'
                           '$\\Rightarrow a^2 = %s + %s - \\left(%s\\right) = %s$. \\\\ \n'
                           'Vậy $a = %s$.'
                           % (b_val, c_val, b_val, c_val, latex(cos_A),
                              b_val**2, c_val**2, latex(bc2_term), latex(a_sq),
                              kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

