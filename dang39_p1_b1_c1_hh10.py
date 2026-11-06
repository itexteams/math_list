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


def bt_dang39_p1_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các số ngẫu nhiên cho bài toán
                # Cho sin(a) = 1/b
                b = random.choice([3, 4, 5, 6])
                # Biểu thức P = m*cot(a) + n*tan(a)
                m = random.choice([2, 3, 4, 5])
                n = random.choice([2, 3, 4, 5])

                # Các bước tính toán bằng sympy
                sin_a = Rational(1, b)
                cos_a_sq = 1 - sin_a**2
                # Vì góc phần tư thứ 2 nên cos âm
                cos_a = -sqrt(cos_a_sq) 
                tan_a = sin_a / cos_a
                cot_a = cos_a / sin_a

                # Giá trị đúng của P
                kq_val = simplify(m * cot_a + n * tan_a)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(kq_val))]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên
                s_set = set()
                while len(s_set) < 3:
                    # Giả sử học sinh nhầm dấu cos > 0
                    fake_cos_a = sqrt(cos_a_sq)
                    fake_tan_a = sin_a / fake_cos_a
                    fake_cot_a = fake_cos_a / sin_a

                    # Các kiểu tính sai có thể xảy ra
                    err1 = simplify(m * fake_cot_a + n * fake_tan_a)
                    err2 = simplify(n * cot_a + m * tan_a)
                    err3 = simplify(-kq_val)
                    err4 = simplify(m * cot_a - n * tan_a)
                    err5 = simplify(m * fake_cot_a - n * fake_tan_a)

                    choices_err = [err1, err2, err3, err4, err5]
                    ch = random.choice(choices_err)

                    # Kiểm tra không trùng với đáp án đúng
                    if ch != kq_val:
                        s_set.add('$%s$' % latex(ch))

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\sin \\alpha = %s$, $90^\\circ < \\alpha < 180^\\circ$. Giá trị của biểu thức $P = %s \\cot \\alpha + %s \\tan \\alpha$ là'''
                                 %(latex(sin_a), latex(m), latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $\\cos^2 \\alpha = 1 - \\sin^2 \\alpha = 1 - \\left(%s\\right)^2 = %s$. \\\\
                             Vì $90^\\circ < \\alpha < 180^\\circ$ nên $\\cos \\alpha < 0$. Suy ra $\\cos \\alpha = %s$. \\\\
                             Khi đó $\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha} = %s$ và $\\cot \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha} = %s$. \\\\
                             Vậy biểu thức $P = %s \\cdot \\left(%s\\right) + %s \\cdot \\left(%s\\right) = %s$.'''
                           %(latex(sin_a), latex(cos_a_sq), 
                             latex(cos_a), 
                             latex(tan_a), latex(cot_a), 
                             latex(m), latex(cot_a), latex(n), latex(tan_a), latex(kq_val)))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

