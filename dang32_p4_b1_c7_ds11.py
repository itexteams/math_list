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


def bt_dang32_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số a (trước x^3) và b (trước x^2)
                # Trong ảnh gốc a=1, b=1
                a = randint(1, 5)
                b = randint(1, 8)

                # Hàm số f(x) khi x != 0
                f_expr = (sqrt(a*x**3 + b*x**2 + 1) - 1) / x


                kq_value = Rational(b, 2)
                kq_latex = latex(kq_value).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_latex)]
                da = random.choice(du)

                # Tạo danh sách các phương án sai (không trùng đáp án đúng)
                s_list = []
                potential_wrongs = [
                    Rational(b, 1), 
                    Rational(b, 4), 
                    Rational(a + b, 2), 
                    Rational(a, 2), 
                    Rational(1, 2), 
                    Integer(0), 
                    Integer(b + 1)
                ]

                for val in potential_wrongs:
                    val_latex = '$%s$' % (latex(val).replace('.', ','))
                    if val_latex != da and val_latex not in s_list:
                        s_list.append(val_latex)

                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                # f(x) được viết dưới dạng piecewise (hàm phân nhánh)
                noidungcauhoi = (
                    'Tính đạo hàm bằng định nghĩa của hàm số '
                    '$f\\left(x\\right) = \\begin{cases} \\frac{\\sqrt{%s x^3 + %s x^2 + 1} - 1}{x} & \\text{khi } x \\neq 0 \\\\ 0 & \\text{khi } x = 0 \\end{cases}$ '
                    'tại điểm $x = 0$.'
                    % (latex(a) if a != 1 else '', latex(b) if b != 1 else '')
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo hình ảnh
                # Biểu thức tử số sau khi rút gọn x^2: ax + b
                tu_rut_gon = a*x + b
                mau_rut_gon = sqrt(a*x**3 + b*x**2 + 1) + 1

                loigiai = (
                    'Ta có $f\\left(0\\right) = 0$.\\\\ '
                    'Do đó: $\\lim_{x \\to 0} \\frac{f\\left(x\\right) - f\\left(0\\right)}{x} '
                    '= \\lim_{x \\to 0} \\frac{\\sqrt{%s x^3 + %s x^2 + 1} - 1}{x^2} '
                    '= \\lim_{x \\to 0} \\frac{%s x^3 + %s x^2}{x^2 \\left(\\sqrt{%s x^3 + %s x^2 + 1} + 1\\right)} \\\\ '
                    '= \\lim_{x \\to 0} \\frac{%s x + %s}{\\sqrt{%s x^3 + %s x^2 + 1} + 1} '
                    '= \\frac{%s}{2} = %s$.\\\\ '
                    'Vậy $f\'\\left(0\\right) = %s$.'
                    % (
                        latex(a) if a != 1 else '', latex(b) if b != 1 else '',
                        latex(a) if a != 1 else '', latex(b) if b != 1 else '',
                        latex(a) if a != 1 else '', latex(b) if b != 1 else '',
                        latex(a) if a != 1 else '', latex(b),
                        latex(a) if a != 1 else '', latex(b) if b != 1 else '',
                        latex(b), kq_latex,
                        kq_latex
                    )
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

