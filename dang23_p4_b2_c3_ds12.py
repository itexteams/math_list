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


def bt_dang23_p4_b2_c3_ds12(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn cận là các số chính phương để khai căn cho đẹp
                n1 = randint(1, 2)      # Cận dưới (1 hoặc 2)
                n2 = n1 + randint(1, 2) # Cận trên lớn hơn cận dưới

                a = n1**2
                b = n2**2
                k = randint(1, 5) # Hệ số k trong tử số (x + k)

                # Tính toán bằng Sympy
                expr = (x + k) / sqrt(x)
                # Hàm nguyên hàm để trình bày lời giải
                # f_split = sqrt(x) + k/sqrt(x) = x^(1/2) + k*x^(-1/2)
                # F = (2/3)*x^(3/2) + 2*k*x^(1/2)

                nguyen_ham = (Rational(2, 3) * x**Rational(3, 2) + 2 * k * sqrt(x))

                val_b = nguyen_ham.subs(x, b)
                val_a = nguyen_ham.subs(x, a)
                kq_chuan = val_b - val_a

                # --- BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN SAI ---
                # Tạo danh sách các đáp án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    # Tạo sai số bằng cách thay đổi tử số hoặc cộng trừ ngẫu nhiên
                    sai_so = Rational(randint(1, 10), 3)
                    if random.choice([True, False]):
                        option = kq_chuan + sai_so
                    else:
                        option = kq_chuan - sai_so

                    if option != kq_chuan and option > 0:
                        s.add('$%s$' % latex(option))

                list_sai = list(s)
                da_d = '\\True $%s$' % latex(kq_chuan)
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                # Trộn thứ tự đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- BƯỚC 2: VIẾT LẠI NỘI DUNG ---
                # Câu hỏi
                noidungcauhoi = (r'Tính $\displaystyle \int_{%s}^{%s} \frac{x + %s}{\sqrt{x}} \, \text{d} x$.' 
                                 % (latex(a), latex(b), latex(k)))

                # Lời giải chi tiết
                loigiai = (r'''Ta có: $\displaystyle \int_{%s}^{%s} \frac{x + %s}{\sqrt{x}} \, \text{d} x = \int_{%s}^{%s} \left( \sqrt{x} + \frac{%s}{\sqrt{x}} \right) \, \text{d} x$ \\
                             $= \left( \frac{2x^{\frac{3}{2}}}{3} + 2 \cdot %s \sqrt{x} \right) \bigg|_{%s}^{%s}$ \\
                             $= \left( %s + %s \right) - \left( %s + %s \right) = %s$.'''
                           % (latex(a), latex(b), latex(k), latex(a), latex(b), latex(k),
                              latex(k), latex(a), latex(b),
                              latex(val_b.args[0] if len(val_b.args)>1 else val_b), latex(val_b.args[1] if len(val_b.args)>1 else 0),
                              latex(val_a.args[0] if len(val_a.args)>1 else val_a), latex(val_a.args[1] if len(val_a.args)>1 else 0),
                              latex(kq_chuan)
                             ))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

