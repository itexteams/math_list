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


def bt_dang16_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # 1. Random loại trục sẽ hỏi
        cac_truc = [('hoành', 'Ox'), ('tung', 'Oy'), ('cao', 'Oz')]
        ten_truc, ki_hieu = random.choice(cac_truc)
        # 2. Random một giá trị a khác 0 từ -20 đến 20
        a = random.choice([i for i in range(-20, 21) if i != 0])
        # 3. Tạo 4 điểm phân biệt với biến a (tự động xử lý dấu - chuẩn)
        diem_Ox = (a, 0, 0)
        diem_Oy = (0, a, 0)
        diem_Oz = (0, 0, a)
        diem_khac = (-a, 0, a)
        # Random ngẫu nhiên tên cho 4 điểm để bài toán luôn mới mẻ
        ten_diem = ['M', 'N', 'P', 'Q']
        random.shuffle(ten_diem)

        # 4. Gán đáp án đúng / sai dựa theo trục được chọn
        if ki_hieu == 'Ox':
            d_dung = diem_Ox
            d_sai1 = diem_Oy
            d_sai2 = diem_Oz
            d_sai3 = diem_khac
            dk_loigiai = 'tung độ và cao độ đều bằng $0$ ($y=0$ và $z=0$)'
        elif ki_hieu == 'Oy':
            d_dung = diem_Oy
            d_sai1 = diem_Ox
            d_sai2 = diem_Oz
            d_sai3 = diem_khac
            dk_loigiai = 'hoành độ và cao độ đều bằng $0$ ($x=0$ và $z=0$)'
        else: # Trường hợp hỏi Oz
            d_dung = diem_Oz
            d_sai1 = diem_Ox
            d_sai2 = diem_Oy
            d_sai3 = diem_khac
            dk_loigiai = 'hoành độ và tung độ đều bằng $0$ ($x=0$ và $y=0$)'

        da_str = '%s(%s; %s; %s)' % (ten_diem[0], d_dung[0], d_dung[1], d_dung[2])
        das1_str = '%s(%s; %s; %s)' % (ten_diem[1], d_sai1[0], d_sai1[1], d_sai1[2])
        das2_str = '%s(%s; %s; %s)' % (ten_diem[2], d_sai2[0], d_sai2[1], d_sai2[2])
        das3_str = '%s(%s; %s; %s)' % (ten_diem[3], d_sai3[0], d_sai3[1], d_sai3[2])

        # Các đáp án trắc nghiệm
        du = ['$%s$' % (da_str)]
        da = random.choice(du)

        s = [
             '$%s$' % (das1_str),
             '$%s$' % (das2_str),
             '$%s$' % (das3_str)
            ]

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Câu hỏi (Tự động điền trục Ox, Oy hoặc Oz tương ứng)
        noidungcauhoi = ('Trong không gian $Oxyz$, điểm nào sau đây thuộc trục %s $%s$? ' % (ten_truc, ki_hieu))
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        # Nội dung lời giải (Giải thích thay đổi tự động bám theo câu hỏi)
        loigiai = ('''Điểm nằm trên trục %s $%s$ thì %s. \\\\
                      Trong các điểm đã cho, chỉ có điểm %s thỏa mãn điều kiện này.'''
                   % (ten_truc, ki_hieu, dk_loigiai, da))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

