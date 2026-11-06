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


def bt_dang24_p3_b1_c2_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        while True:
            # Tọa độ điểm A(xA; yA; zA)
            xA = randint(1, 4)
            yA = randint(-2, 2)
            zA = randint(1, 4)

            # Hai vectơ a = (a1, a2, a3) và b = (b1, b2, b3)
            a1, a2, a3 = randint(1, 3), randint(-4, -1), randint(1, 4)
            b1, b2, b3 = randint(-3, -1), randint(-3, 1), randint(1, 4)

            # Tích có hướng [a, b] = (nx_0, ny_0, nz_0)
            nx_0 = a2 * b3 - a3 * b2
            ny_0 = a3 * b1 - a1 * b3
            nz_0 = a1 * b2 - a2 * b1

            # Điều kiện hai vectơ không cùng phương
            if nx_0 == 0 and ny_0 == 0 and nz_0 == 0:
                continue

            # Mặt phẳng (Q) đi qua A có phương trình: nx_0*(x - xA) + ny_0*(y - yA) + nz_0*(z - zA) = 0
            # <=> nx_0*x + ny_0*y + nz_0*z + D_0 = 0
            D_0 = -(nx_0 * xA + ny_0 * yA + nz_0 * zA)

            # Đề bài cho phương trình dạng ax + by + cz - D_const = 0 (ở mẫu là - 3 = 0)
            # Ta chọn số nguyên dương D_const (từ 2 đến 5) sao cho D_0 chia hết cho -D_const hoặc ngược lại
            D_const = randint(2, 5)

            # Cần tồn tại k hữu tỉ sao cho k * D_0 = -D_const => k = -D_const / D_0
            # Để a, b, c là các số nguyên đẹp, D_0 phải là ước của -D_const hoặc tỉ lệ đẹp
            if D_0 == 0:
                continue

            # Chọn k sao cho a = k*nx_0, b = k*ny_0, c = k*nz_0 đều là số nguyên
            # Rút gọn (nx_0, ny_0, nz_0, D_0) theo ước chung lớn nhất
            gcd_all = math.gcd(math.gcd(abs(nx_0), abs(ny_0)), math.gcd(abs(nz_0), abs(D_0)))
            nx_red = nx_0 // gcd_all
            ny_red = ny_0 // gcd_all
            nz_red = nz_0 // gcd_all
            D_red = D_0 // gcd_all

            # Ta muốn D_red * m = -D_const với m là số nguyên
            # Để đơn giản và luôn nguyên đẹp, ta đặt D_const = abs(D_red) nếu abs(D_red) <= 10 và D_red != 0
            if abs(D_red) > 10 or D_red == 0:
                continue

            if D_red < 0:
                a_val = nx_red
                b_val = ny_red
                c_val = nz_red
                D_const = -D_red
            else:
                a_val = -nx_red
                b_val = -ny_red
                c_val = -nz_red
                D_const = D_red

            ans_val = a_val + b_val + c_val

            # Đảm bảo kết quả là số nguyên trong khoảng (-999, 9999)
            if -999 < ans_val < 9999:
                break

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong không gian với hệ toạ độ $Oxyz$, cho điểm $A(%s;%s;%s)$ và hai vectơ $\\vec{a}=(%s;%s;%s)$, $\\vec{b}=(%s;%s;%s)$. Một mặt phẳng $(Q)$ chứa điểm $A$ và nhận $\\vec{a}, \\vec{b}$ làm cặp vectơ chỉ phương có phương trình là $ax + by + cz - %s = 0$. Tính $a+b+c$.'''
                         % (xA, yA, zA,
                            a1, a2, a3,
                            b1, b2, b3,
                            D_const))

        # Nội dung lời giải
        loigiai = ('''Véctơ pháp tuyến của mặt phẳng $(Q)$ là:\\\\
                   $\\vec{n} = [\\vec{a}, \\vec{b}] = ((%s) \\cdot (%s) - (%s) \\cdot (%s); (%s) \\cdot (%s) - (%s) \\cdot (%s); (%s) \\cdot (%s) - (%s) \\cdot (%s)) = (%s; %s; %s)$.\\\\
                   Mặt phẳng $(Q)$ đi qua điểm $A(%s;%s;%s)$ và nhận vectơ pháp tuyến $\\vec{n}' = (%s; %s; %s)$ có phương trình là:\\\\
                   $%s(x - %s) + (%s)(y - %s) + (%s)(z - %s) = 0 \\Leftrightarrow %s x + %s y + %s z - %s = 0$.\\\\
                   Đồng nhất với phương trình dạng $ax + by + cz - %s = 0$, ta được:\\\\
                   $a = %s, b = %s, c = %s$.\\\\
                   Khi đó $a+b+c = %s + (%s) + (%s) = %s$.'''
                   % (a2, b3, a3, b2, a3, b1, a1, b3, a1, b2, a2, b1,
                      nx_0, ny_0, nz_0,
                      xA, yA, zA,
                      a_val, b_val, c_val,
                      a_val, xA, b_val, yA, c_val, zA,
                      a_val, b_val, c_val, D_const,
                      D_const,
                      a_val, b_val, c_val,
                      a_val, b_val, c_val, ans_val))

        # Đáp án dạng câu trả lời ngắn
        dapan = '\\shortans[0]{$%s$}\n' % (ans_val)

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+').replace('+ -', '-')
    return content

