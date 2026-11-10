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


def bt_dang35_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random phần nguyên và phần thập phân của số đúng
        nguyen = random.randint(15, 60)
        # Chọn phần thập phân 2 chữ số sao cho chữ số thứ hai không phải 0 (ví dụ từ 31 đến 39 hoặc 51 đến 59, ...)
        thap_phan_2 = random.choice([i for i in range(11, 99) if i % 10 != 0])
        
        # Tạo số đúng có 2 chữ số thập phân
        str_so_dung = f"{nguyen}.{thap_phan_2:02d}"
        dec_so_dung = Decimal(str_so_dung)
        
        # Số gần đúng làm tròn đến chữ số thập phân thứ nhất
        dec_so_gan_dung = dec_so_dung.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        str_so_gan_dung = f"{dec_so_gan_dung:.1f}"
        
        # Sai số tuyệt đối
        delta = abs(dec_so_dung - dec_so_gan_dung)
        
        # Chuỗi hiển thị dùng dấu phẩy
        str_dung_vn = str_so_dung.replace('.', ',')
        str_gandung_vn = str_so_gan_dung.replace('.', ',')
        str_delta_vn = f"{delta}".replace('.', ',')
        
        # Các giá trị nhiễu dựa theo mẫu gốc
        s_nhiieu_1 = f"{Decimal(thap_phan_2 % 10) / Decimal('10')}".replace('.', ',')
        s_nhiieu_2 = f"{Decimal(thap_phan_2) / Decimal('1000')}".replace('.', ',')
        s_nhiieu_3 = f"{delta + Decimal('0.1')}".replace('.', ',')
        
        tap_sai = set()
        for val_cand in [s_nhiieu_1, s_nhiieu_2, s_nhiieu_3]:
            if val_cand != str_delta_vn:
                tap_sai.add(val_cand)
                
        # Đảm bảo đủ 3 đáp án sai phân biệt
        d_offset = Decimal('0.01')
        while len(tap_sai) < 3:
            cand = f"{delta + d_offset}".replace('.', ',')
            if cand != str_delta_vn:
                tap_sai.add(cand)
            d_offset += Decimal('0.02')
            
        ds_sai = list(tap_sai)[:3]
        
        # Các đáp án trắc nghiệm
        da = '$%s$' % str_delta_vn
        das1 = '$%s$' % ds_sai[0]
        das2 = '$%s$' % ds_sai[1]
        das3 = '$%s$' % ds_sai[2]
        
        # Câu hỏi
        noidungcauhoi = ('''Số đúng là $%s$ và số gần đúng là $%s$. Sai số tuyệt đối bằng'''
                         % (str_dung_vn, str_gandung_vn)
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
        loigiai = ('''Sai số tuyệt đối là $\\Delta_a = |%s - %s|$.\\\\
    Tính được $\\Delta_a = %s$.'''
                   % (str_dung_vn, str_gandung_vn, str_delta_vn)
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
    