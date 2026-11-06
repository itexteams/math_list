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


def bt_dang33_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3-Suy nghĩ tìm cách random bài toán
                T = randint(10, 15)  # Tổng thời gian bèo phủ kín mặt nước (giờ)
                k = randint(2, 10)   # Tốc độ tăng trưởng (gấp k lần mỗi giờ)
                f_denom = randint(2, 9) # Tỉ lệ phủ kín (1/f_denom)



                val_inside_log = (k**(T+1) - 1) / f_denom + 1
                t_exact = math.log(val_inside_log, k) - 1

                # Làm tròn đến 1 chữ số thập phân
                kq_decimal = Decimal(str(t_exact)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # B4-Điều chỉnh các phương án sai
                # Tạo danh sách các giá trị nhiễu xung quanh đáp án đúng
                s_vals = []
                offsets = [-1.5, -1.1, -0.7, -0.2, 0.3, 0.8, 1.2, 1.6]
                random.shuffle(offsets)

                for offset in offsets:
                    val = float(kq_decimal) + offset
                    val_rounded = round(val, 1)
                    val_str = str(val_rounded).replace('.', ',')
                    if val_str != kq_str and val_str not in s_vals:
                        s_vals.append(val_str)
                    if len(s_vals) == 3:
                        break

                # Câu hỏi
                noidungcauhoi = ('''Một người thả một lá bèo vào một chậu nước. Sau $%s$ giờ bèo sinh sôi phủ kín mặt nước trong chậu. Biết rằng sau mỗi giờ lượng bèo tăng gấp $%s$ lần lượng bèo trước đó và tốc độ tăng không đổi. Hỏi sau mấy giờ thì bèo phủ kín $\\frac{1}{%s}$ mặt nước trong chậu (kết quả làm tròn đến một chữ số phần thập phân)?'''
                                 %(latex(T), latex(k), latex(f_denom)))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq_str))
                da_s1 = '$%s$' % (s_vals[0])
                da_s2 = '$%s$' % (s_vals[1])
                da_s3 = '$%s$' % (s_vals[2])

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Chú thích: Sử dụng công thức cấp số nhân
                loigiai = ('''Sau mỗi giờ, lượng lá bèo phủ trên mặt nước tăng theo cấp số nhân có số hạng đầu $u_1 = 1$, công bội $q = %s$.\\\\
                             Sau $%s$ giờ, lượng lá bèo phủ kín mặt nước là: \\\\
                             $S = 1 + %s + %s^2 + \\dots + %s^{%s} = \\frac{%s^{%s} - 1}{%s - 1} = \\frac{%s^{%s} - 1}{%s}$. \\\\
                             Lượng lá bèo cần để phủ $\\frac{1}{%s}$ mặt nước là: $\\frac{%s^{%s} - 1}{%s \\cdot %s}$. \\\\
                             Giả sử sau $t$ giờ, lá bèo phủ kín được $\\frac{1}{%s}$ mặt nước, ta có: \\\\
                             $1 + %s + %s^2 + \\dots + %s^t = \\frac{%s^{t+1} - 1}{%s} = \\frac{%s^{%s} - 1}{%s}$. \\\\
                             $\\Leftrightarrow %s^{t+1} = \\frac{%s^{%s} - 1}{%s} + 1 \\Leftrightarrow t \\approx %s$.'''
                           %(latex(k), latex(T), latex(k), latex(k), latex(k), latex(T), 
                             latex(k), latex(T+1), latex(k), latex(k), latex(T+1), latex(k-1),
                             latex(f_denom), latex(k), latex(T+1), latex(k-1), latex(f_denom),
                             latex(f_denom), latex(k), latex(k), latex(k), latex(k), latex(k-1),
                             latex(k), latex(T+1), latex(f_denom * (k-1)),
                             latex(k), latex(k), latex(T+1), latex(f_denom), kq_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

