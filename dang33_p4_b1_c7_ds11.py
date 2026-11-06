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


def bt_dang33_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Tìm cách random bài toán
                # Giả sử hàm số có dạng (x^2 - m^2)/(x - m) tại x khác m
                m = random.randint(1, 10)
                m2 = m**2
                # Để hàm số có đạo hàm, trước hết nó phải liên tục
                # lim (x->m) (x^2 - m^2)/(x - m) = lim (x->m) (x + m) = 2m
                # Vậy a = 2m
                correct_a = 2 * m

                # Định dạng số thập phân và thay dấu chấm bằng dấu phẩy
                def format_math(val):
                    return str(latex(val)).replace('.', ',')

                # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                kq = format_math(correct_a)

                # Tạo danh sách các đáp án sai
                s_vals = []
                candidates = [m, m2, m + 1, m - 1, 2 * m + 1, 2 * m - 1, 0, -m]
                for val in candidates:
                    if val != correct_a and val not in s_vals:
                        s_vals.append(val)

                random.shuffle(s_vals)

                # Lấy 3 đáp án sai đầu tiên
                das1_val = s_vals[0]
                das2_val = s_vals[1]
                das3_val = s_vals[2]

                # Các đáp án trắc nghiệm
                da = '$%s$' % kq
                das1 = '$%s$' % format_math(das1_val)
                das2 = '$%s$' % format_math(das2_val)
                das3 = '$%s$' % format_math(das3_val)

                # Câu hỏi (B2: Viết lại y hệt nội dung bài toán)
                # Sử dụng \left( \right) theo yêu cầu
                noidungcauhoi = ('''Tìm $a$ để hàm số $f\\left(x\\right) = \\begin{cases} \\frac{x^2 - %s}{x - %s} & \\text{ khi } x \\neq %s \\\\ a & \\text{ khi } x = %s \\end{cases}$ có đạo hàm tại $x = %s$'''
                                 % (format_math(m2), format_math(m), format_math(m), format_math(m), format_math(m)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Chi tiết, không viết tắt, giống ảnh)
                loigiai = ('''Để hàm số có đạo hàm tại $x = %s$ thì trước hết $f\\left(x\\right)$ phải liên tục tại $x = %s$ \\\\
            Hay $\\lim_{x \\to %s} f\\left(x\\right) = \\lim_{x \\to %s} \\frac{x^2 - %s}{x - %s} = %s = f\\left(%s\\right) = a$ \\\\
            Khi đó, ta có: $\\lim_{x \\to %s} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = \\lim_{x \\to %s} \\frac{\\frac{x^2 - %s}{x - %s} - %s}{x - %s} = 1$. \\\\
            Vậy $a = %s$ là giá trị cần tìm.'''
                           % (format_math(m), format_math(m), 
                              format_math(m), format_math(m), format_math(m2), format_math(m), format_math(correct_a), format_math(m),
                              format_math(m), format_math(m), format_math(m), format_math(m), format_math(m2), format_math(m), format_math(correct_a), format_math(m),
                              format_math(correct_a)))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

