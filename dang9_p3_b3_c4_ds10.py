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


def bt_dang9_p3_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số a, b', và các thành phần của c trong phương trình bậc 2
                # Phương trình có dạng: a*x^2 + 2(m + b_sub)*x + (m^2 + c1*m + c2) = 0
                a = 2
                b_sub = randint(1, 4) # Trong ảnh là 2
                c1 = randint(3, 6)    # Trong ảnh là 4
                c2 = randint(2, 5)    # Trong ảnh là 3

                m = symbols('m')

                # Tính Delta' = (m + b_sub)^2 - a*(m^2 + c1*m + c2)
                # Delta' = m^2 + 2*b_sub*m + b_sub^2 - a*m^2 - a*c1*m - a*c2
                # Delta' = (1-a)m^2 + (2*b_sub - a*c1)m + (b_sub^2 - a*c2)

                A_m = 1 - a
                B_m = 2 * b_sub - a * c1
                C_m = b_sub**2 - a * c2

                # Bất phương trình: A_m*m^2 + B_m*m + C_m >= 0
                # Vì A_m luôn âm (-1), ta có: m^2 - B_m/A_m * m - C_m/A_m <= 0
                # m^2 + (B_m)*m + (C_m) <= 0 (với hệ số m^2 là 1 sau khi đổi dấu)

                # Tìm nghiệm của tam thức bậc hai theo m để tìm khoảng giá trị
                delta_m = B_m**2 - 4*A_m*C_m

                if delta_m < 0:
                    # Trường hợp này hiếm do cách chọn số, nếu xảy ra ta chọn lại bộ số cố định như ảnh
                    A_m, B_m, C_m = -1, -4, -2
                    delta_m = 8
                    b_sub, a, c1, c2 = 2, 2, 4, 3

                m1 = (-B_m - sqrt(delta_m)) / (2 * A_m)
                m2 = (-B_m + sqrt(delta_m)) / (2 * A_m)

                start_val = float(min(m1, m2))
                end_val = float(max(m1, m2))

                # Tìm các giá trị m nguyên
                ds_m = []
                for i in range(math.ceil(start_val), math.floor(end_val) + 1):
                    ds_m.append(i)

                kq = len(ds_m)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(kq))

                # Tạo các phương án sai không trùng đáp án đúng
                s_list = []
                while len(s_list) < 3:
                    sai = randint(max(0, kq - 4), kq + 4)
                    if sai != kq and str(sai) not in s_list:
                        s_list.append(str(sai))

                das1 = '$%s$' % s_list[0]
                das2 = '$%s$' % s_list[1]
                das3 = '$%s$' % s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho phương trình 
                    $%sx^2 + 2(m + %s)x + %s + %sm + m^2 = 0$. Số giá trị nguyên của $m$ để phương trình có nghiệm là'''
                    % (latex(a), latex(b_sub), latex(c2), latex(c1)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Xét $%sx^2 + 2(m + %s)x + m^2 + %sm + %s = 0$, có $\\Delta'_x = (m + %s)^2 - %s(m^2 + %sm + %s)$.\\\\
                    Yêu cầu bài toán $\\Leftrightarrow \\Delta'_x \\ge 0 \\Leftrightarrow m^2 + %sm + %s - %sm^2 - %sm - %s \\ge 0 \\Leftrightarrow %sm^2 + %sm + %s \\ge 0$\\\\
                    $\\Leftrightarrow %sm^2 + %sm + %s \\le 0 \\Leftrightarrow (m + %s)^2 \\le %s \\Leftrightarrow %s \\le m \\le %s$.\\\\
                    Kết hợp với $m \\in \\mathbb{Z}$, ta được $m = \\{%s\\}$ là các giá trị cần tìm. Có $%s$ giá trị nguyên.'''
                    % (latex(a), latex(b_sub), latex(c1), latex(c2), latex(b_sub), latex(a), latex(c1), latex(c2),
                       latex(2*b_sub), latex(b_sub**2), latex(a), latex(a*c1), latex(a*c2), 
                       latex(A_m), latex(B_m), latex(C_m),
                       latex(-A_m), latex(-B_m), latex(-C_m),
                       latex(b_sub), latex(Rational(delta_m, 4)), # (m+2)^2 <= 2
                       latex(simplify(m1)), latex(simplify(m2)),
                       '; '.join(map(str, ds_m)), latex(kq)
                    ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

