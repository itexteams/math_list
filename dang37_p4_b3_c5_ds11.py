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


def bt_dang37_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # A: Số người nhiễm ban đầu
                # r: Số người bị lây từ 1 người sau 1 ngày
                # n: Số ngày khảo sát
                A = random.randint(1, 3) 
                r = random.randint(3, 6)
                n = random.randint(5, 8)

                # Tính toán kết quả
                # Tổng số người sau n ngày là A * (1 + r)^n
                growth_factor = 1 + r
                kq_val = A * (growth_factor**n)

                # Đáp án đúng
                da = '$%s$' % (latex(kq_val))

                # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    # Tạo các phương án sai dựa trên các lỗi logic phổ biến
                    wrong1 = A * (r**n) # Quên cộng 1 vào hệ số lây nhiễm
                    wrong2 = A * (growth_factor**(n-1)) # Nhầm số ngày
                    wrong3 = (A + r)**n # Nhầm công thức
                    wrong4 = kq_val + random.randint(100, 1000)
                    wrong5 = kq_val - random.randint(100, 1000)

                    candidates = [wrong1, wrong2, wrong3, wrong4, wrong5]
                    choice = random.choice(candidates)

                    if choice != kq_val and choice > 0:
                        s.add('$%s$' % (latex(choice)))

                s_list = list(s)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # B2: Viết lại bài toán theo mẫu code python
                # Câu hỏi
                noidungcauhoi = (r'''Giả sử ban đầu có $%s$ người bị nhiễm bệnh COVID-19 và cứ sau $1$ ngày sẽ lây sang $%s$ người khác. Tất cả những người nhiễm bệnh lại tiếp tục lây sang những người khác với tốc độ như trên ($1$ người lây $%s$ người). Hỏi sau $%s$ ngày sẽ có tổng cộng bao nhiêu người nhiễm bệnh? (Biết rằng những người nhiễm bệnh không phát hiện bản thân bị bệnh và không phòng tránh cách ly).'''
                                % (latex(A), latex(r), latex(r), latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Sau $1$ ngày, tổng số người nhiễm bệnh là $%s + %s \cdot %s = %s(1 + %s) = %s \cdot %s$ người. \\
                            Sau $2$ ngày, tổng số người nhiễm bệnh là $%s \cdot %s + (%s \cdot %s) \cdot %s = %s \cdot %s^2$ người. \\
                            Tổng quát, sau $%s$ ngày, tổng số người nhiễm bệnh là $%s(1 + %s)^{%s} = %s$ người. \\
                            Ngoài ra chúng ta có thể áp dụng công thức lãi kép để tính nhanh: \\
                            $S_{n} = A(1 + r)^n = %s(1 + %s)^{%s} = %s$, với $A = %s, r = %s, n = %s$.'''
                          % (latex(A), latex(A), latex(r), latex(A), latex(r), latex(A), latex(growth_factor),
                             latex(A), latex(growth_factor), latex(A), latex(growth_factor), latex(r), latex(A), latex(growth_factor),
                             latex(n), latex(A), latex(r), latex(n), latex(kq_val),
                             latex(A), latex(r), latex(n), latex(kq_val), latex(A), latex(r), latex(n)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

