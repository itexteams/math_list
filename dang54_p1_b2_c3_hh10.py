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


def bt_dang54_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các tham số để đảm bảo tọa độ nguyên
                # Phương trình d1: x + y + m = 0
                # Phương trình d2: 2x - y + n = 0
                # Khoảng cách từ A(a, -m-a) đến d2 là sqrt(S)
                # S = 5 * k^2 (để triệt tiêu mẫu số sqrt(5) của khoảng cách)

                k = random.choice([1, 2])
                S_hv = 5 * (k**2)
                side = k # k*sqrt(5)

                # Tìm m, n sao cho 3a + m + n = 5k hoặc -5k để a nguyên
                # Chọn m, n ngẫu nhiên sau đó điều chỉnh
                m = random.randint(-5, 5)

                # Điều kiện để 3a + m + n = 5k => m + n - 5k chia hết cho 3
                # Hoặc 3a + m + n = -5k => m + n + 5k chia hết cho 3
                # Ta chọn ngẫu nhiên n sao cho có nghiệm a nguyên dương
                found = False
                attempts = 0
                while not found and attempts < 100:
                    n = random.randint(-5, 5)
                    # TH1: 3a = 5k - m - n
                    if (5*k - m - n) % 3 == 0:
                        a_val = (5*k - m - n) // 3
                        if a_val > 0:
                            found = True
                            target_a = a_val
                            break
                    # TH2: 3a = -5k - m - n
                    if (-5*k - m - n) % 3 == 0:
                        a_val = (-5*k - m - n) // 3
                        if a_val > 0:
                            found = True
                            target_a = a_val
                            break
                    attempts += 1

                if not found: # Fallback về giá trị trong ảnh nếu không tìm được (hiếm gặp)
                    m, n, k, S_hv, target_a = -1, 3, 1, 5, 1

                # Tọa độ điểm A
                xA = target_a
                yA = -m - target_a

                # Phương trình đường thẳng AD qua A và vuông góc d2 (2x-y+n=0)
                # AD có dạng: 1(x - xA) + 2(y - yA) = 0 => x + 2y + (-xA - 2yA) = 0
                c_ad = -xA - 2*yA

                # Tọa độ điểm D là giao của AD và d2: 2x - y + n = 0
                # x + 2y + c_ad = 0 => x = -2y - c_ad
                # 2(-2y - c_ad) - y + n = 0 => -5y - 2*c_ad + n = 0 => y = (n - 2*c_ad)/5
                yD = Rational(n - 2*c_ad, 5)
                xD = -2*yD - c_ad

                # Tìm điểm C trên d2 sao cho CD^2 = S_hv
                # C(c, 2c + n). CD^2 = (c - xD)^2 + (2c + n - yD)^2 = S_hv
                c_sym = symbols('c')
                eq_c = Eq((c_sym - xD)**2 + (2*c_sym + n - yD)**2, S_hv)
                sol_c = solve(eq_c, c_sym)

                c1 = sol_c[0]
                c2 = sol_c[1]

                C1_coords = (c1, 2*c1 + n)
                C2_coords = (c2, 2*c2 + n)

                # Đáp án đúng
                da = 'C(%s;%s) \\text{ hoặc } C(%s;%s)' % (latex(C1_coords[0]), latex(C1_coords[1]), latex(C2_coords[0]), latex(C2_coords[1]))
                da_d = '\\True $' + da + '$'

                # Tạo các đáp án sai bằng cách xê dịch tọa độ
                s = []
                offsets = [(-1, 1), (1, -1), (2, 0), (0, -2), (-1, -1)]
                for off in offsets:
                    wrong = 'C(%s;%s) \\text{ hoặc } C(%s;%s)' % (
                        latex(C1_coords[0] + off[0]), latex(C1_coords[1] + off[1]), 
                        latex(C2_coords[0] - off[0]), latex(C2_coords[1] - off[1])
                    )
                    s.append('$' + wrong + '$')

                random.shuffle(s)
                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Trong mặt phẳng với hệ tọa độ $Oxy$, cho hình vuông $ABCD$ trong đó $A$ thuộc đường thẳng '
                    '$d_1: x + y %s = 0$ và $C, D$ nằm trên đường thẳng $d_2: 2x - y %s = 0$. '
                    'Tọa độ điểm $C$, biết hình vuông có diện tích bằng $%s$ và $A$ có hoành độ dương là'
                    % (('+' + str(m) if m > 0 else str(m)), ('+' + str(n) if n > 0 else str(n)), latex(S_hv))
                )

                # Lời giải chi tiết
                loigiai = (
                    'Do $A \\in d_1$ nên $A(a; %s)$ với $a > 0$. Theo giả thiết bài toán, ta có:\\\\'
                    '$S_{ABCD} = %s \\Leftrightarrow d(A, d_2) = \\sqrt{%s} \\Leftrightarrow \\frac{|2a - (%s) %s|}{\\sqrt{2^2 + (-1)^2}} = %s$\\\\'
                    '$\\Leftrightarrow \\frac{|3a %s|}{\\sqrt{5}} = %s \\Leftrightarrow |3a %s| = %s$\\\\'
                    '$\\Leftrightarrow a = %s$ hoặc $a = %s$ (loại).\\\\'
                    'Với $a = %s$, suy ra $A(%s; %s)$.\\\\'
                    'Đường thẳng $AD$ đi qua $A$ và vuông góc với $CD$ (nằm trên $d_2$) nên có phương trình '
                    '$AD: 1(x - %s) + 2(y - %s) = 0 \\Leftrightarrow x + 2y %s = 0$.\\\\'
                    'Tọa độ điểm $D$ là nghiệm của hệ phương trình: '
                    '$\\begin{cases} x + 2y %s = 0 \\\\ 2x - y %s = 0 \\end{cases} \\Rightarrow D(%s; %s)$.\\\\'
                    'Do $C \\in d_2$ nên $C(c; 2c %s)$. Suy ra $\\vec{CD} = (%s - c; %s - (2c %s)) = (%s; %s)$.\\\\ '
                    'Ta có $CD = \\sqrt{%s} \\Leftrightarrow \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s}$\\\\'
                    '$\\Leftrightarrow %s(c %s)^2 = %s \\Leftrightarrow (c %s)^2 = %s \\Leftrightarrow \\left[ \\begin{aligned} & c = %s \\\\ & c = %s \\end{aligned} \\right. $\\\\'
                    'Vậy $C(%s; %s)$ hoặc $C(%s; %s)$.'
                    % (latex(-m-a_val).replace('a', 'a'), latex(S_hv), latex(S_hv), latex(-m-symbols('a')), ('+' + str(n) if n >= 0 else str(n)), latex(sqrt(S_hv)),
                       ('+' + str(m+n) if m+n >= 0 else str(m+n)), latex(sqrt(S_hv)), ('+' + str(m+n) if m+n >= 0 else str(m+n)), latex(5*k),
                       latex(target_a), latex(Rational(-5*k-m-n, 3) if target_a == (5*k-m-n)/3 else Rational(5*k-m-n, 3)),
                       latex(target_a), latex(xA), latex(yA),
                       latex(xA), latex(yA), ('+' + str(c_ad) if c_ad >= 0 else str(c_ad)),
                       ('+' + str(c_ad) if c_ad >= 0 else str(c_ad)), ('+' + str(n) if n >= 0 else str(n)), latex(xD), latex(yD),
                       ('+' + str(n) if n >= 0 else str(n)), latex(xD), latex(yD), ('+' + str(n) if n >= 0 else str(n)), latex(xD-c_sym), latex(yD - (2*c_sym + n)),
                       latex(S_hv), latex(xD-c_sym), latex(yD - (2*c_sym + n)), latex(S_hv),
                       5, latex(-xD), 5*k**2, latex(-xD), k**2, latex(c1), latex(c2),
                       latex(C1_coords[0]), latex(C1_coords[1]), latex(C2_coords[0]), latex(C2_coords[1]))
                )

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

