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


def bt_dang35_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1 & B3: Nghiên cứu đề bài và thực hiện random
                # y = { m*x^2 + n*x + a  khi x != 0
                #     { p*x^2           khi x = 0

                m = randint(2, 6)
                n = randint(-6, 6)
                if n == 0: n = 1
                p = randint(1, 4)

                # Ký hiệu dấu cho n trong biểu thức
                dau_n = "+" if n > 0 else ""

                # Để hàm số có đạo hàm tại x=0, trước hết nó phải liên tục tại x=0
                # lim (x->0) f(x) = a
                # f(0) = p*(0)^2 = 0
                # => a = 0
                da_val = 0
                da = '$a = %s$' % (latex(da_val))

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s_list = [1, -1, 2, -2, n, m, -n]
                # Loại bỏ giá trị trùng với đáp án đúng (0) và các giá trị trùng nhau
                s_list = list(set([val for val in s_list if val != da_val]))
                random.shuffle(s_list)

                das1 = '$a = %s$' % (latex(s_list[0]))
                das2 = '$a = %s$' % (latex(s_list[1]))
                das3 = '$a = %s$' % (latex(s_list[2]))

                # Nội dung câu hỏi (B2 - Viết lại theo mẫu)
                # Sử dụng \left( \right) và %s theo yêu cầu
                noidungcauhoi = ('''Cho hàm số $y = \\begin{cases} %sx^2 %s %sx + a & \\text{khi } x \\neq 0 \\\\ %sx^2 & \\text{khi } x = 0 \\end{cases}$. Tìm $a$ để hàm số có đạo hàm tại $x = 0$.'''
                                 % (latex(m), dau_n, latex(n), latex(p)))

                # Nội dung lời giải chi tiết y hệt mẫu trong ảnh
                loigiai = ('''Ta có $\\lim_{x \\to 0} \\left( %sx^2 %s %sx + a \\right) = a$, $f\\left( 0 \\right) = 0$. \\\\
            Hàm số có đạo hàm tại $x = 0 \\Rightarrow f\\left( x \\right)$ liên tục tại $x = 0 \\Leftrightarrow \\lim_{x \\to 0} \\left( %sx^2 %s %sx + a \\right) = f\\left( 0 \\right) \\Leftrightarrow a = 0$. \\\\
            Khi $a = 0$, ta có: \\\\
            $f'\\left( 0 \\right) = \\lim_{x \\to 0} \\frac{f\\left( x \\right) - f\\left( 0 \\right)}{x - 0} = \\lim_{x \\to 0} \\frac{%sx^2 %s %sx - 0}{x} = \\lim_{x \\to 0} \\frac{x\\left( %sx %s %s \\right)}{x} = \\lim_{x \\to 0} \\left( %sx %s %s \\right) = %s$.'''
                           % (latex(m), dau_n, latex(n),
                              latex(m), dau_n, latex(n),
                              latex(m), dau_n, latex(n),
                              latex(m), dau_n, latex(n),
                              latex(m), dau_n, latex(n),
                              latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Không dùng tiền tố r, thay dấu chấm bằng dấu phẩy cho số thập phân)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi) + 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

