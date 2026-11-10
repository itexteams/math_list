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


def bt_dang37_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random phần nguyên và phần thập phân của kết quả đo (số gần đúng)
        nguyen = random.randint(12, 45)
        tp1 = random.randint(1, 9)
        dec_a = Decimal(str(nguyen)) + Decimal(str(tp1)) / Decimal('10')
        
        # Random độ lệch giữa số đúng và số gần đúng (từ 0.02 đến 0.09)
        lech = random.choice([2, 3, 4, 5, 6, 7, 8, 9])
        dec_lech = Decimal(str(lech)) / Decimal('100')
        
        # Random số đúng có thể lớn hơn hoặc nhỏ hơn số gần đúng
        dau = random.choice([-1, 1])
        dec_so_dung = dec_a + dau * dec_lech
        
        # Sai số tuyệt đối
        delta = abs(dec_so_dung - dec_a)
        
        # Định dạng chuỗi hiển thị số thập phân dùng dấu phẩy
        str_a = f"{dec_a:.1f}".replace('.', ',')
        str_so_dung = f"{dec_so_dung:.2f}".replace('.', ',')
        str_delta = f"{delta:.2f}".replace('.', ',')
        
        # Đơn vị đo
        don_vi = random.choice(['cm', 'm', 'dm', 'mm'])
        
        # Tạo các phương án sai nhiễu
        sai_1 = f"{Decimal(tp1) / Decimal('10'):.1f}".replace('.', ',')
        sai_2 = f"{abs(Decimal('1') - Decimal(str_so_dung.split(',')[1]) / Decimal('100')):.2f}".replace('.', ',')
        sai_3 = f"{delta + Decimal('0.1'):.2f}".replace('.', ',')
        
        tap_sai = set()
        for s_val in [sai_1, sai_2, sai_3]:
            if s_val != str_delta:
                tap_sai.add(s_val)
                
        # Bổ sung các phương án sai phân biệt nếu bị trùng
        buoc = Decimal('0.02')
        while len(tap_sai) < 3:
            cand = f"{delta + buoc:.2f}".replace('.', ',')
            if cand != str_delta:
                tap_sai.add(cand)
            buoc += Decimal('0.03')
            
        ds_sai = list(tap_sai)[:3]
        
        # Các đáp án trắc nghiệm (không có dấu chấm ở cuối phương án)
        da = '$%s$ %s' % (str_delta, don_vi)
        das1 = '$%s$ %s' % (ds_sai[0], don_vi)
        das2 = '$%s$ %s' % (ds_sai[1], don_vi)
        das3 = '$%s$ %s' % (ds_sai[2], don_vi)
    
        # Câu hỏi
        noidungcauhoi = ('''Một phép đo chiều dài cho kết quả $%s$ %s, biết số đúng là $%s$ %s. Sai số tuyệt đối của phép đo là'''
                         % (str_a, don_vi, str_so_dung, don_vi)
                         )
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Sai số tuyệt đối của phép đo là $\\Delta = |%s - %s| = %s$.\\\\
    Vậy sai số tuyệt đối bằng $%s$ %s.'''
                   % (str_so_dung, str_a, str_delta, str_delta, don_vi)
                   )
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
    