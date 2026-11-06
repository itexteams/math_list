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


def bt_dang71_p1_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1: Nghiên cứu và khởi tạo các số ngẫu nhiên
                # Hàm số có dạng y = (mx + n) / sqrt(x^2 + k)
                m = randint(2, 5)
                n = randint(1, 4)
                k = randint(2, 6)

                # Tính toán theo logic BĐT Bu-nhi-a-cốp-xki
                # (mx + n)^2 = (m*x + (n/sqrt(k))*sqrt(k))^2 <= (m^2 + n^2/k)(x^2 + k)
                # y^2 <= (m^2*k + n^2) / k

                tu_so_phuong_sai = m**2 * k + n**2
                mau_so_phuong_sai = k

                # Rút gọn phân số để tìm b nhỏ nhất
                phan_so_rut_gon = Rational(tu_so_phuong_sai, mau_so_phuong_sai)
                P = phan_so_rut_gon.p # Tử số sau rút gọn
                Q = phan_so_rut_gon.q # Mẫu số sau rút gọn

                # Để đưa về dạng sqrt(a)/b với b nhỏ nhất: 
                # M = sqrt(P/Q) = sqrt(P*Q)/Q
                a_val = P * Q
                b_val = Q
                kq_dung = a_val + b_val

                # Điểm rơi x: x/m = sqrt(k)/(n/sqrt(k)) => x = m*k/n
                x_point = Rational(m * k, n)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(kq_dung))

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_dung + random.choice([-10, -5, 2, 5, 10, 15, 20])
                    if sai != kq_dung and sai > 0:
                        s.add('$%s$' % (latex(sai)))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''Gọi $M$ là giá trị lớn nhất của hàm số $y = \frac{%sx + %s}{\sqrt{x^2 + %s}}$. Biết $M = \frac{\sqrt{a}}{b}$ với $a, b \in \mathbb{N}^*$ và $b$ nhỏ nhất. Tổng $a + b$ bằng'''
                                 % (latex(m), latex(n), latex(k)))

                # Nội dung lời giải (B2: Viết lại y hệt logic trong ảnh)
                loigiai = (r'''Áp dụng bất đẳng thức Bu-nhi-a-cốp-xki ta có: \\
                             $\left(%sx + %s\right)^2 = \left(%s \cdot x + \frac{%s}{\sqrt{%s}} \cdot \sqrt{%s}\right)^2 \le \left(%s^2 + \frac{%s^2}{%s}\right)(x^2 + %s)$. \\
                             Suy ra $%sx + %s \le \sqrt{\frac{%s}{%s}} \sqrt{x^2 + %s}$ \\
                             $\Rightarrow \frac{%sx + %s}{\sqrt{x^2 + %s}} \le \sqrt{\frac{%s}{%s}} = \frac{\sqrt{%s}}{%s}$. \\
                             Dấu bằng xảy ra khi $\frac{x}{%s} = \frac{\sqrt{%s}}{\frac{%s}{\sqrt{%s}}} \Leftrightarrow x = %s$. \\
                             Vậy $M = \frac{\sqrt{%s}}{%s}$, tức là $a = %s, b = %s \Rightarrow a + b = %s$.'''
                           % (latex(m), latex(n), latex(m), latex(n), latex(k), latex(k), latex(m), latex(n), latex(k), latex(k),
                              latex(m), latex(n), latex(tu_so_phuong_sai), latex(mau_so_phuong_sai), latex(k),
                              latex(m), latex(n), latex(k), latex(tu_so_phuong_sai), latex(mau_so_phuong_sai), latex(a_val), latex(b_val),
                              latex(m), latex(k), latex(n), latex(k), latex(x_point),
                              latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(kq_dung)
                             ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

