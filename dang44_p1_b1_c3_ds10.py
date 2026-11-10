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


def bt_dang44_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Danh sách các bộ số (m1, d1, m2, d2) đảm bảo tính toán đẹp ra số thập phân hữu hạn
        ds_bo_so = [
            (Decimal('5.0'), Decimal('0.04'), Decimal('20.0'), Decimal('0.10')),
            (Decimal('4.0'), Decimal('0.04'), Decimal('25.0'), Decimal('0.15')),
            (Decimal('10.0'), Decimal('0.08'), Decimal('50.0'), Decimal('0.20')),
            (Decimal('8.0'), Decimal('0.06'), Decimal('40.0'), Decimal('0.16')),
            (Decimal('5.0'), Decimal('0.05'), Decimal('25.0'), Decimal('0.10')),
            (Decimal('20.0'), Decimal('0.10'), Decimal('5.0'), Decimal('0.04')),
            (Decimal('10.0'), Decimal('0.05'), Decimal('40.0'), Decimal('0.30')),
            (Decimal('5.0'), Decimal('0.03'), Decimal('20.0'), Decimal('0.08'))
        ]
        m1, d1, m2, d2 = random.choice(ds_bo_so)
    
        # Tính cận trên sai số tương đối delta
        r1 = d1 / m1
        r2 = d2 / m2
        pct1 = r1 * Decimal('100')
        pct2 = r2 * Decimal('100')
    
        # Định dạng chuỗi hiển thị dấu phẩy
        str_m1 = f"{m1:.1f}".replace('.', ',')
        str_d1 = f"{d1:.2f}".replace('.', ',')
        str_m2 = f"{m2:.1f}".replace('.', ',')
        str_d2 = f"{d2:.2f}".replace('.', ',')
        str_r1 = f"{r1}".replace('.', ',')
        str_r2 = f"{r2}".replace('.', ',')
        str_pct1 = f"{pct1}".replace('.', ',')
        str_pct2 = f"{pct2}".replace('.', ',')
    
        # Xác định đáp án đúng và lời giải
        if r1 < r2:
            da = 'Máy thứ nhất cho kết quả chính xác hơn'
            sai_khac = 'Máy thứ hai cho kết quả chính xác hơn'
            cau_so_sanh = 'Vì $%s < %s$, máy thứ nhất cho kết quả chính xác hơn xét theo sai số tương đối.' % (str_pct1, str_pct2)
        elif r1 > r2:
            da = 'Máy thứ hai cho kết quả chính xác hơn'
            sai_khac = 'Máy thứ nhất cho kết quả chính xác hơn'
            cau_so_sanh = 'Vì $%s < %s$, máy thứ hai cho kết quả chính xác hơn xét theo sai số tương đối.' % (str_pct2, str_pct1)
        else:
            da = 'Hai máy chính xác như nhau'
            sai_khac = 'Máy thứ hai cho kết quả chính xác hơn'
            cau_so_sanh = 'Vì $%s = %s$, hai máy chính xác như nhau xét theo sai số tương đối.' % (str_pct1, str_pct2)
    
        das1 = 'Máy thứ nhất chính xác hơn vì sai số tuyệt đối nhỏ hơn'
        das2 = 'Hai máy chính xác như nhau' if da != 'Hai máy chính xác như nhau' else 'Máy thứ nhất cho kết quả chính xác hơn'
        das3 = 'Không thể đánh giá'
    
        # Đảm bảo không trùng với đáp án đúng
        if da == das1:
            das1 = sai_khac
    
        # Câu hỏi
        noidungcauhoi = ('''Hai máy cân cho kết quả: $m_1 = %s \\pm %s$, $m_2 = %s \\pm %s$. Xét theo sai số tương đối, kết luận đúng là'''
                         % (str_m1, str_d1, str_m2, str_d2)
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
        loigiai = ('''Máy thứ nhất: $\\delta_1 \\le \\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    Máy thứ hai: $\\delta_2 \\le \\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    %s'''
                   % (str_d1, str_m1, str_r1, str_pct1,
                      str_d2, str_m2, str_r2, str_pct2,
                      cau_so_sanh)
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
    