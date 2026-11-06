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


def bt_dang42_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng bi xanh ở hộp 1 (trong ảnh là 5)
                # Hộp 1 luôn có 1 bi đỏ để biến cố B và B_ngang rõ ràng
                b1 = randint(5, 8) 
                n1 = b1 + 1

                # Random số lượng bi đỏ ở hộp 2 (trong ảnh là 4)
                # Hộp 2 ban đầu chỉ chứa bi đỏ
                r2 = randint(4, 7)

                # Tính toán xác suất bằng Sympy
                # B: 3 viên lấy từ hộp 1 cùng màu (cả 3 đều xanh)
                p_b = Rational(binomial(b1, 3), binomial(n1, 3))
                p_not_b = 1 - p_b

                # A: 2 viên lấy từ hộp 2 cùng màu
                # Nếu B xảy ra: Hộp 2 có 3 xanh, r2 đỏ. Tổng 3 + r2 viên.
                n2_cond_b = 3 + r2
                p_a_cond_b = Rational(binomial(3, 2) + binomial(r2, 2), binomial(n2_cond_b, 2))

                # Nếu B không xảy ra (B_ngang): Lấy 2 xanh 1 đỏ từ hộp 1 sang.
                # Hộp 2 có 2 xanh, (r2 + 1) đỏ. Tổng 3 + r2 viên.
                n2_cond_not_b = 3 + r2
                p_a_cond_not_b = Rational(binomial(2, 2) + binomial(r2 + 1, 2), binomial(n2_cond_not_b, 2))

                # Xác suất toàn phần P(A)
                p_a = p_b * p_a_cond_b + p_not_b * p_a_cond_not_b

                # Xác suất Bayes P(B|A)
                p_b_given_a = (p_b * p_a_cond_b) / p_a

                # Kết quả làm tròn đến hàng phần trăm
                kq_val = float(p_b_given_a)
                kq_dec = Decimal(str(kq_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu
                s = []
                while len(s) < 3:
                    nhieu = kq_dec + Decimal(str(random.choice([-0.1, -0.05, 0.05, 0.1, 0.15, -0.15])))
                    if nhieu > 0 and nhieu < 1:
                        val_s = str(nhieu).replace('.', ',')
                        if val_s not in s and val_s != kq:
                            s.append('$%s$' % val_s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Hộp thứ nhất chứa $%s$ viên bi xanh và $1$ viên bi đỏ. Hộp thứ hai chứa $%s$ viên bi đỏ. Lấy ngẫu nhiên $3$ viên bi từ hộp thứ nhất và bỏ vào hộp thứ hai, rồi từ hộp thứ hai lấy ra ngẫu nhiên $2$ viên bi. Biết $2$ viên bi lấy ra ở hộp thứ hai có cùng màu. Xác suất để $3$ viên bi lấy ra từ hộp thứ nhất cũng có cùng màu bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 % (latex(b1), latex(r2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A$ là biến cố $2$ viên bi lấy ra ở hộp thứ hai có cùng màu.\\\\
            Gội $B$ là biến cố $3$ viên bi lấy ra ở hộp thứ nhất có cùng màu.\\\\
            Ta có:\\\\
            $P(B) = \\frac{C_{%s}^3}{C_{%s}^3} = %s, P(\\bar{B}) = 1 - %s = %s$ (vì hộp thứ nhất có $%s$ bi xanh và $1$ bi đỏ nên biến cố $\\bar{B}$ tương ứng với việc lấy được $2$ bi xanh và $1$ bi đỏ).\\\\
            Xác suất để $2$ viên bi được chọn từ hộp thứ hai có cùng màu, biết $3$ viên bi lấy ra ở hộp thứ nhất có cùng màu là:\\\\
            $P(A|B) = \\frac{C_3^2 + C_{%s}^2}{C_{%s}^2} = %s$ (vì sau khi lấy $3$ viên bi màu xanh từ hộp thứ nhất sang thì hộp thứ hai có $3$ bi xanh và $%s$ bi đỏ).\\\\
            Xác suất để $2$ viên bi được chọn từ hộp thứ hai có cùng màu, biết $3$ viên bi lấy ra ở hộp thứ nhất khác màu là:\\\\
            $P(A|\\bar{B}) = \\frac{C_2^2 + C_{%s}^2}{C_{%s}^2} = %s$ (vì sau khi lấy $2$ viên bi màu xanh và $1$ viên bi đỏ từ hộp thứ nhất sang thì hộp thứ hai có $2$ bi xanh và $%s$ bi đỏ).\\\\
            Áp dụng công thức xác suất toàn phần ta có:\\\\
            $P(A) = P(B)P(A|B) + P(\\bar{B})P(A|\\bar{B}) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
            Theo công thức Bayes, ta có: $P(B|A) = \\frac{P(B).P(A|B)}{P(A)} = \\frac{%s \\cdot %s}{%s} = %s \\approx %s$.'''
                           % (latex(b1), latex(n1), latex(p_b), latex(p_b), latex(p_not_b), latex(b1),
                              latex(r2), latex(n2_cond_b), latex(p_a_cond_b), latex(r2),
                              latex(r2 + 1), latex(n2_cond_not_b), latex(p_a_cond_not_b), latex(r2 + 1),
                              latex(p_b), latex(p_a_cond_b), latex(p_not_b), latex(p_a_cond_not_b), latex(p_a),
                              latex(p_b), latex(p_a_cond_b), latex(p_a), latex(p_b_given_a), kq))
                dapan=' \\shortans[0]{$%s$} '%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

