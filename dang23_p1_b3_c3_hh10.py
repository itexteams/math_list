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


def bt_dang23_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            a = random.randint(-5, 5)
            b = random.randint(-5, 5)
            R_squared = random.choice([25, 16, 10, 20, 13]) 

            while True:
                dx = random.randint(-3, 3)
                dy = random.randint(-3, 3)
                if 0 < dx**2 + dy**2 < R_squared:
                    break

            xm = a + dx
            ym = b + dy

            # --- B2: Viết lại bài toán và lời giải ---
            vt_trai_C = (x - a)**2 + (y - b)**2
            pt_C_latex = latex(vt_trai_C) + " = " + str(R_squared)

            n_x, n_y = dx, dy
            const_term = -n_x * xm - n_y * ym

            common = math.gcd(math.gcd(n_x, n_y), const_term)
            n_x //= common
            n_y //= common
            const_term //= common

            if n_x < 0 or (n_x == 0 and n_y < 0):
                n_x, n_y, const_term = -n_x, -n_y, -const_term

            # Hàm xử lý hiển thị phương trình đẹp (xử lý + - thành -)
            def format_pt(A, B, C):
                res = ""
                if A == 1: res += "x"
                elif A == -1: res += "-x"
                elif A != 0: res += f"{A}x"

                if B > 0:
                    res += f" + {B}y" if A != 0 else (f"y" if B == 1 else f"{B}y")
                elif B < 0:
                    res += f" - {abs(B)}y" if A != 0 else (f"-y" if B == -1 else f"{B}y")

                if C > 0: res += f" + {C} = 0"
                elif C < 0: res += f" - {abs(C)} = 0"
                else: res += " = 0"
                return res

            pt_d_dung = format_pt(n_x, n_y, const_term)

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường tròn $(C): %s$ và điểm $M(%s;%s)$. Phương trình đường thẳng $d$ qua $M$ cắt $(C)$ tại 2 điểm phân biệt $A, B$ sao cho độ dài dây cung $AB$ nhỏ nhất là'''
                             % (pt_C_latex, xm, ym))

            # --- Nội dung lời giải ---
            loigiai = (r'''Đường tròn $(C)$ có tâm $I(%s;%s)$ bán kính $R=%s$. \\
            Ta có: $IM = \sqrt{(%s-%s)^2 + (%s-%s)^2} = \sqrt{%s}$. \\
            Vì $IM < R$ nên điểm $M$ nằm trong đường tròn $(C)$. \\
            Gọi $H$ là hình chiếu của $I$ lên $d$, ta có $IH \perp d \Rightarrow IH \leq IM$. \\
            Độ dài dây cung $AB = 2\sqrt{R^2 - IH^2}$. \\
            $AB$ nhỏ nhất khi và chỉ khi $IH$ lớn nhất $\Leftrightarrow H \equiv M$. \\
            Khi đó đường thẳng $d$ đi qua $M$ và vuông góc với $IM$ nên nhận $\vec{IM} = (%s; %s)$ làm vectơ pháp tuyến. \\
            Vậy phương trình đường thẳng $d$ là: $%s$.'''
                       % (a, b, latex(simplify(sqrt(R_squared))), xm, a, ym, b, dx**2+dy**2, dx, dy, pt_d_dung))

            # Tạo đáp án
            da_dung = '$%s$' % pt_d_dung
            s = ['$%s$' % format_pt(n_x, -n_y, const_term + 2), 
                 '$%s$' % format_pt(n_y, -n_x, 1), 
                 '$%s$' % format_pt(n_x, n_y, const_term - 3)]
            list_1 = ['\\True ' + da_dung] + s
            random.shuffle(list_1)

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace ('--','+')
            return content

