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


def bt_dang13_p4_b3_c6_ds11(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
            def format_dec(val):
                return str(float(val)).replace('.', ',')

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Tìm cách random bài toán
                # Chọn xác suất bắn trúng của 3 xạ thủ (p1, p2, p3)
                p1_val = random.choice([0.7, 0.75, 0.8, 0.85])
                p2_val = random.choice([0.6, 0.65, 0.55, 0.5])
                p3_val = random.choice([0.4, 0.45, 0.5, 0.35])

                # Tính xác suất bắn trượt (biến cố đối)
                q1_val = round(1 - p1_val, 2)
                q2_val = round(1 - p2_val, 2)
                q3_val = round(1 - p3_val, 2)

                # Xác suất không ai bắn trúng
                p_bar_val = round(q1_val * q2_val * q3_val, 4)

                # Xác suất có ít nhất một người bắn trúng (Đáp án đúng)
                kq_val = round(1 - p_bar_val, 4)

                # Chuyển sang định dạng chuỗi có dấu phẩy để hiển thị
                p1 = format_dec(p1_val)
                p2 = format_dec(p2_val)
                p3 = format_dec(p3_val)
                q1 = format_dec(q1_val)
                q2 = format_dec(q2_val)
                q3 = format_dec(q3_val)
                p_bar = format_dec(p_bar_val)
                kq = format_dec(kq_val)

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                # Sai lầm 1: Nhân trực tiếp các xác suất trúng
                s1 = round(p1_val * p2_val * p3_val, 2)
                # Sai lầm 2: Lấy xác suất của biến cố đối (không ai trúng)
                s2 = p_bar_val
                # Sai lầm 3: Tổng các xác suất (nếu nhỏ hơn 1) hoặc một giá trị ngẫu nhiên
                s3 = round(kq_val - 0.15, 2)
                s4 = round(kq_val - 0.2, 2)
                s5 = 0.8
                s6 = 0.45

                list_s_raw = [s1, s2, s3, s4, s5, s6]
                for val in list_s_raw:
                    if val != kq_val and val > 0:
                        s.add(format_dec(val))

                s_list = list(s)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Bước 2: Viết lại đề bài và lời giải theo mẫu
                # Câu hỏi
                noidungcauhoi = ('''Ba xạ thủ độc lập cùng bắn vào $1$ tấm bia. Biết rằng xác suất bắn trúng mục tiêu của ba người đó lần lượt là $%s$; $%s$; $%s$. Tính xác suất để có ít nhất một xạ thủ bắn trúng.'''
                                 %(p1, p2, p3))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq))
                da_s1 = '$%s$' % (das1)
                da_s2 = '$%s$' % (das2)
                da_s3 = '$%s$' % (das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Chi tiết, không viết tắt, dùng \left \right)
                loigiai = ('''Gọi biến cố $A$: “Có ít nhất một xạ thủ bắn trúng mục tiêu”.\\\\
                             $A_i$: “Người thứ $i$ bắn trúng mục tiêu”; $i \\in \\left\\{1; 2; 3\\right\\}$.\\\\
                             Lúc đó: $\\overline{A}$ là biến cố không có xạ thủ nào bắn trúng mục tiêu và $\\overline{A} = \\overline{A_1} \\cdot \\overline{A_2} \\cdot \\overline{A_3}$.\\\\
                             Vì $\\overline{A_1}, \\overline{A_2}, \\overline{A_3}$ là các biến cố độc lập nên:\\\\
                             $P\\left(\\overline{A}\\right) = P\\left(\\overline{A_1} \\cdot \\overline{A_2} \\cdot \\overline{A_3}\\right) = P\\left(\\overline{A_1}\\right) \\cdot P\\left(\\overline{A_2}\\right) \\cdot P\\left(\\overline{A_3}\\right) = %s \\cdot %s \\cdot %s = %s$.\\\\
                             Vậy: $P\\left(A\\right) = 1 - P\\left(\\overline{A}\\right) = 1 - %s = %s$.'''
                           %(q1, q2, q3, p_bar, p_bar, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

