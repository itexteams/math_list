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


def bt_dang48_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Danh sách các bộ số (x1, d1, x2, d2)
        ds_bo_so = [
            (Decimal('9.84'), Decimal('0.06'), Decimal('9.72'), Decimal('0.04')),
            (Decimal('8.56'), Decimal('0.05'), Decimal('8.42'), Decimal('0.03')),
            (Decimal('7.95'), Decimal('0.04'), Decimal('7.85'), Decimal('0.06')),
            (Decimal('6.78'), Decimal('0.05'), Decimal('6.65'), Decimal('0.03')),
            (Decimal('5.45'), Decimal('0.03'), Decimal('5.35'), Decimal('0.05')),
            (Decimal('12.35'), Decimal('0.08'), Decimal('12.15'), Decimal('0.05')),
            (Decimal('15.40'), Decimal('0.06'), Decimal('15.20'), Decimal('0.09'))
        ]
        dec_x1, dec_d1, dec_x2, dec_d2 = random.choice(ds_bo_so)
    
        # Tính sai số tương đối làm tròn 5 chữ số thập phân
        val_delta1 = dec_d1 / dec_x1
        val_delta2 = dec_d2 / dec_x2
    
        round_delta1 = val_delta1.quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)
        round_delta2 = val_delta2.quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)
    
        round_pct1 = (round_delta1 * Decimal('100')).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
        round_pct2 = (round_delta2 * Decimal('100')).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
    
        # Định dạng dấu phẩy tiếng Việt
        str_x1 = f"{dec_x1:.2f}".replace('.', ',')
        str_d1 = f"{dec_d1:.2f}".replace('.', ',')
        str_x2 = f"{dec_x2:.2f}".replace('.', ',')
        str_d2 = f"{dec_d2:.2f}".replace('.', ',')
    
        str_delta1 = f"{round_delta1:.5f}".replace('.', ',')
        str_delta2 = f"{round_delta2:.5f}".replace('.', ',')
        str_pct1 = f"{round_pct1:.3f}".replace('.', ',')
        str_pct2 = f"{round_pct2:.3f}".replace('.', ',')
    
        # Xác định đáp án đúng và lời giải tương ứng
        if round_delta1 < round_delta2:
            da = 'Phương pháp thứ nhất'
            das_sai = 'Phương pháp thứ hai'
            so_sanh = 'Vì $%s < %s$, phương pháp thứ nhất chính xác hơn.' % (str_pct1, str_pct2)
        elif round_delta2 < round_delta1:
            da = 'Phương pháp thứ hai'
            das_sai = 'Phương pháp thứ nhất'
            so_sanh = 'Vì $%s < %s$, phương pháp thứ hai chính xác hơn.' % (str_pct2, str_pct1)
        else:
            da = 'Hai phương pháp như nhau'
            das_sai = 'Phương pháp thứ nhất'
            so_sanh = 'Vì $%s = %s$, hai phương pháp như nhau.' % (str_pct1, str_pct2)
    
        das1 = 'Hai phương pháp như nhau' if da != 'Hai phương pháp như nhau' else 'Phương pháp thứ nhất'
        das2 = das_sai
        das3 = 'Không thể so sánh'
    
        # Câu hỏi
        noidungcauhoi = ('''Hai phương pháp đo cho kết quả $x_1 = %s \\pm %s, x_2 = %s \\pm %s$. Xét theo sai số tương đối, phương pháp chính xác hơn là'''
                         % (str_x1, str_d1, str_x2, str_d2)
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
        loigiai = ('''Phương pháp thứ nhất: $\\delta_1 \\le \\frac{%s}{%s} \\approx %s$, tức khoảng $%s$ phần trăm.\\\\
    Phương pháp thứ hai: $\\delta_2 \\le \\frac{%s}{%s} \\approx %s$, tức khoảng $%s$ phần trăm.\\\\
    %s'''
                   % (str_d1, str_x1, str_delta1, str_pct1,
                      str_d2, str_x2, str_delta2, str_pct2,
                      so_sanh)
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
    