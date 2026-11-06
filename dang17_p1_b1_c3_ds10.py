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


def bt_dang17_p1_b1_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
             # Hàm hỗ trợ định dạng số, bỏ số 0 thừa ở đuôi và thay dấu . thành ,
             def format_num(d):
                 s = f"{d:f}".rstrip('0').rstrip('.') if '.' in f"{d:f}" else f"{d:f}"
                 return s.replace('.', ',')

             # Random chiều dài và chiều rộng (đảm bảo dài > rộng)
             x_val = random.randint(20, 50)
             y_val = random.randint(10, x_val - 5)

             # Random sai số (ví dụ: 0.01, 0.02, 0.05, 0.1)
             d_val = Decimal(random.choice(['0.01', '0.02', '0.05', '0.1', '0.2']))

             # Tính toán các giá trị cơ bản
             sum_xy = x_val + y_val
             P_base = 2 * sum_xy

             # Sai số đúng của chu vi P = 2*(dx + dy) = 2*(d + d) = 4d
             err_correct = 4 * d_val

             # Các phương án nhiễu theo logic của ảnh (x10, x0.5, x2)
             # A. 0.4 (tức là 4d * 10 = 40d)
             # C. 0.02 (tức là 4d / 2 = 2d)
             # D. 0.08 (tức là 4d * 2 = 8d)
             err_dist1 = 40 * d_val
             err_dist2 = 2 * d_val
             err_dist3 = 8 * d_val

             # Chuyển đổi sang chuỗi tiếng Việt
             x_str = format_num(x_val)
             y_str = format_num(y_val)
             d_str = format_num(d_val)
             P_base_str = format_num(P_base)
             sum_xy_str = format_num(sum_xy)

             # Câu hỏi
             noidungcauhoi = ('''Một cái ruộng hình chữ nhật có chiều dài là $x = %s\\text{m} \\pm %s\\text{m}$ và chiều rộng là $y = %s\\text{m} \\pm %s\\text{m}$. Chu vi của ruộng là'''
                              % (x_str, d_str, y_str, d_str))

             # Các đáp án
             da_d = ('\\True $P = %s\\text{m} \\pm %s\\text{m}$' % (P_base_str, format_num(err_correct)))
             da_s1 = ('$P = %s\\text{m} \\pm %s\\text{m}$' % (P_base_str, format_num(err_dist1)))
             da_s2 = ('$P = %s\\text{m} \\pm %s\\text{m}$' % (P_base_str, format_num(err_dist2))) 
             da_s3 = ('$P = %s\\text{m} \\pm %s\\text{m}$' % (P_base_str, format_num(err_dist3))) 

             # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
             list_1 = [da_d, da_s1, da_s2, da_s3]
             random.shuffle(list_1)

             # Nội dung lời giải
             loigiai=('''Giả sử $x = %s + a, y = %s + b$ với $-%s \\le a, b \\le %s$.\\\\
            Ta có chu vi ruộng là $P = 2(x + y) = 2(%s + a + %s + b) = 2(%s + a + b) = %s + 2(a+b)$.\\\\
            Vì $-%s \\le a, b \\le %s$ nên $-%s \\le 2(a+b) \\le %s$.\\\\
            Do đó $|P - %s| = |2(a+b)| \\le %s$.\\\\
            Vậy $P = %s\\text{m} \\pm %s\\text{m}$.'''
                      % (x_str, y_str, d_str, d_str,
                         x_str, y_str, sum_xy_str, P_base_str,
                         d_str, d_str, format_num(err_correct), format_num(err_correct),
                         P_base_str, format_num(err_correct),
                         P_base_str, format_num(err_correct)))

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

