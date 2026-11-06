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


def bt_dang44_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Thiết lập các thông số cơ bản
                # Giả sử Parabol y = ax^2 + bx + c
                b = random.randint(2, 6) # Hệ số b
                a_real = random.choice([-3, -2, -1, 1, 2, 3]) # Hệ số a đúng

                # Tính x_I sao cho x_I = -b / (2a)
                x_i = sp.Rational(-b, 2 * a_real)

                # Hệ số c ngẫu nhiên
                c = random.randint(-5, 5)

                # Tính y_I = a*(x_I)^2 + b*x_I + c
                y_i = a_real * (x_i**2) + b * x_i + c

                # Hàm số đúng
                def format_poly(a_val, b_val, c_val):
                    x = symbols('x')
                    poly = a_val*x**2 + b_val*x + c_val
                    return '$y = %s$' % latex(poly)

                da = format_poly(a_real, b, c)

                # 2. Tạo các phương án sai (thay đổi hệ số a hoặc dấu)
                s_vals = set()
                # Các giá trị a sai
                while len(s_vals) < 3:
                    a_sai = a_real + random.choice([-2, -1, 1, 2])
                    if a_sai != a_real and a_sai != 0:
                        s_vals.add(format_poly(a_sai, b, c))

                    # Thêm phương án sai về dấu của b hoặc c để gây nhiễu
                    if len(s_vals) < 3:
                        s_vals.add(format_poly(a_real, -b, c))

                list_sai = list(s_vals)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # 3. Nội dung câu hỏi
                # Chú ý: Trong câu hỏi vẫn để dạng tham số a để người học phải đi tìm a
                c_str = ('+ ' + str(c) if c > 0 else (str(c) if c < 0 else ""))
                noidungcauhoi = (r'Parabol $(P): y = ax^2 + %sx %s$ có đỉnh $I\left(%s; %s\right)$ là'
                                 % (latex(b), c_str, latex(x_i), latex(y_i)))

                # 4. Nội dung lời giải (Trình bày chi tiết từng bước như ảnh mẫu)
                delta_val = b**2 - 4*a_real*c
                loigiai = (r'Vì $(P)$ có đỉnh $I\left(%s; %s\right)$ nên ta có '
                           r'\[ \begin{cases} -\dfrac{b}{2a} = %s \\ -\dfrac{\Delta}{4a} = %s \end{cases} '
                           r'\Leftrightarrow \begin{cases} -\dfrac{%s}{2a} = %s \\ \Delta = %s a \end{cases} '
                           r'\Leftrightarrow \begin{cases} a = %s \\ %s^2 - 4 \cdot a \cdot (%s) = %s a \end{cases} '
                           r'\Leftrightarrow a = %s. \]'
                           r'Vậy $(P):$ %s.'
                           % (latex(x_i), latex(y_i), 
                              latex(x_i), latex(y_i),
                              latex(b), latex(x_i), latex(-4*y_i),
                              latex(a_real), latex(b), latex(c), latex(-4*y_i*a_real),
                              latex(a_real), da))

                # 5. Sắp xếp đáp án ngẫu nhiên
                da_d = '\\True ' + str(da)
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # 6. Xuất nội dung theo cấu trúc yêu cầu
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

