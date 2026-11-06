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


def bt_dang11_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các tham số
                # a: Hệ số bậc nhất (chọn từ -5 đến 5, khác 0 để đề bài hay hơn)
                a = random.choice([i for i in range(-5, 6) if i != 0])

                # b: Để x^2 + ax + b luôn dương, cần b > a^2 / 4
                b_min = math.ceil(a**2 / 4) + 1
                b = b_min + random.randint(0, 3)

                # k: Giá trị của căn thức (t = k). Chọn k từ 2 đến 5 để số không quá lớn
                k = random.randint(2, 5)

                # c: Tính hệ số vế phải để phương trình có nghiệm t = k
                # t = t^2 - b + c => c = b - k^2 + k
                c = b - k**2 + k

                # Tính tích các nghiệm (Vi-et cho x^2 + ax + b - k^2 = 0)
                kq_val = b - k**2
                kq = latex(kq_val)

                # Bước 4: Tạo các phương án nhiễu (không trùng đáp án đúng)
                s_vals = {kq_val + random.randint(1, 5), 
                          kq_val - random.randint(1, 5), 
                          -kq_val, 
                          kq_val + random.choice([-10, 10])}

                # Loại bỏ trường hợp trùng đáp án đúng
                if kq_val in s_vals:
                    s_vals.remove(kq_val)

                s_list = list(s_vals)
                random.shuffle(s_list)

                das1 = '$%s$' % latex(s_list[0])
                das2 = '$%s$' % latex(s_list[1])
                das3 = '$%s$' % latex(s_list[2])

                # Nội dung câu hỏi
                expr_left = sqrt(x**2 + a*x + b)
                expr_right = x**2 + a*x + c
                noidungcauhoi = ('''Tính tích các nghiệm của phương trình $%s = %s$.'''
                                 % (latex(expr_left), latex(expr_right)))

                # Các đáp án
                da_d = ('\\True $%s$' % kq)
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                t_neg = -(k - 1)
                loigiai = ('''Ta có: $x^2 + %s x + %s > 0, \\forall x \\in \\mathbb{R}$ (vì $\\Delta = (%s)^2 - 4 \\cdot %s < 0$). \\\\
                             Phương trình tương đương: \\\\
                             $%s = x^2 + %s x + %s \\Leftrightarrow x^2 + %s x + %s - %s - (%s) = 0$ \\\\
                             $\\Leftrightarrow (%s)^2 - %s - %s = 0$ \\\\
                             $\\Leftrightarrow \\left[ \\begin{aligned} & %s = %s \\text{ (vô nghiệm vì } %s < 0) \\\\ & %s = %s (1) \\end{aligned} \\right.$ \\\\
                             $(1) \\Leftrightarrow %s = %s \\Leftrightarrow x^2 + %s x + %s = 0$. \\\\
                             Do đó, theo định lý Vi-ét: $x_1 \\cdot x_2 = \\frac{%s}{1} = %s$.'''
                           % (latex(a), latex(b), latex(a), latex(b),
                              latex(expr_left), latex(a), latex(c), latex(a), latex(b), latex(expr_left), latex(b-c),
                              latex(expr_left), latex(expr_left), latex(k**2-k),
                              latex(expr_left), latex(t_neg), latex(t_neg),
                              latex(expr_left), latex(k),
                              latex(expr_left), latex(k), latex(a), latex(b - k**2),
                              latex(b - k**2), latex(kq_val)
                              ))

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

