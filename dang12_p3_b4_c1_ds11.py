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


def bt_dang12_p3_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random năm N hoặc hằng số N trong đoạn [-N*pi; N*pi]
                # Bài mẫu gốc N = 2018
                N = random.choice([2018, 2024, 2025, 2026])

                # Tính số lượng giá trị k nguyên thỏa mãn: -N*pi <= k*pi/2 <= N*pi <=> -2N <= k <= 2N
                # Số lượng giá trị k là: 2*N - (-2*N) + 1 = 4*N + 1
                count_k = 4 * N + 1

                # Tính số lượng giá trị m nguyên thỏa mãn: -N*pi <= 5*pi/6 + m*pi <= N*pi <=> -N - 5/6 <= m <= N - 5/6
                # Do đó, m chạy từ -N-1 đến N-1. Số lượng m là: (N-1) - (-N-1) + 1 = 2*N
                count_m = 2 * N

                # Tính số lượng giá trị n nguyên thỏa mãn: -N*pi <= pi/6 + n*pi <= N*pi <=> -N - 1/6 <= n <= N - 1/6
                # Do đó, n chạy từ -N đến N-1. Số lượng n là: (N-1) - (-N) + 1 = 2*N
                count_n = 2 * N

                # Tổng số nghiệm phân biệt là tổng số lượng các số nguyên k, m, n
                kq_num = count_k + count_m + count_n
                kq = str(kq_num)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai không trùng với đáp án đúng
                s = [
                    '$%s$' % (kq_num - 1),
                    '$%s$' % (kq_num - 2),
                    '$%s$' % (kq_num - 4),
                    '$%s$' % (4 * N + 1),
                    '$%s$' % (4 * N + 3)
                ]

                # Lọc bỏ giá trị trùng nếu có (đảm bảo an toàn)
                s = [item for item in s if item != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Số nghiệm của phương trình $\\sin 5x-\\sin x=0$ thuộc đoạn $\\left[ -%s\\pi ;%s\\pi  \\right]$ là bao nhiêu?'''
                                 %(latex(N), latex(N)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các giá trị phân số trong phần biện luận hệ bất phương trình của lời giải
                m_left_tu = -6 * N - 5
                m_right_tu = 6 * N - 5
                n_left_tu = -6 * N - 1
                n_right_tu = 6 * N - 1

                # Nội dung lời giải chi tiết theo đúng cấu trúc từng bước của ảnh gốc
                loigiai = ('''Ta có \\\\
                           $\\sin 5x-\\sin x=0 \\Leftrightarrow \\sin 5x=\\sin x \\Leftrightarrow \\left[ \\begin{aligned} & 5x=x+k2\\pi  \\\\ & 5x=\\pi -x+k2\\pi  \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x=k\\frac{\\pi }{2} \\\\ & x=\\frac{\\pi }{6}+k\\frac{\\pi }{3} \\end{aligned} \\right.$ \\\\
                           $\\Leftrightarrow \\left[ \\begin{aligned} & x=k\\frac{\\pi }{2} & \\left( k\\in \\mathbb{Z} \\right) \\\\ & x=\\frac{5\\pi }{6}+m\\pi  & \\left( m\\in \\mathbb{Z} \\right) \\\\ & x=\\frac{\\pi }{6}+n\\pi  & \\left( n\\in \\mathbb{Z} \\right) \\end{aligned} \\right.$. \\\\
                           Vì $x\\in \\left[ -%s\\pi ;%s\\pi  \\right]$ nên $\\left[ \\begin{aligned} & -%s\\pi \\le k\\frac{\\pi }{2}\\le %s\\pi  \\\\ & -%s\\pi \\le \\frac{5\\pi }{6}+m\\pi \\le %s\\pi  \\\\ & -%s\\pi \\le \\frac{\\pi }{6}+n\\pi \\le %s\\pi  \\end{aligned} \\right. \\Leftrightarrow \\left\\{ \\begin{aligned} & -%s\\le k\\le %s \\\\ & \\frac{%s}{6}\\le m\\le \\frac{%s}{6} \\\\ & \\frac{%s}{6}\\le n\\le \\frac{%s}{6} \\end{aligned} \\right.$. \\\\
                           Do đó có $%s$ giá trị $k$, $%s$ giá trị $m$, $%s$ giá trị $n$, suy ra số nghiệm cần tìm là $%s$ nghiệm.'''
                           %(latex(N), latex(N), 
                             latex(N), latex(N), latex(N), latex(N), latex(N), latex(N),
                             latex(2*N), latex(2*N), latex(m_left_tu), latex(m_right_tu), latex(n_left_tu), latex(n_right_tu),
                             latex(count_k), latex(count_m), latex(count_n), latex(kq_num)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))                                                                                                                                                                                                                                                                                                                          
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

