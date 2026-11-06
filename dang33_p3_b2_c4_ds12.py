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


def bt_dang33_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random các thông số bài toán
                # Tỉ lệ nam từ 60% đến 80%
                nam_percent = random.randint(65, 80)
                nu_percent = 100 - nam_percent

                # Tỉ lệ nam hoàn thành FM sub 4 từ 25% đến 40%
                sub4_nam_percent = random.randint(25, 40)
                # Tỉ lệ nữ hoàn thành FM sub 4 từ 2% đến 8%
                sub4_nu_percent = random.randint(2, 8)

                # Chuyển sang số thập phân để tính toán
                p_a = Decimal(nam_percent) / 100  # P(A)
                p_not_a = Decimal(nu_percent) / 100 # P(not A)
                p_b_a = Decimal(sub4_nam_percent) / 100 # P(B|A)
                p_b_not_a = Decimal(sub4_nu_percent) / 100 # P(B|not A)

                # Tính toán theo công thức Bayes
                tu_so = p_a * p_b_a
                mau_so = (p_a * p_b_a) + (p_not_a * p_b_not_a)
                kq_raw = tu_so / mau_so

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_final = kq_raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Định dạng hiển thị dấu phẩy cho số thập phân
                str_p_a = str(p_a).replace('.', ',')
                str_p_not_a = str(p_not_a).replace('.', ',')
                str_p_b_a = str(p_b_a).replace('.', ',')
                str_p_b_not_a = str(p_b_not_a).replace('.', ',')
                str_kq = str(kq_final).replace('.', ',')

                # Bước 4: Tạo các phương án sai không trùng đáp án đúng
                da_d = '\\True $%s$' % str_kq

                s_list = []
                while len(s_list) < 3:
                    # Tạo sai số ngẫu nhiên từ -0.10 đến 0.10 (trừ 0)
                    offset = Decimal(random.randint(-10, 10)) / 100
                    if offset == 0: continue

                    sai_so = kq_final + offset
                    # Đảm bảo phương án nằm trong khoảng (0, 1)
                    if 0 < sai_so < 1:
                        str_sai = str(sai_so).replace('.', ',')
                        if str_sai != str_kq and ('$%s$' % str_sai) not in s_list:
                            s_list.append('$%s$' % str_sai)

                # Câu hỏi
                noidungcauhoi = ('''Chạy Marathon là môn thể thao chạy bộ đường dài mà tại đó, người chơi sẽ hoàn thành quãng đường 42,195 km trong khoảng thời gian nhất định. "FM sub 4" là một thuật ngữ phổ biến trong cộng đồng những người tham gia chạy Marathon, nó dùng để chỉ thành tích hoàn thành quãng đường 42,195 km dưới 4 giờ. Trong một câu lạc bộ Marathon, tỉ lệ thành viên nam là $%s$\\%%, tỉ lệ thành viên nữ là $%s$\\%%. Đối với nam, tỉ lệ người hoàn thành FM sub 4 là $%s$\\%%; đối với nữ, tỉ lệ người hoàn thành FM sub 4 là $%s$\\%%. Chọn ngẫu nhiên một người từ câu lạc bộ đó. Xác suất để người được chọn là nam bằng bao nhiêu? (kết quả được làm tròn đến hàng phần trăm), biết rằng người chọn đã hoàn thành FM sub 4.'''
                                 %(latex(nam_percent), latex(nu_percent), latex(sub4_nam_percent), latex(sub4_nu_percent)))

                # Các đáp án
                list_1 = [da_d, s_list[0], s_list[1], s_list[2]]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Bước 2)
                loigiai = ('''Gọi $A$ là biến cố chọn được thành viên nam.\\\\
                             Gọi $B$ là biến cố chọn được thành viên đã hoàn thành FM sub 4.\\\\
                             Ta có $P(A) = %s$; $P(\\overline{A}) = %s$; $P(B|A) = %s$; $P(B|\\overline{A}) = %s$.\\\\
                             Xác suất để chọn được người nam trong câu lạc bộ biết người đó đã hoàn thành FM sub 4 là:\\\\
                             $P(A|B) = \\frac{P(A) \\cdot P(B|A)}{P(A) \\cdot P(B|A) + P(\\overline{A}) \\cdot P(B|\\overline{A})} = \\frac{%s \\cdot %s}{%s \\cdot %s + %s \\cdot %s} \\approx %s$.'''
                           %(str_p_a, str_p_not_a, str_p_b_a, str_p_b_not_a, 
                             str_p_a, str_p_b_a, str_p_a, str_p_b_a, str_p_not_a, str_p_b_not_a, str_kq))
                dapan=' \\shortans[0]{$%s$} '%(str_kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

