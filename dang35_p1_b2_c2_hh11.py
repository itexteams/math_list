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


def bt_dang35_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # V: Đỉnh hình chóp
                # H: Đỉnh đáy là chân đường cao (VH vuông góc đáy)
                # R: Đỉnh đáy chứa góc vuông
                # O: Đỉnh đáy còn lại
                cases = [
                    ("A", "B", "C"), # SA vuông góc đáy, vuông tại B
                    ("A", "C", "B"), # SA vuông góc đáy, vuông tại C
                    ("B", "A", "C"), # SB vuông góc đáy, vuông tại A
                    ("B", "C", "A"), # SB vuông góc đáy, vuông tại C
                    ("C", "A", "B"), # SC vuông góc đáy, vuông tại A
                    ("C", "B", "A")  # SC vuông góc đáy, vuông tại B
                ]
                H, R, O = random.choice(cases)
                V = "S"

                # Hàm sắp xếp tên đoạn thẳng theo thứ tự từ điển (VD: "BA" -> "AB")
                def get_line(c1, c2): 
                    return "".join(sorted([c1, c2]))

                # Hàm quy chuẩn tên mặt phẳng
                def get_plane(chars):
                    s = set(chars)
                    if s == set(['S', 'A', 'B']): return "SAB"
                    if s == set(['S', 'B', 'C']): return "SBC"
                    if s == set(['S', 'A', 'C']): return "SAC"
                    return "SAB"

                # Xác định đường thẳng và mặt phẳng cho đáp án đúng
                L_true = get_line(O, R)
                P_true = get_plane([V, H, R])
                da_tuple = (L_true, P_true)

                # Sinh tất cả các tổ hợp (Đường thẳng, Mặt phẳng) hợp lệ để làm nhiễu
                all_lines = ["AB", "BC", "AC"]
                all_planes = ["SAB", "SBC", "SAC"]
                valid_combinations = []

                for l in all_lines:
                    for p in all_planes:
                        # Điều kiện: Đường thẳng không được nằm hoàn toàn trong mặt phẳng
                        if not set(l).issubset(set(p)):
                            valid_combinations.append((l, p))

                # Lọc ra các đáp án nhiễu (khác đáp án đúng)
                distractors = [c for c in valid_combinations if c != da_tuple]
                selected_distractors = random.sample(distractors, 3)

                # Chuẩn bị chuỗi LaTeX cho các đáp án
                da = '$%s \\perp (%s)$' % (da_tuple[0], da_tuple[1])
                s = ['$%s \\perp (%s)$' % (c[0], c[1]) for c in selected_distractors]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $%s$ và $%s%s \\perp (ABC)$. Khẳng định nào sau đây đúng?''' 
                                 % (R, V, H))

                # Xử lý các đáp án vào list để trộn ngẫu nhiên
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải
                loigiai = ('''Ta có: $%s \\perp %s%s$ (do $%s%s \\perp (ABC)$) và $%s \\perp %s$ nên $%s \\perp (%s)$.''' 
                           % (L_true, V, H, V, H, L_true, get_line(H, R), L_true, P_true))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

