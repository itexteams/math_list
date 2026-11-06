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


def bt_dang27_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM ---
                # S_target: Số tiền mục tiêu (triệu đồng), ví dụ từ 10 đến 100 triệu
                S_target_val = random.choice([10, 20, 30, 50, 100]) 
                S_target_display = S_target_val * 1000000

                # r_percent: Lãi suất mỗi tháng (%) từ 0.4% đến 0.8%
                r_percent = random.choice([0.4, 0.5, 0.6, 0.7, 0.8])
                r = r_percent / 100

                # n_months: Số tháng gửi, từ 10 đến 24 tháng
                n_months = random.randint(10, 24)

                # Tính toán số tiền T hàng tháng theo công thức: 
                # T = (S * r) / ((1 + r) * ((1 + r)^n - 1))
                tu_so = S_target_display * r
                mau_so = (1 + r) * ((1 + r)**n_months - 1)
                T_exact = tu_so / mau_so

                # Làm tròn đến hàng đơn vị (vì tiền đồng thường không để lẻ thập phân)
                kq_val = int(round(T_exact))
                da_dung = f"{kq_val:,}".replace(',', '.') # Định dạng 635.301

                # --- BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN SAI ---
                # Tạo các đáp án sai bằng cách cộng/trừ các khoảng ngẫu nhiên và đảm bảo không trùng
                s_options = set()
                while len(s_options) < 3:
                    sai_lech = random.choice([-2000, -1500, -1000, 1000, 1500, 2000, 5000])
                    temp_sai = kq_val + sai_lech
                    if temp_sai != kq_val:
                        s_options.add(f"{temp_sai:,}".replace(',', '.'))

                list_sai = list(s_options)

                # --- BƯỚC 2: VIẾT LẠI NỘI DUNG THEO MẪU ---
                # Câu hỏi
                noidungcauhoi = ('''Một người mỗi tháng đều đặn gửi vào ngân hàng một khoản tiền $T$ theo hình thức lãi kép với lãi suất $%s\\%%$ mỗi tháng. Biết sau $%s$ tháng người đó có số tiền là $%s$ triệu đồng. Hỏi số tiền $T$ gần với số tiền nào nhất trong các số sau.'''
                                 %(latex(r_percent).replace('.', ','), 
                                   latex(n_months), 
                                   latex(S_target_val)))

                # Các đáp án
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = '$' + str(list_sai[0]) + '$'
                da_s2 = '$' + str(list_sai[1]) + '$'
                da_s3 = '$' + str(list_sai[2]) + '$'

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có: Số tiền cả lãi lẫn gốc sau $%s$ tháng gửi là: $S_{%s} = \\frac{T}{r}(1+r)[(1+r)^{%s} - 1]$ \\\\
                             Vậy: $%s = \\frac{T}{%s}(1+%s)[(1+%s)^{%s} - 1] \\Leftrightarrow T \\approx %s$.'''
                           %(latex(n_months), latex(n_months), latex(n_months),
                             f"{S_target_display:,}".replace(',', '.'), 
                             latex(r), latex(r), latex(r), latex(n_months), 
                             str(da_dung)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

