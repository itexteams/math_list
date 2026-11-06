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


def bt_dang19_p3_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn cận dưới m = 1 để ln(m) = 0 cho đúng form a + blnc
                m = 1
                # Chọn cận trên n sao cho n < 9 (theo điều kiện c < 9)
                n = random.randint(2, 8)
                # Chọn hằng số k ngẫu nhiên
                k = random.randint(1, 10)

                # Tính toán các hệ số
                # Tích phân = [x + k*ln(x)] từ m đến n = (n - m) + k*ln(n)
                a = n - m
                b = k
                c = n

                # Kết quả cần tìm là tổng S = a + b + c
                kq_val = a + b + c
                kq = str(kq_val)

                # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai != kq_val:
                        s_set.add(sai)

                s_list = list(s_set)
                das1 = '$%s$' % s_list[0]
                das2 = '$%s$' % s_list[1]
                das3 = '$%s$' % s_list[2]

                # Câu hỏi
                # Biểu thức tích phân: (x + k)/x
                noidungcauhoi = (r'Cho tích phân $\int_{%s}^{%s} \frac{x + %s}{x} \text{d} x = a + b \ln c$ với $a, b, c \in \mathbb{Z}, c < 9$. Tính tổng $S = a + b + c$.'
                                 % (latex(m), latex(n), latex(k)))

                # Các đáp án
                da_d = '\\True $%s$' % kq
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'Ta có: $\int_{%s}^{%s} \frac{x + %s}{x} \text{d} x = \int_{%s}^{%s} \left( 1 + \frac{%s}{x} \right) \text{d} x = \left( x + %s \ln|x| \right) \bigg|_{%s}^{%s} = (%s + %s \ln %s) - (%s + %s \ln %s) = %s + %s \ln %s$. \\'
                           r'Suy ra $a = %s, b = %s, c = %s$. \\'
                           r'Vậy $S = a + b + c = %s + %s + %s = %s$.'
                           % (latex(m), latex(n), latex(k), latex(m), latex(n), latex(k), latex(k), latex(m), latex(n),
                              latex(n), latex(k), latex(n), latex(m), latex(k), latex(m),
                              latex(a), latex(b), latex(c),
                              latex(a), latex(b), latex(c),
                              latex(a), latex(b), latex(c), latex(kq_val)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

