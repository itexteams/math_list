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


def bt_dang6_p3_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (ở đây là dạng 1 dựa trên hình ảnh)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Tổng số học sinh n
                n = randint(40, 60)
                # Số học sinh thích Toán (nA), Sử (nB) và cả hai (nAnB)
                # Đảm bảo nAnB < nA và nAnB < nB và nA + nB - nAnB <= n
                nAnB = randint(5, 12)
                nA = randint(25, 35)
                nB = randint(15, 25)

                # Kiểm tra tính hợp lệ của dữ liệu ngẫu nhiên
                while nA + nB - nAnB > n:
                    n = n + 5

                # --- Tính toán xác suất ---
                pa_frac = Rational(nA, n)
                pb_frac = Rational(nB, n)
                panb_frac = Rational(nAnB, n)

                paub_frac = pa_frac + pb_frac - panb_frac
                p_final_frac = 1 - paub_frac

                # Chuyển đổi sang số thập phân và làm tròn đến hàng phần trăm
                kq_val = float(p_final_frac)
                kq_decimal = Decimal(str(kq_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # --- B4: Điều chỉnh các phương án sai không trùng đáp án đúng ---
                da = '$%s$' % (kq_str)

                s = []
                while len(s) < 3:
                    # Tạo các phương án sai loanh quanh đáp án đúng
                    sai_val = float(kq_decimal) + random.choice([-0.1, 0.1, -0.05, 0.05, -0.12, 0.08])
                    if sai_val > 0 and sai_val < 1:
                        sai_decimal = Decimal(str(sai_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                        sai_str = '$%s$' % (str(sai_decimal).replace('.', ','))
                        if sai_str != da and sai_str not in s:
                            s.append(sai_str)

                das1, das2, das3 = s[0], s[1], s[2]

                # --- Nội dung câu hỏi ---
                noidungcauhoi = ('''Lớp 11A1 có $%s$ học sinh, trong đó có $%s$ bạn thích học môn Toán, $%s$ bạn thích học môn Lịch sử và $%s$ bạn thích cả hai môn trên. Chọn ngẫu nhiên một bạn trong lớp. Xác suất để bạn đó không thích cả môn Toán và môn Lịch sử là bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 % (latex(n), latex(nA), latex(nB), latex(nAnB)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # --- B2: Viết lời giải chi tiết theo mẫu ---
                # Chuẩn bị phân số latex cho lời giải
                loigiai = ('''Gọi $A$ là biến cố "Học sinh thích học môn Toán". Suy ra $P\\left( A \\right) = \\frac{%s}{%s} = %s$. \\\\
                             $B$ là biến cố "Học sinh thích học môn Lịch sử". Suy ra $P\\left( B \\right) = \\frac{%s}{%s} = %s$. \\\\
                             $A \\cap B$ là biến cố "Học sinh thích cả môn Toán và môn Lịch sử". Suy ra $P\\left( AB \\right) = \\frac{%s}{%s} = %s$. \\\\
                             $A \\cup B$ là biến cố "Học sinh thích môn Toán hoặc môn Lịch sử". \\\\
                             $P\\left( A \\cup B \\right) = P\\left( A \\right) + P\\left( B \\right) - P\\left( A \\cap B \\right) = %s + %s - %s = %s$. \\\\
                             $\\overline{A \\cup B}$ là biến cố "Học sinh không thích cả môn Toán và môn Lịch sử". \\\\
                             Theo tính chất xác suất, ta có: $P\\left( \\overline{A \\cup B} \\right) = 1 - P\\left( A \\cup B \\right) = 1 - %s = %s \\approx %s$.'''
                           % (latex(nA), latex(n), latex(pa_frac),
                              latex(nB), latex(n), latex(pb_frac),
                              latex(nAnB), latex(n), latex(panb_frac),
                              latex(pa_frac), latex(pb_frac), latex(panb_frac), latex(paub_frac),
                              latex(paub_frac), latex(p_final_frac), kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)
            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

