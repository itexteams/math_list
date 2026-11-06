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


def bt_dang6_p4_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn ngẫu nhiên P(A) và P(B) là các số thập phân từ 0.1 đến 0.8
                p_a_val = random.randint(2, 8) / 10
                p_b_val = random.randint(2, 8) / 10

                # Tạo biến cố độc lập hoặc không độc lập
                is_independent = random.choice([True, False])

                if is_independent:
                    p_ab_val = round(p_a_val * p_b_val, 2)
                else:
                    # Nếu không độc lập, ta lấy tích rồi cộng/trừ một khoảng nhỏ (đảm bảo 0 < P(AB) < min(P(A),P(B)))
                    p_ab_val = round(p_a_val * p_b_val + 0.11, 2) 
                    if p_ab_val >= min(p_a_val, p_b_val) or p_ab_val >= 1:
                        p_ab_val = round(abs(p_a_val * p_b_val - 0.13), 2)

                # Chuyển định dạng số thập phân sang string dùng dấu phẩy theo yêu cầu
                pa_str = str(p_a_val).replace('.', ',')
                pb_str = str(p_b_val).replace('.', ',')
                pab_str = str(p_ab_val).replace('.', ',')

                # Kiểm tra mệnh đề đúng
                # Trong bài toán gốc, đáp án đúng là C hoặc D tùy thuộc vào tích
                check_val = round(p_a_val * p_b_val, 2)
                check_str = str(check_val).replace('.', ',')

                if p_ab_val == check_val:
                    da_dung = "A và B là hai biến cố độc lập"
                    # B4: Điều chỉnh các phương án sai
                    s = ["A và B là hai biến cố xung khắc",
                         "A và B là hai biến cố đối",
                         "A và B là hai biến cố không độc lập"]
                else:
                    da_dung = "A và B là hai biến cố không độc lập"
                    s = ["A và B là hai biến cố xung khắc",
                         "A và B là hai biến cố đối",
                         "A và B là hai biến cố độc lập"]

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # B2: Viết lại đề bài theo mẫu
                noidungcauhoi = ('''Cho $A$ và $B$ là hai biến cố. Biết $P\\left( A \\right) = %s; P\\left( B \\right) = %s; P\\left( AB \\right) = %s$. Xét tính độc lập của hai biến cố.'''
                                 %(pa_str, pb_str, pab_str))

                da_d = ('\\True ' + da_dung)
                da_s1 = das1
                da_s2 = das2
                da_s3 = das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (không viết tắt)
                if p_ab_val == check_val:
                    ket_luan = "bằng $P\\left( AB \\right)$ nên hai biến cố $A$ và $B$ độc lập."
                else:
                    ket_luan = "khác $P\\left( AB \\right)$ nên hai biến cố $A$ và $B$ không độc lập."

                loigiai = ('''Ta có $P\\left( A \\right) \\cdot P\\left( B \\right) = %s \\cdot %s = %s$. \\\\
                             Vì $P\\left( A \\right) \\cdot P\\left( B \\right) %s %s$. \\\\
                             Do đó, %s'''
                           %(pa_str, pb_str, check_str, 
                             "=" if p_ab_val == check_val else "\\neq", 
                             pab_str,
                             da_dung))

            # B1: Xuất câu trắc nghiệm theo đúng cấu trúc content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

