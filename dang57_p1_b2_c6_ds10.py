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


def bt_dang57_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Vòng lặp đảm bảo số lượng các cặp kết quả tìm được không quá nhiều cũng không quá ít (từ 2 đến 6 cặp)
                while True:
                    n = random.randint(8, 12)
                    S = random.randint(11, 2 * n - 3)

                    # Tìm các cặp thỏa mãn: tổng >= S và tổng là số lẻ
                    pairs = []
                    for i in range(1, n):
                        for j in range(i + 1, n + 1):
                            if (i + j) >= S and (i + j) % 2 != 0:
                                pairs.append((i, j))

                    nA = len(pairs)
                    if 2 <= nA <= 6:
                        break

                # Tính không gian mẫu
                n_omega = n * (n - 1) // 2

                # Hàm hỗ trợ định dạng phân số LaTeX
                def format_frac(num, den):
                    f = frac(num, den)
                    if f.denominator == 1:
                        return str(f.numerator)
                    return "\\frac{%s}{%s}" % (f.numerator, f.denominator)

                # Tính đáp án đúng
                P_correct = frac(nA, n_omega)
                da = '$%s$' % format_frac(P_correct.numerator, P_correct.denominator)

                # Tạo các đáp án nhiễu
                distractors_set = set()
                distractors_set.add(frac(nA, n * (n - 1)))               # Sai lầm: dùng chỉnh hợp
                distractors_set.add(frac(nA, n * n))                     # Sai lầm: rút có hoàn lại
                distractors_set.add(frac(nA + 1, n_omega))               # Sai lầm: đếm dư 1 cặp
                distractors_set.add(frac(max(1, nA - 1), n_omega))       # Sai lầm: đếm thiếu 1 cặp

                # Sai lầm: Quên điều kiện "số lẻ" (tính tất cả các tổng >= S)
                all_pairs = [(i,j) for i in range(1, n) for j in range(i+1, n+1) if (i+j) >= S]
                distractors_set.add(frac(len(all_pairs), n_omega))

                # Loại bỏ đáp án đúng khỏi tập nhiễu (nếu vô tình trùng)
                distractors_set.discard(P_correct)

                # Nếu thiếu đáp án nhiễu, thêm ngẫu nhiên
                while len(distractors_set) < 3:
                    random_den = random.choice([12, 18, 36, 24, n_omega])
                    distractors_set.add(frac(random.randint(1, 10), random_den))
                    distractors_set.discard(P_correct)

                # Lấy 3 đáp án nhiễu
                wrong_choices = random.sample(list(distractors_set), 3)
                s = ['$%s$' % format_frac(w.numerator, w.denominator) for w in wrong_choices]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong một thùng có $%s$ thẻ ghi các số tự nhiên từ $1$ đến $%s$. Rút ngẫu nhiên cùng lúc hai thẻ. Xác suất để tổng hai số ghi trên hai thẻ rút được là một số lẻ lớn hơn hoặc bằng $%s$ bằng''' 
                                 % (n, n, S))

                # Các đáp án trộn ngẫu nhiên
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi liệt kê các cặp số
                pairs_str = ";".join(["(%s;%s)" % (p[0], p[1]) for p in pairs])

                # Lời giải
                loigiai = ('''Số phần tử của không gian mẫu là $n(\\Omega) = C_{%s}^2 = %s$. \\\\
                Gọi $A$ là biến cố: "Tổng hai số ghi trên hai thẻ rút được là một số lẻ lớn hơn hoặc bằng $%s$". \\\\
                Ta có các cặp số có tổng là số lẻ và lớn hơn hoặc bằng $%s$ là $%s \\Rightarrow n(A) = %s$. \\\\
                Vậy xác suất của biến cố $A$ là $P(A) = \\frac{%s}{%s} = %s$.'''
                           % (n, n_omega, S, S, pairs_str, nA, nA, n_omega, format_frac(P_correct.numerator, P_correct.denominator)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

