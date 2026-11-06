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


def bt_dang15_p1_b1_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random số chia (k)
                # Trong ảnh gốc k = 5. Ta có thể chọn k trong khoảng [3, 4, 5, 6]
                k = random.choice([3, 4, 5, 6])

                # Bước 2: Tìm các tổng chia hết cho k (từ 2 đến 12)
                sums_divisible = [s for s in range(2, 13) if s % k == 0]

                # Tìm các cặp (i, j) cho từng tổng
                all_events = {}
                total_favorable = 0
                for s in sums_divisible:
                    pairs = []
                    for i in range(1, 7):
                        for j in range(1, 7):
                            if i + j == s:
                                pairs.append((i, j))
                    all_events[s] = pairs
                    total_favorable += len(pairs)

                # Đáp án đúng
                kq = total_favorable
                da = '$%s$' % (kq)

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                    if sai > 0 and sai != kq:
                        s.add('$%s$' % (sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Gieo 2 con xúc xắc cân đối và đồng chất. Số khả năng để "Tổng số chấm xuất hiện trên hai con xúc xắc chia hết cho %s" là'''
                                 %(latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết theo mẫu ảnh)
                # Tên các biến cố: A, B, C, D...
                event_labels = ['A', 'B', 'C', 'D', 'E']
                loigiai_parts = []

                # Xây dựng các dòng liệt kê biến cố
                for idx, s_val in enumerate(sums_divisible):
                    label = event_labels[idx]
                    pairs_str = "; ".join([f"\\left({p[0]};{p[1]}\\right)" for p in all_events[s_val]])
                    line = ('''Gọi biến cố $%s$ "Tổng số chấm xuất hiện trên hai con xúc xắc là %s" \\\\
                             $%s = \\left\\{%s\\right\\} \\Rightarrow n\\left(%s\\right) = %s$.''' 
                            % (label, latex(s_val), label, pairs_str, label, len(all_events[s_val])))
                    loigiai_parts.append(line)

                # Kết luận
                names = " \\cup ".join(event_labels[:len(sums_divisible)])
                sum_n = " + ".join([f"n\\left({event_labels[i]}\\right)" for i in range(len(sums_divisible))])
                sum_val = " + ".join([str(len(all_events[s_val])) for s_val in sums_divisible])

                loigiai_head = '''Gọi biến cố $H$ "Tổng số chấm xuất hiện trên hai con xúc xắc chia hết cho %s". \\\\
                                Khi đó $H = %s$ là các biến cố xung khắc.''' % (latex(k), names)

                loigiai_body = " \\\\ ".join(loigiai_parts)

                loigiai_tail = '''\\\\ Số các kết quả thuận lợi cho biến cố $H$ là: \\\\
                                $n\\left(H\\right) = %s = %s = %s$.''' % (sum_n, sum_val, kq)

                loigiai = loigiai_head + " \\\\ " + loigiai_body + loigiai_tail

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

