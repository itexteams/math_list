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


def bt_dang6_p4_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')


            # Bước 1: Random hai số nguyên m, n phân biệt để làm nghiệm x
            list_so = [1, 2, 3, 4, 5, 6]
            m = random.choice(list_so)
            list_so.remove(m)
            n = random.choice(list_so)

            # Sắp xếp để trình bày lời giải từ nhỏ đến lớn hoặc ngược lại cho đẹp
            m, n = sorted([m, n])

            # Bước 2: Tính toán các hệ số a, b, c để phương trình có nghiệm t1=1/n^2, t2=1/m^2
            # Chọn a = 3 để triệt tiêu số 3 ở mẫu khi tính c
            a_val = 3
            b_val = 3 * (m**2 + n**2)
            c_val = m**2 * n**2
            d_val = random.randint(1, 20) # Hằng số tự do không ảnh hưởng đạo hàm

            # Các giá trị phục vụ lời giải
            coeff_t2 = 3 * c_val
            coeff_t1 = b_val
            t1 = Rational(1, n**2)
            t2 = Rational(1, m**2)

            # Biểu thức hàm số và đạo hàm
            f_expr = a_val*x + b_val/x - c_val/x**3 + d_val
            f_prime_expr = a_val - b_val/x**2 + 3*c_val/x**4

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r"Cho hàm số $f(x) = %s$. Giải phương trình $f'(x) = 0$." 
                             % latex(f_expr).replace('+-', '-').replace('- -', '+'))

            # --- Các đáp án ---
            da_dung = r"\True $x = \pm %s, x = \pm %s$" % (m, n)
            da_s1 = r"$x = \pm %s, x = \pm %s$" % (m, n + 1)
            da_s2 = r"$x = \pm %s$" % (m + n)
            da_s3 = r"$x = \pm %s, x = \pm %s$" % (m + 1, n + 2)

            list_1 = [da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- Nội dung lời giải ---
            loigiai = (r"Ta có $f'(x) = \left( %s \right)' = %s$." % (latex(f_expr), latex(f_prime_expr)) + r"\\" + "\n" +
                       r"Phương trình $f'(x) = 0 \Leftrightarrow %s = 0 \quad (1)$." % latex(f_prime_expr) + r"\\" + "\n" +
                       r"Đặt $t = \frac{1}{x^2}, (t > 0)$. Khi đó $(1)$ trở thành:" + r"\\" + "\n" +
                       r"$%s t^2 - %s t + %s = 0 \Leftrightarrow \left[\begin{aligned} &t = %s \\ &t = %s \end{aligned} \right.$" 
                       % (coeff_t2, coeff_t1, a_val, latex(t1), latex(t2)) + r"\\" + "\n" +
                       r"Với $t = %s \Leftrightarrow \frac{1}{x^2} = %s \Leftrightarrow x^2 = %s \Leftrightarrow x = \pm %s$." 
                       % (latex(t1), latex(t1), n**2, n) + r"\\" + "\n" +
                       r"Với $t = %s \Leftrightarrow \frac{1}{x^2} = %s \Leftrightarrow x^2 = %s \Leftrightarrow x = \pm %s$." 
                       % (latex(t2), latex(t2), m**2, m) + r"\\" + "\n" +
                       r"Vậy phương trình $f'(x) = 0$ có $4$ nghiệm $x = \pm %s, x = \pm %s$." % (m, n))

            # Xử lý hiển thị dấu toán học cho chuẩn
            loigiai = loigiai.replace('+-', '-').replace('- -', '+')

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

