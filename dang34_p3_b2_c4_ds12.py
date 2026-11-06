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


def bt_dang34_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các giá trị cơ bản để tạo đề bài hợp lý
                # P(A): Xác suất bé An được đi theo mẹ
                b = random.randint(4, 8)
                a = random.randint(1, b - 1)
                pA = Rational(a, b)
                pA_bar = 1 - pA

                # P(B|A): Xác suất được mua đồ chơi khi đi theo mẹ (thường cao)
                d = 10
                c = random.randint(6, 9)
                pB_A = Rational(c, d)
                pB_A_percent = int(float(pB_A) * 100)

                # P(B|not A): Xác suất được mua đồ chơi khi KHÔNG đi theo mẹ (đây là giá trị cần tìm)
                # Ta chọn trước giá trị này để bài toán luôn có nghiệm đẹp
                f = 10
                e = random.randint(2, 5)
                pB_notA_target = Rational(e, f)

                # Tính P(B) theo công thức xác suất toàn phần
                pB = pA * pB_A + pA_bar * pB_notA_target

                # Tính P(A|B) theo công thức Bayes để đưa vào đề bài
                pA_B = (pA * pB_A) / pB

                # Kết quả cần tìm (kq)
                kq_val = float(pB_notA_target)
                kq3 = Decimal(str(kq_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                # Tạo các phương án nhiễu
                sai_so = [0.1, 0.2, -0.1, -0.2, 0.3, -0.3]
                random.shuffle(sai_so)

                s = []
                for delta in sai_so:
                    val = float(kq3) + delta
                    if 0 < val < 1 and val != float(kq3):
                        s.append('$%s$' % (str(round(val, 1)).replace('.', ',')))

                # Đảm bảo có ít nhất 3 đáp án sai
                while len(s) < 3:
                    val = random.uniform(0.1, 0.9)
                    s.append('$%s$' % (str(round(val, 1)).replace('.', ',')))

                da = '$%s$' % kq
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Xác suất bé An được mẹ dẫn theo khi đi mua sắm là $%s$. Khi bé An được đi theo mẹ thì $%s$\\%% bé sẽ được mua đồ chơi. Khi bé không đi theo mẹ, có thể mẹ vẫn mua đồ chơi cho bé. Xác suất bé được đi theo mẹ biết rằng bé được mẹ mua cho đồ chơi là $%s$. Khi bé không đi theo mẹ, xác suất bé được mẹ mua cho đồ chơi là bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (latex(pA), latex(pB_A_percent), latex(pA_B)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A$ là biến cố: "Bé An được mẹ dẫn theo khi đi mua sắm".\\\\
                             Biến cố đối $\\bar{A}$: "Bé An không được đi theo mẹ".\\\\
                             Gọi $B$ là biến cố: "Bé An được mẹ mua đồ chơi".\\\\
                             Theo đề bài, ta có:\\\\
                             $P(A) = %s \\Rightarrow P(\\bar{A}) = 1 - P(A) = %s$.\\\\
                             $P(B|A) = %s\\%% = %s$.\\\\
                             $P(A|B) = %s$.\\\\
                             Ta cần tính $P(B|\\bar{A})$.\\\\
                             Áp dụng công thức xác suất điều kiện: $P(B) \\cdot P(A|B) = P(A) \\cdot P(B|A)$\\\\
                             $\\Rightarrow P(B) = \\frac{P(A) \\cdot P(B|A)}{P(A|B)} = \\frac{%s \\cdot %s}{%s} = %s$.\\\\
                             Mặt khác, theo công thức xác suất toàn phần:\\\\
                             $P(B) = P(A) \\cdot P(B|A) + P(\\bar{A}) \\cdot P(B|\\bar{A})$\\\\
                             $\\Leftrightarrow %s = %s \\cdot %s + %s \\cdot P(B|\\bar{A})$\\\\
                             $\\Leftrightarrow %s = %s + %s \\cdot P(B|\\bar{A})$\\\\
                             $\\Leftrightarrow %s \\cdot P(B|\\bar{A}) = %s \\Rightarrow P(B|\\bar{A}) = %s \\approx %s$.'''
                           % (latex(pA), latex(pA_bar), 
                              latex(pB_A_percent), latex(pB_A), 
                              latex(pA_B),
                              latex(pA), latex(pB_A), latex(pA_B), latex(pB),
                              latex(pB), latex(pA), latex(pB_A), latex(pA_bar),
                              latex(pB), latex(pA * pB_A), latex(pA_bar),
                              latex(pA_bar), latex(pB - pA * pB_A), latex(pB_notA_target), kq))
                dapan=' \\shortans[0]{$%s$} '%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

