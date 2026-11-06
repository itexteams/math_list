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


def bt_dang33_p1_b1_c2_hh12(self):
            # B1: Tạo tọa độ điểm A(ax, ay, az) ngẫu nhiên
            # Để bài toán hay, ax và az không nên đồng thời bằng 0
            ax = random.choice([i for i in range(-5, 6) if i != 0])
            ay = randint(-5, 5)
            az = random.choice([i for i in range(-5, 6) if i != 0])

            # B2: Giải thuật tìm phương trình mặt phẳng chứa Oy: Ax + Cz = 0
            # Đi qua A(ax, ay, az) => A*ax + C*az = 0.
            # Chọn A = az, C = -ax
            A_val = az
            C_val = -ax

            # Rút gọn hệ số bằng GCD
            common = math.gcd(A_val, C_val)
            A_val //= common
            C_val //= common

            # Đảm bảo hệ số đầu tiên dương cho đẹp
            if A_val < 0:
                A_val, C_val = -A_val, -C_val

            # Tạo biểu thức vế trái bằng SymPy để tự động sửa lỗi "1z" hay "0z"
            expr_correct = A_val * x + C_val * z
            da_dung_str = latex(expr_correct) + " = 0"

            # B3: Tạo các phương án nhiễu (không trùng đáp án đúng)
            s_list = []

            # Nhiễu 1: Thay đổi hệ số
            expr_s1 = (A_val + 1) * x + C_val * z
            s_list.append(latex(expr_s1) + " = 0")

            # Nhiễu 2: Thay bằng trục khác (chứa Ox thay vì Oy chẳng hạn: By + Cz = 0)
            expr_s2 = ay * y + C_val * z
            if expr_s2 == 0 or expr_s2 == expr_correct: # Tránh lỗi biểu thức rỗng
                expr_s2 = A_val * x + C_val * z + randint(1, 5)
            s_list.append(latex(expr_s2) + " = 0")

            # Nhiễu 3: Mặt phẳng không đi qua gốc tọa độ (Vế phải khác 0)
            const_term = randint(1, 5)
            s_list.append(latex(expr_correct) + f" = {const_term}")

            # Lọc trùng lặp phương án sai và đúng
            s_list = list(set(s_list))
            if da_dung_str in s_list:
                s_list.remove(da_dung_str)

            # Đảm bảo đủ 3 phương án sai
            while len(s_list) < 3:
                extra_expr = A_val * x + (C_val + len(s_list)) * z
                s_list.append(latex(extra_expr) + " = 0")

            random.shuffle(s_list)
            das1, das2, das3 = s_list[0], s_list[1], s_list[2]

            # B4: Nội dung câu hỏi và lời giải
            noidungcauhoi = (f"Trong không gian $Oxyz$, cho điểm $A({ax}; {ay}; {az})$. "
                             f"Phương trình mặt phẳng $(\\alpha)$ đi qua $A$ và chứa trục $Oy$ là")

            da_d = f"\\True ${da_dung_str}$"
            list_1 = [da_d, f"${das1}$", f"${das2}$", f"${das3}$"]
            random.shuffle(list_1)

            loigiai = (f"Mặt phẳng $(\\alpha)$ chứa trục $Oy$ nên có phương trình dạng $Ax + Cz = 0$ (với $A^2 + C^2 > 0$).\\\\ "
                       f"Vì $A({ax}; {ay}; {az}) \\in (\\alpha)$ nên ta có: "
                       f"$A \\cdot ({ax}) + C \\cdot ({az}) = 0 \\Leftrightarrow {ax}A + {az}C = 0$.\\\\ "
                       f"Chọn $A = {A_val}, C = {C_val}$.\\\\ "
                       f"Vậy phương trình mặt phẳng $(\\alpha)$ là ${da_dung_str}$.")

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

