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


def bt_dang37_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các hệ số ngẫu nhiên để đảm bảo bài toán có nghiệm đẹp


                m = randint(-5, 5)
                n = randint(-5, 5)
                k = randint(1, 4)
                q = 2 * k
                p = q + 1


                val_a = n - k - 1
                val_b = 1 - m - n - val_a

                # Các hằng số bổ trợ cho lời giải
                sum_mn = m + n
                c_cont = 1 - sum_mn # b = c_cont - a
                f1_val = val_a + sum_mn

                # Đáp án đúng
                da_text = "a = %s; b = %s" % (latex(val_a), latex(val_b))
                da_d = "\\True $%s$" % da_text

                # Tạo các đáp án sai
                s = [
                    "$a = %s; b = %s$" % (latex(val_b), latex(val_a)),
                    "$a = %s; b = %s$" % (latex(val_a + 1), latex(val_b - 1)),
                    "$a = %s; b = %s$" % (latex(-val_a), latex(val_b)),
                    "$a = %s; b = %s$" % (latex(val_a), latex(-val_b)),
                    "$a = %s; b = %s$" % (latex(val_a - 2), latex(val_b + 2)),
                ]

                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Câu hỏi
                # f(x) biểu diễn dạng latex
                noidungcauhoi = ('''Tìm $a; b$ để hàm số $f\\left( x \\right) = \\begin{cases} %s x^2 %s x %s & \\text{ khi } x \\ge 1 \\\\ \\sqrt{%s - %s x} - bx & \\text{ khi } x < 1 \\end{cases}$ có đạo hàm tại điểm $x = 1$.'''
                                 % ( "a" if val_a == 1 else "-a" if val_a == -1 else "a", 
                                     "+ " + latex(m) if m > 0 else latex(m) if m < 0 else "",
                                     "+ " + latex(n) if n > 0 else latex(n) if n < 0 else "",
                                     latex(p), latex(q) ))

                # Các đáp án vào danh sách
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có: \\\\
                             $f\\left( 1 \\right) = a + %s = %s$. \\\\
                             $\\lim_{x \\to 1^+} f\\left( x \\right) = \\lim_{x \\to 1^+} \\left( ax^2 %s x %s \\right) = a %s$. \\\\
                             $\\lim_{x \\to 1^-} f\\left( x \\right) = \\lim_{x \\to 1^-} \\left( \\sqrt{%s - %s x} - bx \\right) = 1 - b$. \\\\
                             Hàm số liên tục tại $x = 1$ nên $\\lim_{x \\to 1^+} f\\left( x \\right) = \\lim_{x \\to 1^-} f\\left( x \\right) = f\\left( 1 \\right) \\Leftrightarrow a %s = 1 - b \\Leftrightarrow b = %s - a$. \\\\
                             Đạo hàm bên phải: \\\\
                             $f'\\left( 1^+ \\right) = \\lim_{x \\to 1^+} \\frac{f\\left( x \\right) - f\\left( 1 \\right)}{x - 1} = \\lim_{x \\to 1^+} \\frac{ax^2 %s x %s - \\left( a %s \\right)}{x - 1} = \\lim_{x \\to 1^+} \\left( ax + a %s \\right) = 2a %s$. \\\\
                             Đạo hàm bên trái: \\\\
                             $f'\\left( 1^- \\right) = \\lim_{x \\to 1^-} \\frac{f\\left( x \\right) - f\\left( 1 \\right)}{x - 1} = \\lim_{x \\to 1^-} \\frac{\\sqrt{%s - %s x} - bx - \\left( a %s \\right)}{x - 1}$ \\\\
                             Thay $b = %s - a$ vào ta được: \\\\
                             $f'\\left( 1^- \\right) = \\lim_{x \\to 1^-} \\frac{\\sqrt{%s - %s x} - \\left( %s - a \\right)x - a %s}{x - 1}$ \\\\
                             $= \\lim_{x \\to 1^-} \\left( a %s - \\frac{%s}{\\sqrt{%s - %s x} + 1} \\right) = a %s$. \\\\
                             Hàm số có đạo hàm tại điểm $x = 1 \\Leftrightarrow f'\\left( 1^+ \\right) = f'\\left( 1^- \\right) \\Leftrightarrow 2a %s = a %s \\Leftrightarrow a = %s$. \\\\
                             Với $a = %s$, ta có $b = %s - \\left( %s \\right) = %s$. \\\\
                             Vậy $a = %s; b = %s$ là giá trị cần tìm.'''
                           % ( latex(sum_mn), "a" + ("+ " + latex(sum_mn) if sum_mn > 0 else latex(sum_mn) if sum_mn < 0 else ""),
                               "+ " + latex(m) if m > 0 else latex(m) if m < 0 else "",
                               "+ " + latex(n) if n > 0 else latex(n) if n < 0 else "",
                               "+ " + latex(sum_mn) if sum_mn > 0 else latex(sum_mn) if sum_mn < 0 else "",
                               latex(p), latex(q),
                               "+ " + latex(sum_mn) if sum_mn > 0 else latex(sum_mn) if sum_mn < 0 else "",
                               latex(c_cont),
                               "+ " + latex(m) if m > 0 else latex(m) if m < 0 else "",
                               "+ " + latex(n) if n > 0 else latex(n) if n < 0 else "",
                               "+ " + latex(sum_mn) if sum_mn > 0 else latex(sum_mn) if sum_mn < 0 else "",
                               "+ " + latex(m) if m > 0 else latex(m) if m < 0 else "",
                               "+ " + latex(m) if m > 0 else latex(m) if m < 0 else "",
                               latex(p), latex(q),
                               "+ " + latex(sum_mn) if sum_mn > 0 else latex(sum_mn) if sum_mn < 0 else "",
                               latex(c_cont),
                               latex(p), latex(q), latex(c_cont),
                               "+ " + latex(sum_mn) if sum_mn > 0 else latex(sum_mn) if sum_mn < 0 else "",
                               latex(-c_cont), latex(q), latex(p), latex(q),
                               latex(-c_cont - k),
                               "+ " + latex(m) if m > 0 else latex(m) if m < 0 else "",
                               latex(-c_cont - k),
                               latex(val_a), latex(val_a), latex(c_cont), latex(val_a), latex(val_b),
                               latex(val_a), latex(val_b)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

