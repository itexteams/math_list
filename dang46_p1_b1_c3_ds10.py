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


def bt_dang46_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Danh sách các độ chia / vạch chia nhỏ nhất thường gặp và đơn vị tương ứng
        ds_vach = [
            (Decimal('0.2'), 'cm'),
            (Decimal('0.1'), 'cm'),
            (Decimal('0.5'), 'cm'),
            (Decimal('1'), 'cm'),
            (Decimal('1'), 'mm'),
            (Decimal('2'), 'mm'),
            (Decimal('0.2'), 'm')
        ]
        dec_vach, don_vi = random.choice(ds_vach)
        
        # Độ chính xác bằng một nửa vạch chia nhỏ nhất: d = vach / 2
        dec_d = dec_vach / Decimal('2')
        
        # Định dạng chuỗi hiển thị số thập phân dùng dấu phẩy
        str_vach = f"{dec_vach}".replace('.', ',')
        str_d = f"{dec_d}".replace('.', ',')
        
        # Tạo các phương án sai theo mẫu đề gốc:
        # B: chính bằng vạch chia nhỏ nhất
        sai_1 = str_vach
        # C: gấp đôi vạch chia nhỏ nhất
        sai_2 = f"{dec_vach * Decimal('2')}".replace('.', ',')
        # D: một giá trị nguyên khác hoặc 1
        sai_3 = '1' if str_d != '1' and str_vach != '1' else '0,5'
        
        tap_sai = set()
        for s_val in [sai_1, sai_2, sai_3]:
            if s_val != str_d:
                tap_sai.add(s_val)
                
        # Bổ sung các phương án sai nếu bị trùng lặp
        buoc = Decimal('0.3')
        while len(tap_sai) < 3:
            cand = f"{dec_d + buoc}".replace('.', ',')
            if cand != str_d:
                tap_sai.add(cand)
            buoc += Decimal('0.2')
            
        ds_sai = list(tap_sai)[:3]
        
        # Các đáp án trắc nghiệm (không có dấu chấm ở cuối)
        da = '$%s$ %s' % (str_d, don_vi)
        das1 = '$%s$ %s' % (ds_sai[0], don_vi)
        das2 = '$%s$ %s' % (ds_sai[1], don_vi)
        das3 = '$%s$ %s' % (ds_sai[2], don_vi)
    
        # Câu hỏi
        noidungcauhoi = ('''Một thước có vạch chia nhỏ nhất là $%s$ %s. Theo chú ý trong bài học, khi đo trực tiếp bằng thước này có thể lấy độ chính xác bằng'''
                         % (str_vach, don_vi)
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
        loigiai = ('''Theo chú ý trong bài học, trong phép đo trực tiếp có thể lấy độ chính xác bằng một nửa đơn vị của vạch chia nhỏ nhất.\\\\
    Vạch chia nhỏ nhất là $%s$ %s, nên $d = \\frac{%s}{2} = %s$.\\\\
    Vậy có thể lấy độ chính xác bằng $%s$ %s.'''
                   % (str_vach, don_vi, str_vach, str_d,
                      str_d, don_vi)
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
    