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


def bt_dang40_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo các thiết lập ban đầu
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Ngẫu nhiên hóa tỷ lệ mặt ngửa của đồng xu thứ hai (ví dụ từ 60% đến 85%)
                p_percent = random.randint(60, 85)
                p_ngua = p_percent / 100
                p_sap = 1 - p_ngua

                # Tính toán các xác suất thành phần
                # P(B|A1): Đồng xu cân đối (1/2 * 1/2 * 2 cách sắp xếp S-N, N-S)
                p_b_a1 = Rational(1, 2) 

                # P(B|A2): Đồng xu bị lỗi
                p_b_a2_val = 2 * p_ngua * p_sap

                # P(B|A3): Đồng xu hai mặt ngửa (không thể ra mặt sấp)
                p_b_a3 = 0

                # Tính xác suất hậu nghiệm P(A2|B) theo công thức Bayes
                # Vì P(A1)=P(A2)=P(A3)=1/3 nên mẫu số là (1/3)*(P(B|A1) + P(B|A2) + P(B|A3))
                # Công thức rút gọn: P(B|A2) / (P(B|A1) + P(B|A2) + P(B|A3))
                mau_so = 0.5 + p_b_a2_val + 0
                kq_chua_tron = p_b_a2_val / mau_so

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_decimal = Decimal(str(kq_chua_tron)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Tạo các đáp án sai (đảm bảo không trùng đáp án đúng)
                sai_set = set()
                while len(sai_set) < 3:
                    sai_val = float(kq_decimal) + random.choice([-0.15, -0.1, -0.05, 0.05, 0.1, 0.15, 0.2])
                    sai_val = round(max(0.05, min(0.95, sai_val)), 2)
                    sai_str = str(Decimal(str(sai_val)).quantize(Decimal('0.01'))).replace('.', ',')
                    if sai_str != kq_str:
                        sai_set.add(f'${sai_str}$')

                list_sai = list(sai_set)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Có ba đồng xu được đựng trong một hộp kín. Đồng xu thứ nhất là một đồng xu cân đối với tỷ lệ mặt ngửa và mặt sấp bằng nhau. Đồng xu thứ hai là một đồng xu bị lỗi có khả năng mặt ngửa xuất hiện là $%s$\\%%. Đồng xu thứ ba là một đồng xu hai mặt ngửa (khi tung luôn ra mặt ngửa). Bạn An lấy ngẫu nhiên một đồng xu từ hộp và tung nó hai lần. Kết quả của hai lần tung cho thấy xuất hiện một lần mặt sấp và một lần mặt ngửa. Xác suất để đồng xu bạn đã chọn là đồng xu thứ hai (đồng xu bị lỗi) bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).'''
                                 % (latex(p_percent)))

                # Các đáp án
                da_d = '\\True $' + kq_str + '$'
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                p_ngua_latex = str(p_ngua).replace('.', ',')
                p_sap_latex = str(round(p_sap, 2)).replace('.', ',')
                p_b_a2_latex = str(round(p_b_a2_val, 4)).replace('.', ',')

                loigiai = ('''Gọi $A_n$ là biến cố chọn đồng xu thứ $n$ ($n=1; 2; 3$).\\\\
                            $B$ là biến cố tung hai lần thì thấy xuất hiện một lần mặt sấp và một lần mặt ngửa.\\\\
                            Vì chọn ngẫu nhiên nên $P(A_1) = P(A_2) = P(A_3) = \\frac{1}{3}$.\\\\
                            Lấy ngẫu nhiên một đồng xu tung hai lần được một mặt sấp và một mặt ngửa thì ta có ba trường hợp như sau:\\\\
                            Trường hợp 1: Chọn được đồng xu thứ nhất là S-N và N-S nên $P(B | A_1) = 2 \\cdot \\left(\\frac{1}{2}\\right)^2 = \\frac{1}{2}$.\\\\
                            Trường hợp 2: Chọn được đồng xu thứ hai là S-N và N-S nên ta có: $P(B | A_2) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
                            Trường hợp 3: Chọn được đồng xu thứ ba là N-N nên $P(B | A_3) = 0$.\\\\
                            Áp dụng công thức Bayes ta tính được xác suất chọn được đồng xu thứ hai là:\\\\
                            $P(A_2 | B) = \\frac{P(B | A_2) \\cdot P(A_2)}{P(A_1) \\cdot P(B | A_1) + P(A_2) \\cdot P(B | A_2) + P(A_3) \\cdot P(B | A_3)} = \\frac{%s \\cdot \\frac{1}{3}}{\\frac{1}{3} \\cdot \\frac{1}{2} + %s \\cdot \\frac{1}{3} + 0 \\cdot \\frac{1}{3}} \\approx %s$.\\\\
                            Vậy xác suất chọn được đồng xu thứ hai là $%s$.'''
                           % (p_ngua_latex, p_sap_latex, p_sap_latex, p_ngua_latex, p_b_a2_latex,
                              p_b_a2_latex, p_b_a2_latex, kq_str, kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

