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


def bt_dang38_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (theo mẫu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán
                n_pairs = random.randint(8, 12)
                n_shoes = 2 * n_pairs
                k_select = 4

                # Tính toán không gian mẫu dùng sp.binomial
                omega = sp.binomial(n_shoes, k_select)

                # Tính toán biến cố đối A_bar
                c_n_4 = sp.binomial(n_pairs, k_select)
                ways_per_shoe = 2**k_select

                n_A_bar = c_n_4 * ways_per_shoe
                n_A = omega - n_A_bar

                # Xác suất
                prob = sp.Rational(n_A, omega)
                da = latex(prob)

                # Bước 4: Các phương án sai
                s = []
                w1 = sp.Rational(n_A_bar, omega)
                if w1 != prob: s.append('$%s$' % latex(w1))

                w2 = sp.Rational(sp.binomial(n_pairs, 2), omega)
                if w2 != prob: s.append('$%s$' % latex(w2))

                while len(s) < 3:
                    fake_val = sp.Rational(random.randint(10, 100), random.randint(101, 500))
                    if fake_val != prob and ('$%s$' % latex(fake_val)) not in s:
                        s.append('$%s$' % latex(fake_val))

                das1, das2, das3 = s[0], s[1], s[2]

                noidungcauhoi = ('''Một người có $%s$ đôi giày khác nhau và trong lúc đi du lịch vội quá nên đã lấy ngẫu nhiên $%s$ chiếc. Xác suất để trong $%s$ chiếc giày lấy ra có ít nhất một đôi bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 % (latex(n_pairs), latex(k_select), latex(k_select)))

                da_d = ('\\True $%s$' % da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                h1=Rational(n_A, omega)
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')

                loigiai = ('''Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\
                           Gọi $A$ là biến cố "trong $%s$ chiếc giày lấy ra có ít nhất một đôi". \\\\
                           Suy ra $\\overline{A}$ là biến cố "trong $%s$ chiếc giày lấy ra không có đôi nào". \\\\
                           - Số cách chọn $%s$ đôi giày từ $%s$ đôi là $C_{%s}^{%s}$. \\\\
                           - Trong mỗi đôi chọn ra một chiếc thì mỗi chiếc có $C_2^1$ cách chọn. Suy ra $%s$ chiếc có $\\left(C_2^1\\right)^{%s}$ cách chọn. \\\\
                           Suy ra số phần tử của biến cố $\\overline{A}$ là $n\\left(\\overline{A}\\right) = C_{%s}^{%s} \\cdot \\left(C_2^1\\right)^{%s} = %s$. \\\\
                           Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = %s - %s = %s$. \\\\
                           Vậy xác suất cần tính là $P\\left(A\\right) = \\frac{%s}{%s} = %s \\approx %s$.'''
                           % (latex(n_shoes), latex(k_select), latex(omega),
                              latex(k_select), latex(k_select),
                              latex(k_select), latex(n_pairs), latex(n_pairs), latex(k_select),
                              latex(k_select), latex(k_select),
                              latex(n_pairs), latex(k_select), latex(k_select), latex(n_A_bar),
                              latex(omega), latex(n_A_bar), latex(n_A),
                              latex(n_A), latex(omega), da, kqz))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

