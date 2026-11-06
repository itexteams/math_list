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


def bt_dang15_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Hàm tính tổ hợp nCr
            def nCr(n, r):
                if r < 0 or r > n:
                    return 0
                return math.comb(n, r)

            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số cho bài toán
                # Hộp I: w1 trắng, r1 đỏ. Hộp II: w2 trắng, r2 đỏ.
                w1 = random.randint(4, 7)
                r1 = random.randint(5, 8)
                w2 = random.randint(8, 12)
                r2 = random.randint(12, 18)

                total1 = w1 + r1
                total2 = w2 + r2

                # Bước 2: Tính toán n(A) - Số cách lấy ra 1 quả bóng trắng từ hộp II sau khi chuyển
                # Trường hợp 1: Chuyển 2 trắng. Số cách: C(w1, 2). Hộp II mới có w2+2 trắng.
                c1 = nCr(w1, 2)
                n_a1 = c1 * (w2 + 2)

                # Trường hợp 2: Chuyển 1 trắng, 1 đỏ. Số cách: C(w1, 1)*C(r1, 1). Hộp II mới có w2+1 trắng.
                c2 = nCr(w1, 1) * nCr(r1, 1)
                n_a2 = c2 * (w2 + 1)

                # Trường hợp 3: Chuyển 2 đỏ. Số cách: C(r1, 2). Hộp II mới có w2 trắng.
                c3 = nCr(r1, 2)
                n_a3 = c3 * w2

                nA = n_a1 + n_a2 + n_a3

                # Bước 3: Tính toán n(A giao B) - Số cách lấy ra quả trắng và quả đó thuộc nhóm mới chuyển sang
                # Trường hợp 1: Có 2 quả trắng mới chuyển.
                n_ab1 = c1 * 2
                # Trường hợp 2: Có 1 quả trắng mới chuyển.
                n_ab2 = c2 * 1
                # Trường hợp 3: Không có quả trắng nào mới chuyển.
                n_ab3 = 0

                nAB = n_ab1 + n_ab2 + n_ab3

                # Bước 4: Tính xác suất P(B|A) = nAB / nA
                prob = frac(nAB, nA)
                a = prob.numerator
                b = prob.denominator
                kq_final = a + b

                # Bước 5: Tạo các đáp án nhiễu
                da = str(kq_final)
                s = set()
                while len(s) < 3:
                    fake = kq_final + random.choice([-3, -2, -1, 1, 2, 3, 5, 7])
                    if fake > 0 and fake != kq_final:
                        s.add(str(fake))

                list_s = list(s)
                das1, das2, das3 = list_s[0], list_s[1], list_s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Có hai chiếc hộp, hộp I có $%s$ quả bóng màu trắng và $%s$ quả bóng màu đỏ, hộp II có $%s$ quả bóng màu trắng và $%s$ quả bóng màu đỏ, các quả bóng có cùng kích thước và khối lượng. Lấy ngẫu nhiên hai quả bóng từ hộp I bỏ vào hộp II. Sau đó, lấy ra ngẫu nhiên một quả bóng từ hộp II. Xác suất để quả bóng được lấy ra từ hộp II là quả bóng được chuyển từ hộp I sang, biết rằng quả bóng đó có màu trắng là $\\frac{a}{b}$ (là phân số tối giản). Tổng $a+b$ bằng bao nhiêu?'''
                                 % (latex(w1), latex(r1), latex(w2), latex(r2)))

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A$ là biến cố: "Quả bóng lấy ra từ hộp thứ II có màu trắng". Gọi $B$ là biến cố: "Quả bóng lấy ra từ hộp thứ II là quả từ hộp I".\\\\
                             Ta cần tính $P(B | A) = \\frac{P(AB)}{P(A)} = \\frac{n(A \\cap B)}{n(A)}$.\\\\
                             + Tính $n(A)$:\\\\
                             - Trường hợp 1: Hai quả bóng lấy từ hộp I chuyển sang hộp II đều màu trắng. Khi đó hộp II có $%s$ quả bóng trắng, $%s$ quả bóng đỏ. Vậy trường hợp này có số cách lấy là: $C_{%s}^2 \\cdot %s = %s$.\\\\
                             - Trường hợp 2: Hai quả bóng lấy từ hộp I chuyển sang hộp II có một quả trắng, một quả đỏ. Khi đó hộp II có $%s$ quả bóng trắng, $%s$ quả bóng đỏ. Vậy trường hợp này có số cách lấy là: $C_{%s}^1 \\cdot C_{%s}^1 \\cdot %s = %s$.\\\\
                             - Trường hợp 3: Hai quả bóng lấy từ hộp I chuyển sang hộp II đều màu đỏ. Khi đó hộp II có $%s$ quả bóng trắng, $%s$ quả bóng đỏ. Vậy trường hợp này có số cách lấy là: $C_{%s}^2 \\cdot %s = %s$.\\\\
                             Từ đó suy ra: $n(A) = %s + %s + %s = %s$.\\\\
                             + Tính $n(A \\cap B)$:\\\\
                             Ta có $n(A \\cap B) = C_{%s}^2 \\cdot 2 + C_{%s}^1 \\cdot C_{%s}^1 \\cdot 1 = %s + %s = %s$.\\\\
                             Vậy $P(B | A) = \\frac{n(A \\cap B)}{n(A)} = \\frac{%s}{%s} = \\frac{%s}{%s} \\Rightarrow a+b = %s + %s = %s$.'''
                           % (latex(w2+2), latex(r2), latex(w1), latex(w2+2), latex(n_a1),
                              latex(w2+1), latex(r2+1), latex(w1), latex(r1), latex(w2+1), latex(n_a2),
                              latex(w2), latex(r2+2), latex(r1), latex(w2), latex(n_a3),
                              latex(n_a1), latex(n_a2), latex(n_a3), latex(nA),
                              latex(w1), latex(w1), latex(r1), latex(n_ab1), latex(n_ab2), latex(nAB),
                              latex(nAB), latex(nA), latex(a), latex(b), latex(a), latex(b), latex(kq_final)
                              ))
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_final))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

