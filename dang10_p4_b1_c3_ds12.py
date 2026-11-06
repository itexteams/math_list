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


def bt_dang10_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')


            k = random.randint(1, 5)
            m = random.randint(1, 5)

            a = 3 * k
            b = 2 * m

            # f'(x) = a*sqrt(x) + b/root(x, 3)
            f_prime_latex = r"%s\sqrt{x} + \frac{%s}{\sqrt[3]{x}}" % (a, b)

            # Giá trị f(1) cho trước
            val_f1 = random.randint(-5, 10)

            # Tính toán các hệ số của f(x)
            coeff1 = 2 * k  # Hệ số của x*sqrt(x)
            coeff2 = 3 * m  # Hệ số của căn bậc 3 của x^2

            # f(1) = coeff1 + coeff2 + C = val_f1 => C = val_f1 - coeff1 - coeff2
            C = val_f1 - coeff1 - coeff2

            # Hàm số đúng
            f_x_correct = r"%sx\sqrt{x} + %s\sqrt[3]{x^2} %s" % (
                coeff1 if coeff1 != 1 else "",
                coeff2 if coeff2 != 1 else "",
                f"+ {C}" if C > 0 else (f"- {abs(C)}" if C < 0 else "")
            )

            # B4: Tạo các phương án sai (không trùng đáp án đúng)
            # Sai lệch hằng số C hoặc sai hệ số
            s = [
                r"%sx\sqrt{x} + %s\sqrt[3]{x^2} %s" % (coeff1, coeff2, f"+ {C+random.choice([-2, 1, 2])}"),
                r"%sx\sqrt{x} + %s\sqrt[3]{x} %s" % (coeff1, coeff2, f"+ {C}" if C != 0 else ""), # Sai bậc căn
                r"%s\sqrt{x} + %s\sqrt[3]{x^2} %s" % (coeff1, coeff2, f"+ {C}" if C != 0 else ""), # Thiếu x ở số hạng đầu
                r"%sx\sqrt{x} - %s\sqrt[3]{x^2} %s" % (coeff1, coeff2, f"+ {C}" if C != 0 else ""), # Sai dấu
            ]

            # Loại bỏ trùng lặp nếu có và lấy 3 đáp án sai
            s = list(set(s))
            if f_x_correct in s: s.remove(f_x_correct)
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Nội dung câu hỏi
            noidungcauhoi = (r"Tìm hàm số $y = f(x)$, biết $f'(x) = %s$ ($x > 0$) và $f(1) = %s$." 
                             % (f_prime_latex, val_f1))

            # Nội dung lời giải
            loigiai = ("""Ta có $f(x) = \\int \\left( %s \\right) \\text{d}x = %sx\\sqrt{x} + %s\\sqrt[3]{x^2} + C$. \\\\
                         Theo giả thiết $f(1) = %s \\Rightarrow %s(1) + %s(1) + C = %s \\Rightarrow C = %s$. \\\\
                         Vậy $f(x) = %s$."""
                       % (f_prime_latex, coeff1, coeff2, val_f1, coeff1, coeff2, val_f1, C, f_x_correct))

            # Trình bày trắc nghiệm
            da_d = r'\True $%s$' % f_x_correct
            list_1 = [da_d, f'$%s$'%das1, f'$%s$'%das2, f'$%s$'%das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

