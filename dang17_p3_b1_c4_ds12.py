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


def bt_dang17_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1 & 3: Thiết lập thông số ngẫu nhiên
                w1 = randint(7, 10)   # Số bi trắng hộp 1
                r1 = randint(5, 8)    # Số bi đỏ hộp 1
                w2 = randint(4, 6)    # Số bi trắng hộp 2
                r2 = randint(6, 9)    # Số bi đỏ hộp 2

                n1 = w1 + r1          # Tổng bi hộp 1
                n2 = w2 + r2          # Tổng bi hộp 2

                # Tính toán các xác suất thành phần (Sử dụng binomial thay cho comb)
                # TH1: 2 trắng từ hộp 1 sang hộp 2
                p_h1 = Rational(binomial(w1, 2), binomial(n1, 2))
                p_b_given_h1 = Rational(binomial(w2 + 2, 3), binomial(n2 + 2, 3))
                h1_b = p_h1 * p_b_given_h1

                # TH2: 2 đỏ từ hộp 1 sang hộp 2
                p_h2 = Rational(binomial(r1, 2), binomial(n1, 2))
                p_b_given_h2 = Rational(binomial(w2, 3), binomial(n2 + 2, 3))
                h2_b = p_h2 * p_b_given_h2

                # TH3: 1 trắng 1 đỏ từ hộp 1 sang hộp 2
                p_h3 = Rational(binomial(w1, 1) * binomial(r1, 1), binomial(n1, 2))
                p_b_given_h3 = Rational(binomial(w2 + 1, 3), binomial(n2 + 2, 3))
                h3_b = p_h3 * p_b_given_h3

                # Xác suất đầy đủ P(B)
                pb = h1_b + h2_b + h3_b

                # Xác suất hậu nghiệm P(H1|B)
                kq_fraction = h1_b / pb
                kq_float = float(kq_fraction)

                # Làm tròn đến hàng phần mười
                kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Tạo các phương án nhiễu
                da = '$%s$' % (kq_str)
                s_vals = []
                for offset in [-0.2, -0.1, 0.1, 0.2]:
                    val = float(kq_decimal) + offset
                    if 0 < val < 1:
                        s_vals.append('$%s$' % (str(round(val, 1)).replace('.', ',')))

                random.shuffle(s_vals)
                das1, das2, das3 = s_vals[:3]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Có hai hộp đựng bi. Hộp thứ nhất chứa $%s$ viên bi màu trắng, $%s$ viên bi màu đỏ, hộp thứ hai chứa $%s$ viên bi màu trắng, $%s$ viên bi màu đỏ. Lấy ngẫu nhiên $2$ viên bi từ hộp thứ nhất bỏ sang hộp thứ hai, sau đó lấy ngẫu nhiên $3$ viên bi từ hộp thứ hai. Xác suất lấy được cả $2$ viên bi thuộc hộp thứ nhất bỏ sang hộp thứ hai đều màu trắng, biết rằng $3$ viên bi lấy ra sau cùng từ hộp thứ hai đều màu trắng bằng bao nhiêu? (kết quả làm tròn đến hàng phần mười).'''
                                 % (latex(w1), latex(r1), latex(w2), latex(r2)))

                # Đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Gọi $H_1$ là biến cố "2 viên bi chuyển từ hộp 1 sang hộp 2 là 2 viên trắng". \\\\
                             Gọi $H_2$ là biến cố "2 viên bi chuyển từ hộp 1 sang hộp 2 là 2 viên đỏ". \\\\
                             Gọi $H_3$ là biến cố "2 viên bi chuyển từ hộp 1 sang hộp 2 là 1 viên trắng, 1 viên đỏ". \\\\
                             Gọi $B$ là biến cố "3 viên bi lấy ra từ hộp hai sau khi chuyển đều là màu trắng". \\\\
                             Trường hợp 1: Chuyển 2 viên trắng. Khi đó: \\\\
                             $P(H_1 \\cap B) = \\frac{C_{%s}^2}{C_{%s}^2} \\cdot \\frac{C_{%s}^3}{C_{%s}^3} = %s$. \\\\
                             Trường hợp 2: Chuyển 2 viên đỏ. Khi đó: \\\\
                             $P(H_2 \\cap B) = \\frac{C_{%s}^2}{C_{%s}^2} \\cdot \\frac{C_{%s}^3}{C_{%s}^3} = %s$. \\\\
                             Trường hợp 3: Chuyển 1 viên trắng và 1 viên đỏ. Khi đó: \\\\
                             $P(H_3 \\cap B) = \\frac{C_{%s}^1 \\cdot C_{%s}^1}{C_{%s}^2} \\cdot \\frac{C_{%s}^3}{C_{%s}^3} = %s$. \\\\
                             Xác suất để 3 viên lấy ra từ hộp hai đều màu trắng là: \\\\
                             $P(B) = P(H_1 \\cap B) + P(H_2 \\cap B) + P(H_3 \\cap B) = %s$. \\\\
                             Xác suất cần tìm (áp dụng công thức Bayes): \\\\
                             $P(H_1|B) = \\frac{P(H_1 \\cap B)}{P(B)} = \\frac{%s}{%s} = %s \\approx %s$.'''
                           % (latex(w1), latex(n1), latex(w2+2), latex(n2+2), latex(h1_b),
                              latex(r1), latex(n1), latex(w2), latex(n2+2), latex(h2_b),
                              latex(w1), latex(r1), latex(n1), latex(w2+1), latex(n2+2), latex(h3_b),
                              latex(pb), latex(h1_b), latex(pb), latex(kq_fraction), latex(kq_str)))
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))
            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

