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


def bt_dang18_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random số liệu cho bài toán
                # Hộp 1: r1 bi đỏ, b1 bi xanh -> n1 tổng bi
                r1 = random.randint(4, 8)
                b1 = random.randint(3, 6)
                n1 = r1 + b1

                # Hộp 2: r2 bi đỏ, b2 bi xanh -> n2 tổng bi
                r2 = random.randint(4, 8)
                b2 = random.randint(3, 6)
                n2 = r2 + b2

                # Bước 2: Tính toán theo logic bài toán
                # n(B): Số cách lấy 2 viên có ít nhất 1 bi đỏ
                # n(B) = Tổng cách lấy - Cách lấy 2 viên đều xanh
                n_omega = n1 * n2
                n_B = n_omega - (b1 * b2)

                # n(AB): Như lấy được bi đỏ (Như thuộc hộp II) và có ít nhất 1 bi đỏ
                # Vì Như lấy bi đỏ đã thỏa mãn "có ít nhất 1 đỏ", nên n(AB) là số cách Như lấy đỏ từ hộp II và Minh lấy bất kỳ từ hộp I
                n_AB = n1 * r2

                # Tính xác suất P(A|B) = n(AB)/n(B)
                prob = Rational(n_AB, n_B)
                a = prob.p # Tử số của phân số tối giản
                b = prob.q # Mẫu số của phân số tối giản

                # Kết quả cần tìm: a - b
                ans_val = a - b

                # Bước 3: Tạo các phương án nhiễu (không trùng đáp án đúng)
                da = '$%s$' % latex(ans_val)

                s = []
                offsets = [-3, -2, -1, 1, 2, 3, 5]
                for offset in offsets:
                    wrong_val = ans_val + offset
                    s.append('$%s$' % latex(wrong_val))

                # Trộn và lấy 3 đáp án sai
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Bước 4: Soạn nội dung câu hỏi (sử dụng latex)
                noidungcauhoi = (
                    'Có hai hộp đựng các viên bi: Hộp $I$ có $%s$ bi đỏ và $%s$ bi xanh, hộp $II$ có $%s$ bi đỏ và $%s$ bi xanh '
                    '(các viên bi có cùng kích thước và khối lượng). Bạn Minh lấy ngẫu nhiên một viên bi từ hộp $I$, '
                    'bạn Như lấy ngẫu nhiên một viên bi từ hộp $II$. Biết rằng có viên bi đỏ được lấy ra, '
                    'khi đó xác suất để bạn Như lấy được viên bi đỏ là $\\frac{a}{b}$ ($a, b \\in \\mathbb{N}^*, \\frac{a}{b}$ tối giản). '
                    'Hiệu $a-b$ bằng bao nhiêu?'
                    % (latex(r1), latex(b1), latex(r2), latex(b2))
                )

                # Bước 5: Soạn nội dung lời giải chi tiết
                loigiai = (
                    'Gọi $A$ là biến cố: "Bạn Như lấy được viên bi đỏ". \\\\ '
                    'Gọi $B$ là biến cố: "Có viên bi đỏ trong hai viên được lấy ra". \\\\ '
                    'Ta cần tìm xác suất $P(A|B)$. \\\\ '
                    'Theo công thức xác suất có điều kiện: $P(A|B) = \\frac{P(AB)}{P(B)} = \\frac{n(AB)}{n(B)}$. \\\\ '
                    'Ta có $n(B) = C_{%s}^1 \\cdot C_{%s}^1 - C_{%s}^1 \\cdot C_{%s}^1 = %s$ '
                    '(số cách lấy hai viên bi trong đó có ít nhất 1 bi đỏ) và \\\\ '
                    '$n(AB) = C_{%s}^1 \\cdot C_{%s}^1 = %s$ (số cách lấy hai viên bi trong đó viên bi của bạn Như là bi đỏ). \\\\ '
                    'Thay số, ta được $P(A|B) = \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\ '
                    'Vậy $a=%s, b=%s \\Rightarrow a-b = %s$.'
                    % (latex(n1), latex(n2), latex(b1), latex(b2), latex(n_B), 
                       latex(n1), latex(r2), latex(n_AB), 
                       latex(n_AB), latex(n_B), latex(a), latex(b), 
                       latex(a), latex(b), latex(ans_val))
                )
                dapan=' \\shortans[0]{$%s$} '%(latex(ans_val))

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo đúng định dạng
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

