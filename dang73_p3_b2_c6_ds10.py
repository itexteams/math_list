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


def bt_dang73_p3_b2_c6_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random số đội của 3 miền và số đội cần chọn k (chẵn để k/2 nguyên)
        # Gốc: nB = 6, nT = 5, nN = 4, k = 6
        nB = randint(5, 7)
        nT = randint(4, 6)
        nN = randint(3, 5)
        k = 6
        N = nB + nT + nN

        # Không gian mẫu: chọn k đội từ N đội
        n_omega = math.comb(N, k)

        c_b1 = math.comb(nB, 1)
        rem1 = k - 1
        # Chọn rem1 = 5 đội từ nT + nN đội, trừ đi TH chỉ có miền Trung hoặc chỉ có miền Nam
        all_TN1 = math.comb(nT + nN, rem1)
        only_T1 = math.comb(nT, rem1) if nT >= rem1 else 0
        only_N1 = math.comb(nN, rem1) if nN >= rem1 else 0
        th1_TN = all_TN1 - only_T1 - only_N1
        so_cach_th1 = c_b1 * th1_TN

        # Trường hợp 2: b = 2
        c_b2 = math.comb(nB, 2)
        rem2 = k - 2
        all_TN2 = math.comb(nT + nN, rem2)
        only_T2 = math.comb(nT, rem2) if nT >= rem2 else 0
        only_N2 = math.comb(nN, rem2) if nN >= rem2 else 0
        th2_TN = all_TN2 - only_T2 - only_N2
        so_cach_th2 = c_b2 * th2_TN

        # Trường hợp 3: b = 3
        c_b3 = math.comb(nB, 3)
        rem3 = k - 3
        all_TN3 = math.comb(nT + nN, rem3)
        only_T3 = math.comb(nT, rem3) if nT >= rem3 else 0
        only_N3 = math.comb(nN, rem3) if nN >= rem3 else 0
        th3_TN = all_TN3 - only_T3 - only_N3
        so_cach_th3 = c_b3 * th3_TN

        # Tổng số cách thỏa mãn biến cố A
        nA = so_cach_th1 + so_cach_th2 + so_cach_th3
        p_frac = Rational(nA, n_omega)

        # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
        number = Decimal(float(p_frac))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong một cuộc thi lập trình trí tuệ nhân tạo cấp quốc gia, có %s đội thi xuất sắc đến từ 3 miền: %s đội miền Bắc, %s đội miền Trung và %s đội miền Nam. Ban tổ chức muốn chọn ngẫu nhiên một nhóm gồm %s đội thi để tham gia vòng triển lãm quốc tế. Xác suất để nhóm %s đội được chọn có đầy đủ đại diện của cả 3 miền, đồng thời số đội miền Bắc được chọn không vượt quá tổng số đội của miền Trung và miền Nam được chọn bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                         %(N, nB, nT, nN, k, k
                         ))

        # Nội dung lời giải
        loigiai = ('''Ta có \\\\
    Tổng số đội tham gia là $%s + %s + %s = %s$ đội. \\\\
    Số phần tử của không gian mẫu là: $n(\\Omega) = C_{%s}^{%s} = %s$. \\\\
    Gọi $A$ là biến cố: "Nhóm %s đội được chọn có đầy đủ đại diện của cả 3 miền, đồng thời số đội miền Bắc không vượt quá tổng số đội của miền Trung và miền Nam". \\\\
    Gọi số đội miền Bắc, miền Trung, miền Nam được chọn lần lượt là $b, t, n$ ($b, t, n \\in \\mathbb{N}^*$). \\\\
    Theo giả thiết: \\\\
    $b + t + n = %s$ và $b \\le t + n$. \\\\
    Suy ra $b \\le %s - b \\Leftrightarrow 2b \\le %s \\Leftrightarrow b \\le %s$. \\\\
    Vì có đủ đại diện cả 3 miền nên $b \\ge 1$, do đó $b \\in \\{1; 2; 3\\}$. \\\\
    Ta xét các trường hợp sau: \\\\
    - Trường hợp 1: $b = 1$ (chọn 1 đội miền Bắc): \\\\
    Số cách chọn 1 đội miền Bắc là $C_{%s}^1 = %s$ cách. \\\\
    Ta cần chọn thêm $%s - 1 = %s$ đội từ $%s + %s = %s$ đội của miền Trung và miền Nam sao cho có cả hai miền: \\\\
    Số cách chọn là $C_{%s}^{%s} - C_{%s}^{%s} - C_{%s}^{%s} = %s - %s - %s = %s$ cách. \\\\
    Suy ra số cách chọn ở trường hợp này là: $%s \\cdot %s = %s$ cách. \\\\
    - Trường hợp 2: $b = 2$ (chọn 2 đội miền Bắc): \\\\
    Số cách chọn 2 đội miền Bắc là $C_{%s}^2 = %s$ cách. \\\\
    Ta cần chọn thêm $%s - 2 = %s$ đội từ %s đội của miền Trung và miền Nam sao cho có cả hai miền: \\\\
    Số cách chọn là $C_{%s}^{%s} - C_{%s}^{%s} - C_{%s}^{%s} = %s - %s - %s = %s$ cách. \\\\
    Suy ra số cách chọn ở trường hợp này là: $%s \\cdot %s = %s$ cách. \\\\
    - Trường hợp 3: $b = 3$ (chọn 3 đội miền Bắc): \\\\
    Số cách chọn 3 đội miền Bắc là $C_{%s}^3 = %s$ cách. \\\\
    Ta cần chọn thêm $%s - 3 = %s$ đội từ %s đội của miền Trung và miền Nam sao cho có cả hai miền: \\\\
    Số cách chọn là $C_{%s}^{%s} - C_{%s}^{%s} - C_{%s}^{%s} = %s - %s - %s = %s$ cách. \\\\
    Suy ra số cách chọn ở trường hợp này là: $%s \\cdot %s = %s$ cách. \\\\
    Số phần tử thuận lợi cho biến cố $A$ là: \\\\
    $n(A) = %s + %s + %s = %s$. \\\\
    Xác suất của biến cố $A$ là: \\\\
    $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = \\frac{%s}{%s} \\approx %s$.'''
                   %(nB, nT, nN, N,
                     N, k, n_omega,
                     k,
                     k, k, k, k // 2,
                     nB, c_b1,
                     k, rem1, nT, nN, nT + nN,
                     nT + nN, rem1, nT, rem1, nN, rem1, all_TN1, only_T1, only_N1, th1_TN,
                     c_b1, th1_TN, so_cach_th1,
                     nB, c_b2,
                     k, rem2, nT + nN,
                     nT + nN, rem2, nT, rem2, nN, rem2, all_TN2, only_T2, only_N2, th2_TN,
                     c_b2, th2_TN, so_cach_th2,
                     nB, c_b3,
                     k, rem3, nT + nN,
                     nT + nN, rem3, nT, rem3, nN, rem3, all_TN3, only_T3, only_N3, th3_TN,
                     c_b3, th3_TN, so_cach_th3,
                     so_cach_th1, so_cach_th2, so_cach_th3, nA,
                     nA, n_omega, p_frac.p, p_frac.q, str(kq_str)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n'
               '\\end{minipage} \n\n')
    return content

