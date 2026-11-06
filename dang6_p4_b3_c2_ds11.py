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


def bt_dang6_p4_b3_c2_ds11(self):
            # Khai báo biến
            # --- Khai báo biến và Random giá trị ---
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random Khối lượng ban đầu m0 (chọn số chẵn để dễ chia)
                m0_list = [20, 30, 40, 42, 50, 60, 80, 100]
                m0 = random.choice(m0_list)

                # Random Chu kì bán rã T (đơn vị có thể là ngày, năm, giờ)
                T = random.randint(50, 500)

                # Kí hiệu chất phóng xạ (có thể giữ nguyên hoặc random)
                Po_list = ["^{210}_{84}Po", "^{14}_{6}C", "^{238}_{92}U", "^{131}_{53}I"]
                Po = random.choice(Po_list)

                # Random đơn vị thời gian
                donvi_t = random.choice(["ngày", "năm", "giờ"])

                # --- Tính toán và Kết quả ---
                # Số hạng tổng quát u_n = m0 / 2^n
                kq_a = '\\frac{%s}{2^n}'%(latex(m0))

                # Các đáp án nhiễu dựa trên lỗi sai thường gặp
                # Nhiễu 1: Nhầm m0 thành u1 = m0/2 (khối lượng sau chu kì 1)
                m0_half = Rational(m0, 2)
                kq_s1 = '\\frac{%s}{2^n}'%(latex(m0_half)) 

                # Nhiễu 2: Sai công thức cấp số nhân (dùng n-1 thay vì n)
                kq_s2 = '\\frac{%s}{2^{n-1}}'%(latex(m0)) 

                # Nhiễu 3: Sai công bội (dùng 2^n thay vì (1/2)^n)
                kq_s3 = '%s \\cdot 2^n'%(latex(m0))

                # --- Định dạng Đáp án ---
                # Đáp án đúng
                da = ('\\True $u_n = %s$'%(kq_a))

                # Danh sách các đáp án sai
                s = ['$' + kq_s1 + '$', 
                     '$' + kq_s2 + '$', 
                     '$' + kq_s3 + '$'
                    ]

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một mẫu chất phóng xạ $%s$ có khối lượng ban đầu $m_0 = %s$ mg, có chu kì bán rã $T=%s$ %s.
            Gọi $u_n$ là khối lượng còn lại của mẫu chất phóng xạ sau $n$ chu kì bán rã ($n \\in \\mathbb{N}^*$). Tìm số hạng tổng quát của dãy số $(u_n)$.'''
                                  %(Po, latex(m0), latex(T), donvi_t
                                  ))

                # Các đáp án
                da_d = da
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Giải thích công thức)
                loigiai=('''Sau mỗi chu kì bán rã, khối lượng mẫu chất phóng xạ còn lại giảm một nửa. \\\\
            Điều này tạo ra một cấp số nhân với:
            Khối lượng ban đầu (khối lượng sau 0 chu kì): $u_0 = m_0 = %s$ mg.
            Công bội $q = \\frac{1}{2}$.\\\\
            Khối lượng còn lại sau $n$ chu kì bán rã là số hạng tổng quát của cấp số nhân $u_n = u_0 \\cdot q^n$: \\\\
            $$u_n = m_0 \\cdot \\left(\\frac{1}{2}\\right)^n = \\frac{%s}{2^n}$$'''
                          %(latex(m0), latex(m0)
                          ))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

