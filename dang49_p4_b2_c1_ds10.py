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


def bt_dang49_p4_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến và chọn dạng (giữ nguyên cấu trúc mẫu)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random dữ liệu bài toán
                # n_all: số học sinh giỏi cả 3 môn
                n_all = randint(1, 3)

                # n_tl, n_th, n_lh: số học sinh giỏi các cặp 2 môn (phải lớn hơn n_all)
                n_tl = randint(n_all + 2, n_all + 4)
                n_th = randint(n_all + 2, n_all + 4)
                n_lh = randint(n_all + 1, n_all + 3)

                # n_t, n_l, n_h: tổng số học sinh giỏi từng môn (phải lớn hơn tổng các phần giao)
                n_t = n_tl + n_th - n_all + randint(2, 5)
                n_l = n_tl + n_lh - n_all + randint(2, 5)
                n_h = n_th + n_lh - n_all + randint(2, 5)

                # Bước 2: Tính toán kết quả
                # Số học sinh giỏi ĐÚNG 2 môn = (Tổng giỏi 2 môn) - 3 * (Giỏi cả 3 môn)
                # Hoặc: (n_tl - n_all) + (n_th - n_all) + (n_lh - n_all)
                val_tl = n_tl - n_all
                val_th = n_th - n_all
                val_lh = n_lh - n_all
                kq_val = val_tl + val_th + val_lh

                kq = str(kq_val)

                # Bước 3: Tạo các phương án sai
                s = []
                while len(s) < 3:
                    sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4])
                    if sai > 0 and sai != kq_val and str(sai) not in s:
                        s.append(str(sai))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (Sử dụng %s và định dạng LaTeX)
                noidungcauhoi = ('''Lớp 10A$_{1}$ có $%s$ học sinh giỏi Toán, $%s$ học sinh giỏi Lý, $%s$ học sinh giỏi Hóa, $%s$ học sinh giỏi cả Toán và Lý, $%s$ học sinh giỏi cả Toán và Hóa, $%s$ học sinh giỏi cả Lý và Hóa, $%s$ học sinh giỏi cả 3 môn Toán, Lý, Hóa. Tìm số học sinh giỏi đúng hai môn học của lớp 10A$_{1}$.'''
                                 %(latex(n_t), latex(n_l), latex(n_h), latex(n_tl), latex(n_th), latex(n_lh), latex(n_all)))

                # Các đáp án
                da_d = ('\\True ' + '$%s$' % (kq))
                da_s1 = '$%s$' % (das1)
                da_s2 = '$%s$' % (das2) 
                da_s3 = '$%s$' % (das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai=('''Gọi $T, L, H$ lần lượt là tập hợp các học sinh giỏi Toán, Lý, Hóa.\\\\
                         Số học sinh chỉ giỏi đúng hai môn Toán và Lý là: $%s - %s = %s$ (học sinh).\\\\
                         Số học sinh chỉ giỏi đúng hai môn Toán và Hóa là: $%s - %s = %s$ (học sinh).\\\\
                         Số học sinh chỉ giỏi đúng hai môn Lý và Hóa là: $%s - %s = %s$ (học sinh).\\\\
                         Số học sinh giỏi đúng hai môn của lớp 10A$_{1}$ là:\\\\
                         $%s + %s + %s = %s$ (học sinh).'''
                         %(latex(n_tl), latex(n_all), latex(val_tl),
                           latex(n_th), latex(n_all), latex(val_th),
                           latex(n_lh), latex(n_all), latex(val_lh),
                           latex(val_tl), latex(val_th), latex(val_lh), latex(kq_val)))

            # Xuất câu trắc nghiệm (giữ nguyên cấu trúc mẫu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

