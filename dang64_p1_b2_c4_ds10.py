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


def bt_dang64_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo tọa độ đỉnh I(x_i; y_i) ngẫu nhiên
                xi = random.randint(-3, 3)
                yi = random.randint(-3, 3)

                # Tạo tọa độ điểm A(x_a; y_a) sao cho x_a != x_i để tồn tại parabol
                # Để đơn giản và số đẹp, ta chọn x_a = x_i + 1 hoặc x_i - 1
                xa = xi + random.choice([-1, 1])
                # Tính y_a dựa trên một giá trị 'a' nguyên ngẫu nhiên để đảm bảo a, b, c đẹp
                a_val = random.randint(-3, 3)
                if a_val == 0: a_val = 2 # Đảm bảo a khác 0

                # Phương trình Parabol: y = a(x - xi)^2 + yi
                # Suy ra ya = a_val*(xa - xi)^2 + yi
                ya = a_val * (xa - xi)**2 + yi

                # Từ y = ax^2 + bx + c, ta có hệ thức:
                # 1. -b/(2a) = xi => b = -2*a*xi
                # 2. a*xi^2 + b*xi + c = yi => c = yi + a*xi^2

                a = a_val
                b = -2 * a * xi
                c = yi + a * (xi**2)

                # Tính giá trị biểu thức T = a^3 + b^2 - 2c
                val_T = a**3 + b**2 - 2*c

                # Các đáp án trắc nghiệm
                da = '$%s$' % val_T

                # Tạo các phương án nhiễu (không trùng với đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = val_T + random.choice([-10, -5, 2, 5, 10, 12, 15, -2, 7])
                    if sai != val_T:
                        s.add('$%s$' % sai)

                list_s = list(s)
                das1, das2, das3 = list_s[0], list_s[1], list_s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (r'Biết đồ thị hàm số $y = ax^2 + bx + c, (a, b, c \in \mathbb{R}; a \neq 0)$ đi qua điểm $A(%s;%s)$ và có đỉnh $I(%s;%s)$. Giá trị biểu thức $T = a^3 + b^2 - 2c$ bằng'
                                 % (latex(xa), latex(ya), latex(xi), latex(yi)))

                # Các đáp án
                da_d = r'\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (r'''Đồ thị hàm số $y = ax^2 + bx + c$ đi qua điểm $A(%s;%s)$ và có đỉnh $I(%s;%s)$ nên ta có hệ phương trình:
            \\
            $\begin{cases} a(%s)^2 + b(%s) + c = %s \\ -\frac{b}{2a} = %s \\ a(%s)^2 + b(%s) + c = %s \end{cases} \Leftrightarrow \begin{cases} %sa + %sb + c = %s \\ b = %sa \\ %sa + %sb + c = %s \end{cases} \Leftrightarrow \begin{cases} a = %s \\ b = %s \\ c = %s \end{cases}$.
            \\
            Vậy $T = a^3 + b^2 - 2c = (%s)^3 + (%s)^2 - 2(%s) = %s$.'''
                           % (latex(xa), latex(ya), latex(xi), latex(yi),
                              latex(xa), latex(xa), latex(ya),
                              latex(xi),
                              latex(xi), latex(xi), latex(yi),
                              latex(xa**2), latex(xa), latex(ya),
                              latex(-2*xi),
                              latex(xi**2), latex(xi), latex(yi),
                              latex(a), latex(b), latex(c),
                              latex(a), latex(b), latex(c), latex(val_T)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

