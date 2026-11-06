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


def bt_dang34_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # f(x) = (a*x) / (b + |x|) -> f'(0) = a/b
                a = randint(2, 9)
                b = randint(1, 4)

                # Tính toán kết quả đúng
                ket_qua = Rational(a, b)

                # Hàm hỗ trợ định dạng latex chuẩn Việt Nam
                def format_latex(expr):
                    return latex(expr).replace('.', ',')

                # Các đáp án trắc nghiệm
                da_dung_str = '$f\'\\left(0\\right) = %s$' % format_latex(ket_qua)

                # Tạo danh sách các giá trị nhiễu (Sửa lỗi typo ở đây)
                nhieu_list = [
                    0, 
                    1, 
                    Rational(b, a), 
                    a + b, 
                    a,
                    b
                ]
                # Lọc bỏ giá trị trùng với đáp án đúng
                nhieu_list = [val for val in nhieu_list if val != ket_qua]

                # Lấy ngẫu nhiên 3 giá trị từ danh sách nhiễu đã lọc
                ds_nhieu = random.sample(nhieu_list, 3)

                da_s1_val = ds_nhieu[0]
                da_s2_val = ds_nhieu[1]
                da_s3_val = ds_nhieu[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f\\left(x\\right) = \\frac{%sx}{%s + \\left|x\\right|}$. Giá trị của $f\'\\left(0\\right)$ bằng'''
                                 % (latex(a), latex(b)))

                # Các đáp án
                da_d = ('\\True ' + da_dung_str)
                da_s1 = '$f\'\\left(0\\right) = %s$' % format_latex(da_s1_val)
                da_s2 = '$f\'\\left(0\\right) = %s$' % format_latex(da_s2_val)
                da_s3 = '$f\'\\left(0\\right) = %s$' % format_latex(da_s3_val)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: $f\'\\left(0\\right) = \\lim_{x \\to 0} \\frac{f\\left(x\\right) - f\\left(0\\right)}{x} = \\lim_{x \\to 0} \\frac{%s}{%s + \\left|x\\right|}$. \\\\
                             Mà $\\lim_{x \\to 0^+} \\frac{%s}{%s + \\left|x\\right|} = \\lim_{x \\to 0^+} \\frac{%s}{%s + x} = %s$; \\\\
                             $\\lim_{x \\to 0^-} \\frac{%s}{%s + \\left|x\\right|} = \\lim_{x \\to 0^-} \\frac{%s}{%s - x} = %s$. \\\\
                             $\\Rightarrow \\lim_{x \\to 0^+} \\frac{%s}{%s + \\left|x\\right|} = \\lim_{x \\to 0^-} \\frac{%s}{%s + \\left|x\\right|} = %s$ \\\\
                             $\\Rightarrow f\'\\left(0\\right) = \\lim_{x \\to 0} \\frac{%s}{%s + \\left|x\\right|} = %s$. \\\\
                             Kết luận: $f\'\\left(0\\right) = %s$.'''
                           % (latex(a), latex(b), 
                              latex(a), latex(b), latex(a), latex(b), format_latex(ket_qua),
                              latex(a), latex(b), latex(a), latex(b), format_latex(ket_qua),
                              latex(a), latex(b), latex(a), latex(b), format_latex(ket_qua),
                              latex(a), latex(b), format_latex(ket_qua), format_latex(ket_qua)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

