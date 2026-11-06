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


def bt_dang33_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1 & 3: Tạo số ngẫu nhiên cho bài toán
                # Parabol y = ax^2 + bx + c
                a = random.choice([1, 2, 3, 4, 5, -1, -2, -3])
                x_ts = random.randint(-5, 5) # Trục đối xứng x = x_ts
                while x_ts == 0: x_ts = random.randint(-5, 5)

                y_cut = random.randint(-10, 10) # Cắt Oy tại M(0; y_cut)

                # Tính toán b và c
                # Trục đối xứng x = -b/(2a) => b = -2*a*x_ts
                b = -2 * a * x_ts
                # Cắt Oy tại (0; c) => c = y_cut
                c = y_cut

                # Đáp án đúng
                # Tạo biểu thức để sympy tự rút gọn dấu (vd: 2x^2 + -4x + 4 thành 2x^2 - 4x + 4)
                x_sym = symbols('x')
                f_x = a*x_sym**2 + b*x_sym + c
                kq_dung = '$y = %s$' % latex(f_x)

                # Bước 4: Tạo các phương án sai (đảm bảo không trùng)
                s = set()
                while len(s) < 3:
                    a_false = a + random.choice([-1, 1])
                    if a_false == 0: a_false = a + 2
                    b_false = b + random.choice([-2, 2, -1, 1])
                    c_false = c + random.choice([-2, 2, -1, 1])
                    f_false = a_false*x_sym**2 + b_false*x_sym + c_false
                    expr_false = '$y = %s$' % latex(f_false)
                    if expr_false != kq_dung:
                        s.add(expr_false)

                list_s = list(s)
                da_s1, da_s2, da_s3 = list_s[0], list_s[1], list_s[2]

                # Câu hỏi (B2: Viết lại theo nội dung ảnh)
                noidungcauhoi = (r'Xác định parabol $y = %sx^2 + bx + c$, biết rằng parabol đó có trục đối xứng $x = %s$ và cắt $Oy$ tại điểm $M(0; %s)$.'
                                 % (latex(a) if a != 1 else "", latex(x_ts), latex(y_cut)))

                # Các đáp án
                da_d = r'\True ' + kq_dung
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết y hệt logic trong ảnh)
                loigiai = (r'Vì $(P)$ có trục đối xứng $x = %s$ nên $-\frac{b}{2a} = %s \Leftrightarrow b = -2a \cdot (%s) \Leftrightarrow b = %s$.\\'
                           r'Hơn nữa $(P)$ cắt trục $Oy$ tại điểm $M(0; %s)$ nên $%s \cdot 0^2 + b \cdot 0 + c = %s \Leftrightarrow c = %s$.\\'
                           r'Vậy $(P): %s$.'
                           % (latex(x_ts), latex(x_ts), latex(x_ts), latex(b),
                              latex(y_cut), latex(a), latex(y_cut), latex(c),
                              kq_dung.replace('$', '')))

            # Bước 2: Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

