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


def bt_dang18_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # w: số quả cầu trắng, b: số quả cầu đen
                w = randint(5, 12)
                b = randint(10, 18)
                tong = w + b

                # Tính toán các giá trị cho lời giải
                n_omega = tong * (tong - 1)
                n_trang = w * (w - 1)
                n_den = b * (b - 1)
                n_A = n_trang + n_den

                # Kết quả xác suất rút gọn
                kq_frac = Rational(n_A, n_omega)
                kq = latex(kq_frac)

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = []
                # Phương án sai 1: Lấy 2 quả khác màu
                sai1 = Rational(2 * w * b, n_omega)
                if sai1 != kq_frac:
                    s.append('$%s$' % (latex(sai1)))

                # Phương án sai 2: Chỉ tính trường hợp 2 quả trắng
                sai2 = Rational(n_trang, n_omega)
                if sai2 != kq_frac:
                    s.append('$%s$' % (latex(sai2)))

                # Phương án sai 3: Chỉ tính trường hợp 2 quả đen
                sai3 = Rational(n_den, n_omega)
                if sai3 != kq_frac:
                    s.append('$%s$' % (latex(sai3)))

                # Bổ sung phương án sai nếu bị trùng hoặc thiếu
                while len(s) < 3:
                    tu_random = randint(10, 90)
                    mau_random = n_omega
                    sai_rd = Rational(tu_random, mau_random)
                    if sai_rd != kq_frac and ('$%s$' % (latex(sai_rd))) not in s:
                        s.append('$%s$' % (latex(sai_rd)))

                # Chọn đáp án
                da = '$%s$' % (kq)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2: Viết lại y hệt bài toán)
                noidungcauhoi = ('''Một chiếc hộp đựng $%s$ quả cầu trắng, $%s$ quả cầu đen. Lần thứ nhất lấy ngẫu nhiên một quả cầu trong hộp, lần thứ hai lấy ngẫu nhiên 1 quả cầu trong các quả cầu còn lại. Xác suất để kết quả của hai lần lấy được 2 quả cầu cùng màu là'''
                                 % (latex(w), latex(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết chi tiết giống nội dung trong ảnh)
                loigiai = ('''Không gian mẫu là lấy hai quả cầu trong hộp một cách lần lượt ngẫu nhiên. \\\\
                             Suy ra số phần tử của không gian mẫu là $n(\\Omega) = C_{%s}^1 C_{%s}^1 = %s$. \\\\
                             Gọi $A$ là biến cố "Hai quả cầu được lấy cùng màu". Ta có các trường hợp thuận lợi cho biến cố $A$ như sau: \\\\
                             + TH1: Lần thứ nhất lấy một quả màu trắng và lần thứ hai cũng màu trắng. Do đó trường hợp này có $C_{%s}^1 C_{%s}^1 = %s$ cách. \\\\
                             + TH2: Lần thứ nhất lấy một quả màu đen và lần thứ hai cũng màu đen. Do đó trường hợp này có $C_{%s}^1 C_{%s}^1 = %s$ cách. \\\\
                             Suy ra số phần tử của biến cố $A$ là $n(A) = C_{%s}^1 C_{%s}^1 + C_{%s}^1 C_{%s}^1 = %s + %s = %s$. \\\\
                             Vậy xác suất cần tính $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.'''
                           % (latex(tong), latex(tong - 1), latex(n_omega),
                              latex(w), latex(w - 1), latex(n_trang),
                              latex(b), latex(b - 1), latex(n_den),
                              latex(w), latex(w - 1), latex(b), latex(b - 1), latex(n_trang), latex(n_den), latex(n_A),
                              latex(n_A), latex(n_omega), kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

