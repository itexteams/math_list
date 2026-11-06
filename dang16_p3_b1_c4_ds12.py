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


def bt_dang16_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Tổng số học sinh (ví dụ từ 200 đến 500)
                tong = random.randint(20, 50) * 10 
                # Số học sinh thực sự bị nhiễm (chiếm khoảng 30-50%)
                nhiem = random.randint(int(tong*0.3), int(tong*0.5))
                khong_nhiem = tong - nhiem

                # Xác suất dương tính thật (90% -> 98%)
                p_duong_that_he_so = random.randint(85, 98)
                p_duong_that = p_duong_that_he_so / 100

                # Xác suất dương tính giả (3% -> 8%)
                p_duong_gia_he_so = random.randint(3, 8)
                p_duong_gia = p_duong_gia_he_so / 100

                # --- Tính toán theo công thức Bayes ---
                # P(N) và P(not N)
                p_n = Rational(nhiem, tong)
                p_not_n = 1 - p_n

                # P(D) = P(N)*P(D|N) + P(not N)*P(D|not N)
                p_d = float(p_n) * p_duong_that + float(p_not_n) * p_duong_gia

                # P(N|D) = [P(N)*P(D|N)] / P(D)
                ket_qua_chua_lam_tron = (float(p_n) * p_duong_that) / p_d

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_decimal = Decimal(str(ket_qua_chua_lam_tron)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # --- B4: Tạo các phương án sai không trùng đáp án đúng ---
                set_da = {kq_decimal}
                while len(set_da) < 4:
                    sai_lech = Decimal(str(random.uniform(-0.2, 0.2))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    phuong_an_sai = kq_decimal + sai_lech
                    if phuong_an_sai > 0 and phuong_an_sai < 1 and phuong_an_sai != kq_decimal:
                        set_da.add(phuong_an_sai)

                list_da_tron = [str(x).replace('.', ',') for x in set_da]
                random.shuffle(list_da_tron)

                da_dung_str = '$' + kq_str + '$'

                # Tìm vị trí đáp án đúng trong list đã trộn để gán \True
                choices = []
                for item in list_da_tron:
                    if item == kq_str:
                        choices.append('\\True $' + item + '$')
                    else:
                        choices.append('$' + item + '$')

                # Câu hỏi
                noidungcauhoi = ('''Trong một đợt kiểm tra sức khỏe tại trường có $%s$ học sinh được xét nghiệm một loại virus. Trong đó, biết rằng có $%s$ bạn thật sự bị nhiễm virus. Nếu một bạn bị nhiễm, thì xét nghiệm cho kết quả dương tính (tức là phát hiện đúng bệnh) với xác suất $%s\\%%$. Nếu một bạn không bị nhiễm, thì xét nghiệm vẫn có thể báo nhầm là dương tính (gọi là dương tính giả), với xác suất $%s\\%%$. Giả sử một bạn có kết quả xét nghiệm dương tính. Hỏi xác suất để bạn đó thật sự bị nhiễm virus là bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 %(latex(tong), latex(nhiem), latex(p_duong_that_he_so), latex(p_duong_gia_he_so)))

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $N$ là biến cố học sinh bị nhiễm virus và $D$ là biến cố xét nghiệm cho kết quả dương tính. \\\\
                             Ta có: $P(N) = \\frac{%s}{%s} \\Rightarrow P(\\overline{N}) = 1 - \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
                             Theo giả thiết: $P(D|N) = %s$ và $P(D|\\overline{N}) = %s$. \\\\
                             Xác suất để một học sinh có kết quả xét nghiệm dương tính là: \\\\
                             $P(D) = P(N) \\cdot P(D|N) + P(\\overline{N}) \\cdot P(D|\\overline{N}) = \\frac{%s}{%s} \\cdot %s + \\frac{%s}{%s} \\cdot %s = %s$. \\\\
                             Xác suất để học sinh đó thật sự bị nhiễm virus khi biết kết quả xét nghiệm dương tính là: \\\\
                             $P(N|D) = \\frac{P(N) \\cdot P(D|N)}{P(D)} = \\frac{\\frac{%s}{%s} \\cdot %s}{%s} \\approx %s$.'''
                             %(latex(nhiem), latex(tong), latex(nhiem), latex(tong), latex(khong_nhiem), latex(tong),
                               latex(p_duong_that).replace('.', ','), latex(p_duong_gia).replace('.', ','),
                               latex(nhiem), latex(tong), latex(p_duong_that).replace('.', ','),
                               latex(khong_nhiem), latex(tong), latex(p_duong_gia).replace('.', ','),
                               latex(round(p_d, 4)).replace('.', ','),
                               latex(nhiem), latex(tong), latex(p_duong_that).replace('.', ','),
                               latex(round(p_d, 4)).replace('.', ','),
                               kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

