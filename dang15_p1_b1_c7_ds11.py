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


def bt_dang15_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # f(x) = (a*x) / (b + |c*x|)
                a = random.randint(2, 9)
                b = random.randint(1, 5)
                c = random.randint(1, 3)

                # Hàm số ban đầu để tính toán
                f = (a * x) / (b + Abs(c * x))

                # Tính đạo hàm tại 0 bằng định nghĩa: lim (x->0) [f(x) - f(0)] / x
                # f(0) luôn bằng 0 với dạng này
                f_0 = 0
                bieu_thuc_lim = a / (b + Abs(c * x))

                # Tính giới hạn 2 bên
                L_plus = limit(bieu_thuc_lim, x, 0, dir='+')
                L_minus = limit(bieu_thuc_lim, x, 0, dir='-')

                # Kết quả đạo hàm
                kq_val = L_plus # Trong trường hợp này giới hạn 2 bên luôn bằng a/b
                kq_tex = latex(kq_val)

                # Các đáp án trắc nghiệm
                da_dung = f'${kq_tex}$'

                # Tạo các đáp án sai ngẫu nhiên
                s = [
                    f'$0$',
                    f'$ 1$',
                    f'${latex(kq_val + 1)}$',
                    f'${latex(sp.Rational(1, b))}$',
                    f'${latex(a + b)}$'
                ]

                # Loại bỏ đáp án đúng nếu lỡ trùng trong danh sách sai
                if da_dung in s:
                    s.remove(da_dung)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # B2: Viết lại đề bài và lời giải
                # Nội dung câu hỏi
                mau_so_tex = f"{b} + |{c}x|" if c > 1 else f"{b} + |x|"
                noidungcauhoi = (f'Cho hàm số $f(x) = \\frac{{{a}x}}{{{mau_so_tex}}}$. Khi đó $f\'(0)$ bằng')

                # Đáp án
                da_d = '\\True ' + str(da_dung)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f'''Ta có: $f\'(0) = \\lim_{{x \\to 0}} \\frac{{f(x) - f(0)}}{{x}} = \\lim_{{x \\to 0}} \\frac{{{a}}}{{{mau_so_tex}}}$. \\\\
                             Mà $\\lim_{{x \\to 0^+}} \\frac{{{a}}}{{{mau_so_tex}}} = \\lim_{{x \\to 0^+}} \\frac{{{a}}}{{{b} + {c}x}} = {kq_tex}$; \\\\
                             $\\lim_{{x \\to 0^-}} \\frac{{{a}}}{{{mau_so_tex}}} = \\lim_{{x \\to 0^-}} \\frac{{{a}}}{{{b} - {c}x}} = {kq_tex}$. \\\\
                             $\\Rightarrow \\lim_{{x \\to 0^+}} \\frac{{{a}}}{{{mau_so_tex}}} = \\lim_{{x \\to 0^-}} \\frac{{{a}}}{{{mau_so_tex}}} = {kq_tex}$. \\\\
                             $\\Rightarrow f\'(0) = \\lim_{{x \\to 0}} \\frac{{{a}}}{{{mau_so_tex}}} = {kq_tex}$. \\\\
                             Kết luận: $f\'(0) = {kq_tex}$.''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

