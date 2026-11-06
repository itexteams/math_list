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


def bt_dang53_p1_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Để giữ đúng logic lời giải như hình mẫu:
                # 1. Khối 12 phải có số học sinh >= k (để có trường hợp "chỉ có khối 12")
                # 2. Khối 11 và 10 phải có số học sinh < k (để không có trường hợp "chỉ có khối 11" hoặc "chỉ có khối 10")
                # 3. Tổng số học sinh mỗi cặp khối phải >= k
                k = 6
                n12 = randint(6, 8)  # Số học sinh khối 12
                n11 = randint(4, 5)  # Số học sinh khối 11
                n10 = randint(4, 5)  # Số học sinh khối 10
                N = n12 + n11 + n10

                def combinations(n, r):
                    if r > n or r < 0:
                        return 0
                    return math.comb(n, r)

                # Tính toán các bước theo lời giải mẫu
                total_ways = combinations(N, k)
                c_only_12 = combinations(n12, k)
                c_10_11 = combinations(n10 + n11, k)

                # Chỉ có khối 10 và 12 (loại trừ trường hợp chỉ có khối 12)
                c_10_12_all = combinations(n10 + n12, k)
                c_10_12_strictly = c_10_12_all - c_only_12

                # Chỉ có khối 11 và 12 (loại trừ trường hợp chỉ có khối 12)
                c_11_12_all = combinations(n11 + n12, k)
                c_11_12_strictly = c_11_12_all - c_only_12

                # Đáp án đúng
                kq_dung = total_ways - c_only_12 - c_10_11 - c_10_12_strictly - c_11_12_strictly

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                da = '$%s$' % (kq_dung)

                s_list = [
                    total_ways,
                    kq_dung - randint(1, 100),
                    kq_dung + randint(1, 100),
                    c_10_11 + c_10_12_strictly + c_11_12_strictly,
                    combinations(N-1, k),
                    combinations(N, k-1)
                ]

                # Lọc các phương án sai để không trùng nhau và không trùng đáp án đúng
                wrong_candidates = []
                for val in s_list:
                    if val != kq_dung and val > 0 and val not in wrong_candidates:
                        wrong_candidates.append(val)

                while len(wrong_candidates) < 3:
                    val = kq_dung + randint(-200, 200)
                    if val != kq_dung and val > 0 and val not in wrong_candidates:
                        wrong_candidates.append(val)

                random.shuffle(wrong_candidates)
                das1 = '$%s$' % (wrong_candidates[0])
                das2 = '$%s$' % (wrong_candidates[1])
                das3 = '$%s$' % (wrong_candidates[2])

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ học sinh giỏi gồm $%s$ học sinh khối 12, $%s$ học sinh khối 11 và $%s$ học sinh khối 10. Hỏi có bao nhiêu cách chọn ra $%s$ học sinh sao cho mỗi khối có ít nhất 1 học sinh?'''
                                 %(latex(N), latex(n12), latex(n11), latex(n10), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Số cách chọn $%s$ học sinh bất kỳ trong $%s$ học sinh là $C_{%s}^{%s} = %s$.\\\\
                             Số cách chọn $%s$ học sinh chỉ có khối 12 là $C_{%s}^{%s} = %s$ cách.\\\\
                             Số cách chọn $%s$ học sinh chỉ có khối 10 và 11 là $C_{%s}^{%s} = %s$ cách.\\\\
                             Số cách chọn $%s$ học sinh chỉ có khối 10 và 12 là $C_{%s}^{%s} - C_{%s}^{%s} = %s$ cách.\\\\
                             Số cách chọn $%s$ học sinh chỉ có khối 11 và 12 là $C_{%s}^{%s} - C_{%s}^{%s} = %s$ cách.\\\\
                             Do đó số cách chọn $%s$ học sinh sao cho mỗi khối có ít nhất 1 học sinh là\\\\
                             $%s - %s - %s - %s - %s = %s$ cách.'''
                         %(latex(k), latex(N), latex(N), latex(k), latex(total_ways),
                           latex(k), latex(n12), latex(k), latex(c_only_12),
                           latex(k), latex(n10 + n11), latex(k), latex(c_10_11),
                           latex(k), latex(n10 + n12), latex(k), latex(n12), latex(k), latex(c_10_12_strictly),
                           latex(k), latex(n11 + n12), latex(k), latex(n12), latex(k), latex(c_11_12_strictly),
                           latex(k), latex(total_ways), latex(c_only_12), latex(c_10_11), latex(c_10_12_strictly), latex(c_11_12_strictly), latex(kq_dung)
                          ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

