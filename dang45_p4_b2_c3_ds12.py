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


def bt_dang45_p4_b2_c3_ds12(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN ---
            t_sym = symbols('t')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                # Chọn t_max là số nguyên từ 2 đến 6
                t_max_val = random.randint(2, 6)
                # Chọn n là số nguyên chẵn để n/2 đẹp (từ 2, 4, 6)
                n_val = random.choice([2, 4])
                # Tính m để t_max là số nguyên: m = n * t_max
                m_val = n_val * t_max_val

                # Hàm gia tốc và vận tốc
                a_func = m_val - n_val * t_sym
                v_func = integrate(a_func, t_sym) # hằng số C=0 do xuất phát từ trạng thái dừng

                # Tính quãng đường S = tích phân v(t) từ 0 đến t_max_val
                s_val = integrate(v_func, (t_sym, 0, t_max_val))

                # Đáp án đúng
                kq = s_val
                da_d_str = '$%s$' % latex(kq)

                # Tạo các phương án sai (không trùng với đáp án đúng)
                s_distractors = set()
                while len(s_distractors) < 3:
                    # Tạo sai số dựa trên các biến số
                    wrong = kq + random.choice([-2, -1, 1, 2, 3, 5, 10])
                    if wrong > 0 and wrong != kq:
                        s_distractors.add('$%s$' % latex(wrong))

                list_distractors = list(s_distractors)

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (
                    '''Một ôtô đang dừng và bắt đầu chuyển động theo một đường thẳng với gia tốc $a(t) = %s - %st \\text{ (m/s}^2)$, trong đó $t$ là khoảng thời gian tính bằng giây kể từ lúc ôtô bắt đầu chuyển động. Tìm quãng đường (đơn vị: m) ôtô đi được từ lúc bắt đầu chuyển động đến khi vận tốc của ôtô đạt giá trị lớn nhất.'''
                    % (m_val, n_val)
                )

                # --- ĐÁP ÁN ---
                da_d = '\\True ' + da_d_str
                da_s1 = list_distractors[0]
                da_s2 = list_distractors[1]
                da_s3 = list_distractors[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- LỜI GIẢI CHI TIẾT ---
                # v(t) = nguyên hàm a(t)
                v_tex = latex(v_func).replace('**2', '^2')
                # t_max tính bằng công thức đỉnh parabol hoặc đạo hàm
                loigiai = (
                    '''Ta có $v(t) = \\int a(t) \\text{d}t = \\int (%s - %st) \\text{d}t = %s + C$.\\\\
                    Vì xe bắt đầu chuyển động từ trạng thái dừng nên khi $t=0, v=0 \\Rightarrow C=0$.\\\\
                    Do đó $v(t) = %s$.\\\\
                    Vận tốc đạt giá trị lớn nhất khi $v'(t) = a(t) = 0 \\Leftrightarrow %s - %st = 0 \\Leftrightarrow t = %s$ (s).\\\\
                    Quãng đường xe đi được trong $%s$ giây đầu là:\\\\
                    $S = \\int_{0}^{%s} (%s) \\text{d}t = \\left. \\left( %s \\right) \\right|_{0}^{%s} = %s$ m.'''
                    % (m_val, n_val, v_tex, 
                       v_tex, 
                       m_val, n_val, t_max_val,
                       t_max_val, t_max_val, v_tex, latex(integrate(v_func, t_sym)), t_max_val, latex(kq))
                )

            # --- XUẤT KẾT QUẢ ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

