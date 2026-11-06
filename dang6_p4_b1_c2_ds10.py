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


def bt_dang6_p4_b1_c2_ds10(self):
            # Khai báo biến
            # Gọi x, y để sympy tự động xử lý dấu và loại bỏ hệ số 1 (ví dụ 1x -> x)
            x, y = symbols('x y')

            # 1. Random các hệ số đã rút gọn (a, b, c, d) - Đảm bảo là số dương
            a = random.randint(1, 3)
            b = random.randint(1, 4)
            c = random.randint(1, 4)
            d = random.randint(1, 3)

            # 2. Random hằng số bên vế phải sau khi rút gọn
            R1 = random.randint(8, 15) * 10  # Ví dụ: 80, 90, 100...
            R2 = random.randint(5, 10) * 10  # Ví dụ: 50, 60, 80...

            # 3. Random hệ số nhân để tạo ra đề bài gốc
            k1 = random.randint(2, 5)   # Tỉ lệ cho phương trình nguyên liệu
            k2 = random.randint(10, 20) # Tỉ lệ cho phương trình thời gian

            # 4. Tính toán ngược ra số liệu của đề bài
            m1 = a * k1
            m2 = b * k1
            M = R1 * k1

            t1 = c * k2
            t2 = d * k2
            T = R2 * k2

            # 5. Xử lý hiển thị biểu thức bằng sympy để chuẩn format (tự mất 1x, xử lý dấu)
            eq1_raw = m1*x + m2*y
            eq2_raw = t1*x + t2*y

            eq1_simp = a*x + b*y
            eq2_simp = c*x + d*y

            # 6. Tính kết quả S
            S = a - b - c + d

            # Các đáp án trắc nghiệm
            da = f"${S}$"

            # Sinh đáp án nhiễu (sai) và đảm bảo không bị trùng lặp bằng Set
            tap_dap_an_sai = set()
            while len(tap_dap_an_sai) < 3:
                sai = S + random.choice([-3, -2, -1, 1, 2, 3])
                if sai != S:
                    tap_dap_an_sai.add(f"${sai}$")

            tap_dap_an_sai = list(tap_dap_an_sai)
            das1 = tap_dap_an_sai[0]
            das2 = tap_dap_an_sai[1]
            das3 = tap_dap_an_sai[2]

            # Câu hỏi
            noidungcauhoi = (f'''Một xưởng sản xuất hai loại sản phẩm, mỗi kg sản phẩm loại một cần ${m1}$kg nguyên liệu và ${t1}$ giờ. '''
                             f'''Mỗi sản phẩm loại hai cần ${m2}$kg nguyên liệu và ${t2}$ giờ. Xưởng có ${M}$kg nguyên liệu và ${T}$ giờ làm việc. '''
                             f'''Gọi $x, y$ lần lượt là số kg loại một và loại hai cần sản xuất, các bất phương trình (1): $ax + by \\le {R1}$ và (2): $cx + dy \\le {R2}$ '''
                             f'''lần lượt là bất phương trình biểu diễn ràng buộc về số nguyên liệu và số giờ cần dùng để sản xuất các loại sản phẩm. Tính $S = a - b - c + d$.''')

            # Các đáp án (trộn ngẫu nhiên)
            da_d = '\\True ' + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (f'''Gọi $x \\ (x \\ge 0)$ là số kg loại một cần sản xuất, $y \\ (y \\ge 0)$ là số kg loại hai cần sản xuất. Suy ra số nguyên liệu cần dùng là ${latex(eq1_raw)}$. \\\\'''
                       f'''Theo giả thiết bài toán xưởng có ${M}$kg nguyên liệu và ${T}$ giờ làm việc, suy ra ${latex(eq1_raw)} \\le {M}$ hay ${latex(eq1_simp)} \\le {R1}$; \\\\'''
                       f'''${latex(eq2_raw)} \\le {T}$ hay ${latex(eq2_simp)} \\le {R2}$.\\\\ '''
                       f'''Vậy $a = {a}; b = {b}; c = {c}; d = {d}$. Suy ra $S = {a} - {b} - {c} + {d} = {S}$.''')


            # ================= XUẤT CÂU TRẮC NGHIỆM =================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

