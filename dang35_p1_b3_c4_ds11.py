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


def bt_dang35_p1_b3_c4_ds11(self):
            # Khai báo biến
            # Trong đề gốc: a = 2, b = 1
            a = random.randint(2, 8)
            b = random.randint(-5, 5)

            # Tính toán giá trị giới hạn L = lim_{x->1} [a*root(x,3) - x + (1-a)] / (x-1)
            # Công thức tính nhanh: L = a/3 - 1
            L = Rational(a, 3) - 1

            # Tại x = 1, y(1) = m*(1) + b = m + b
            # Để hàm số liên tục: m + b = L => m = L - b
            kq_m = L - b

            # --- TẠO ĐÁP ÁN ---
            da_dung = '$m = %s$' % latex(kq_m)

            # Tạo các đáp án nhiễu bằng cách thay đổi giá trị
            s = [
                '$m = %s$' % latex(kq_m + 1),
                '$m = %s$' % latex(kq_m - 1),
                '$m = %s$' % latex(Rational(a+3, 3) - b),
                '$m = %s$' % latex(-kq_m),
                '$m = %s$' % latex(kq_m + Rational(1, 3)),
                '$m = %s$' % latex(kq_m - Rational(2, 3)),
            ]
            random.shuffle(s)
            das1, das2, das3 = s[:3]

            # --- NỘI DUNG CÂU HỎI ---
            # Biểu thức tử số: a*cbrt(x) - x + (1-a)
            tu_so = '%s\\sqrt[3]{x} - x %s' % (a, latex(1-a) if 1-a < 0 else '+ ' + str(1-a))
            bieu_thuc_m = 'mx %s' % (latex(b) if b < 0 else '+ ' + str(b))

            noidungcauhoi = (r'''Giá trị của $m$ để hàm số $y = \begin{cases} \dfrac{%s}{x-1}, & x \neq 1 \\ %s, & x = 1 \end{cases}$ liên tục trên $\mathbb{R}$ là'''
                            % (tu_so, bieu_thuc_m))

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = (r'''Xét $x \neq 1$, hàm số $y = \dfrac{%s}{x-1}$ liên tục trên khoảng $(-\infty;1)$ và $(1;+\infty)$.\\
            Xét $x = 1$, ta có $y(1) = m + %s$ và \\
            $\lim_{x \to 1} y = \lim_{x \to 1} \dfrac{%s(\sqrt[3]{x}-1) - (x-1)}{x-1} = \lim_{x \to 1} \left( \dfrac{%s}{\sqrt[3]{x^2} + \sqrt[3]{x} + 1} - 1 \right) = \dfrac{%s}{3} - 1 = %s$.\\
            Để hàm số liên tục tại $x = 1$ thì $\lim_{x \to 1} y = y(1) \Leftrightarrow m + %s = %s \Leftrightarrow m = %s$.'''
                      % (tu_so, b, a, a, a, latex(L), b, latex(L), latex(kq_m)))

            # --- XUẤT KẾT QUẢ ---
            da_d = '\\True ' + da_dung
            list_ans = [da_d, das1, das2, das3]
            random.shuffle(list_ans)

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

