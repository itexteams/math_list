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


def bt_dang10_p3_b2_c7_ds11(self):
            # Khai báo biến
            # s(t) = t^2 + mt + c
            t0 = random.randint(2, 6) # Thời điểm t
            v_target = random.randint(10, 50) / 2.0 # Vận tốc tức thời (ví dụ: 4.5, 5.0, ...)
            c = random.randint(5, 20) # Hằng số tự do trong phương trình quãng đường

            # --- Tính toán giá trị m ---
            # v(t) = s'(t) = 2t + m
            # v(t0) = 2*t0 + m = v_target => m = v_target - 2*t0
            m_val = v_target - 2 * t0

            # Định dạng số thực sang chuỗi có dấu phẩy
            def format_decimal(val):
                d = Decimal(float(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                return str(d).replace('.', ',')

            m_str = format_decimal(m_val)

            # --- Tạo các phương án trắc nghiệm ---
            da_dung = '$%s$' % m_str
            s = []
            offsets = [-2, -1.5, -1, 0.5, 1, 1.5, 2, 3]
            for offset in offsets:
                sai_val = m_val + offset
                sai_str = '$%s$' % format_decimal(sai_val)
                if sai_str != da_dung and sai_str not in s:
                    s.append(sai_str)

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # --- Nội dung câu hỏi ---
            # s(t) = t^2 + mt + 10
            noidungcauhoi = ('''Cho một vật chuyển động theo phương trình $s\\left(t\\right) = t^2 + mt + %s$. Trong đó: $s$ là quãng đường vật đi được (mét) và $t$ là thời gian vật chuyển động (giây). Giá trị của tham số $m$ biết tại thời điểm $t = %s$ thì vận tốc tức thời của vật là $%s$ m/s bằng bao nhiêu? (làm tròn kết quả đến hàng phần mười).'''
                            %(latex(c), latex(t0), format_decimal(v_target)))

            # --- Nội dung lời giải ---
            # v(t) = 2t + m. Tại t=t0, v(t0)=v_target <=> 2*t0 + m = v_target
            loigiai = ('''Vận tốc của vật tại thời điểm $t$ là: $v\\left(t\\right) = s'\\left(t\\right) = 2t + m$. \\\\
                        Vận tốc tức thời của vật là $%s$ m/s khi $v\\left(%s\\right) = %s \\Leftrightarrow 2 \\cdot %s + m = %s \\Leftrightarrow m = %s$.'''
                        %(format_decimal(v_target), latex(t0), format_decimal(v_target), 
                          latex(t0), format_decimal(v_target), format_decimal(m_val)))
            dapan='\\shortans[0]{$%s$}\n'%(format_decimal(m_val))
            # --- Sắp xếp đáp án ---
            da_d = '\\True ' + da_dung
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # --- Xuất kết quả theo mẫu ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

