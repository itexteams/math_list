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


def bt_dang36_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến danh sách dạng (ở đây chỉ có 1 dạng)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random số liệu bài toán
                # p1 là tỷ lệ nhóm đại học (%), p2 là nhóm cao đẳng
                p1 = random.randint(55, 75) 
                p2 = 100 - p1

                # e1 là tỷ lệ tinh giản nhóm đại học (%), e2 là nhóm cao đẳng
                e1 = random.randint(8, 12)
                e2 = random.randint(14, 20)

                # Chuyển sang số thập phân để tính toán
                P_A = Rational(p1, 100)
                P_notA = Rational(p2, 100)
                P_E_A = Rational(e1, 100)
                P_E_notA = Rational(e2, 100)

                # Tính xác suất toàn phần P(E)
                P_E = P_A * P_E_A + P_notA * P_E_notA

                # Tính xác suất hậu nghiệm P(A|E) theo định lý Bayes
                P_A_E_val = (P_A * P_E_A) / P_E

                # Làm tròn đến hàng phần trăm (2 chữ số sau dấu phẩy)
                kq_num = float(P_A_E_val)
                kq_rounded = Decimal(str(kq_num)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Định dạng hiển thị số thập phân dùng dấu phẩy
                str_P_A = str(float(P_A)).replace('.', ',')
                str_P_notA = str(float(P_notA)).replace('.', ',')
                str_P_E_A = str(float(P_E_A)).replace('.', ',')
                str_P_E_notA = str(float(P_E_notA)).replace('.', ',')
                str_P_E = str(float(P_E)).replace('.', ',')
                str_kq = str(kq_rounded).replace('.', ',')

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % str_kq

                # Tạo các đáp án nhiễu (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    sai_val = kq_rounded + Decimal(str(random.choice([-0.05, -0.03, -0.02, 0.02, 0.03, 0.05])))
                    str_sai = str(sai_val).replace('.', ',')
                    ans_sai = '$%s$' % str_sai
                    if ans_sai != da_dung and ans_sai not in s:
                        s.append(ans_sai)

                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một cơ quan hành chính nhà nước thực hiện việc tinh giản biên chế thông qua phỏng vấn. Tỷ lệ nhân viên của cơ quan thuộc hai nhóm trình độ: Đại học, Cao đẳng lần lượt là $%s\\%%$ và $%s\\%%$. Qua phỏng vấn thì tỷ lệ nhân viên bị tinh giản của nhóm đại học là $%s\\%%$, nhóm cao đẳng là $%s\\%%$. Chọn một nhân viên bất kỳ đã bị tinh giản thì hãy tính xác suất để người này có trình độ đại học bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'''
                                 %(latex(p1), latex(p2), latex(e1), latex(e2)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A$ là biến cố: "nhân viên được chọn thuộc nhóm trình độ đại học";\\\\
                             $B$ là biến cố: "nhân viên được chọn thuộc nhóm trình độ cao đẳng";\\\\
                             $E$ là biến cố: "nhân viên được chọn bị tinh giản".\\\\
                             Ta có $B = \\overline{A}$.\\\\
                             Ta cần tính $P(E)$. Theo công thức xác suất toàn phần, ta có:\\\\
                             $P(E) = P(A) \\cdot P(E|A) + P(\\overline{A}) \\cdot P(E|\\overline{A})$.\\\\
                             Theo bài ra ta có: $P(A) = %s, P(\\overline{A}) = P(B) = %s$.\\\\
                             $P(E|A)$ là xác suất để nhân viên bị tinh giản, thuộc nhóm trình độ đại học.\\\\
                             Theo bài ra ta có $P(E|A) = %s$.\\\\
                             $P(E|\\overline{A})$ là xác suất để nhân viên bị tinh giản, thuộc nhóm trình độ cao đẳng.\\\\
                             Theo bài ra ta có $P(E|\\overline{A}) = %s$.\\\\
                             Thay vào ta được:\\\\
                             $P(E) = P(A) \\cdot P(E|A) + P(\\overline{A}) \\cdot P(E|\\overline{A}) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
                             Ta có xác suất để nhân viên được chọn có trình độ đại học, biết rằng nhân viên này đã bị tinh giản, chính là xác suất $P(A|E)$.\\\\
                             Theo công thức Bayes và kết quả ở trên, ta có:\\\\
                             $P(A|E) = \\frac{P(A) \\cdot P(E|A)}{P(E)} = \\frac{%s \\cdot %s}{%s} \\approx %s$.'''
                           %(str_P_A, str_P_notA, str_P_E_A, str_P_E_notA, 
                             str_P_A, str_P_E_A, str_P_notA, str_P_E_notA, str_P_E,
                             str_P_A, str_P_E_A, str_P_E, str_kq))
                dapan=' \\shortans[0]{$%s$} '%(str_kq)
            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

