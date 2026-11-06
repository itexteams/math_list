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


def bt_dang57_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- Bước 1: Sinh số ngẫu nhiên cho bài toán ---
                # Parabol đi qua A(0; c) -> c là tung độ gốc
                c_val = random.randint(3, 8) 
                # Tọa độ đỉnh (x_i; y_i)
                x_i = random.randint(1, 4)
                y_i = random.randint(1, 5)

                # Đảm bảo y_i < c_val để parabol có bề lõm hướng lên (đạt cực tiểu)
                # Nếu không thỏa mãn, ta đảo lại
                if y_i >= c_val:
                    y_i = c_val - random.randint(2, 4)

                # --- Bước 2: Giải hệ phương trình tìm a, b ---
                # Hệ: -b/(2a) = x_i  => b = -2*a*x_i
                # Thay vào y = ax^2 + bx + c tại đỉnh: a*(x_i)^2 + (-2*a*x_i)*x_i + c = y_i
                # => a*(x_i^2 - 2x_i^2) = y_i - c => -a*(x_i^2) = y_i - c

                a_num = c_val - y_i
                a_den = x_i**2
                a_val = Rational(a_num, a_den)
                b_val = -2 * a_val * x_i

                # Biểu thức Parabol
                x = symbols('x')
                f_x = a_val*x**2 + b_val*x + c_val
                delta = b_val**2 - 4*a_val*c_val

                # --- Bước 3: Tạo các phương án nhiễu (sai) ---
                kq_dung = '$y = %s$' % latex(f_x)

                # Tạo danh sách các phương án sai bằng cách thay đổi hệ số
                s = [
                    '$y = %s$' % latex(a_val*x**2 - b_val*x + c_val),
                    '$y = %s$' % latex(-a_val*x**2 + b_val*x + c_val),
                    '$y = %s$' % latex(a_val*x**2 + b_val*x - c_val),
                    '$y = %s$' % latex(Rational(1,2)*a_val*x**2 + b_val*x + c_val),
                    '$y = %s$' % latex(a_val*x**2 + 2*b_val*x + c_val),
                    '$y = %s$' % latex(a_val*x**2 + b_val*x + c_val + 1)
                ]

                # Loại bỏ trùng lặp với đáp án đúng nếu có
                if kq_dung in s:
                    s.remove(kq_dung)

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # --- Bước 4: Nội dung câu hỏi và lời giải ---
                noidungcauhoi = (r'''Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó đạt cực tiểu bằng $%s$ tại $x = %s$ và đồ thị hàm số đi qua điểm $A(0;%s)$?'''
                                 %(latex(y_i), latex(x_i), latex(c_val)))

                da_d = ('\\True ' + str(kq_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết theo mẫu hình ảnh
                loigiai = (r'''Vì hàm số đạt cực tiểu bằng $%s$ tại $x = %s$ và đồ thị hàm số đi qua điểm $A(0;%s)$ nên ta có:
                \[
                \begin{cases}
                -\dfrac{b}{2a} = %s \\
                -\dfrac{\Delta}{4a} = %s \\
                c = %s
                \end{cases} \Leftrightarrow 
                \begin{cases}
                b = %s a \\
                b^2 - 4ac = %s a \\
                c = %s
                \end{cases} \Leftrightarrow
                \begin{cases}
                b = %s a \\
                (%s a)^2 - 4a(%s) = %s a \\
                c = %s
                \end{cases}
                \]
                Giải hệ trên ta được $a = %s, b = %s, c = %s$. \\
                Do đó $(P)$ là parabol nên $a \neq 0$, ta chọn $a = %s, b = %s, c = %s$.\\
                Vậy $(P): y = %s$.'''
                           %(latex(y_i), latex(x_i), latex(c_val),
                             latex(x_i), latex(y_i), latex(c_val),
                             latex(-2*x_i), latex(-4*y_i), latex(c_val),
                             latex(-2*x_i), latex(-2*x_i), latex(c_val), latex(-4*y_i), latex(c_val),
                             latex(a_val), latex(b_val), latex(c_val),
                             latex(a_val), latex(b_val), latex(c_val),
                             latex(f_x)))

            # --- Bước 5: Xuất nội dung ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

