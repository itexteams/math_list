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


def bt_dang41_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo giá trị ngẫu nhiên
                n = randint(1, 9)      # Phần nguyên
                c = randint(10, 98)    # Chu kỳ (vô hạn tuần hoàn)

                # 2. Tính toán giá trị a = n + c/99
                # Vì chu kỳ có 2 chữ số nên mẫu số là 99
                phan_so_a = Rational(n * 99 + c, 99)

                x_val = phan_so_a.p # Tử số tối giản
                y_val = phan_so_a.q # Mẫu số tối giản
                tong_xy = x_val + y_val

                # 3. Tạo các phương án nhiễu (sai)
                kq = tong_xy
                s = [
                    '$%s$' % (kq + randint(1, 10)),
                    '$%s$' % (kq - randint(1, 10)),
                    '$%s$' % (kq + randint(11, 20)),
                    '$%s$' % (kq - randint(11, 20)),
                    '$%s$' % (x_val + 99 if y_val != 99 else x_val + 90), # Trường hợp chưa tối giản
                ]

                da_dung = '$%s$' % (kq)

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # 4. Nội dung câu hỏi (B2)
                # Định dạng chuỗi lặp lại: n,cccc...
                chuoi_lap = str(n) + "," + str(c) + str(c) + str(c) + "..."

                noidungcauhoi = ('''Cho số $a = %s$ là số thập phân vô hạn tuần hoàn có chu kỳ là $%s$, số $a$ được biểu diễn dưới dạng phân số tối giản dạng $a = \\frac{x}{y}$, trong đó $x$ và $y$ là các số nguyên dương. Tổng $x + y$ bằng bao nhiêu?'''
                                 % (chuoi_lap, latex(c)))

                # 5. Nội dung lời giải (B2)
                loigiai = ('''Ta có $a = %s + \\frac{%s}{100} + \\frac{%s}{100^2} + \\frac{%s}{100^3} + \\dots = %s + \\frac{\\frac{%s}{100}}{1 - \\frac{1}{100}} = %s + \\frac{%s}{99} = \\frac{%s}{%s}$. \\\\
                             Vì $\\frac{%s}{%s}$ là phân số tối giản nên suy ra $\\begin{cases} x = %s \\\\ y = %s \\end{cases} \\Rightarrow x + y = %s$.'''
                           % (latex(n), latex(c), latex(c), latex(c), latex(n), latex(c), latex(n), latex(c), 
                              latex(x_val), latex(y_val), latex(x_val), latex(y_val), latex(x_val), latex(y_val), latex(tong_xy)))

                # 6. Đưa các đáp án vào danh sách và trộn
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(tong_xy))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+ 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

