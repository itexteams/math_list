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


def bt_dang16_p3_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Danh sách các bộ số (a1, d1, a2, d2) đảm bảo tính toán đẹp ra số thập phân hữu hạn
        ds_bo_so = [
            (90, Decimal('0.45'), 200, Decimal('0.60')),
            (80, Decimal('0.40'), 150, Decimal('0.60')),
            (100, Decimal('0.50'), 250, Decimal('0.50')),
            (120, Decimal('0.48'), 160, Decimal('0.80')),
            (60, Decimal('0.30'), 150, Decimal('0.45')),
            (200, Decimal('0.80'), 80, Decimal('0.24')),
            (150, Decimal('0.60'), 100, Decimal('0.30')),
            (250, Decimal('0.75'), 200, Decimal('1.00'))
        ]
        a1, d1, a2, d2 = random.choice(ds_bo_so)
    
        dec_a1 = Decimal(str(a1))
        dec_a2 = Decimal(str(a2))
    
        # Tính sai số tương đối và phần trăm
        delta1 = d1 / dec_a1
        delta2 = d2 / dec_a2
        pct1 = delta1 * Decimal('100')
        pct2 = delta2 * Decimal('100')
    
        # Định dạng hiển thị dấu phẩy theo chuẩn Việt Nam
        str_a1 = str(a1)
        str_d1 = f"{d1:.2f}".replace('.', ',')
        str_delta1 = f"{delta1}".replace('.', ',')
        str_pct1 = f"{pct1}".replace('.', ',')
    
        str_a2 = str(a2)
        str_d2 = f"{d2:.2f}".replace('.', ',')
        str_delta2 = f"{delta2}".replace('.', ',')
        str_pct2 = f"{pct2}".replace('.', ',')
    
        # Tạo bảng hiển thị dữ liệu
        bang_du_lieu = '''\\begin{center}
    \\begin{tabular}{|c|c|}
    \\hline
    \\textbf{Phương pháp} & \\textbf{Kết quả} \\\\
    \\hline
    1 & $%s \\pm %s$ \\\\
    \\hline
    2 & $%s \\pm %s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (str_a1, str_d1, str_a2, str_d2)
    
        # Xác định phương pháp có sai số tương đối nhỏ hơn
        if delta1 < delta2:
            ans_num = 1
            loi_giai_so_sanh = 'Vì $%s < %s$, phương pháp 1 có sai số tương đối nhỏ hơn.' % (str_pct1, str_pct2)
        else:
            ans_num = 2
            loi_giai_so_sanh = 'Vì $%s < %s$, phương pháp 2 có sai số tương đối nhỏ hơn.' % (str_pct2, str_pct1)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Hai phép đo được cho trong bảng:
    %s
    Phương pháp nào có sai số tương đối nhỏ hơn? Trả lời bằng số thứ tự của phương pháp.'''
                         % bang_du_lieu
                         )
    
        # Nội dung lời giải
        loigiai = ('''Phương pháp 1: $\\delta_1 \\le \\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    Phương pháp 2: $\\delta_2 \\le \\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    %s'''
                   % (str_d1, str_a1, str_delta1, str_pct1,
                      str_d2, str_a2, str_delta2, str_pct2,
                      loi_giai_so_sanh)
                   )
    
        # Đáp án ngắn
        dapan = '\\shortans[0]{$%s$}\n' % (ans_num)
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
    