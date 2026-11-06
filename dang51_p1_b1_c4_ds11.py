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


def bt_dang51_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM HỆ SỐ ---
                # Chọn một hệ số k ngẫu nhiên cho tử số (k*n). 
                # Nếu k=1 thì về bài toán gốc trong ảnh.
                k = randint(1, 10) 

                # Biến n để hiển thị trong công thức
                n_sym = symbols('n')

                # Kết quả đúng của bài toán là k/2
                res_fraction = Rational(k, 2)

                # --- BƯỚC 2: TẠO ĐÁP ÁN NHIỄU ---
                # Tạo các đáp án sai dựa trên kết quả đúng
                kq = res_fraction # Đáp án đúng

                # Đáp án sai 1: Quên chia 2 (kết quả là k)
                kq_sai1 = Rational(k, 1)

                # Đáp án sai 2: Chia 4 thay vì chia 2 (k/4)
                kq_sai2 = Rational(k, 4)

                # Đáp án sai 3: Cộng thêm 1 vào tử số ((k+2)/2 hoặc một giá trị khác)
                kq_sai3 = Rational(k + 2, 2)

                # Xử lý trường hợp trùng lặp đáp án (hiếm gặp nhưng cần thiết)
                while kq_sai3 == kq or kq_sai3 == kq_sai1 or kq_sai3 == kq_sai2:
                    kq_sai3 = kq_sai3 + 1

                # Format đáp án cho đẹp (dùng latex)
                du = ['$%s$' % latex(kq)]
                da = random.choice(du) # Đáp án đúng được chọn (chỉ có 1 cái trong list du)

                # Danh sách các đáp án nhiễu
                s = ['$%s$' % latex(kq_sai1),
                     '$%s$' % latex(kq_sai2),
                     '$%s$' % latex(kq_sai3)]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- BƯỚC 3: NỘI DUNG CÂU HỎI ---
                # Tử số hiển thị: n nếu k=1, ngược lại là kn
                tu_so_str = "n" if k == 1 else f"{k}n"

                noidungcauhoi = ('''Cho dãy số $(u_n)$ như sau: $u_n = \\frac{%s}{1+n^2+n^4}, \\forall n=1, 2, \\dots$ Giới hạn $\\lim_{n \\to +\\infty} (u_1 + u_2 + \\dots + u_n)$ bằng'''
                                 % (tu_so_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- BƯỚC 4: NỘI DUNG LỜI GIẢI ---
                # Xử lý chuỗi hiển thị cho phần tách biểu thức
                # Nếu k=1 thì phân số đầu là 1/2, nếu k khác 1 thì là k/2
                he_so_tach = "\\frac{1}{2}" if k == 1 else f"\\frac{{{k}}}{{2}}"

                # Logic lời giải chi tiết
                loigiai = ('''Ta có $u_n = \\frac{%s}{(1+n^2)^2 - n^2} = \\frac{%s}{(n^2+n+1)(n^2-n+1)} = %s \\left( \\frac{1}{n^2-n+1} - \\frac{1}{n^2+n+1} \\right)$. \\\\
                         Ta có $u_1 + u_2 + \\dots + u_n = %s \\left( 1 - \\frac{1}{3} + \\frac{1}{3} - \\frac{1}{7} + \\dots + \\frac{1}{n^2-n+1} - \\frac{1}{n^2+n+1} \\right)$ \\\\
                         $= %s \\left( 1 - \\frac{1}{n^2+n+1} \\right) = %s \\frac{n^2+n}{n^2+n+1}$. \\\\
                         Suy ra $\\lim_{n \\to +\\infty} (u_1 + u_2 + \\dots + u_n) = %s \\lim_{n \\to +\\infty} \\frac{1+\\frac{1}{n}}{1+\\frac{1}{n}+\\frac{1}{n^2}} = %s$.'''
                         % (tu_so_str, tu_so_str, he_so_tach, 
                            he_so_tach, 
                            he_so_tach, he_so_tach, 
                            he_so_tach, latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

