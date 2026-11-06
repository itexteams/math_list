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


def bt_dang44_p3_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hằng số k trong phương trình y = mx - k và y = -mx - k
                # Chọn k sao cho k^2 dễ chia để tạo ra số nguyên m
                k = random.choice([4, 6, 8, 10])

                # Chọn diện tích tối thiểu S_min sao cho số lượng m không quá lớn (từ 1 đến 4)
                # S = k^2 / m > S_min  => m < k^2 / S_min
                # Ta chọn S_min dựa trên k
                if k == 4:
                    s_min = random.choice([5, 8, 10]) # m < 3.2, m < 2, m < 1.6
                elif k == 6:
                    s_min = random.choice([10, 12, 15]) # m < 3.6, m < 3, m < 2.4
                else:
                    s_min = random.choice([15, 20, 25])

                # Tính toán giá trị giới hạn của m: m < k^2 / s_min
                limit = Rational(k**2, s_min)
                limit_float = float(limit)

                # Tập hợp các số nguyên dương m
                S_set = []
                for m_val in range(1, 20): # Xét m nguyên dương
                    if m_val < limit_float:
                        S_set.append(m_val)

                kq_count = len(S_set) # Số phần tử của tập S

                # Đáp án đúng
                da = '$%s$' % (latex(kq_count))

                # Tạo các phương án sai
                s = []
                # Thêm các giá trị lân cận nhưng phải là số tự nhiên và khác đáp án đúng
                for i in [1, 2, 3, 4, 5]:
                    if i != kq_count:
                        s.append('$%s$' % (latex(i)))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hai đường thẳng $d_1 : y = mx - %s$; $d_2 : y = -mx - %s$. Gọi $S$ là tập hợp các giá trị nguyên dương của $m$ để tam giác tạo thành bởi $d_1, d_2$ và trục hoành có diện tích lớn hơn $%s$. Số phần tử của tập $S$ bằng bao nhiêu?'''
                                 % (latex(k), latex(k), latex(s_min)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Tọa độ A, B là giao điểm với trục hoành (y=0)
                # mx - k = 0 => x = k/m; -mx - k = 0 => x = -k/m
                loigiai = ('''$d_1 : y = mx - %s, d_2 : y = -mx - %s$.\\\\
                             $d_1, d_2$ cắt nhau và cùng cắt trục hoành khi $m \\neq 0$.\\\\
                             Gọi $A\\left(\\frac{%s}{m}; 0\\right), B\\left(-\\frac{%s}{m}; 0\\right)$ lần lượt là giao điểm của $d_1, d_2$ và trục hoành.\\\\
                             Phương trình hoành độ giao điểm của $d_1, d_2$: $mx - %s = -mx - %s \\Leftrightarrow 2mx = 0 \\Leftrightarrow x = 0$.\\\\
                             Gọi $C$ là giao điểm của $d_1$ và $d_2$ thì $C(0; -%s)$.\\\\
                             Diện tích tam giác $ABC$ là: $S_{ABC} = \\frac{1}{2} d(C, Ox) \\cdot AB$.\\\\
                             Có $d(C, Ox) = |y_C| = %s$, $AB = |x_A - x_B| = \\left| \\frac{%s}{m} - \\left( -\\frac{%s}{m} \\right) \\right| = \\frac{%s}{|m|}$.\\\\
                             $\\Rightarrow S_{ABC} = \\frac{1}{2} \\cdot %s \\cdot \\frac{%s}{|m|} = \\frac{%s}{|m|}$.\\\\
                             Theo đề bài: $S_{ABC} > %s \\Leftrightarrow \\frac{%s}{|m|} > %s \\Leftrightarrow |m| < %s$.\\\\
                             Vì $m$ là số nguyên dương nên $m \\in \\{%s\\}$.\\\\
                             Vậy số phần tử của tập $S$ là $%s$.'''
                           % (latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k),
                              latex(k), latex(k), latex(k), latex(2*k), 
                              latex(k), latex(2*k), latex(k**2),
                              latex(s_min), latex(k**2), latex(s_min), latex(limit),
                              ', '.join(map(str, S_set)), latex(kq_count)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_count)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

