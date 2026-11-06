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


def bt_dang8_p3_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các hệ số để bài toán luôn có nghiệm nguyên đẹp
                # s = -(1/a)*t^3 + b*t^2 + c
                # v = -(3/a)*t^2 + 2bt
                # v' = -(6/a)t + 2b = 0 => t = (2b*a)/6 = (a*b)/3

                # Chọn a và b sao cho (a*b) chia hết cho 3
                a_val = random.choice([2, 3, 6])
                if a_val == 2:
                    b_val = random.choice([3, 6, 9])
                elif a_val == 3:
                    b_val = random.choice([1, 2, 3, 4, 5])
                else: # a_val == 6
                    b_val = random.choice([1, 2, 3])

                c_val = randint(10, 30)

                # Biểu thức s(t)
                coeff_t3 = Rational(-1, a_val)
                s_expr = coeff_t3 * t**3 + b_val * t**2 + c_val

                # Vận tốc v(t) = s'(t)
                v_expr = diff(s_expr, t)

                # Thời điểm vận tốc cực đại (v' = 0)
                t_max_v = (a_val * b_val) // 3

                # Vận tốc cực đại
                v_max = v_expr.subs(t, t_max_v)

                # Quãng đường tại thời điểm t_max_v
                s_at_t_max = s_expr.subs(t, t_max_v)

                kq_num = int(s_at_t_max)
                da = '$%s$' % (latex(kq_num))

                # Tạo các phương án sai
                s_wrong = set()
                while len(s_wrong) < 3:
                    wrong = kq_num + random.choice([-5, -3, -2, 2, 3, 5, 10, -10])
                    if wrong > 0 and wrong != kq_num:
                        s_wrong.add('$%s$' % (latex(wrong)))

                s_list = list(s_wrong)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một chuyển động theo quy luật là $s = %s$ với $t$ giây là khoảng thời gian tính từ khi vật bắt đầu chuyển động và $s$ (mét) là quãng đường vật di chuyển được trong khoảng thời gian đó. Quãng đường vật đi được bắt đầu từ lúc vật chuyển động tới thời điểm vật đạt được vận tốc lớn nhất bằng bao nhiêu?'''
                                 % (latex(s_expr)))

                # Nội dung lời giải
                # v(t) = s'(t) = -3/a t^2 + 2bt
                v_latex = latex(v_expr)
                # Tìm t để v đạt max (đỉnh parabol)
                # v' = -6/a t + 2b = 0
                v_prime = diff(v_expr, t)

                loigiai = ('''Ta có: $s = %s \\Rightarrow v\\left(t\\right) = s'\\left(t\\right) = %s$. \\\\
                             Xét hàm vận tốc $v\\left(t\\right) = %s$. \\\\
                             Đây là hàm số bậc hai có đồ thị là một parabol có bề lõm quay xuống dưới. \\\\
                             Vận tốc đạt giá trị lớn nhất khi $t = -\\frac{B}{2A} = %s$ (giây). \\\\
                             Khi đó quãng đường vật đi được là: $s = s\\left(%s\\right) = %s$ (m).'''
                           % (latex(s_expr), v_latex, v_latex, latex(t_max_v),
                              latex(t_max_v), latex(kq_num)
                              ))
                dapan='\\shortans[0]{$%s$}\n'%(kq_num)
                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

