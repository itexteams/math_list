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


def bt_dang41_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Danh sách các bộ số (a1, d1, a2, d2) đảm bảo tính toán đẹp và ra số thập phân hữu hạn
        ds_bo_so = [
            (80, Decimal('0.8'), 30, Decimal('0.45')),
            (60, Decimal('0.6'), 40, Decimal('0.8')),
            (50, Decimal('0.5'), 25, Decimal('0.5')),
            (100, Decimal('0.5'), 50, Decimal('0.4')),
            (80, Decimal('0.4'), 50, Decimal('0.4')),
            (120, Decimal('0.6'), 40, Decimal('0.3')),
            (90, Decimal('0.9'), 60, Decimal('0.9')),
            (75, Decimal('0.75'), 50, Decimal('0.75'))
        ]
        a1, d1, a2, d2 = random.choice(ds_bo_so)
    
        # Tính cận trên sai số tương đối
        r1 = d1 / Decimal(str(a1))
        r2 = d2 / Decimal(str(a2))
        pct1 = r1 * Decimal('100')
        pct2 = r2 * Decimal('100')
    
        # Định dạng dấu phẩy theo quy tắc
        str_d1 = f"{d1}".replace('.', ',')
        str_d2 = f"{d2}".replace('.', ',')
        str_r1 = f"{r1}".replace('.', ',')
        str_r2 = f"{r2}".replace('.', ',')
        str_pct1 = f"{pct1}".replace('.', ',')
        str_pct2 = f"{pct2}".replace('.', ',')
    
        # Xác định đáp án đúng và lời giải tương ứng
        if r1 < r2:
            da = 'Phép đo thứ nhất'
            das_sai_chon = 'Phép đo thứ hai'
            so_sanh = 'Vì $%s < %s$, phép đo thứ nhất có sai số tương đối nhỏ hơn.' % (str_pct1, str_pct2)
        elif r1 > r2:
            da = 'Phép đo thứ hai'
            das_sai_chon = 'Phép đo thứ nhất'
            so_sanh = 'Vì $%s < %s$, phép đo thứ hai có sai số tương đối nhỏ hơn.' % (str_pct2, str_pct1)
        else:
            da = 'Hai phép đo có sai số tương đối bằng nhau'
            das_sai_chon = 'Phép đo thứ nhất'
            so_sanh = 'Vì $%s = %s$, hai phép đo có sai số tương đối bằng nhau.' % (str_pct1, str_pct2)
    
        das1 = 'Hai phép đo có sai số tương đối bằng nhau' if da != 'Hai phép đo có sai số tương đối bằng nhau' else 'Phép đo thứ hai'
        das2 = 'Không thể so sánh'
        das3 = das_sai_chon
    
        # Câu hỏi
        noidungcauhoi = ('''Hai phép đo cùng một loại đại lượng cho kết quả: $a_1 = %s \\pm %s$, $a_2 = %s \\pm %s$. Phép đo nào có sai số tương đối nhỏ hơn?'''
                         % (latex(a1), str_d1, latex(a2), str_d2)
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
        loigiai = ('''Phép đo thứ nhất có cận trên sai số tương đối $\\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    Phép đo thứ hai có cận trên sai số tương đối $\\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    %s'''
                   % (str_d1, latex(a1), str_r1, str_pct1,
                      str_d2, latex(a2), str_r2, str_pct2,
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
    