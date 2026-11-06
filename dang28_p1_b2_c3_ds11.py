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


def bt_dang28_p1_b2_c3_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khống chế tổng độ lệch để mẫu số là ước của 20, giúp kết quả luôn là số nguyên đẹp
                clean_pairs = [
                    (1, 1), (1, 3), (3, 1), (2, 2), # tổng mẫu = 2 hoặc 4
                    (1, 4), (2, 3), (3, 2), (4, 1), # tổng mẫu = 5
                    (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2) # tổng mẫu = 10
                ]
                delta1, delta2 = random.choice(clean_pairs)

                # Random tần số lớn nhất (nhóm chứa mốt) và các tần số xung quanh
                n_m = random.randint(15, 25)
                n_mm1 = n_m - delta1
                n_mp1 = n_m - delta2

                # Random tần số của nhóm đầu và nhóm cuối sao cho nhỏ hơn tần số kề mốt
                f1 = random.randint(3, n_mm1 - 1)
                f5 = random.randint(3, n_mp1 - 1)

                # Tính kết quả Mốt
                kq_val = 40 + int((delta1 / (delta1 + delta2)) * 20)
                da_str = str(kq_val)

                # Sinh các phương án nhiễu ngẫu nhiên
                distractors = set()
                while len(distractors) < 3:
                    fake_ans = random.randint(41, 59)
                    if fake_ans != kq_val:
                        distractors.add(str(fake_ans))

                d_list = list(distractors)

                # Các đáp án trắc nghiệm
                da = '$%s$' % da_str
                das1 = '$%s$' % d_list[0]
                das2 = '$%s$' % d_list[1]
                das3 = '$%s$' % d_list[2]

                # Vẽ bảng bằng LaTeX
                table_latex = ('''\\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|}
            \\hline
            \\textbf{Thời gian (phút)} & $[0; 20)$ & $[20; 40)$ & $[40; 60)$ & $[60; 80)$ & $[80; 100)$ \\\\
            \\hline
            \\textbf{Số học sinh} & %s & %s & %s & %s & %s \\\\
            \\hline
            \\end{tabular}
            \\end{center}''' % (f1, n_mm1, n_m, n_mp1, f5))

                # Câu hỏi
                noidungcauhoi = ('Khảo sát thời gian tập thể dục của một số học sinh khối 11 thu được mẫu số liệu ghép nhóm sau: \n%s\n Mốt của mẫu số liệu ghép nhóm trên là' % table_latex)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Nhóm chứa mốt (nhóm có tần số cao nhất) là $[40; 60)$. \\\\
            Ta có: $u_m = 40; u_{m+1} = 60 \\Rightarrow u_{m+1} - u_m = 60 - 40 = 20$; $n_{m-1} = %s$; $n_m = %s$; $n_{m+1} = %s$. \\\\
            Mốt của mẫu số liệu ghép nhóm là $M_0 = 40 + \\frac{%s - %s}{(%s - %s) + (%s - %s)} \\cdot 20 = %s$.'''
                         % (n_mm1, n_m, n_mp1, n_m, n_mm1, n_m, n_mm1, n_m, n_mp1, da_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

