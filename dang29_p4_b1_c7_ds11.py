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


def bt_dang29_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random điểm x0 (chọn các giá trị nguyên khác 0, -1 để mẫu số đẹp và không quá đơn giản)
                x0_val = random.choice([-4, -3, -2, 1, 2, 3])

                # f(x) = 1 / (x^2 + x + 1)
                # Tính f(x0)
                d0 = x0_val**2 + x0_val + 1 # Giá trị mẫu số tại x0

                # Biểu thức f(x) - f(x0) = 1/(x^2+x+1) - 1/d0
                # f(x) - f(x0) = (d0 - (x^2 + x + 1)) / (d0 * (x^2 + x + 1))
                # Tử số: -x^2 - x + (d0 - 1)
                # Vì d0 = x0^2 + x0 + 1 nên d0 - 1 = x0^2 + x0
                # Tử số = -x^2 - x + x0^2 + x0 = -(x^2 - x0^2) - (x - x0) = -(x-x0)(x+x0) - (x-x0) = -(x-x0)(x + x0 + 1)

                v_phu = x0_val + 1 # Giá trị (x0 + 1) dùng trong phân tích (x - x0)(x + x0 + 1)

                # Tính đạo hàm f'(x0) = -(2*x0 + 1) / (x0^2 + x0 + 1)^2
                tu_kq = -(2 * x0_val + 1)
                mau_kq = d0**2
                kq_final = Rational(tu_kq, mau_kq)

                # Đáp án đúng
                da = '$%s$' % (latex(kq_final))

                # Tạo các đáp án sai
                s = [
                    '$%s$' % (latex(Rational(-tu_kq, mau_kq))),
                    '$%s$' % (latex(Rational(tu_kq + 1, mau_kq))),
                    '$%s$' % (latex(Rational(tu_kq, d0))),
                    '$%s$' % (latex(Rational(1, d0))),
                    '$%s$' % (latex(Rational(-1, d0))),
                    '$%s$' % (latex(Rational(2 * x0_val, mau_kq)))
                ]

                # Loại bỏ đáp án đúng nếu lỡ trùng trong danh sách sai
                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tính đạo hàm bằng định nghĩa của hàm số $y = f\\left(x\\right) = \\frac{1}{x^2 + x + 1}$ tại điểm $x_0 = %s$.'''
                                 % (latex(x0_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu ảnh
                # Phân tích tử số: -x^2 - x + (d0-1) = -(x - x0)(x + x0 + 1)
                # Trong ảnh x0 = -2, tử số là -(x-1)(x+2) -> v_phu = -2+1 = -1 -> -(x - (-1))(x+2) = -(x+1)(x+2)
                # Lưu ý: Trong ảnh là -(x-1)(x+2). Với x0 = -2, (x-x0) = (x+2). (x+x0+1) = (x-2+1) = (x-1). Đúng.

                loigiai = ('''Tại $x_0 = %s$ ta có: \\\\
                             $f\\left(x\\right) - f\\left(x_0\\right) = f\\left(x\\right) - f\\left(%s\\right)$ \\\\
                             $= \\frac{1}{x^2 + x + 1} - \\frac{1}{%s} = \\frac{1}{%s} \\cdot \\frac{%s - x^2 - x - 1}{x^2 + x + 1} = \\frac{1}{%s} \\cdot \\frac{-x^2 - x + %s}{x^2 + x + 1} = -\\frac{1}{%s} \\cdot \\frac{\\left(x - %s\\right)\\left(x - %s\\right)}{x^2 + x + 1}$. \\\\
                             Suy ra: \\\\
                             $\\frac{f\\left(x\\right) - f\\left(x_0\\right)}{x - x_0} = \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = -\\frac{1}{%s} \\cdot \\frac{\\left(x - %s\\right)\\left(x - %s\\right)}{x^2 + x + 1} \\cdot \\frac{1}{x - %s} = -\\frac{1}{%s} \\cdot \\frac{x - %s}{x^2 + x + 1}$. \\\\
                             Vậy: \\\\
                             $f'\\left(%s\\right) = \\lim_{x \\to %s} \\frac{f\\left(x\\right) - f\\left(x_0\\right)}{x - x_0} = \\lim_{x \\to %s} \\left[ -\\frac{1}{%s} \\cdot \\frac{x - %s}{x^2 + x + 1} \\right] = -\\frac{1}{%s} \\cdot \\frac{%s - %s}{%s^2 + %s + 1} = %s$.'''
                           % (latex(x0_val), latex(x0_val),
                              latex(d0), latex(d0), latex(d0), 
                              latex(d0), latex(d0 - 1), 
                              latex(d0), latex(v_phu), latex(x0_val),
                              latex(x0_val), latex(x0_val),
                              latex(d0), latex(v_phu), latex(x0_val), latex(x0_val),
                              latex(d0), latex(v_phu),
                              latex(x0_val), latex(x0_val), latex(x0_val),
                              latex(d0), latex(v_phu),
                              latex(d0), latex(x0_val), latex(v_phu), latex(x0_val), latex(x0_val),
                              latex(kq_final)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

