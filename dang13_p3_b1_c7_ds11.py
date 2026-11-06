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


def bt_dang13_p3_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Hàm số có dạng f(x) = k/x. Trong ảnh k=1.
                k = random.randint(1, 6)
                # Chọn hoành độ x0 sao cho y0 đẹp (nguyên hoặc phân số đơn giản)
                x0 = random.choice([1, 2, 3])
                y0 = Rational(k, x0)

                # Tính đạo hàm f'(x) = -k/x^2 để tìm hệ số góc a
                a = Rational(-k, x0**2)

                # Phương trình tiếp tuyến: y = a(x - x0) + y0 <=> y = ax - a*x0 + y0
                # Vậy b = -a*x0 + y0
                b = -a * x0 + y0

                # Tính giá trị biểu thức T = 2a + b theo yêu cầu đề bài trong ảnh
                res_T = 2*a + b

                # Định dạng kết quả cho đáp án
                kq = latex(res_T).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % kq]
                da = random.choice(du)

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s_vals = set()
                while len(s_vals) < 3:
                    # Tạo các giá trị nhiễu bằng cách cộng/trừ số nguyên vào kết quả đúng
                    off = random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    alt_val = res_T + off
                    alt_str = '$%s$' % latex(alt_val).replace('.', ',')
                    if alt_str != da:
                        s_vals.add(alt_str)

                s = list(s_vals)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Bước 2: Viết lại bài toán theo mẫu code python
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f\\left(x\\right)=\\frac{%s}{x}$ có đồ thị $(C)$ và điểm $M\\left(%s;%s\\right) \\in (C)$. Phương trình tiếp tuyến với $(C)$ tại điểm $M$ có dạng $y = ax + b$. Giá trị $T = 2a + b$ bằng bao nhiêu?'''
                                 %(latex(k), latex(x0), latex(y0).replace('.', ',')))

                # Nội dung lời giải (Trình bày chi tiết từng bước)
                loigiai = ('''Hệ số góc của tiếp tuyến tại điểm $M\\left(%s;%s\\right) \\in (C)$ là:\\\\
                             $a = f'\\left(%s\\right) = \\lim_{x \\to %s} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = \\lim_{x \\to %s} \\frac{\\frac{%s}{x} - %s}{x - %s} = %s$.\\\\
                             Phương trình tiếp tuyến tại $M\\left(%s;%s\\right) \\in (C)$ có dạng:\\\\
                             $y = f'\\left(%s\\right)\\left(x - %s\\right) + %s \\iff y = %sx + %s$.\\\\
                             Từ đó suy ra $a = %s$ và $b = %s$.\\\\
                             Khi đó giá trị biểu thức cần tìm là $T = 2a + b = 2 \\cdot \\left(%s\\right) + %s = %s$.'''
                           %(latex(x0), latex(y0).replace('.', ','), 
                             latex(x0), latex(x0), latex(x0), latex(x0), 
                             latex(x0), latex(k), latex(y0), latex(x0), latex(a),
                             latex(x0), latex(y0).replace('.', ','), 
                             latex(x0), latex(x0), latex(y0).replace('.', ','), 
                             latex(a), latex(b).replace('.', ','),
                             latex(a), latex(b).replace('.', ','),
                             latex(a), latex(b).replace('.', ','), latex(res_T).replace('.', ',')
                            ))
                dapan='\\shortans[0]{$%s$}\n'%(res_T)
                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content      

