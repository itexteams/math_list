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


def bt_dang32_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến danh sách dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN ---
                # Số bi xanh và đỏ (tổng nên là số tròn hoặc dễ tính)
                n_xanh = randint(25, 40)
                n_do = randint(15, 25)
                tong_bi = n_xanh + n_do

                # Tỷ lệ phần trăm được đánh số (70% -> 0.7)
                pt_xanh = randint(55, 85) 
                pt_do = randint(45, 75)

                # Tính toán các xác suất thành phần theo Sympy Rational để chính xác
                p_a = Rational(n_xanh, tong_bi)
                p_not_a = Rational(n_do, tong_bi)
                p_b_a = Rational(pt_xanh, 100)
                p_b_not_a = Rational(pt_do, 100)

                # Công thức Bayes: P(A|B) = [P(A)*P(B|A)] / [P(A)*P(B|A) + P(not A)*P(B|not A)]
                tu_so = p_a * p_b_a
                mau_so = (p_a * p_b_a) + (p_not_a * p_b_not_a)
                kq_chinh_xac = tu_so / mau_so

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_float = float(kq_chinh_xac)
                kq_round = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Chuyển định dạng số thập phân sang dấu phẩy cho hiển thị
                kq_str = str(kq_round).replace('.', ',')

                # --- BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN SAI ---
                # Tạo các đáp án nhiễu (không trùng với đáp án đúng)
                sai_lech = [0.05, 0.12, -0.08, 0.15, -0.12, 0.07]
                random.shuffle(sai_lech)

                list_s = []
                for delta in sai_lech:
                    val = float(kq_round) + delta
                    if 0 < val < 1:
                        s_val = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                        s_str = str(s_val).replace('.', ',')
                        if s_str != kq_str and s_str not in list_s:
                            list_s.append('$%s$' % s_str)

                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                da_d = '\\True $%s$' % kq_str

                # --- BƯỚC 2: VIẾT LẠI Y HỆT BÀI TOÁN THEO MẪU ---
                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Một chiếc hộp có %s viên bi, trong đó có %s viên bi màu xanh và %s viên bi màu đỏ, '
                    'các viên bi có kích thước và khối lượng giống nhau. Sau khi kiểm tra, người ta thấy có %s%% '
                    'số viên bi màu xanh được đánh số và %s%% số viên bi màu đỏ được đánh số, những viên bi còn lại '
                    'không đánh số. Lấy ngẫu nhiên một viên bi từ hộp đó. Biết rằng, viên bi lấy ra được đánh số, '
                    'xác suất để viên bi đó có màu xanh bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'
                    % (latex(tong_bi), latex(n_xanh), latex(n_do), latex(pt_xanh), latex(pt_do))
                )

                # Nội dung lời giải chi tiết
                # Chuyển các giá trị sang string có dấu phẩy để dùng trong lời giải
                p_b_a_val = str(float(p_b_a)).replace('.', ',')
                p_b_not_a_val = str(float(p_b_not_a)).replace('.', ',')

                loigiai = (
                    'Gọi $A$ là biến cố "Viên bi lấy ra có màu xanh" \\\\ '
                    '$B$ là biến cố "Viên bi lấy ra được đánh số". \\\\ '
                    'Theo bài ra ta có $P(A) = \\frac{%s}{%s} = %s, P(\\overline{A}) = \\frac{%s}{%s} = %s, '
                    'P(B|A) = %s, P(B|\\overline{A}) = %s$. \\\\ '
                    'Áp dụng công thức Bayes, ta có xác suất viên bi lấy ra có màu xanh khi biết nó đã được đánh số là: \\\\ '
                    '$P(A|B) = \\frac{P(A).P(B|A)}{P(A).P(B|A) + P(\\overline{A}).P(B|\\overline{A})} '
                    '= \\frac{%s \\cdot %s}{%s \\cdot %s + %s \\cdot %s} '
                    '= \\frac{%s}{%s} \\approx %s$.'
                    % (latex(n_xanh), latex(tong_bi), latex(p_a), latex(n_do), latex(tong_bi), latex(p_not_a),
                       p_b_a_val, p_b_not_a_val,
                       latex(p_a), p_b_a_val, latex(p_a), p_b_a_val, latex(p_not_a), p_b_not_a_val,
                       latex(tu_so), latex(mau_so), kq_str)
                )
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Không dùng raw string r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

