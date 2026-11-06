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


def bt_dang76_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Nghiên cứu và random các thông số
                # Parabol y = x^2 + c
                # Đường thẳng y = mx + d
                c = random.randint(1, 4)  
                d = random.randint(-6, -1) 

                # Phương trình hoành độ giao điểm: x^2 + c = mx + d <=> x^2 - mx + (c - d) = 0
                k = c - d
                delta_const = 4 * k
                limit = math.sqrt(delta_const)

                # Bước 2: Tìm các giá trị m nguyên thỏa mãn m^2 < 4k
                m_values = []
                m_start = math.ceil(-limit + 0.000001)
                m_end = math.floor(limit - 0.000001)

                for m_val in range(m_start, m_end + 1):
                    m_values.append(m_val)

                kq_dung = len(m_values)

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo phương án nhiễu quanh đáp án đúng
                    nhieu = kq_dung + random.choice([-3, -2, -1, 1, 2, 3])
                    if nhieu > 0 and nhieu != kq_dung:
                        s.add(f'${nhieu}$')

                das = list(s)
                das1 = das[0]
                das2 = das[1]
                das3 = das[2]

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu giá trị nguyên của $m$ để đường thẳng $y = mx %s$ không có điểm chung với Parabol $y = x^2 + %s$?'''
                                 %(latex(d), latex(c)))

                # Các đáp án
                da_d = ('\\True $%s$'%(kq_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2 & 3: Nội dung lời giải chi tiết y hệt mẫu trong ảnh
                loigiai = ('''Phương trình hoành độ giao điểm: $x^2 + %s = mx %s \\Leftrightarrow x^2 - mx + %s = 0$ (*).\\\\
                           Đường thẳng $y = mx %s$ không có điểm chung với Parabol $y = x^2 + %s \\Leftrightarrow$ Phương trình (*) vô nghiệm \\\\
                           $\\Leftrightarrow \\Delta < 0 \\Leftrightarrow m^2 - %s < 0 \\Leftrightarrow -%s < m < %s$.\\\\
                           Vì $m \\in \\mathbb{Z} \\Rightarrow m \\in \\{%s\\}$.\\\\
                           Vậy có $%s$ giá trị nguyên $m$ thỏa mãn bài toán.'''
                           %(latex(c), latex(d), latex(k), 
                             latex(d), latex(c),
                             latex(delta_const), latex(round(limit, 2)), latex(round(limit, 2)),
                             '; '.join(map(str, m_values)),
                             latex(kq_dung)
                            ))

            # Xuất câu trắc nghiệm đúng cấu trúc content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

