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


def bt_dang16_p4_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Số lượng bi xanh (b), đỏ (d), vàng (v)
                b = randint(4, 7)
                d = randint(3, 5)
                v = randint(2, 4)
                tong = b + d + v

                # Tính toán các giá trị tổ hợp C(n, k)
                def tinh_C(n, k):
                    return math.comb(n, k)

                omega = tinh_C(tong, 2)
                c_b = tinh_C(b, 2)
                c_d = tinh_C(d, 2)
                c_v = tinh_C(v, 2)

                tu_so = c_b + c_d + c_v
                kq_phanso = Rational(tu_so, omega)

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                da = '$%s$' % (latex(kq_phanso))

                s = set()
                while len(s) < 3:
                    # Tạo các phương án sai bằng cách thay đổi tử số hoặc dùng các giá trị ngẫu nhiên
                    sai_tu = randint(1, omega - 1)
                    if sai_tu != tu_so:
                        phanso_sai = Rational(sai_tu, omega)
                        s.add('$%s$' % (latex(phanso_sai)))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi (B2 - Viết lại y hệt đề bài)
                noidungcauhoi = ('''Một hộp đựng $%s$ viên bi xanh, $%s$ viên bi đỏ và $%s$ viên bi vàng. Chọn ngẫu nhiên hai viên bi. Tính xác suất để chọn được hai viên bi cùng màu.'''
                                 % (latex(b), latex(d), latex(v)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2 - Viết lại chi tiết, không viết tắt)
                # Sử dụng ký hiệu tổ hợp C theo đúng định dạng ảnh
                comb_tong = 'C_{%s}^2' % (tong)
                comb_b = 'C_{%s}^2' % (b)
                comb_d = 'C_{%s}^2' % (d)
                comb_v = 'C_{%s}^2' % (v)

                loigiai = ('''Gọi $A$ là biến cố: "Chọn được hai viên bi xanh". \\\\
                           $B$ là biến cố: "Chọn được hai viên bi đỏ". \\\\
                           $C$ là biến cố: "Chọn được hai viên bi vàng". \\\\
                           Khi đó biến cố: "Chọn được hai viên bi cùng màu" là biến cố $A \\cup B \\cup C$. Do $A, B, C$ đôi một xung khắc với nhau nên theo quy tắc cộng ta có $P\\left( A \\cup B \\cup C \\right) = P\\left( A \\right) + P\\left( B \\right) + P\\left( C \\right)$. \\\\
                           Ta có $P\\left( A \\right) = \\frac{%s}{%s} = \\frac{%s}{%s}; P\\left( B \\right) = \\frac{%s}{%s} = \\frac{%s}{%s}; P\\left( C \\right) = \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
                           Vậy $P\\left( A \\cup B \\cup C \\right) = \\frac{%s}{%s} + \\frac{%s}{%s} + \\frac{%s}{%s} = \\frac{%s}{%s}$.'''
                           % (comb_b, comb_tong, latex(c_b), latex(omega),
                              comb_d, comb_tong, latex(c_d), latex(omega),
                              comb_v, comb_tong, latex(c_v), latex(omega),
                              latex(c_b), latex(omega), latex(c_d), latex(omega), latex(c_v), latex(omega),
                              latex(tu_so), latex(omega)
                              ))

            # Xuất câu trắc nghiệm (Đúng cấu trúc mẫu, không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

