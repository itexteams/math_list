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


def bt_dang8_p3_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và sinh dữ liệu ngẫu nhiên (B3)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random biên độ A từ 2 đến 5
                A = random.choice([2, 3, 4, 5])
                # Random hằng số tịnh tiến B (mực nước trung bình)
                B = random.choice([10, 11, 12, 13, 14, 15])

                # Mẫu số của pha ban đầu \pi/m, chọn sao cho nghiệm t là số nguyên đẹp
                # Biểu thức: \pi*t/6 + \pi/m = k*2\pi => t/6 + 1/m = 2k => t = 12k - 6/m
                # Chọn m sao cho 6 chia hết cho m (m có thể là 2, 3, 6)
                m = random.choice([2, 3, 6])
                t_tru = 6 // m

                # Tính toán giá trị k nguyên dương nhỏ nhất sao cho t > 0
                # t = -t_tru + 12k > 0 => 12k > t_tru => k > t_tru / 12
                # Vì t_tru có thể là 1, 2, 3 nên với k = 1 luôn thỏa mãn t > 0
                k_chon = 1
                t_dung = -t_tru + 12 * k_chon

                h_max = A + B
                h_min = B - A

                # Tạo đáp án đúng định dạng chuỗi
                da_text = 't = %s\\text{(h)}' % (latex(t_dung))

                # Tạo danh sách các phương án sai (B4)
                s_vals = []
                fake_offsets = [2, 4, 5, 8, 12, 14, 15, 22]
                for fo in fake_offsets:
                    if fo != t_dung and fo not in s_vals:
                        s_vals.append(fo)

                random.shuffle(s_vals)
                das1 = 't = %s\\text{(h)}' % (latex(s_vals[0]))
                das2 = 't = %s\\text{(h)}' % (latex(s_vals[1]))
                das3 = 'y = %s\\text{(m)}' % (latex(h_max)) # Phương án bẫy giá trị cực đại

                # Định dạng câu hỏi sử dụng %s theo đúng mẫu
                noidungcauhoi = ('''Hằng ngày, mực nước của con kênh lên xuống theo thủy triều. Độ sâu $h\\text{(m)}$ của mực nước trong kênh tính theo thời gian $t\\text{(h)}$ được cho bởi công thức $h = %s \\cos \\left( \\frac{\\pi t}{6} + \\frac{\\pi}{%s} \\right) + %s$. Khi nào mực nước của kênh là cao nhất với thời gian ngắn nhất?'''
                                 %(latex(A), latex(m), latex(B)))

                # Nội dung lời giải chi tiết từng bước
                loigiai = ('''Ta có: $-1 \\le \\cos \\left( \\frac{\\pi t}{6} + \\frac{\\pi}{%s} \\right) \\le 1 \\Leftrightarrow %s \\le h \\le %s$. Do đó mực nước cao nhất của kênh là $%s\\text{m}$ đạt được khi \\\\
                           $\\cos \\left( \\frac{\\pi t}{6} + \\frac{\\pi}{%s} \\right) = 1 \\Leftrightarrow \\frac{\\pi}{6} t + \\frac{\\pi}{%s} = k2\\pi \\Leftrightarrow t = -%s + 12k$.\\\\
                           Vì $t > 0 \\Leftrightarrow -%s + 12k > 0 \\Leftrightarrow k > \\frac{%s}{12}$.\\\\
                           Chọn số $k$ nguyên dương nhỏ nhất thỏa mãn $k > \\frac{%s}{12}$ là $k = 1 \\Rightarrow t = %s$.'''
                           %(latex(m), latex(h_min), latex(h_max), latex(h_max),
                             latex(m), latex(m), latex(t_tru),
                             latex(t_tru), latex(t_tru), latex(t_tru), latex(t_dung)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(t_dung))
                # Các phương án trắc nghiệm không thêm dấu chấm ở cuối
                da_d = ('\\True $' + str(da_text) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Trộn ngẫu nhiên thứ tự các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất chuỗi định dạng cấu trúc mẫu minipage hoàn chỉnh
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

