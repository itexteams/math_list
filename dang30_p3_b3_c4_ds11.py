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


def bt_dang30_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang=='1':
                # B3 - Suy nghĩ tìm cách random: 
                # Thay vì cố định -2 và 2, ta chọn 2 số nguyên m và n ngẫu nhiên
                m = random.randint(-9, -1) # Giá trị âm
                n = random.randint(1, 9)   # Giá trị dương

                # Tính toán các hệ số để hiển thị bất đẳng thức f(m) > 0 và f(n) < 0
                # f(x) = x^3 + ax^2 + bx + c
                # f(m) = m^3 + m^2*a + m*b + c
                m3 = m**3
                m2 = m**2

                # f(n) = n^3 + n^2*a + n*b + c
                n3 = n**3
                n2 = n**2

                # Tạo chuỗi hiển thị bất đẳng thức
                # Điều kiện 1: f(m) > 0 <=> m3 + m2*a + m*b + c > 0
                cond1 = f"{m3} + {m2}a {'+' if m >= 0 else ''}{m}b + c > 0"
                # Điều kiện 2: f(n) < 0 <=> n3 + n2*a + n*b + c < 0
                cond2 = f"{n3} + {n2}a {'+' if n >= 0 else ''}{n}b + c < 0"

                # Đáp án đúng luôn là 3
                da_dung = "3"

                # Các đáp án sai
                s = ["0", "1", "2", "Vô số"]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = (r'''Cho số thực $a, b, c$ thỏa mãn $\begin{cases} %s \\ %s \end{cases}$. Số giao điểm của đồ thị hàm số $y = x^3 + ax^2 + bx + c$ và trục $Ox$ là bao nhiêu?'''
                                %(cond1, cond2))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Đặt $f(x) = x^3 + ax^2 + bx + c$. Ta có: \\
                             $f(%s) = %s > 0$ \\
                             $f(%s) = %s < 0$ \\
                             Hàm số $f(x)$ là hàm đa thức liên tục trên $\mathbb{R}$. \\
                             + Vì $\begin{cases} f(%s) > 0 \\ f(%s) < 0 \end{cases} \Rightarrow f(%s).f(%s) < 0$ nên đồ thị cắt $Ox$ tại ít nhất 1 điểm trong khoảng $(%s; %s)$. \\
                             + Vì $f(%s) < 0$ và $\lim_{x \to +\infty} f(x) = +\infty$ nên đồ thị cắt $Ox$ tại ít nhất 1 điểm trong khoảng $(%s; +\infty)$. \\
                             + Vì $f(%s) > 0$ và $\lim_{x \to -\infty} f(x) = -\infty$ nên đồ thị cắt $Ox$ tại ít nhất 1 điểm trong khoảng $(-\infty; %s)$. \\
                             Mà $f(x)$ là hàm bậc ba nên đồ thị cắt $Ox$ tối đa tại 3 điểm. \\
                             Vậy đồ thị hàm số cắt trục $Ox$ tại đúng $3$ điểm.'''
                             %(m, cond1.split('>')[0], n, cond2.split('<')[0], 
                               m, n, m, n, m, n, 
                               n, n, 
                               m, m))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(3))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

