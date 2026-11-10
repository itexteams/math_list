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


def bt_dang45_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Danh sách các bộ số (m_P, d_P, m_Q, d_Q) đảm bảo phép chia ra số thập phân đẹp
        ds_bo_so = [
            (Decimal('2.5'), Decimal('0.02'), Decimal('20'), Decimal('0.10')),
            (Decimal('2.0'), Decimal('0.02'), Decimal('25'), Decimal('0.10')),
            (Decimal('5.0'), Decimal('0.05'), Decimal('10'), Decimal('0.05')),
            (Decimal('10'), Decimal('0.04'), Decimal('2.5'), Decimal('0.02')),
            (Decimal('25'), Decimal('0.10'), Decimal('5.0'), Decimal('0.05')),
            (Decimal('50'), Decimal('0.15'), Decimal('10'), Decimal('0.05')),
            (Decimal('4.0'), Decimal('0.04'), Decimal('20'), Decimal('0.08')),
            (Decimal('15'), Decimal('0.06'), Decimal('5.0'), Decimal('0.03'))
        ]
        m_P, d_P, m_Q, d_Q = random.choice(ds_bo_so)
    
        # Tính cận trên sai số tương đối delta
        delta_P = d_P / m_P
        delta_Q = d_Q / m_Q
        pct_P = delta_P * Decimal('100')
        pct_Q = delta_Q * Decimal('100')
    
        # Định dạng dấu phẩy theo chuẩn Việt Nam
        str_mP = f"{m_P}".replace('.', ',')
        str_dP = f"{d_P:.2f}".replace('.', ',')
        str_mQ = f"{m_Q}".replace('.', ',')
        str_dQ = f"{d_Q:.2f}".replace('.', ',')
    
        str_deltaP = f"{delta_P}".replace('.', ',')
        str_deltaQ = f"{delta_Q}".replace('.', ',')
        str_pctP = f"{pct_P}".replace('.', ',')
        str_pctQ = f"{pct_Q}".replace('.', ',')
    
        # Bảng số liệu dạng LaTeX
        bang_du_lieu = '''\\begin{center}
    \\begin{tabular}{|c|c|}
    \\hline
    \\textbf{Dây chuyền} & \\textbf{Khối lượng ghi trên bao} \\\\
    \\hline
    P & $%s \\pm %s\\text{ kg}$ \\\\
    \\hline
    Q & $%s \\pm %s\\text{ kg}$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (str_mP, str_dP, str_mQ, str_dQ)
    
        # Xác định đáp án đúng và lời giải
        if delta_P < delta_Q:
            da = 'Dây chuyền P'
            das_sai = 'Dây chuyền Q'
            ket_luan = 'Vì $%s < %s$, dây chuyền P cho kết quả chính xác hơn.' % (str_pctP, str_pctQ)
        elif delta_Q < delta_P:
            da = 'Dây chuyền Q'
            das_sai = 'Dây chuyền P'
            ket_luan = 'Vì $%s < %s$, dây chuyền Q cho kết quả chính xác hơn.' % (str_pctQ, str_pctP)
        else:
            da = 'Hai dây chuyền như nhau'
            das_sai = 'Dây chuyền P'
            ket_luan = 'Vì $%s = %s$, hai dây chuyền cho kết quả chính xác như nhau.' % (str_pctP, str_pctQ)
    
        das1 = 'Hai dây chuyền như nhau' if da != 'Hai dây chuyền như nhau' else 'Dây chuyền P'
        das2 = das_sai
        das3 = 'Không đủ dữ kiện'
    
        # Câu hỏi
        noidungcauhoi = ('''Hai dây chuyền đóng gói cho kết quả:
    %s
    Xét theo sai số tương đối, dây chuyền nào cho kết quả chính xác hơn?'''
                         % bang_du_lieu
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
        loigiai = ('''Dây chuyền P có cận trên sai số tương đối $\\delta_P \\le \\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    Dây chuyền Q có cận trên sai số tương đối $\\delta_Q \\le \\frac{%s}{%s} = %s$, tức $%s$ phần trăm.\\\\
    %s'''
                   % (str_dP, str_mP, str_deltaP, str_pctP,
                      str_dQ, str_mQ, str_deltaQ, str_pctQ,
                      ket_luan)
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
    