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


def bt_dang11_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # d: x = x0 + u1*t, y = y0 + u2*t
                # Trong ảnh: x = 2 (u1=0), y = -1 + 6t (u2=6)
                u1 = randint(-5, 5)
                u2 = randint(1, 10) * random.choice([-1, 1])
                x0 = randint(-10, 10)
                y0 = randint(-10, 10)

                # Vectơ chỉ phương u = (u1, u2)
                # Vectơ pháp tuyến n = (a, b) = (u2, -u1) hoặc (-u2, u1)
                # Ở đây ta chọn n = (u2, -u1)
                a = u2
                b = -u1

                # Kết quả tích a*b
                kq_val = a * b

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                # Các đáp án trắc nghiệm
                da = '$' + str(kq_val) + '$'

                s_list = []
                while len(s_list) < 3:
                    # Tạo các giá trị sai như u1*u2, u1+u2, hoặc số ngẫu nhiên
                    wrong = random.choice([u1 * u2, u1 + u2, x0 * y0, randint(-20, 20)])
                    val_str = '$' + str(wrong) + '$'
                    if val_str != da and val_str not in s_list:
                        s_list.append(val_str)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                # Tạo chuỗi hiển thị t (nếu u=0 thì không hiện t)
                x_part = latex(x0) if u1 == 0 else latex(x0 + u1*symbols('t'))
                y_part = latex(y0) if u2 == 0 else latex(y0 + u2*symbols('t'))

                # Viết lại y hệt cấu trúc bài toán
                noidungcauhoi = ('''Cho đường thẳng $d: \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. Khi đó $\\vec{n}(a;b)$ là vecto pháp tuyến của đường thẳng $d$. Giá trị $a \\cdot b$ bằng bao nhiêu?'''
                                  %(x_part, y_part))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Bước 2)
                loigiai = ('''Từ phương trình tham số của đường thẳng $d$, ta xác định được một vectơ chỉ phương là $\\vec{u}=(%s; %s)$.\\\\
                             Khi đó, một vectơ pháp tuyến của đường thẳng $d$ là $\\vec{n}(a; b) = (%s; %s)$.\\\\
                             Suy ra $a = %s$ và $b = %s$.\\\\
                             Vậy tích $a \\cdot b = %s \\cdot (%s) = %s$.'''
                           %(latex(u1), latex(u2), latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), latex(kq_val)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))
            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

