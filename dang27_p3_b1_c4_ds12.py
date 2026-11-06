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


def bt_dang27_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng bi của màu thứ 3 (bi màu đỏ trong hình)
                # Giữ nguyên 2 bi xanh và 2 bi vàng để đảm bảo logic bài toán không quá phức tạp
                k = random.randint(2, 4) # Số bi màu đỏ
                tong_bi = 4 + k

                # Danh sách màu sắc để random tên gọi cho sinh động
                colors = ['xanh', 'đỏ', 'vàng', 'tím', 'trắng', 'đen']
                random.shuffle(colors)
                c1, c2, c3 = colors[0], colors[1], colors[2]
                # c1: bi không đứng cạnh nhau (xanh)
                # c2: bi đứng cạnh nhau (vàng)
                # c3: bi còn lại (đỏ)

                # 1. Tính số cách xếp sao cho 2 bi c1 không đứng cạnh nhau: n(Omega)
                # n(Omega) = (tong_bi)! - (tong_bi - 1)! * 2!
                omega = factorial(tong_bi) - factorial(tong_bi - 1) * 2

                # 2. Tính số cách xếp sao cho 2 bi c2 cạnh nhau và 2 bi c1 không cạnh nhau: n(A)
                # Coi 2 bi c2 là 1 nhóm: có 2! cách xếp nội bộ
                # Xếp nhóm c2 và k bi c3: có (k + 1) vật thể -> (k + 1)! cách xếp
                # Số vị trí trống để xếp 2 bi c1 là (k + 2) vị trí: _ O _ O _ ... _
                # Số cách xếp 2 bi c1 vào k+2 vị trí là A(k+2, 2)
                vi_tri_trong = k + 2
                cach_xep_c1 = vi_tri_trong * (vi_tri_trong - 1)
                cach_xep_con_lai = factorial(k + 1) * 2
                nA = cach_xep_c1 * cach_xep_con_lai

                # 3. Tính xác suất
                prob = Rational(nA, omega)
                val_prob = float(prob)

                # Làm tròn đến hàng phần trăm theo yêu cầu
                kq_decimal = Decimal(str(val_prob)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % kq_str

                # Tạo các đáp án nhiễu
                s = set()
                while len(s) < 3:
                    nhieu = val_prob + random.choice([-0.1, 0.1, -0.05, 0.05, -0.15, 0.15])
                    if nhieu > 0 and nhieu < 1:
                        val_nhieu = Decimal(str(nhieu)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                        str_nhieu = '$%s$' % str(val_nhieu).replace('.', ',')
                        if str_nhieu != da_dung:
                            s.add(str_nhieu)

                list_nhieu = list(s)
                da_s1 = list_nhieu[0]
                da_s2 = list_nhieu[1]
                da_s3 = list_nhieu[2]

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ viên bi đôi một khác nhau, gồm $2$ viên bi màu %s, $2$ viên bi màu %s và $%s$ viên bi màu %s. Xếp ngẫu nhiên $%s$ viên bi đó thành một hàng ngang. Xác suất để $2$ viên bi màu %s đứng cạnh nhau bằng bao nhiêu? Biết $2$ viên bi màu %s không đứng cạnh nhau (kết quả làm tròn đến hàng phần trăm).'''
                                 % (latex(tong_bi), c1, c2, latex(k), c3, latex(tong_bi), c2, c1))

                # Lời giải chi tiết
                loigiai = ('''Tính số cách xếp sao cho $2$ viên bi màu %s không đứng cạnh nhau và $2$ viên bi màu %s đứng cạnh nhau: \\\\
            + Ta coi $2$ bi màu %s là $1$ nhóm, có $2! = 2$ cách xếp nội bộ nhóm này. \\\\
            + Xếp $%s$ viên bi màu %s và nhóm $2$ bi màu %s: Có $%s$ vật thể, số cách xếp là $(%s + 1)! = %s! = %s$ (cách). \\\\
            + Khi đó có $%s$ vị trí trống để xếp $2$ viên bi màu %s sao cho chúng không cạnh nhau. Số cách xếp là: $A_{%s}^2 = %s$ (cách). \\\\
            Vậy có: $%s \\cdot %s = %s$ (cách). \\\\
            + Số cách xếp sao cho $2$ viên bi màu %s không đứng cạnh nhau (không gian mẫu thu hẹp) là: $%s! - %s! \\cdot 2! = %s$ (cách). \\\\
            Tính xác suất: \\\\
            Yêu cầu đề bài có thể hiểu là: Trong số $%s$ cách xếp $2$ viên bi màu %s không đứng cạnh nhau thì có bao nhiêu cách mà $2$ bi màu %s đứng cạnh nhau. \\\\
            Từ đó: Xác suất cần tìm là: $\\frac{%s}{%s} \\approx %s$.'''
                           % (c1, c2, c2, latex(k), c3, c2, latex(k+1), latex(k), latex(k+1), factorial(k+1), 
                              latex(vi_tri_trong), c1, latex(vi_tri_trong), latex(cach_xep_c1), 
                              latex(cach_xep_con_lai), latex(cach_xep_c1), latex(nA), 
                              c1, latex(tong_bi), latex(tong_bi-1), latex(omega),
                              latex(omega), c1, c2, latex(nA), latex(omega), kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

                # Các đáp án
                da_d = '\\True ' + str(da_dung)
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

