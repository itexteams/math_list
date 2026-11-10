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


def bt_dang47_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Danh sách các bộ số (dân số a, độ chính xác d) đảm bảo phép chia ra số thập phân hữu hạn đẹp
        ds_bo_so = [
            (1250000, 10000),
            (2500000, 10000),
            (2000000, 10000),
            (1600000, 8000),
            (1500000, 15000),
            (800000, 4000),
            (500000, 2000),
            (1250000, 5000),
            (2000000, 4000)
        ]
        a, d = random.choice(ds_bo_so)
    
        dec_a = Decimal(str(a))
        dec_d = Decimal(str(d))
        val_tp = dec_d / dec_a
        val_pct = val_tp * Decimal('100')
    
        # Định dạng dấu phẩy theo chuẩn tiếng Việt
        str_tp = f"{val_tp}".replace('.', ',')
        str_pct = f"{val_pct}".replace('.', ',')
    
        # Tạo các phương án sai theo mẫu đề gốc (8%, 0,08%, 1,25%, ...)
        sai_1 = f"{val_pct * Decimal('10')}".replace('.', ',')
        sai_2 = f"{val_pct / Decimal('10')}".replace('.', ',')
        # Thêm phương án gây nhiễu từ các chữ số đầu của dân số
        str_dau = str(a).rstrip('0')
        if len(str_dau) >= 2:
            sai_3 = f"{Decimal(str_dau) / Decimal('100')}".replace('.', ',')
        else:
            sai_3 = f"{val_pct * Decimal('2')}".replace('.', ',')
    
        tap_sai = set()
        for s_val in [sai_1, sai_2, sai_3]:
            if s_val != str_pct:
                tap_sai.add(s_val)
    
        # Đảm bảo đủ 3 phương án sai phân biệt và khác phương án đúng
        buoc = Decimal('0.5')
        while len(tap_sai) < 3:
            cand = f"{val_pct + buoc}".replace('.', ',')
            if cand != str_pct:
                tap_sai.add(cand)
            buoc += Decimal('0.5')
    
        ds_sai = list(tap_sai)[:3]
    
        # Các đáp án trắc nghiệm (không có dấu chấm ở cuối)
        da = '$%s\\%%$' % str_pct
        das1 = '$%s\\%%$' % ds_sai[0]
        das2 = '$%s\\%%$' % ds_sai[1]
        das3 = '$%s\\%%$' % ds_sai[2]
    
        # Câu hỏi
        noidungcauhoi = ('''Dân số một khu vực được công bố là $%s \\pm %s$ người. Sai số tương đối không vượt quá'''
                         % (latex(a), latex(d))
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
        loigiai = ('''Cận trên của sai số tương đối là $\\delta \\le \\frac{%s}{%s} = %s$.\\\\
    Đổi sang phần trăm: $%s \\cdot 100 = %s$.\\\\
    Vậy sai số tương đối không vượt quá $%s$ phần trăm.'''
                   % (latex(d), latex(a), str_tp,
                      str_tp, str_pct,
                      str_pct)
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
    