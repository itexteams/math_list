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


def bt_dang59_p1_b2_c3_ds12(self):
            # Khai báo biến
            a = random.choice([2, 3, 4, 6]) # Hệ số của x^2
            y0 = random.choice([1, 2, 3, 5]) # Giá trị f(1)
            x_target = random.choice([4, 9, 16, 25]) # Điểm cần tính f(x)

            x = symbols('x')


            C_val = Rational(y0) - Rational(a, 3)

            # Hàm f(x) cuối cùng
            f_x = Rational(a, 3) * x**2 + C_val * sqrt(x)

            # Kết quả f(x_target)
            kq_val = f_x.subs(x, x_target)
            kq = latex(kq_val)

            # Bước 3: Tạo các phương án sai (không trùng đáp án đúng)
            s = set()
            while len(s) < 3:
                # Tạo nhiễu bằng cách thay đổi giá trị quanh đáp án đúng
                sai = kq_val + random.choice([-5, -2, -1, 1, 2, 5, 10, 15])
                if sai != kq_val and sai > 0:
                    s.add('$%s$' % latex(sai))

            list_sai = list(s)
            das1 = list_sai[0]
            das2 = list_sai[1]
            das3 = list_sai[2]

            # Bước 4: Soạn nội dung câu hỏi và lời giải bằng LaTeX
            noidungcauhoi = (r"Cho hàm số $y=f(x)$ có đạo hàm trên $(0;+\infty)$ và thỏa mãn $%s x^2 + f(x) = 2xf'(x), \forall x > 0$. Biết $f(1) = %s$, giá trị của $f(%s)$ bằng"
                             % (latex(a), latex(y0), latex(x_target)))

            da_d = r'\True $%s$' % kq
            list_ans = [da_d, das1, das2, das3]
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            # Chuẩn bị các phân số cho lời giải
            a_chia_2 = Rational(a, 2)
            a_chia_3 = Rational(a, 3)

            loigiai = (r"Với $\forall x > 0$, ta có: " + "\n" +
                       r"$$%s x^2 + f(x) = 2xf'(x) \Leftrightarrow f'(x) - \frac{1}{2x}f(x) = \frac{%s}{2}x$$ " % (latex(a), latex(a)) + "\n" +
                       r"$$\Leftrightarrow \left( \frac{1}{\sqrt{x}} f(x) \right)' = \frac{%s}{2}\sqrt{x} \Rightarrow \frac{1}{\sqrt{x}} f(x) = \frac{%s}{3}\sqrt{x^3} + C.$$ " % (latex(a), latex(a)) + "\n" +
                       r"Thay $f(1) = %s \Rightarrow \frac{1}{\sqrt{1}} \cdot %s = \frac{%s}{3} \cdot 1 + C \Rightarrow C = %s.$ " % (latex(y0), latex(y0), latex(a), latex(C_val)) + "\n" +
                       r"Khi đó $f(x) = \sqrt{x} \left( \frac{%s}{3}x\sqrt{x} + %s \right) = \frac{%s x^2 + %s \sqrt{x}}{3}$." % (latex(a), latex(C_val), latex(a), latex(3*C_val)) + "\n" +
                       r"Vậy $f(%s) = %s$." % (latex(x_target), kq))

            # Bước 5: Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

