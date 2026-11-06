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


def bt_dang10_p4_b3_c4_ds11(self):
            # Khai báo biến ký hiệu cho SymPy
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM ---
                # Ta chọn a và c ngẫu nhiên, sau đó tính b = c^2 - a để đảm bảo mẫu bằng 0 tại x = a
                a = random.randint(1, 6)      # Điểm x_0
                c = random.randint(2, 5)      # Hằng số trong căn
                b = c**2 - a                  # Để sqrt(a+b) - c = 0
                k = 2 * c                     # Giá trị f(a) để hàm số liên tục

                # Khai báo biểu thức Sympy để tính toán chính xác
                x = symbols('x')
                f_limit_expr = (x - a) / (sqrt(x + b) - c)

                # Các mệnh đề trắc nghiệm
                da_dung = f"Hàm số liên tục tại $x = {a}$."
                s1 = f"Hàm số gián đoạn tại $x = {a}$."
                s2 = f"Hàm số không xác định tại $x = {a}$."
                s3 = f"Hàm số liên tục trên $(-\\infty; {a})$ nhưng gián đoạn tại $x = {a}$."

                # Xử lý đáp án đúng và sai
                da_d = '\\True ' + da_dung
                list_1 = [da_d, s1, s2, s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                # Định dạng lại biểu thức phân số để hiển thị đẹp trong LaTeX
                tu_so = f"x - {a}" if a > 0 else f"x + {abs(a)}"
                mau_so = f"\\sqrt{{x + {b}}} - {c}" if b > 0 else f"\\sqrt{{x - {abs(b)}}} - {c}"

                noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} \dfrac{%s}{%s} & \text{khi } x \neq %s \\ %s & \text{khi } x = %s \end{cases}$. Xét tính liên tục của hàm số tại $x=%s$.'''
                                 % (tu_so, mau_so, latex(a), latex(k), latex(a), latex(a)))

                # Nội dung lời giải (B2 - Viết lại y hệt logic trong ảnh)
                loigiai = (r'''Tập xác định: $D = [%s; +\infty)$. \\
                             $\displaystyle \lim_{x \to %s} f(x) = \lim_{x \to %s} \frac{%s}{%s} = \lim_{x \to %s} \frac{(x - %s)(\sqrt{x + %s} + %s)}{x - %s} = \lim_{x \to %s} (\sqrt{x + %s} + %s) = %s$. \\
                             $f(%s) = %s$. \\
                             $\Rightarrow \displaystyle \lim_{x \to %s} f(x) = f(%s)$. \\
                             Vậy hàm số liên tục tại $x = %s$.'''
                           % (latex(-b), 
                              latex(a), latex(a), tu_so, mau_so, 
                              latex(a), latex(a), latex(b), latex(c), latex(a), 
                              latex(a), latex(b), latex(c), latex(k),
                              latex(a), latex(k),
                              latex(a), latex(a),
                              latex(a)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

