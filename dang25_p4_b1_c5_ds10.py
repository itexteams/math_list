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


def bt_dang25_p4_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng quả cầu sao cho n_xanh < n_vang < n_do để logic trừ số luôn dương
                n_xanh = randint(5, 10)
                n_vang = randint(n_xanh + 1, 15)
                n_do = randint(n_vang + 1, 20)

                # Tính toán kết quả theo logic:
                # 1. Chọn quả xanh (có ít số nhất)
                # 2. Chọn quả vàng (loại đi 1 số đã chọn ở quả xanh)
                # 3. Chọn quả đỏ (loại đi 2 số đã chọn ở xanh và vàng)
                cach_xanh = n_xanh
                cach_vang = n_vang - 1
                cach_do = n_do - 2

                kq_int = cach_xanh * cach_vang * cach_do
                kq = str(kq_int).replace('.', ',')

                # Tạo các phương án sai
                s = set()
                while len(s) < 3:
                    sai = kq_int + random.choice([-10, -5, 5, 10, 20, -2, 2, 1, -1])
                    if sai != kq_int and sai > 0:
                        s.add('$%s$' % (str(sai).replace('.', ',')))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ quả cầu đỏ được đánh số từ $1$ đến $%s$, $%s$ quả cầu xanh được đánh số từ $1$ đến $%s$ và $%s$ quả cầu vàng được đánh số từ $1$ đến $%s$. Tính số cách lấy ra $3$ quả cầu khác màu và khác số.'''
                                 % (latex(n_do), latex(n_do), 
                                    latex(n_xanh), latex(n_xanh), 
                                    latex(n_vang), latex(n_vang)))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta thực hiện chọn các quả cầu theo trình tự sau: \\\\
                             Bước 1: Chọn quả cầu màu xanh. Vì có $%s$ quả cầu xanh đánh số từ $1$ đến $%s$ nên có $%s$ cách chọn. \\\\
                             Bước 2: Chọn quả cầu màu vàng. Vì có $%s$ quả cầu vàng đánh số từ $1$ đến $%s$ nhưng phải có số khác với quả cầu màu xanh đã chọn, nên có $%s - 1 = %s$ cách chọn. \\\\
                             Bước 3: Chọn quả cầu màu đỏ. Vì có $%s$ quả cầu đỏ đánh số từ $1$ đến $%s$ nhưng phải có số khác với quả cầu màu xanh và quả cầu màu vàng đã chọn, nên có $%s - 2 = %s$ cách chọn. \\\\
                             Vậy theo quy tắc nhân, số cách lấy ra $3$ quả cầu thỏa mãn yêu cầu bài toán là: \\\\
                             $%s \\cdot %s \\cdot %s = %s$ cách chọn.'''
                           % (latex(n_xanh), latex(n_xanh), latex(cach_xanh),
                              latex(n_vang), latex(n_vang), latex(n_vang), latex(cach_vang),
                              latex(n_do), latex(n_do), latex(n_do), latex(cach_do),
                              latex(cach_xanh), latex(cach_vang), latex(cach_do), latex(kq_int)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

