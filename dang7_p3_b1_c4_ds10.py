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


def bt_dang7_p3_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Khai báo biến cấu trúc
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random bài toán
                # Chọn a và b là hai nghiệm nguyên dương để tập xác định đẹp (a < b)
                a_val = randint(1, 4)
                b_val = randint(a_val + 1, a_val + 5)

                # Hệ số của tam thức bậc hai: -x^2 + (a+b)x - ab
                sum_ab = a_val + b_val
                prod_ab = a_val * b_val
                # Biểu thức dưới căn: f(x) = -x^2 + sum*x - prod
                f_x = -x**2 + sum_ab*x - prod_ab

                # Tử số (không ảnh hưởng tập xác định nhưng làm bài toán phong phú)
                k = randint(1, 10)
                tu_so = x + k

                # Kết quả đúng
                S_val = a_val**2 + b_val**2
                da = '$S = %s$' % (latex(S_val))

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    # Các lỗi sai phổ biến: a+b, a^2-b^2, (a+b)^2, hoặc cộng trừ ngẫu nhiên
                    wrong_vals = [
                        a_val + b_val,
                        abs(a_val**2 - b_val**2),
                        (a_val + b_val)**2,
                        S_val + randint(1, 5),
                        S_val - randint(1, 3)
                    ]
                    val = random.choice(wrong_vals)
                    if val != S_val and val > 0:
                        s_set.add('$S = %s$' % (latex(val)))

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Giả sử $D = (a; b)$ là tập xác định của hàm số $y = \frac{%s}{\sqrt{%s}}$. Giá trị $S = a^2 + b^2$ là'''
                                 % (latex(tu_so), latex(f_x)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Hàm số xác định khi $%s > 0 \Leftrightarrow %s < x < %s$. \\
                             Tập xác định: $D = (%s; %s)$ nên $a = %s; b = %s$. \\
                             $\Rightarrow S = a^2 + b^2 = %s^2 + %s^2 = %s$.'''
                           % (latex(f_x), latex(a_val), latex(b_val),
                              latex(a_val), latex(b_val), latex(a_val), latex(b_val),
                              latex(a_val), latex(b_val), latex(S_val)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(S_val))

            # Xuất câu trắc nghiệm theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

