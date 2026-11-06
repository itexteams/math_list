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


def bt_dang16_p1_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các xác suất cơ bản (từ 0.1 đến 0.9 để số liệu đẹp như mẫu)
                B_val = random.randint(1, 9)
                A_B_val = random.randint(1, 9)
                A_Bbar_val = random.randint(1, 9)

                # Đảm bảo P(A|B) khác P(A|B ngang) để bài toán không bị tầm thường
                while A_B_val == A_Bbar_val:
                    A_Bbar_val = random.randint(1, 9)

                pB = B_val / 10.0
                pA_B = A_B_val / 10.0
                pA_Bbar = A_Bbar_val / 10.0

                # Tính xác suất biến cố đối P(B ngang)
                pBbar = (10 - B_val) / 10.0

                # Tính xác suất P(A) bằng công thức xác suất toàn phần
                pA = round(pB * pA_B + pBbar * pA_Bbar, 2)

                # Hàm chuyển đổi số thực sang định dạng chuỗi dùng dấu phẩy (chuẩn Việt Nam)
                def format_num(val):
                    if val == int(val):
                        return str(int(val))
                    return str(round(val, 2)).replace('.', ',')

                pB_str = format_num(pB)
                pA_B_str = format_num(pA_B)
                pA_Bbar_str = format_num(pA_Bbar)
                pBbar_str = format_num(pBbar)
                pA_str = format_num(pA)

                # Tạo các phương án nhiễu (Set để tránh trùng lặp)
                wrong_set = set()
                wrong_set.add(round(pB * pA_B, 2))                   # Lỗi 1: Chỉ tính phần P(B)*P(A|B)
                wrong_set.add(round(pBbar * pA_Bbar, 2))             # Lỗi 2: Chỉ tính phần P(B ngang)*P(A|B ngang)
                wrong_set.add(round(pB * pA_Bbar + pBbar * pA_B, 2)) # Lỗi 3: Nhân chéo nhầm các xác suất
                wrong_set.add(round(1 - pA, 2))                      # Lỗi 4: Tính nhầm sang P(A ngang)

                distractors = []
                for w in wrong_set:
                    if w != pA and 0 < w < 1:
                        distractors.append(w)

                # Bổ sung phương án ngẫu nhiên nếu thuật toán phía trên chưa đủ 3 nhiễu
                while len(distractors) < 3:
                    w = round(random.randint(1, 99) / 100.0, 2)
                    if w != pA and w not in distractors:
                        distractors.append(w)

                random.shuffle(distractors)

                # Chuẩn bị đáp án trắc nghiệm (Tuyệt đối không có dấu chấm cuối đáp án)
                da = '$%s$' % pA_str
                das1 = '$%s$' % format_num(distractors[0])
                das2 = '$%s$' % format_num(distractors[1])
                das3 = '$%s$' % format_num(distractors[2])

                # Câu hỏi (Dùng chuỗi thay vì raw string)
                noidungcauhoi = ('''Cho hai biến cố $A$, $B$ với $P(B)=%s$; $P(A|B)=%s$ và $P(A|\\overline{B})=%s$. Khi đó $P(A)$ bằng''' 
                                 % (pB_str, pA_B_str, pA_Bbar_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có: $P(\\overline{B}) = 1 - P(B) = 1 - %s = %s$\\\\
            Theo công thức xác suất toàn phần ta có:\\\\
            $P(A) = P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B}) = %s \\cdot %s + %s \\cdot %s = %s$.''' 
                           % (pB_str, pBbar_str, pB_str, pA_B_str, pBbar_str, pA_Bbar_str, pA_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

