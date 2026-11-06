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


def bt_dang49_p4_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Khởi tạo các hệ số random để đảm bảo tính nguyên và đẹp
                # f(x) = a1*x + b1 khi x >= x0
                # f(x) = a2*x^2 + b2 khi x < x0
                x0 = 1 # Điểm chia nhánh thường là 1 cho đơn giản

                # Random a1 sao cho a1/2 là số nguyên
                a1 = 2 * randint(1, 4) 
                b1 = randint(-5, 5)

                # Random a2 sao cho a2/3 là số nguyên
                a2 = 3 * randint(1, 3)
                b2 = randint(-5, 5)

                # Điểm cho trước F(k) = v
                k = randint(-2, 0) # Thường cho k < x0
                v = randint(2, 5)

                # Điểm cần tính F(m) + n*F(p)
                m = randint(-3, 0) # Nhánh trái
                p = randint(2, 4)  # Nhánh phải
                n_factor = randint(2, 5)

                # 2. Tính toán nguyên hàm và hằng số C
                # Nhánh x < x0: F2(x) = (a2/3)x^3 + b2x + C2
                # F2(k) = v => C2 = v - (a2/3*k^3 + b2*k)
                C2 = v - (Rational(a2, 3)*k**3 + b2*k)

                # Nhánh x >= x0: F1(x) = (a1/2)x^2 + b1x + C1
                # Tính liên tục tại x0: F1(x0) = F2(x0)
                # (a1/2)x0^2 + b1*x0 + C1 = (a2/3)x0^3 + b2*x0 + C2
                val_F2_at_x0 = Rational(a2, 3)*x0**3 + b2*x0 + C2
                C1 = val_F2_at_x0 - (Rational(a1, 2)*x0**2 + b1*x0)

                # 3. Tính giá trị biểu thức F(m) + n*F(p)
                # Vì m < x0 và p >= x0
                val_F_m = Rational(a2, 3)*m**3 + b2*m + C2
                val_F_p = Rational(a1, 2)*p**2 + b1*p + C1
                res = val_F_m + n_factor * val_F_p

                kq = latex(res)

                # 4. Tạo các phương án nhiễu
                du = ['$%s$' % kq]
                da = du[0]

                s = set()
                while len(s) < 3:
                    sai = res + randint(-5, 5)
                    if sai != res:
                        s.add('$ %s $' % latex(sai))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # 5. Nội dung câu hỏi
                # f(x) = a1*x + b1 (x >= x0) | a2*x^2 + b2 (x < x0)
                f_left = a2*x**2 + b2
                f_right = a1*x + b1

                noidungcauhoi = (r'Cho hàm số $f(x) = \begin{cases} %s & \text{khi } x \ge %s \\ %s & \text{khi } x < %s \end{cases}$. Giả sử $F$ là nguyên hàm của $f$ trên $\mathbb{R}$ thỏa mãn $F(%s) = %s$. Tính $F(%s) + %s F(%s)$.'
                                 % (latex(f_right), latex(x0), latex(f_left), latex(x0), latex(k), latex(v), latex(m), latex(n_factor), latex(p)))

                # 6. Nội dung lời giải
                F1_expr = latex(Rational(a1, 2)*x**2 + b1*x)
                F2_expr = latex(Rational(a2, 3)*x**3 + b2*x)

                loigiai = (r'''Tập xác định: $D = \mathbb{R}$. \\
                            Với $x > %s$ hay $x < %s$ thì hàm số $f(x)$ là hàm đa thức nên liên tục. \\
                            Mặt khác: $\lim_{x \to %s^-} f(x) = %s$; $\lim_{x \to %s^+} f(x) = %s$. \\
                            Ta có $\lim_{x \to %s^-} f(x) = \lim_{x \to %s^+} f(x) = f(%s)$ nên hàm số liên tục trên $\mathbb{R}$. \\
                            Với $x \ge %s$ thì $\int f(x) \text{d}x = %s + C_1$. \\
                            Với $x < %s$ thì $\int f(x) \text{d}x = %s + C_2$. \\
                            Mà $F(%s) = %s$ nên $C_2 = %s$. \\
                            Khi đó $F(x) = \begin{cases} %s + C_1 & \text{khi } x \ge %s \\ %s + %s & \text{khi } x < %s \end{cases}$. \\
                            Đồng thời $F(x)$ cũng liên tục trên $\mathbb{R}$ nên: $\lim_{x \to %s^-} F(x) = \lim_{x \to %s^+} F(x) = F(%s) \Leftrightarrow %s = %s + C_1 \Leftrightarrow C_1 = %s$. \\
                            Do đó $F(x) = \begin{cases} %s + %s & \text{khi } x \ge %s \\ %s + %s & \text{khi } x < %s \end{cases}$. \\
                            Vậy: $F(%s) + %s F(%s) = %s + %s \cdot (%s) = %s$.'''
                            % (latex(x0), latex(x0), 
                               latex(x0), latex(f_left.subs(x, x0)), latex(x0), latex(f_right.subs(x, x0)),
                               latex(x0), latex(x0), latex(x0),
                               latex(x0), F1_expr,
                               latex(x0), F2_expr,
                               latex(k), latex(v), latex(C2),
                               F1_expr, latex(x0), F2_expr, latex(C2), latex(x0),
                               latex(x0), latex(x0), latex(x0), latex(val_F2_at_x0), latex(Rational(a1, 2)*x0**2 + b1*x0), latex(C1),
                               F1_expr, latex(C1), latex(x0), F2_expr, latex(C2), latex(x0),
                               latex(m), latex(n_factor), latex(p), latex(val_F_m), latex(n_factor), latex(val_F_p), latex(res)
                            ))

                # 7. Xuất câu trắc nghiệm
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
            return content

