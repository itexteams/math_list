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


def bt_dang21_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random dữ liệu (Xác suất An thắng mỗi séc)
                # Chọn các giá trị xác suất để kết quả không quá lẻ và thực tế
                p_win = random.choice([0.35, 0.4, 0.42, 0.45, 0.48])
                q_lose = round(1 - p_win, 2)

                # Tính toán các xác suất thành phần
                # P(A): Thắng sau 3 séc
                pa = p_win**3
                # P(B): Thắng sau 4 séc (thắng 2 trong 3 séc đầu và thắng séc cuối)
                pb = math.comb(3, 1) * (p_win**3) * q_lose
                # P(C): Thắng sau 5 séc (thắng 2 trong 4 séc đầu và thắng séc cuối)
                pc = math.comb(4, 2) * (p_win**3) * (q_lose**2)

                ph = pa + pb + pc

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_val = Decimal(str(ph)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq_val).replace('.', ',')

                # Các đáp án trắc nghiệm
                da = '$%s$' % (kq)

                # Tạo các phương án nhiễu (sai) và đảm bảo không trùng đáp án đúng
                s = []
                while len(s) < 3:
                    sai_val = kq_val + Decimal(str(random.choice([-0.05, -0.03, 0.02, 0.04, 0.06, 0.12])))
                    sai_str = '$%s$' % (str(sai_val).replace('.', ','))
                    if sai_str != da and sai_str not in s:
                        s.append(sai_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''An và Bình thi đấu với nhau một trận bóng bàn, người nào thắng trước $3$ séc sẽ giành chiến thắng chung cuộc. Xác suất An thắng mỗi séc là $%s$ (không có hòa). Xác suất An thắng chung cuộc bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).'''
                                 % (str(p_win).replace('.', ',')))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Biết số trận thắng trước là $3$ sẽ giành chiến thắng chung cuộc nên An phải chơi tối đa $5$ trận. \\\\
            Gọi $H$ là biến cố: "An thắng chung cuộc", \\\\
            $A$ là biến cố: "An thắng trận sau $3$ séc", \\\\
            $B$ là biến cố: "An thắng trận sau $4$ séc", \\\\
            $C$ là biến cố: "An thắng trận sau $5$ séc". \\\\
            Khi đó, $H = A \\cup B \\cup C$ và $A, B, C$ đôi một xung khắc. \\\\
            Áp dụng quy tắc cộng xác suất, ta có: $P(H) = P(A) + P(B) + P(C)$. \\\\
            - Xác suất An thắng trận sau $3$ séc là $P(A) = (%s)^3 = %s$. \\\\
            - Để An thắng trận sau $4$ séc thì An phải thắng $2$ trong $3$ séc đầu và séc cuối thắng. Suy ra xác suất An thắng trận sau $4$ séc là: \\\\
            $P(B) = C_3^2 \\cdot (%s)^3 \\cdot %s = %s$. \\\\
            - Để An thắng trận sau $5$ séc thì An phải thắng $2$ trong $4$ séc đầu và séc cuối thắng. Suy ra xác suất An thắng trận sau $5$ séc là: \\\\
            $P(C) = C_4^2 \\cdot (%s)^3 \\cdot (%s)^2 = %s$. \\\\
            Vậy xác suất An thắng chung cuộc là $P(H) = %s \\approx %s$.'''
                           % (str(p_win).replace('.', ','), str(round(pa, 5)).replace('.', ','),
                              str(p_win).replace('.', ','), str(q_lose).replace('.', ','), str(round(pb, 5)).replace('.', ','),
                              str(p_win).replace('.', ','), str(q_lose).replace('.', ','), str(round(pc, 5)).replace('.', ','),
                              str(round(ph, 5)).replace('.', ','), kq))
                dapan=' \\shortans[0]{$%s$} '%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

