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


def bt_dang58_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tổng số thẻ N (chọn bội số của 3 để chia đều 3 nhóm)
                N = random.choice([12, 15, 18, 21, 24])
                m = N // 3 # Số thẻ mỗi nhóm

                # Random hệ số của biểu thức k1*a + k2*b
                k1 = random.randint(1, 5)
                k2 = random.randint(1, 5)

                # Tính toán tổ hợp và xác suất
                omega = sp.binomial(N, 3)
                c1 = sp.binomial(m, 3) # Chọn 3 thẻ từ 1 nhóm
                c4 = m * m * m         # Chọn mỗi nhóm 1 thẻ

                # Số kết quả thuận lợi
                nA = 3 * c1 + c4

                # Xác suất P = a/b
                P = sp.Rational(nA, omega)
                a = P.p
                b = P.q

                # Kết quả biểu thức k1*a + k2*b
                kq_val = k1 * a + k2 * b
                kq = str(kq_val)

                # Tạo hình vẽ TikZ tự động tương ứng với số lượng thẻ N
                cols = m
                tikz_template = ('\\begin{center}\n'
                                 '\\begin{tikzpicture}[line width=1pt]\n'
                                 '\\draw[rounded corners=5pt, fill=green!10, draw=green!50!black] (-0.7, -0.7) rectangle (%s, 3.8);\n'
                                 '\\node[text=green!50!black, font=\\bfseries] at (%s, 3.3) {GIẢI MÃ CON SỐ};\n'
                                 '%s'
                                 '\\end{tikzpicture}\n'
                                 '\\end{center}')
                cards_tikz = ""
                for r in range(1, 4):
                    for c in range(1, cols + 1):
                        val = (r - 1) * cols + c
                        x_pos = (c - 1) * 1.2
                        y_pos = (3 - r) * 1.2
                        cards_tikz += ('\\draw[fill=yellow!20, draw=orange] (%s,%s) rectangle (%s,%s);\n' % (x_pos-0.4, y_pos-0.4, x_pos+0.4, y_pos+0.4))
                        cards_tikz += ('\\node[text=red!80!black, font=\\bfseries] at (%s,%s) {%s};\n' % (x_pos, y_pos, val))

                rect_w = (cols - 1) * 1.2 + 0.7
                title_x = (cols - 1) * 1.2 / 2
                hinh_ve = tikz_template % (rect_w, title_x, cards_tikz)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)
                s = ['$%s$'%(kq_val + 1),
                     '$%s$'%(kq_val + 2),
                     '$%s$'%(kq_val + 3),
                     '$%s$'%(kq_val - 1),
                     '$%s$'%(kq_val - 2),
                     '$%s$'%(kq_val - 3),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Để tạo hứng thú cho học sinh khối 10, câu lạc bộ Toán học của trường THPT Nguyễn Du tổ chức một trò chơi mang tên "Giải mã con số". Ban tổ chức chuẩn bị $%s$ tấm thẻ được đánh số thứ tự từ $1$ đến $%s$ và xếp trên một bảng chơi như hình minh họa bên dưới.
            %s
            Luật chơi như sau: Một học sinh tham gia sẽ bốc ngẫu nhiên $3$ tấm thẻ từ bảng. Học sinh đó sẽ giành chiến thắng và nhận được một phần quà nếu tổng các số ghi trên $3$ tấm thẻ rút được là một số chia hết cho $3$. Giả sử xác suất để học sinh đó giành chiến thắng là phân số tối giản $\\frac{a}{b}$ (với $a, b \\in \\mathbb{N}^*$). Giá trị của biểu thức $%sa + %sb$ bằng bao nhiêu?'''
                                 % (N, N, hinh_ve, k1, k2))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các nhóm tập hợp cho lời giải
                g1 = "; ".join(str(i) for i in range(3, N + 1, 3))
                g2 = "; ".join(str(i) for i in range(1, N + 1, 3))
                g3 = "; ".join(str(i) for i in range(2, N + 1, 3))

                # Nội dung lời giải
                loigiai = ('''Không gian mẫu $\\Omega$ là tập hợp các cách bốc ngẫu nhiên $3$ tấm thẻ từ $%s$ tấm thẻ. \\\\
            Số phần tử của không gian mẫu là: $n\\left(\\Omega\\right) = C_{%s}^{3} = %s$. \\\\
            Gọi biến cố $A$: "Tổng các số ghi trên $3$ tấm thẻ rút được là một số chia hết cho $3$". \\\\
            Chia $%s$ tấm thẻ thành 3 nhóm dựa trên số dư khi chia cho $3$: \\\\
            Nhóm 1 (chia hết cho 3): gồm các số $\\left\\{%s\\right\\}$. Nhóm này có $%s$ tấm thẻ. \\\\
            Nhóm 2 (chia 3 dư 1): gồm các số $\\left\\{%s\\right\\}$. Nhóm này có $%s$ tấm thẻ. \\\\
            Nhóm 3 (chia 3 dư 2): gồm các số $\\left\\{%s\\right\\}$. Nhóm này có $%s$ tấm thẻ. \\\\
            Để tổng 3 số bốc được chia hết cho 3, ta có các trường hợp sau: \\\\
            Trường hợp 1: 3 tấm thẻ đều thuộc Nhóm 1. Số cách bốc là $C_{%s}^{3} = %s$. \\\\
            Trường hợp 2: 3 tấm thẻ đều thuộc Nhóm 2. Số cách bốc là $C_{%s}^{3} = %s$. \\\\
            Trường hợp 3: 3 tấm thẻ đều thuộc Nhóm 3. Số cách bốc là $C_{%s}^{3} = %s$. \\\\
            Trường hợp 4: 1 tấm thẻ thuộc Nhóm 1, 1 tấm thẻ thuộc Nhóm 2, 1 tấm thẻ thuộc Nhóm 3. Số cách bốc là $C_{%s}^{1} \\cdot C_{%s}^{1} \\cdot C_{%s}^{1} = %s$. \\\\
            Số kết quả thuận lợi cho biến cố $A$ là: $n\\left(A\\right) = %s + %s + %s + %s = %s$. \\\\
            Xác suất của biến cố $A$ là: $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
            Theo đề bài, phân số này được rút gọn tối giản thành $\\frac{a}{b}$, suy ra $a = %s$ và $b = %s$. \\\\
            Vậy giá trị của biểu thức $%sa + %sb$ là: $%s \\cdot %s + %s \\cdot %s = %s$.'''
                           % (N, N, omega, N, 
                              g1, m, 
                              g2, m, 
                              g3, m, 
                              m, c1, m, c1, m, c1, 
                              m, m, m, c4, 
                              c1, c1, c1, c4, nA, 
                              nA, omega, a, b, 
                              a, b, 
                              k1, k2, k1, a, k2, b, kq_val))
                dapan='\\shortans[0]{$%s$}\n'%(kq_val)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

