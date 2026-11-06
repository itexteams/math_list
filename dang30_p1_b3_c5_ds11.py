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


def bt_dang30_p1_b3_c5_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random khoảng (A; B)
                # Để bài toán có nghiệm nguyên dương, ta chọn A từ 2 đến 6
                A = random.randint(2, 6)
                # Chọn B sao cho B > A. Để số nghiệm không quá lớn, chọn B gần A
                B = A + random.randint(1, 3)

                # Các hệ số trong căn: cm + d - x
                c = 2
                d = 1
                # Cơ số logarit (không ảnh hưởng kết quả nhưng làm đẹp đề)
                coso = random.choice([2, 3, 5])

                # Giải điều kiện:
                # 1. m <= A
                # 2. cm + d >= B  => m >= (B - d) / c

                low_bound = math.ceil((B - d) / c)
                up_bound = A

                # Tìm danh sách các giá trị m nguyên dương
                list_m = [m for m in range(low_bound, up_bound + 1) if m > 0]
                kq_num = len(list_m)

                # --- BƯỚC 4: ĐIỀU CHỈNH ĐÁP ÁN SAI ---
                # Đáp án đúng
                da_d_val = str(kq_num)

                # Tạo danh sách đáp án nhiễu (không trùng đáp án đúng)
                s_options = set()
                while len(s_options) < 3:
                    # Tạo các số quanh đáp án đúng, đảm bảo >= 0
                    wrong = kq_num + random.choice([-2, -1, 1, 2, 3])
                    if wrong >= 0 and str(wrong) != da_d_val:
                        s_options.add(str(wrong))

                list_s_options = list(s_options)

                # Câu hỏi
                noidungcauhoi = ('''Có tất cả bao nhiêu giá trị nguyên dương của tham số $m$ để hàm số 
            $y = \\frac{1}{\\sqrt{%sm+%s-x}} + \\log_{%s} \\sqrt{x-m}$ xác định trên khoảng $(%s;%s)$?'''
                                 % (latex(c), latex(d), latex(coso), latex(A), latex(B)))

                # Các đáp án
                da_d = ('\\True $' + da_d_val + '$')
                da_s1 = '$' + list_s_options[0] + '$'
                da_s2 = '$' + list_s_options[1] + '$'
                da_s3 = '$' + list_s_options[2] + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                if len(list_m) > 0:
                    chuoi_m = "m \\in \\{" + "; ".join(map(str, list_m)) + "\\}"
                else:
                    chuoi_m = "m \\in \\emptyset"

                loigiai = ('''Hàm số xác định $\\Leftrightarrow \\begin{cases} %sm+%s-x > 0 \\\\ x-m > 0 \\end{cases} 
            \\Leftrightarrow \\begin{cases} x < %sm+%s \\\\ x > m \\end{cases} \\Rightarrow D = (m; %sm+%s)$. \\\\
            Hàm số đã cho xác định trên khoảng $(%s;%s)$ nên $(%s;%s) \\subset D = (m; %sm+%s) \\Leftrightarrow \\begin{cases} m \\le %s \\\\ %sm+%s \\ge %s \\end{cases}$ \\\\
            $\\Leftrightarrow \\begin{cases} m \\le %s \\\\ %sm \\ge %s \\end{cases} \\Leftrightarrow %s \\le m \\le %s$. \\\\
            Vì $m$ nguyên dương nên $%s$. Vậy có $%s$ giá trị.'''
                           % (latex(c), latex(d), latex(c), latex(d), latex(c), latex(d),
                              latex(A), latex(B), latex(A), latex(B), latex(c), latex(d),
                              latex(A), latex(c), latex(d), latex(B),
                              latex(A), latex(c), latex(B-d),
                              latex(low_bound), latex(up_bound),
                              chuoi_m, latex(kq_num)
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

