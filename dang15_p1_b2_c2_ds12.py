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


def bt_dang15_p1_b2_c2_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random khoảng bắt đầu để các khoảng ghép nhóm dịch chuyển (10, 20, 30, 40)
                A_val = random.choice([10, 20, 30, 40])

                # Sử dụng các bộ tần số cho kết quả số nguyên đẹp (Trung bình và Phương sai đều nguyên)
                f_sets = [
                    (8, 18, 24, 10),  # Bộ số liệu gốc (N=60, s2=84)
                    (10, 20, 10, 10), # (N=50, s2=104)
                    (5, 15, 20, 10),  # (N=50, s2=81)
                    (10, 10, 20, 10)  # (N=50, s2=104)
                ]
                f1, f2, f3, f4 = random.choice(f_sets)

                # Các mốc khoảng ghép nhóm
                v1 = A_val
                v2 = A_val + 10
                v3 = A_val + 20
                v4 = A_val + 30
                v5 = A_val + 40

                # Các giá trị đại diện (trung điểm)
                m1 = A_val + 5
                m2 = A_val + 15
                m3 = A_val + 25
                m4 = A_val + 35

                # Tổng số quan sát
                N = f1 + f2 + f3 + f4

                # Tính toán Giá trị trung bình và Phương sai
                x_bar = (f1*m1 + f2*m2 + f3*m3 + f4*m4) // N
                s2 = (f1*(m1 - x_bar)**2 + f2*(m2 - x_bar)**2 + f3*(m3 - x_bar)**2 + f4*(m4 - x_bar)**2) // N

                # Các đáp án trắc nghiệm
                da = "s^2 = %s" % (s2)
                da_d = ('\\True $%s$' % da)

                s_opts = [
                    "s^2 = %s" % (s2 + 1),
                    "s^2 = %s" % (s2 + 2),
                    "s^2 = %s" % (s2 + 3),
                    "s^2 = %s" % (s2 - 1),
                    "s^2 = %s" % (s2 - 2),
                    "s^2 = %s" % (s2 - 3)
                ]

                das1 = random.choice(s_opts)
                s_opts.remove(das1)
                das2 = random.choice(s_opts)
                s_opts.remove(das2)
                das3 = random.choice(s_opts)

                # Các đáp án
                da_s1 = '$%s$' % das1
                da_s2 = '$%s$' % das2
                da_s3 = '$%s$' % das3

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('''Cho bảng phân bố tần số ghép nhóm về độ dài của $%s$ lá dương xỉ trưởng thành như sau:
                    \\begin{center}
                    \\begin{tabular}{|c|c|c|c|c|}
                    \\hline
                    Độ dài (cm) & $[%s;%s)$ & $[%s;%s)$ & $[%s;%s)$ & $[%s;%s]$ \\\\
                    \\hline
                    Tần số & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                    \\hline
                    \\end{tabular}
                    \\end{center}
                    Phương sai của mẫu số liệu ghép nhóm là'''
                    % (latex(N), latex(v1), latex(v2), latex(v2), latex(v3), latex(v3), latex(v4), latex(v4), latex(v5),
                       latex(f1), latex(f2), latex(f3), latex(f4)))

                # Nội dung lời giải
                loigiai = ('''Ta viết lại bảng trên có bổ sung giá trị đại diện:
                    \\begin{center}
                    \\begin{tabular}{|c|c|c|c|c|}
                    \\hline
                    Độ dài (cm) & $[%s;%s)$ & $[%s;%s)$ & $[%s;%s)$ & $[%s;%s]$ \\\\
                    \\hline
                    Giá trị đại diện & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                    \\hline
                    Tần số & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                    \\hline
                    \\end{tabular}
                    \\end{center}
                    Giá trị trung bình của mẫu số liệu ghép nhóm: $\\overline{x} = \\frac{%s \\cdot %s + %s \\cdot %s + %s \\cdot %s + %s \\cdot %s}{%s} = %s$.\\\\
                    Phương sai mẫu số liệu ghép nhóm là:
                    $$s^2 = \\frac{%s \\cdot (%s - %s)^2 + %s \\cdot (%s - %s)^2 + %s \\cdot (%s - %s)^2 + %s \\cdot (%s - %s)^2}{%s} = %s.$$'''
                    % (latex(v1), latex(v2), latex(v2), latex(v3), latex(v3), latex(v4), latex(v4), latex(v5),
                       latex(m1), latex(m2), latex(m3), latex(m4),
                       latex(f1), latex(f2), latex(f3), latex(f4),
                       latex(m1), latex(f1), latex(m2), latex(f2), latex(m3), latex(f3), latex(m4), latex(f4), latex(N), latex(x_bar),
                       latex(f1), latex(m1), latex(x_bar), latex(f2), latex(m2), latex(x_bar), latex(f3), latex(m3), latex(x_bar), latex(f4), latex(m4), latex(x_bar), latex(N), latex(s2)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

