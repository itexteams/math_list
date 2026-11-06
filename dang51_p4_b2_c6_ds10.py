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


def bt_dang51_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (giữ cấu trúc lisdang của mẫu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các số liệu của bài toán
                # n1: bi đỏ, n2: bi xanh, n3: bi vàng
                n1 = randint(3, 5) 
                n2 = randint(5, 7)
                n3 = randint(6, 9)
                tong_bi = n1 + n2 + n3
                so_chon = 3

                # Tính toán các giá trị
                # Số phần tử không gian mẫu n(Omega)
                n_omega = int(binomial(tong_bi, so_chon))

                # Biến cố đối A_gach: 3 viên có đủ 3 màu (1 đỏ, 1 xanh, 1 vàng)
                n_A_bar = n1 * n2 * n3

                # Xác suất biến cố đối P(A_bar)
                p_A_bar = Rational(n_A_bar, n_omega)

                # Xác suất cần tìm P(A) = 1 - P(A_bar)
                p_A = 1 - p_A_bar

                # Đáp án đúng
                da = '$' + latex(p_A) + '$'

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                # Phương án sai 1: Xác suất của biến cố đối
                s.append('$' + latex(p_A_bar) + '$')
                # Phương án sai 2: Nhầm lẫn cách tính (ví dụ 1/n_omega hoặc các giá trị thường gặp)
                s.append('$\\frac{1}{' + str(n_omega // 2 if n_omega % 2 == 0 else n_omega) + '}$')
                s.append('$\\frac{1}{' + str(n_omega + randint(10, 50)) + '}$')

                # Kiểm tra loại bỏ trùng lặp và trùng đáp án đúng
                s = list(set(s))
                if da in s:
                    s.remove(da)
                while len(s) < 3:
                    random_val = Rational(randint(1, n_omega-1), n_omega)
                    val_str = '$' + latex(random_val) + '$'
                    if val_str != da and val_str not in s:
                        s.append(val_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2 - Viết lại nội dung từ ảnh)
                noidungcauhoi = ('''Một túi chứa $%s$ viên bi đỏ, $%s$ viên bi xanh và $%s$ viên bi vàng. Chọn ngẫu nhiên $%s$ viên bi. Tính xác suất để $%s$ viên bi được chọn không có đủ cả ba màu.'''
                                 % (latex(n1), latex(n2), latex(n3), latex(so_chon), latex(so_chon)))

                # Đáp án đúng có tiền tố \True
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2 - Giống hệt cấu trúc ảnh)
                loigiai = ('''Gọi $A$ là biến cố " $%s$ viên bi được chọn không có đủ cả ba màu". \\\\
                             Biến cố đối của $A$ là $\\overline{A}$: " $%s$ viên bi được chọn có đủ cả ba màu". \\\\
                             Số phần tử của không gian mẫu: $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\
                             Số kết quả thuận lợi cho biến cố $\\overline{A}$ là $n\\left(\\overline{A}\\right) = %s \\cdot %s \\cdot %s = %s$. \\\\
                             Xác suất của $\\overline{A}$ là $P\\left(\\overline{A}\\right) = \\frac{n\\left(\\overline{A}\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$. \\\\
                             Xác suất cần tìm là $P\\left(A\\right) = 1 - P\\left(\\overline{A}\\right) = 1 - %s = %s$.'''
                           % (latex(so_chon), latex(so_chon), 
                              latex(tong_bi), latex(so_chon), latex(n_omega),
                              latex(n1), latex(n2), latex(n3), latex(n_A_bar),
                              latex(n_A_bar), latex(n_omega), latex(p_A_bar),
                              latex(p_A_bar), latex(p_A)
                              ))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

