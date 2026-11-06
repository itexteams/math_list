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


def bt_dang22_p3_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Ta có f(n) = n(n+1)/2
                # Biểu thức trong log: [f(a) - f(b) - k] / 2 = 10^T
                # => k = f(a) - f(b) - 2 * 10^T

                # Chọn ngẫu nhiên T (kết quả) là 1, 2 hoặc 3
                kq_v = random.randint(1, 3) 

                # Chọn ngẫu nhiên a và b sao cho k > 0 và biểu thức hợp lý
                a = random.randint(80, 120)
                b = random.randint(30, 70)

                f_a = a * (a + 1) // 2
                f_b = b * (b + 1) // 2

                # Tính k để log(...) = kq_v
                k = f_a - f_b - 2 * (10**kq_v)

                # Nếu k âm (hiếm), ta gán cứng lại để đảm bảo bài toán có nghĩa
                if k <= 0:
                    a, b, k, kq_v = 96, 69, 241, 3
                    f_a = a * (a + 1) // 2
                    f_b = b * (b + 1) // 2

                # Đáp án đúng
                da = '$%s$' % (latex(kq_v))

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    sai = kq_v + random.choice([-2, -1, 1, 2, 4])
                    if sai > 0 and str(sai) not in s and sai != kq_v:
                        s.append('$%s$' % (latex(sai)))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2-Viết lại y hệt cấu trúc bài toán)
                noidungcauhoi = (r'''Cho $f(1)=1, f(m+n)=f(m)+f(n)+mn$ với mọi $m, n \in \mathbb{N}^*$. Giá trị của biểu thức $T = \log \left[ \frac{f(%s) - f(%s) - %s}{2} \right]$ bằng bao nhiêu?'''
                                 % (latex(a), latex(b), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2-Viết lại chi tiết theo logic toán học)
                loigiai = (r'''Có $f(1)=1, f(m+n)=f(m)+f(n)+mn$. \\
                           Ta có: $f(n) = f(n-1+1) = f(n-1) + f(1) + (n-1) \cdot 1 = f(n-1) + n$. \\
                           $\Rightarrow f(n) = f(n-1) + n = f(n-2) + (n-1) + n = \dots = f(1) + 2 + \dots + n$. \\
                           $\Rightarrow f(n) = \frac{n(n+1)}{2}$. \\
                           Áp dụng: \\
                           $f(%s) = \frac{%s \cdot %s}{2} = %s$. \\
                           $f(%s) = \frac{%s \cdot %s}{2} = %s$. \\
                           Vậy $T = \log \left[ \frac{%s - %s - %s}{2} \right] = \log \left[ \frac{%s}{2} \right] = \log(%s) = %s$.'''
                           % (latex(a), latex(a), latex(a+1), latex(f_a),
                              latex(b), latex(b), latex(b+1), latex(f_b),
                              latex(f_a), latex(f_b), latex(k), latex(f_a - f_b - k), latex(10**kq_v), latex(kq_v)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_v))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

