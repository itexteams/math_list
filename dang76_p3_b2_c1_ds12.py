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


def bt_dang76_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        x = symbols('x')

        # Hàm số dạng h(x) = -a*x^2 + b*x + c
        # Chọn đỉnh x_0 = b / (2*a) là số nguyên nằm trong khoảng (10, 25)
        # Tổng số ngày trong tháng là N_days = 30
        n_days = 30
        a_val = randint(3, 8)
        x_dinh = randint(12, 22)
        b_val = 2 * a_val * x_dinh
        c_val = randint(20, 60) * 10

        # Hàm số h(x)
        h_func = -a_val * x**2 + b_val * x + c_val
        dh = sp.diff(h_func, x)


        so_ngay = x_dinh - 1

        # Tính các giá trị tại các mốc của BBT để trình bày
        h_1 = h_func.subs(x, 1)
        h_dinh = h_func.subs(x, x_dinh)
        h_max_day = h_func.subs(x, n_days)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cửa hàng kinh doanh đồ trang trí nhận thấy lợi nhuận mỗi ngày trong một tháng (%s ngày) được ước tính theo hàm số $h(x)=%s$ (nghìn đồng) với $x$ là ngày thứ $x$ trong tháng ($1 \\le x \\le %s, x \\in \\mathbb{N}$). Hỏi trong tháng đó, có bao nhiêu ngày mà lợi nhuận của cửa hàng tăng so với ngày liền trước đó?'''
                         %(str(n_days),
                           latex(h_func),
                           str(n_days)
                         ))

        # Nội dung lời giải
        loigiai = ('''Xét hàm số $h(x)=%s$ liên tục trên đoạn $[1;%s]$. \\\\
    Ta có: $h'(x)=%s$. \\\\
    Cho $h'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\
    Bảng biến thiên của hàm số trên đoạn $[1;%s]$:
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\tkzTabInit[lgt=1.5, espcl=3]{$x$/0.8, $h'(x)$/0.8, $h(x)$/2}{$1$, $%s$, $%s$}
    \\tkzTabLine{,+,0,-,}
    \\tkzTabVar{-/$%s$, +/$%s$, -/$%s$}
    \\end{tikzpicture}
    \\end{center}
    Căn cứ bảng biến thiên, ta thấy: \\\\
    Hàm số $h(x)$ đồng biến trên đoạn $[1;%s]$ và nghịch biến trên đoạn $[%s;%s]$. \\\\
    Do đó, với $x \\in \\{%s;%s\\}$, ta có $h(x) > h(x-1)$ khi và chỉ khi $x \\le %s$. \\\\
    Vì vậy, $x \\in \\{2; 3; \\ldots; %s\\}$. \\\\
    Số ngày mà lợi nhuận tăng so với ngày liền trước đó là: $%s - 2 + 1 = %s$ (ngày).'''
                   %(latex(h_func), str(n_days),
                     latex(dh),
                     latex(dh), str(x_dinh),
                     str(n_days),
                     str(x_dinh), str(n_days),
                     str(h_1), str(h_dinh), str(h_max_day),
                     str(x_dinh), str(x_dinh), str(n_days),
                     str(2), str(n_days),
                     str(x_dinh),
                     str(x_dinh),
                     str(x_dinh), str(so_ngay)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(so_ngay))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content

