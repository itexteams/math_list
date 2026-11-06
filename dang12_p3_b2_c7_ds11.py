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


def bt_dang12_p3_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random các số trong bài toán
                # f(t) = (a*t + b) / (t + c)
                a = randint(15, 45)
                b = randint(5, 20)
                c = randint(2, 8)

                nam_bat_dau = random.choice([1970, 1980, 1990, 2000])
                khoang_cach_nam = randint(30, 60)
                nam_target = nam_bat_dau + khoang_cach_nam

                # Tính toán đạo hàm f'(t) = (a*c - b) / (t + c)^2
                tu_so_dao_ham = a * c - b
                t_val = nam_target - nam_bat_dau

                f_prime_val = float(tu_so_dao_ham) / (t_val + c)**2

                # Làm tròn đến hàng phần trăm (0.01)
                kq_decimal = Decimal(str(f_prime_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                # Tạo danh sách các giá trị nhiễu
                s_vals = []
                while len(s_vals) < 3:
                    sai_so = random.choice([-0.01, 0.01, -0.02, 0.02, 0.05, -0.05])
                    nhieu = kq_decimal + Decimal(str(sai_so))
                    nhieu_str = str(nhieu).replace('.', ',')
                    if nhieu > 0 and nhieu_str != kq_str and nhieu_str not in s_vals:
                        s_vals.append(nhieu_str)

                # Câu hỏi
                noidungcauhoi = ('''Số dân của một thị trấn sau $%s$ năm kể từ năm $%s$ được ước tính bởi công thức $f\\left(t\\right) = \\frac{%st + %s}{t + %s}$ (đơn vị: nghìn người). Biết rằng đạo hàm của hàm số $f$ biểu thị tốc độ tăng dân số của thị trấn (đơn vị: nghìn người/năm). Hỏi vào năm $%s$, tốc độ tăng dân số của thị trấn này là bao nhiêu nghìn người/năm? (Kết quả làm tròn đến hàng phần trăm).'''
                                 %(latex(t), latex(nam_bat_dau), latex(a), latex(b), latex(c), latex(nam_target)
                                 ))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq_str))
                da_s1 = '$%s$' % (s_vals[0])
                da_s2 = '$%s$' % (s_vals[1])
                da_s3 = '$%s$' % (s_vals[2])

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tốc độ tăng dân số của thị trấn tại thời điểm $t$ năm kể từ năm $%s$ là: \\\\
                             $f\'\\left(t\\right) = \\frac{%s \\cdot \\left(t + %s\\right) - \\left(%st + %s\\right) \\cdot 1}{\\left(t + %s\\right)^2} = \\frac{%s}{\\left(t + %s\\right)^2}$ (nghìn người/năm). \\\\
                             Vào năm $%s$, $t = %s - %s = %s$ nên tốc độ tăng dân số của thị trấn tại thời điểm này là: \\\\
                             $f\'\\left(%s\\right) = \\frac{%s}{\\left(%s + %s\\right)^2} \\approx %s$ (nghìn người/năm).'''
                           % (latex(nam_bat_dau), latex(a), latex(c), latex(a), latex(b), latex(c), latex(tu_so_dao_ham), latex(c),
                              latex(nam_target), latex(nam_target), latex(nam_bat_dau), latex(t_val),
                              latex(t_val), latex(tu_so_dao_ham), latex(t_val), latex(c), kq_str
                              ))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

