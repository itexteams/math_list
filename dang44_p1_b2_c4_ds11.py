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


def bt_dang44_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM CÁC THÔNG SỐ ĐỂ ĐẢM BẢO NGHIỆM NGUYÊN ---
                # Giả sử tử số có dạng: (x - x0)(ax + k)
                x0 = random.randint(2,9) # Điểm giới hạn (thường là 1, 2, 3)
                a_val = random.randint(2,9) # Hệ số a
                k_val = random.randint(2, 9) # Hệ số tự do của nhân tử thứ 2

                # Khai triển: (x - x0)(ax + k) = ax^2 + (k - a*x0)x - k*x0
                # Vậy b = k - a*x0
                # Vậy c = -k*x0
                b_val = k_val - a_val * x0
                c_val = -k_val * x0

                # Giá trị giới hạn L = ax0 + k
                L_val = a_val * x0 + k_val

                # Tính giá trị biểu thức mục tiêu: P = a^2 + b^2 + a + b
                kq_val = a_val**2 + b_val**2 + a_val + b_val
                da = '$%s$' % (latex(kq_val))

                # --- BƯỚC 2: TẠO ĐÁP ÁN NHIỄU ---
                s = set()
                while len(s) < 3:
                    sai = kq_val + random.choice([-2, -1, 1, 2, 3, 5, 10])
                    if sai != kq_val and sai > 0:
                        s.add('$%s$' % (latex(sai)))
                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # --- BƯỚC 3: XỬ LÝ HIỂN THỊ DẤU ---
                # Để tránh viết "+ -5", ta xử lý hiển thị số c
                dau_c = "+" if c_val > 0 else ""
                dau_b = "+" if b_val > 0 else ""

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'''Cho $a, b$ là số nguyên và $\lim_{x \to %s} \frac{ax^2 + bx %s %s}{x - %s} = %s$. Giá trị $a^2 + b^2 + a + b$ bằng'''
                                 % (latex(x0), dau_c, latex(c_val), latex(x0), latex(L_val)))

                # --- BƯỚC 5: NỘI DUNG LỜI GIẢI ---
                # Tính toán các bước trung gian cho lời giải
                tong_ab = -c_val/x0 # a*x0 + b = -c/x0

                loigiai = (r'''Vì $\lim_{x \to %s} \frac{ax^2 + bx %s %s}{x - %s} = %s$ hữu hạn nên $x = %s$ phải là nghiệm của phương trình \\
                           $ax^2 + bx %s %s = 0$ suy ra $a(%s)^2 + b(%s) %s %s = 0 \Rightarrow b = %s - %s a$. \\
                           Khi đó $\lim_{x \to %s} \frac{ax^2 + (%s - %s a)x %s %s}{x - %s} = \lim_{x \to %s} \frac{(x - %s)(ax + %s)}{x - %s} = a(%s) + %s = %s$. \\
                           Giải phương trình ta được $a = %s$, từ đó suy ra $b = %s$. \\
                           Vậy giá trị biểu thức: $a^2 + b^2 + a + b = %s^2 + %s^2 + %s + %s = %s$.'''
                           % (latex(x0), dau_c, latex(c_val), latex(x0), latex(L_val), latex(x0),
                              dau_c, latex(c_val), latex(x0), latex(x0), dau_c, latex(c_val), latex(-c_val//x0), latex(x0),
                              latex(x0), latex(-c_val//x0), latex(x0), dau_c, latex(c_val), latex(x0), 
                              latex(x0), latex(x0), latex(k_val), latex(x0), latex(x0), latex(k_val), latex(L_val),
                              latex(a_val), latex(b_val),
                              latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(kq_val)))

                # Trộn đáp án
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất kết quả theo format mẫu
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

