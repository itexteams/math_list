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


def bt_dang27_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số
                n_tong = randint(40, 60)
                n_cap = randint(3, 6)
                n_chon = 3

                # Bước 2: Tính toán các giá trị cho lời giải
                # Sử dụng binomial(n, k) thay cho combinations
                omega = binomial(n_tong, n_chon)

                # Biến cố đối X_ngang: Chọn được 1 cặp giống nhau và 1 phiếu khác
                # Số cách chọn 1 cặp từ n_cap cặp: binomial(n_cap, 1) = n_cap
                # Số cách chọn 1 phiếu còn lại từ (n_tong - 2) phiếu: binomial(n_tong - 2, 1)
                n_x_ngang = n_cap * (n_tong - 2)

                # Số phần tử của biến cố X: n(X) = n(Omega) - n(X_ngang)
                n_x = omega - n_x_ngang

                # Xác suất P(X)
                kq_fraction = Rational(n_x, omega)
                da = '$%s$' % latex(kq_fraction)

                # Bước 3: Tạo các phương án sai
                s = []
                # Phương án sai 1: Quên trừ đi phần biến cố đối (tức là tính xác suất của biến cố đối)
                s1 = Rational(n_x_ngang, omega)
                if s1 != kq_fraction:
                    s.append('$%s$' % latex(s1))

                # Phương án sai 2: Nhầm số phiếu còn lại là (n_tong - 1) thay vì (n_tong - 2)
                n_x_ngang_sai = n_cap * (n_tong - 1)
                s2 = Rational(max(1, omega - n_x_ngang_sai), omega)
                if s2 != kq_fraction:
                    s.append('$%s$' % latex(s2))

                # Phương án sai 3: Biến đổi ngẫu nhiên tử số
                s3 = Rational(abs(n_x - randint(5, 15)), omega)
                s4 = Rational(n_x + randint(5, 15), omega)
                s.append('$%s$' % latex(s3))
                s.append('$%s$' % latex(s4))

                # Lọc trùng và trộn
                s = list(set(s))
                if da in s: s.remove(da)
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi
                noidungcauhoi = ('''Trong một kì thi vấn đáp thí sinh $A$ phải đứng trước ban giám khảo chọn ngẫu nhiên $%s$ phiếu câu hỏi từ $1$ thùng gồm $%s$ phiếu câu hỏi, trong đó có $%s$ cặp phiếu câu hỏi mà mỗi cặp phiếu có nội dung khác nhau từng đôi một và trong mỗi cặp phiếu có nội dung giống nhau. Xác suất để thí sinh $A$ chọn được $%s$ phiếu câu hỏi có nội dung khác nhau bằng'''
                                 % (latex(n_chon), latex(n_tong), latex(n_cap), latex(n_chon)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Không gian mẫu là số cách chọn tùy ý $%s$ phiếu câu hỏi từ $%s$ phiếu câu hỏi. \\\\
                             Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\
                             Gọi $X$ là biến cố "Thí sinh $A$ chọn được $%s$ phiếu câu hỏi khác nhau". \\\\
                             Để tìm số phần tử của $X$ ta tìm số phần tử của biến cố $\\overline{X}$, lúc này cần chọn được $1$ cặp trong $%s$ cặp phiếu có câu hỏi giống nhau và chọn $1$ phiếu trong $%s$ phiếu còn lại. \\\\
                             Suy ra số phần tử của biến cố $\\overline{X}$ là $n\\left(\\overline{X}\\right) = C_{%s}^{1} \\cdot C_{%s}^{1} = %s \\cdot %s = %s$. \\\\
                             Vậy xác suất cần tính $P\\left(X\\right) = \\frac{n\\left(X\\right)}{n\\left(\\Omega\\right)} = \\frac{n\\left(\\Omega\\right) - n\\left(\\overline{X}\\right)}{n\\left(\\Omega\\right)} = \\frac{%s - %s}{%s} = %s$.'''
                           % (latex(n_chon), latex(n_tong), latex(n_tong), latex(n_chon), latex(omega),
                              latex(n_chon), latex(n_cap), latex(n_tong - 2),
                              latex(n_cap), latex(n_tong - 2), latex(n_cap), latex(n_tong - 2), latex(n_x_ngang),
                              latex(omega), latex(n_x_ngang), latex(omega), latex(kq_fraction)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

