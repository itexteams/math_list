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


def bt_dang9_p3_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số tiền gửi (triệu đồng) và lãi suất (%)
                A = randint(15, 50)
                r_pct = random.choice([0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
                r = r_pct / 100

                # Hàm hỗ trợ làm tròn đến hàng phần trăm và đổi dấu '.' thành ','
                def fmt(val):
                    d = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    return str(d).replace('.', ',')

                # Tính toán từng bước
                t1_val = A * (1 + r)
                t1_str = fmt(t1_val)

                t2_val = t1_val + A
                t2_str = fmt(t2_val)

                kq_val = t2_val * (1 + r)
                kq_str = fmt(kq_val)

                r_pct_str = str(r_pct).replace('.', ',')
                r_val_str = str(r).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % (kq_str)

                # Các phương án sai (đảm bảo không trùng đáp án đúng và không trùng nhau)
                w1 = fmt(A * (1 + r)**2)          # Quên gửi tiền ở đầu tháng 2
                w2 = fmt(2 * A * (1 + r))         # Tính sai công thức lãi kép
                w3 = fmt(t2_val)                  # Quên tính lãi tháng thứ 2
                w4 = fmt(kq_val + 0.5)            # Nhầm số liệu
                w5 = fmt(kq_val - 0.5)            # Nhầm số liệu

                wrong_set = set()
                for v in [w1, w2, w3, w4, w5]:
                    if v != kq_str:
                        wrong_set.add('$%s$' % (v))

                s = list(wrong_set)
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Vào đầu mỗi tháng, ông An đều gửi vào ngân hàng số tiền cố định $%s$ triệu đồng theo hình thức lãi kép với lãi suất $%s\\%%$/tháng. Số tiền ông An có được sau tháng thứ hai (đơn vị: triệu đồng) bằng bao nhiêu? (làm tròn đến hàng phần chục).'''
                                 % (latex(A), r_pct_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Đổi $%s\\%% = %s$.\\\\
            Cuối tháng thứ nhất, số tiền cả gốc và lãi ông An có được là:\\\\
            $%s \\cdot (1 + %s) = %s$ (triệu đồng).\\\\
            Đầu tháng thứ hai, ông An gửi thêm $%s$ triệu đồng nên tổng số tiền trong ngân hàng là:\\\\
            $%s + %s = %s$ (triệu đồng).\\\\
            Cuối tháng thứ hai, số tiền cả gốc và lãi ông An có được là:\\\\
            $%s \\cdot (1 + %s) = %s \\approx %s$ (triệu đồng).'''
                           % (r_pct_str, r_val_str,
                              latex(A), r_val_str, t1_str,
                              latex(A), t1_str, latex(A), t2_str,
                              t2_str, r_val_str, str(Decimal(str(kq_val))).replace('.', ','), kq_str))
            dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

