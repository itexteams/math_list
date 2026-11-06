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


def bt_dang34_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn ngẫu nhiên mẫu số n là số lẻ (5, 7, hoặc 9)
                # Bài mẫu gốc là n = 7
                n = random.choice([5, 7, 9])

                # Số lượng số hạng trong tổng: (n - 1) / 2
                num_terms = (n - 1) // 2

                # Tính giá trị chính xác của tổng bằng SymPy
                # Tổng cos(2k*pi / n) từ k=1 đến num_terms luôn bằng -1/2
                val_kq = Rational(-1, 2)

                # Đáp án đúng
                da = '$%s$' % (latex(val_kq))

                # Tạo các phương án sai ngẫu nhiên
                s = [
                    '$\\frac{1}{2}$',
                    '$\\frac{1}{4}$',
                    '$-\\frac{1}{4}$',
                    '$1$',
                    '$-1$',
                    '$0$'
                ]
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Xây dựng chuỗi câu hỏi cho đề bài
                chuoi_ch = []
                for k in range(1, num_terms + 1):
                    chuoi_ch.append('\\cos \\frac{%s\\pi}{%s}' % (str(2 * k), str(n)))
                noidungcauhoi = ('Tính giá trị của $' + ' + '.join(chuoi_ch) + '$.')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xây dựng các bước giải chi tiết động theo tham số n để khớp hoàn toàn cấu trúc ảnh gốc
                bieuthuc_goc = ' + '.join(chuoi_ch)

                chuoi_tuso_1 = ' \\cdot \\left(' + bieuthuc_goc + '\\right)'

                # Biến đổi tích thành tổng: sin(pi/n)cos(2k*pi/n) = 1/2 * [sin((2k+1)pi/n) + sin((1-2k)pi/n)]
                chuoi_buoc_2 = []
                for k in range(1, num_terms + 1):
                    tu_so_1 = 2 * k + 1
                    tu_so_2 = 1 - 2 * k
                    if tu_so_2 < 0:
                        chuoi_buoc_2.append('\\sin \\frac{%s\\pi}{%s} + \\sin \\left(-\\frac{%s\\pi}{%s}\\right)' % (str(tu_so_1), str(n), str(abs(tu_so_2)), str(n)))
                    else:
                        chuoi_buoc_2.append('\\sin \\frac{%s\\pi}{%s} + \\sin \\frac{%s\\pi}{%s}' % (str(tu_so_1), str(n), str(tu_so_2), str(n)))

                chuoi_tuso_2 = ' + '.join(chuoi_buoc_2)

                # Sau khi triệt tiêu đại số, tử số cuối cùng còn lại sin(-pi/n) hoặc tương đương
                tu_cuoi = 1 - 2 * num_terms
                chuoi_tuso_3 = '\\sin \\left(-\\frac{%s\\pi}{%s}\\right)' % (str(abs(tu_cuoi)), str(n))

                # Nội dung lời giải hoàn chỉnh từng bước
                loigiai = ('''Ta có $%s = \\frac{\\sin \\frac{\\pi}{%s}%s}{\\sin \\frac{\\pi}{%s}}$ \\\\
            = $\\frac{%s}{2\\sin \\frac{\\pi}{%s}} = \\frac{%s}{2\\sin \\frac{\\pi}{%s}} = -\\frac{1}{2}$.'''
                           % (bieuthuc_goc, str(n), chuoi_tuso_1, str(n), chuoi_tuso_2, str(n), chuoi_tuso_3, str(n)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

