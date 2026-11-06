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


def bt_dang26_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo ngẫu nhiên các thông số bài toán: cos(k*x) = p*m - q
                k = randint(2, 6) # Hệ số góc của x
                p = randint(2, 5) # Hệ số của m
                q = randint(2, 7) # Hệ số tự do độc lập

                # Tính toán các giá trị biên của đoạn [a, b] cho m sao cho -1 <= p*m - q <= 1
                # <=> q - 1 <= p*m <= q + 1
                bien_trai = q - 1
                bien_phai = q + 1

                a_val = Rational(bien_trai, p)
                b_val = Rational(bien_phai, p)

                # Biểu thức cần tính: p*a + b
                kq_bieuthuc = p * a_val + b_val

                # Chuyển đổi định dạng LaTeX cho kết quả đúng và xử lý dấu thập phân nếu có
                da_dung_str = ('$%s$' % latex(kq_bieuthuc)).replace('.', ',')

                # Các phương án sai (nhiễu)
                # Tạo danh sách các giá trị nhiễu xung quanh đáp án chính xác
                s_vals = [
                    kq_bieuthuc + 1,
                    kq_bieuthuc - 2,
                    Rational(q, p),
                    kq_bieuthuc + Rational(1, 2),
                    kq_bieuthuc - 1,
                    Rational(bien_trai + bien_phai, p)
                ]

                # Lọc bỏ phần tử trùng với đáp án đúng (nếu có)
                s_vals = [val for val in s_vals if val != kq_bieuthuc]

                # Lấy ngẫu nhiên 3 phương án sai từ danh sách
                s_chosen = random.sample(s_vals, 3)

                das1 = ('$%s$' % latex(s_chosen[0])).replace('.', ',')
                das2 = ('$%s$' % latex(s_chosen[1])).replace('.', ',')
                das3 = ('$%s$' % latex(s_chosen[2])).replace('.', ',')

                # Đề bài câu hỏi mẫu ứng với tham số ngẫu nhiên
                noidungcauhoi = ('''Cho phương trình $\\cos %sx = %sm - %s$. Gọi đoạn $[a;b]$ là tập hợp tất cả các giá trị của $m$ để phương trình có nghiệm. Giá trị $%sa + b$ bằng'''
                                 % (latex(k), latex(p), latex(q), latex(p)))

                # Các phương án trả lời
                da_d = ('\\True ' + str(da_dung_str))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và xáo trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo các bước của ảnh mẫu
                loigiai = ('''Phương trình đã cho có nghiệm khi $-1 \\le %sm - %s \\le 1 \\Leftrightarrow %s \\le %sm \\le %s \\Leftrightarrow %s \\le m \\le %s$. \\\\
                           Khi đó tập hợp tất cả các giá trị của $m$ để phương trình có nghiệm là $\\left[%s;%s\\right]$. \\\\
                           Ta được $a = %s$; $b = %s$. Suy ra $%sa + b = %s$.'''
                           % (latex(p), latex(q), latex(bien_trai), latex(p), latex(bien_phai), latex(a_val), latex(b_val),
                              latex(a_val), latex(b_val),
                              latex(a_val), latex(b_val), latex(p), latex(kq_bieuthuc)))

            # Xuất câu trắc nghiệm định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

