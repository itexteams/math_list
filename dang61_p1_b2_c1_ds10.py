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


def bt_dang61_p1_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo ngẫu nhiên số lượng cử tri ở từng vùng đơn lẻ trong biểu đồ Venn để đảm bảo tính logic
                x7 = random.randint(8, 12)     # Số cử tri thích cả 3 ứng cử viên A, B, C
                x4 = random.randint(6, 12)     # Chỉ thích A và B
                x5 = random.randint(6, 12)     # Chỉ thích B và C
                x6 = random.randint(10, 15)    # Chỉ thích C và A

                x1 = random.randint(12, 18)    # Chỉ thích A
                x2 = random.randint(15, 25)    # Chỉ thích B
                x3 = random.randint(15, 25)    # Chỉ thích C (Đây chính là đáp án đúng)

                x0 = random.randint(5, 15)     # Không thích ứng cử viên nào

                # Tính toán các thông số tổng hợp xuất hiện trong đề bài
                nu = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7  # Tổng số cử tri được phỏng vấn
                nA = x1 + x4 + x6 + x7                      # Tổng số cử tri thích A
                nB = x2 + x4 + x5 + x7                      # Tổng số cử tri thích B
                nC = x3 + x5 + x6 + x7                      # Tổng số cử tri thích C
                nAB = x4 + x7                               # Thích A và B
                nBC = x5 + x7                               # Thích B và C
                nCA = x6 + x7                               # Thích C và A
                nABC = x7                                   # Thích cả A, B, C

                kq = x3

                # Đáp án trắc nghiệm đúng
                da = '$%s$' % (latex(kq))

                # Tạo danh sách các phương án sai (nhiễu) không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    wrong = kq + random.choice([-5, -3, -2, -1, 1, 2, 3, 5])
                    sub_wrong = nC - nCA - nBC  # Lỗi sai phổ biến khi quên cộng lại phần giao ba tập hợp
                    if wrong > 0 and wrong != kq:
                        s.add('$%s$' % (latex(wrong)))
                    if sub_wrong > 0 and sub_wrong != kq:
                        s.add('$%s$' % (latex(sub_wrong)))
                    if x1 != kq:
                        s.add('$%s$' % (latex(x1)))
                    if x2 != kq:
                        s.add('$%s$' % (latex(x2)))

                list_s = list(s)
                random.shuffle(list_s)
                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trước kì bầu cử một phóng viên đã phỏng vấn thăm dò tình cảm $%s$ cử tri đối với ba ứng cử viên $A, B, C$ và có kết quả như sau: số cử tri có tình cảm với ứng cử viên: $A$ là $%s$, $B$ là $%s$, $C$ là $%s$, $A$ và $B$ là $%s$, $B$ và $C$ là $%s$, $C$ và $A$ là $%s$, $A, B$ và $C$ là $%s$. Hỏi số cử tri chỉ có tình cảm với ứng cử viên $C$ là bao nhiêu?'''
                                 %(latex(nu), latex(nA), latex(nB), latex(nC), latex(nAB), latex(nBC), latex(nCA), latex(nABC)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A, B, C$ lần lượt là tập hợp các cử tri có tình cảm với ứng cử viên $A, B, C$. \\\\
                             Theo giả thiết từ đề bài, ta có các số liệu sau: \\\\
                             $|A| = %s$, $|B| = %s$, $|C| = %s$, \\\\
                             $|A \\cap B| = %s$, $|B \\cap C| = %s$, $|C \\cap A| = %s$, \\\\
                             $|A \\cap B \\cap C| = %s$. \\\\
                             Số cử tri chỉ có tình cảm với duy nhất ứng cử viên $C$ được tính bằng công thức: \\\\
                             $|C| - |A \\cap C| - |B \\cap C| + |A \\cap B \\cap C| = %s - %s - %s + %s = %s$.'''
                           %(latex(nA), latex(nB), latex(nC),
                             latex(nAB), latex(nBC), latex(nCA),
                             latex(nABC), latex(nC), latex(nCA), latex(nBC), latex(nABC), latex(kq)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
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

