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


def bt_dang20_p1_b1_c6_ds10(self):
            # Khai báo biến
            # Random biến cố A: "ít nhất hai mặt sấp liên tiếp" hoặc "ít nhất hai mặt ngửa liên tiếp"
            loai_bien_co = random.choice(['sấp', 'ngửa'])
            s = 'S'
            n = 'N'

            if loai_bien_co == 'sấp':
                mat = 'sấp'
                # A = {SSS, SSN, NSS}
                tap_A = ['SSS', 'SSN', 'NSS']
            else:
                mat = 'ngửa'
                # A = {NNN, NNS, SNN}
                tap_A = ['NNN', 'NNS', 'SNN']

            # B là biến cố "Kết quả ba lần gieo là như nhau"
            # B = {SSS, NNN}
            tap_B = ['SSS', 'NNN']

            # Biến cố A hợp B (A U B)
            # Sử dụng set để hợp nhất và loại bỏ trùng lặp, sau đó chuyển về list để sắp xếp cho đẹp
            tap_hop = list(set(tap_A) | set(tap_B))
            tap_hop.sort() # Sắp xếp để đáp án trông gọn gàng

            # Tạo chuỗi LaTeX cho các tập hợp
            str_A = '\\{' + ','.join(tap_A) + '\\}'
            str_B = '\\{' + ','.join(tap_B) + '\\}'
            str_hop = '\\{' + ','.join(tap_hop) + '\\}'

            # --- B4: Điều chỉnh các phương án sai ---
            # Tạo một danh sách các phần tử của không gian mẫu Omega
            omega = ['SSS', 'SSN', 'SNS', 'SNN', 'NSS', 'NSN', 'NNS', 'NNN']

            # Đáp án đúng
            da_dung = '$A \\cup B = ' + str_hop + '$'

            # Tạo các đáp án sai bằng cách lấy các tập hợp khác nhau
            # Sai 1: Chỉ lấy tập B
            sai1 = '$A \\cup B = ' + str_B + '$'
            # Sai 2: Lấy A hợp B nhưng thiếu 1 phần tử hoặc thêm 1 phần tử sai (ví dụ thêm SNS)
            tam_sai2 = list(set(tap_hop) | {'SNS'})
            if 'SNS' in tap_hop: # Nếu SNS vô tình có trong tập hợp rồi thì bỏ nó đi
                tam_sai2 = [x for x in tap_hop if x != tap_hop[0]]
            tam_sai2.sort()
            sai2 = '$A \\cup B = \\{' + ','.join(tam_sai2) + '\\}$'
            # Sai 3: Không gian mẫu
            sai3 = '$A \\cup B = \\Omega$'

            # Kiểm tra trùng lặp (đảm bảo các đáp án sai không trùng đáp án đúng)
            list_wrong = [sai1, sai2, sai3]
            while da_dung in list_wrong:
                # Nếu trùng, tạo một tập ngẫu nhiên khác
                random_sub = random.sample(omega, 5)
                random_sub.sort()
                new_sai = '$A \\cup B = \\{' + ','.join(random_sub) + '\\}$'
                if new_sai != da_dung:
                    # Thay thế cái bị trùng
                    idx = list_wrong.index(da_dung)
                    list_wrong[idx] = new_sai

            # --- B2: Viết lại bài toán theo mẫu ---

            # Câu hỏi
            noidungcauhoi = ('Gieo một đồng xu cân đối và đồng nhất liên tiếp ba lần. Gọi $A$ là biến cố "Có ít nhất hai mặt %s xuất hiện liên tiếp" và $B$ là biến cố "Kết quả ba lần gieo là như nhau". Biến cố $A \\cup B$ là' 
                             % (mat))

            # Các đáp án
            da_d = ('\\True ' + da_dung)
            da_s1 = list_wrong[0]
            da_s2 = list_wrong[1]
            da_s3 = list_wrong[2]

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = ('Không gian mẫu khi gieo đồng xu ba lần là: \\\\'
                       '$\\Omega = \\{SSS, SSN, SNS, SNN, NSS, NSN, NNS, NNN\\}$. \\\\'
                       'Biến cố $A$ là "Có ít nhất hai mặt %s xuất hiện liên tiếp": \\\\'
                       '$A = %s$. \\\\'
                       'Biến cố $B$ là "Kết quả ba lần gieo là như nhau": \\\\'
                       '$B = %s$. \\\\'
                       'Khi đó, biến cố $A \\cup B$ gồm các phần tử thuộc ít nhất một trong hai tập hợp $A$ hoặc $B$: \\\\'
                       '$A \\cup B = %s$.' 
                       % (mat, str_A, str_B, str_hop))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + ' \n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

