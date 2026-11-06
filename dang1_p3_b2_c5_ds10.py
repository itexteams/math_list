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


def bt_dang1_p3_b2_c5_ds10(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dùng vòng lặp để đảm bảo kq_val < 9999
                while True:
                    a = random.randint(2, 3)  # Giảm bớt phạm vi số lượng từng loại
                    b = random.randint(2, 3)
                    c = random.randint(2, 3)
                    t = a + b + c             # Tổng số sách
                    k = 5                     # Số sách lấy ra tặng

                    # Điều kiện tiên quyết: Tổng số sách phải >= k
                    if t < k: continue

                    # Tính toán theo Nguyên lý bao hàm - loại trừ
                    # Tổng số cách tặng 5 cuốn bất kỳ cho 5 học sinh (Chỉnh hợp)
                    xa = math.perm(t, k)

                    # S1: Tặng hết sách Toán
                    xb = math.comb(t - a, k - a) * math.factorial(k) if k >= a else 0
                    # S2: Tặng hết sách Hóa
                    xc = math.comb(t - b, k - b) * math.factorial(k) if k >= b else 0
                    # S3: Tặng hết sách Sinh
                    xd = math.comb(t - c, k - c) * math.factorial(k) if k >= c else 0

                    # Các trường hợp trùng (Giao điểm): Tặng hết cả 2 loại sách cùng lúc
                    s12 = math.comb(t - (a + b), k - (a + b)) * math.factorial(k) if k >= (a + b) else 0
                    s23 = math.comb(t - (b + c), k - (b + c)) * math.factorial(k) if k >= (b + c) else 0
                    s13 = math.comb(t - (a + c), k - (a + c)) * math.factorial(k) if k >= (a + c) else 0

                    # Kết quả cuối cùng
                    kq_val = xa - (xb + xc + xd) + (s12 + s23 + s13)

                    # Kiểm tra điều kiện kq < 9999
                    if kq_val < 9999:
                        break

                kq = str(kq_val)

                # 2. Tạo nội dung câu hỏi
                noidungcauhoi = ('Một thầy giáo có $%s$ cuốn sách đôi một khác nhau, trong đó có $%s$ cuốn Toán, '
                                 '$%s$ cuốn Hóa và $%s$ cuốn Sinh. Ông muốn lấy ra $5$ cuốn và tặng cho $5$ học sinh '
                                 'sao cho sau khi tặng mỗi loại sách còn lại ít nhất một cuốn. '
                                 'Khi đó tất cả số cách tặng bằng bao nhiêu?'
                                 % (latex(t), latex(a), latex(b), latex(c)))

                # 3. Tạo nội dung lời giải
                buoc_giao = ''
                if (s12 + s23 + s13) > 0:
                    buoc_giao = ('Các trường hợp tặng hết đồng thời hai loại sách là: '
                                 '$S_{12} = %s$; $S_{23} = %s$; $S_{13} = %s$. \\\\'
                                 'Theo nguyên lý bao hàm - loại trừ, số cách tặng thỏa mãn là: '
                                 '$S - (S_1 + S_2 + S_3) + (S_{12} + S_{23} + S_{13}) = %s$ (cách).' 
                                 % (latex(s12), latex(s23), latex(latex(s13)), latex(kq_val)))
                else:
                    buoc_giao = ('Vì không thể tặng hết cùng lúc hai loại sách nên số cách tặng thỏa mãn là '
                                 '$S - S_1 - S_2 - S_3 = %s$ (cách).' % latex(kq_val))

                loigiai = ('Số cách lấy $5$ cuốn sách bất kỳ tặng cho $5$ học sinh là $S = A_{%s}^{5} = %s$ (cách). \\\\'
                           'Số cách tặng mà loại sách Toán không còn cuốn nào là $S_1 = C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot 5! = %s$ (cách). \\\\'
                           'Số cách tặng mà loại sách Hóa không còn cuốn nào là $S_2 = C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot 5! = %s$ (cách). \\\\'
                           'Số cách tặng mà loại sách Sinh không còn cuốn nào là $S_3 = C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot 5! = %s$ (cách). \\\\'
                           '%s'
                           % (latex(t), latex(xa), 
                              latex(a), latex(a), latex(t-a), latex(k-a), latex(xb),
                              latex(b), latex(b), latex(t-b), latex(k-b), latex(xc),
                              latex(c), latex(c), latex(t-c), latex(k-c), latex(xd),
                              buoc_giao))
                dapan=' \\shortans[0]{$%s$} '%(kq)
                # 4. Các đáp án trắc nghiệm
                da_d = ('\\True $%s$' % (kq))

                s_set = set()
                while len(s_set) < 3:
                    offset = random.choice([120, -120, 240, -240, 500, 1000, -500])
                    nhieu = kq_val + offset
                    if nhieu > 0 and nhieu != kq_val:
                        s_set.add('$%s$' % (latex(nhieu)))

                list_ans = [da_d] + list(s_set)
                random.shuffle(list_ans)

                # 5. Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

