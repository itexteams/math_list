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


def bt_dang32_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi (để mở rộng sau này)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Tổng số tiền (triệu đồng)
                A_tong = random.choice([400, 500, 600, 800]) 
                # Số tiền gửi khoản 1 (triệu đồng)
                A1 = random.choice([200, 250, 300, 450])
                if A1 >= A_tong: A1 = A_tong - 100
                A2 = A_tong - A1

                # Lãi suất khoản 2 (cố định hoặc random nhẹ)
                r2_val = random.choice([0.2, 0.25, 0.3, 0.35])

                # Đáp án đúng x (lãi suất quý - đơn vị %)
                x_true = random.choice([1.1, 1.2, 1.3, 1.4, 1.5, 1.6])

                # --- Tính toán giá trị S (Tổng tiền cả gốc lẫn lãi sau 1 năm) ---
                # S = A1 * (1 + x/100)^4 + A2 * (1 + r2/100)^12
                S_val = float(A1 * (1 + x_true/100)**4 + A2 * (1 + r2_val/100)**12)

                # Định dạng hiển thị tiền: 416.780.000 đồng tương đương 416,78 triệu
                # Làm tròn S đến 3 chữ số thập phân để đẹp số tiền đồng
                S_rounded = Decimal(str(S_val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
                S_display = str(S_rounded).replace('.', ',')
                S_money_full = "{:,.0f}".format(float(S_rounded) * 1000000).replace(',', '.')

                # --- B4: Điều chỉnh các phương án sai ---
                kq = str(x_true).replace('.', ',')
                da = '$%s$' % kq

                # Tạo danh sách đáp án nhiễu
                s = []
                offsets = [-0.2, -0.1, 0.1, 0.2, 0.3, -0.3]
                for offset in offsets:
                    val = round(x_true + offset, 1)
                    if val > 0 and val != x_true:
                        s.append('$%s$' % str(val).replace('.', ','))

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # --- B2: Viết lại nội dung đề bài và lời giải ---
                noidungcauhoi = ('''Anh Dũng đem gửi tiết kiệm số tiền là %s triệu đồng ở hai loại kỳ hạn khác nhau. Anh gửi %s triệu đồng theo kỳ hạn 3 tháng với lãi suất $x\\%%$ một quý. Số tiền còn lại anh gửi theo kỳ hạn 1 tháng với lãi suất $%s\\%%$ một tháng. Biết rằng nếu không rút lãi thì số lãi sẽ được nhập vào số gốc để tính lãi cho kỳ hạn tiếp theo. Sau một năm số tiền cả gốc và lãi của anh là %s đồng. Tính $x$.'''
                                 % (A_tong, A1, str(r2_val).replace('.', ','), S_money_full))

                # Nội dung lời giải chi tiết
                loigiai = ('''Số tiền gửi ở kỳ hạn 1 tháng là $%s - %s = %s$ (triệu đồng).\\\\
                             Sau một năm (4 quý), số tiền cả gốc và lãi của khoản gửi kỳ hạn 3 tháng là: $T_1 = %s(1 + x\\%%)^4$.\\\\
                             Sau một năm (12 tháng), số tiền cả gốc và lãi của khoản gửi kỳ hạn 1 tháng là: $T_2 = %s(1 + %s\\%%)^{12}$.\\\\
                             Theo đề bài, tổng số tiền sau 1 năm là %s triệu đồng, ta có phương trình:\\\\
                             $%s(1 + x\\%%)^4 + %s(1 + %s\\%%)^{12} = %s$\\\\
                             $\\Leftrightarrow %s(1 + x\\%%)^4 \\approx %s$\\\\
                             $\\Leftrightarrow (1 + x\\%%)^4 \\approx %s \\Leftrightarrow 1 + x\\%% \\approx %s \\Leftrightarrow x \\approx %s$.'''
                           % (A_tong, A1, A2, 
                              A1, 
                              A2, str(r2_val).replace('.', ','),
                              S_display,
                              A1, A2, str(r2_val).replace('.', ','), S_display,
                              A1, round(float(S_rounded) - A2*(1+r2_val/100)**12, 4),
                              round((float(S_rounded) - A2*(1+r2_val/100)**12)/A1, 4),
                              round(((float(S_rounded) - A2*(1+r2_val/100)**12)/A1)**(1/4), 4),
                              kq))

                # --- Xuất câu trắc nghiệm ---
                da_d = '\\True ' + str(da)
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

