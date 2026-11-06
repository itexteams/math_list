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


def bt_dang31_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo các biến ký hiệu
            x = symbols('x')

            # Danh sách dạng (hiện tại có 1 dạng theo hình ảnh)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các hệ số của tam thức bậc hai f(x) = x^2 + ax + b
                # Để đạo hàm tại x0 là số nguyên, ta chọn x0, a, b nguyên
                x0 = random.randint(-5, 5)
                a = random.randint(-5, 10)
                b = random.randint(-10, 10)

                # Tính giá trị f(x0) để hàm số liên tục (điều kiện cần để có đạo hàm)
                # f(x0) = x0^2 + a*x0 + b
                y0 = x0**2 + a*x0 + b

                # Tính đạo hàm tại x0 bằng định nghĩa: f'(x0) = lim (x->x0) [f(x) - f(x0)] / (x - x0)
                # f'(x) = 2x + a => f'(x0) = 2*x0 + a
                kq_val = 2*x0 + a

                # Đáp án đúng
                kq = str(kq_val).replace('.', ',')
                du = ['$%s$' % kq]
                da = random.choice(du)

                # Tạo các phương án nhiễu (không trùng với đáp án đúng)
                s = []
                while len(s) < 3:
                    sai = kq_val + random.choice([-2, -1, 1, 2, 3, 4])
                    if str(sai) != kq and str(sai) not in s:
                        s.append('$%s$' % str(sai).replace('.', ','))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi: Tính đạo hàm bằng định nghĩa
                # Sử dụng các lệnh LaTeX cho hàm phân nhánh
                noidungcauhoi = (
                    'Tính đạo hàm bằng định nghĩa của hàm số $f\\left(x\\right) = \\begin{cases} x^2 + %sx + %s & \\text{khi } x \\neq %s \\\\ %s & \\text{khi } x = %s \\end{cases}$ tại điểm $x = %s$.'
                    % (latex(a), latex(b), latex(x0), latex(y0), latex(x0), latex(x0))
                )

                # Xử lý trường hợp hệ số âm/dương để biểu thức đẹp hơn (optional but better)
                noidungcauhoi = noidungcauhoi.replace('+ -', '- ')

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo đúng format trong ảnh
                # Tính tử số: (x^2 + ax + b) - y0 = x^2 + ax + (b - y0)
                c_new = b - y0
                # Phân tích tử số luôn có nghiệm x0: (x - x0)(x - nghiệm_kia)
                # Nghiệm còn lại là: -(a + x0)
                nghiem_kia = -(a + x0)
                tu_so_phantich = '\\left(x - %s\\right)\\left(x %s %s\\right)' % (
                    latex(x0), 
                    '+' if -nghiem_kia >= 0 else '', 
                    latex(-nghiem_kia)
                )
                tu_so_phantich = tu_so_phantich.replace('+ -', '- ')

                loigiai = (
                    'Ta có: $f\\left(%s\\right) = %s$. \\\\ '
                    'Do đó: $\\lim_{x \\to %s} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} '
                    '= \\lim_{x \\to %s} \\frac{x^2 + %sx + %s - \\left(%s\\right)}{x - %s}$ \\\\ '
                    '$= \\lim_{x \\to %s} \\frac{x^2 + %sx %s %s}{x - %s} '
                    '= \\lim_{x \\to %s} \\frac{%s}{x - %s}$ \\\\ '
                    '$= \\lim_{x \\to %s} \\left(x %s %s\\right) = %s$. \\\\ '
                    'Vậy $f\'\\left(%s\\right) = %s$.'
                    % (
                        latex(x0), latex(y0),
                        latex(x0), latex(x0), latex(x0),
                        latex(x0), latex(a), latex(b), latex(y0), latex(x0),
                        latex(x0), latex(a), '+' if c_new >= 0 else '', latex(c_new), latex(x0),
                        latex(x0), tu_so_phantich, latex(x0),
                        latex(x0), '+' if -nghiem_kia >= 0 else '', latex(-nghiem_kia), latex(kq_val),
                        latex(x0), latex(kq_val)
                    )
                )
                loigiai = loigiai.replace('+ -', '- ').replace('  ', ' ')

            # Xuất câu trắc nghiệm theo cấu trúc yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

