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


def bt_dang30_p1_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            m, x = symbols('m x')

            # B1 & B3: Thiết lập thông số và logic random
            m1 = random.randint(-5, 2)
            m2 = m1 + random.choice([1, 2, 3, 4, 5]) 

            if (m1 + m2) % 2 == 0:
                m2 += 1

            B = int(-(m1 + m2 + 1) / 2)
            C = int(m1 * m2 - B**2)

            expr_b = 2*(m + B)
            expr_c = m + C
            delta_prime = m**2 + (2*B + 1)*m + (B**2 + C)

            # Ngẫu nhiên loại câu hỏi
            loai_cau_hoi = random.choice(['vo_nghiem', 'nghiem_kep', 'hai_nghiem'])

            if loai_cau_hoi == 'vo_nghiem':
                yeu_cau = "vô nghiệm"
                dieu_kien_delta = r"\Delta' < 0"
                # Dòng 4 dạng điều kiện m
                dieu_kien_m = r"%s < m < %s" % (m1, m2)
                da_dung = r'$m \in (%s; %s)$' % (m1, m2)
                s = [r'$(-\infty; %s) \cup (%s; +\infty)$' % (m1, m2), 
                     r'$[%s; %s]$' % (m1, m2), 
                     r'$(-\infty; %s] \cup [%s; +\infty)$' % (m1, m2)]

            elif loai_cau_hoi == 'nghiem_kep':
                yeu_cau = "có nghiệm kép"
                dieu_kien_delta = r"\Delta' = 0"
                # Dòng 4 dạng điều kiện m
                dieu_kien_m = r"\left[\begin{aligned} & m = %s \\ & m = %s \end{aligned}\right." % (m1, m2)
                da_dung = r'$m \in \{%s; %s\}$' % (m1, m2)
                s = [r'$m = %s$' % m1, r'$m = %s$' % m2, r'$m \in \{%s; %s\}$' % (m1-1, m2+1)]

            else: # hai_nghiem
                yeu_cau = "có hai nghiệm phân biệt"
                dieu_kien_delta = r"\Delta' > 0"
                # Dòng 4 dạng điều kiện m
                dieu_kien_m = r"\left[\begin{aligned} & m < %s \\ & m > %s \end{aligned}\right." % (m1, m2)
                da_dung = r'$m \in (-\infty; %s) \cup (%s; +\infty)$' % (m1, m2)
                s = [r'$(%s; %s)$' % (m1, m2), 
                     r'$[%s; %s]$' % (m1, m2), 
                     r'$(-\infty; %s] \cup [%s; +\infty)$' % (m1, m2)]

            # Câu hỏi
            noidungcauhoi = (r'Tập các giá trị $m$ để phương trình $-x^2 + (%s) x + %s = 0$ %s là' 
                             % (latex(expr_b), latex(expr_c), yeu_cau))

            # Trộn đáp án
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d] + [str(ans) for ans in random.sample(s, 3)]
            random.shuffle(list_1)

            # Lời giải - Dòng thứ 4 đã được chuyển sang dạng điều kiện của m
            dau_bpt = "<" if loai_cau_hoi == 'vo_nghiem' else ("=" if loai_cau_hoi == 'nghiem_kep' else ">")

            loigiai = (r'''Phương trình %s \\
            $\Leftrightarrow %s \Leftrightarrow (%s)^2 - (-1)(%s) %s 0$ \\
            $\Leftrightarrow %s %s 0$ \\
            $\Leftrightarrow %s$ \\
            Vậy %s.''' 
            % (yeu_cau, dieu_kien_delta, latex(m + B), latex(expr_c), dau_bpt, latex(delta_prime), dau_bpt, dieu_kien_m, da_dung))

            # B2: Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

