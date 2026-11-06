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


def bt_dang11_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng trẻ em
                so_tre = randint(250, 350)

                # Định hướng nghiệm để tạo điểm cực đại t1 nằm trong khoảng [5, 19]
                t1 = randint(8, 11)   # Điểm cực đại (đây là đáp án chính xác)
                t2 = randint(15, 18)  # Điểm cực tiểu

                # Random hệ số tự do của đạo hàm để tạo số thập phân thực tế
                # Ví dụ chọn 3A = 0.003 để biểu thức đạo hàm đẹp, hoặc lấy số gần bằng đề gốc
                A_val = round(random.choice([0.00095, 0.001, 0.00105, 0.000989]), 6)

                # Tính toán các hệ số dựa trên công thức hàm bậc ba S(t) = A*t^3 + B*t^2 + C*t + D
                # S'(t) = 3A*t^2 + 2B*t + C = 3A*(t - t1)*(t - t2)
                coeff_3A = 3 * A_val
                coeff_2B = -3 * A_val * (t1 + t2)
                coeff_C = 3 * A_val * t1 * t2

                B_val = round(coeff_2B / 2, 5)
                C_val = round(coeff_C, 4)
                D_val = round(random.uniform(1.2, 1.6), 2)

                # Định dạng chuỗi hiển thị số thập phân dùng dấu phẩy cho đề bài
                A_str = str(A_val).replace('.', ',')
                B_str = str(abs(B_val)).replace('.', ',')
                C_str = str(C_val).replace('.', ',')
                D_str = str(D_val).replace('.', ',')

                # Nghiệm cực đại nguyên bản
                kq_num = t1
                kq = str(kq_num)

                # Các đáp án trắc nghiệm
                du = ['$%s$ tuổi' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu quanh đáp án đúng
                s = [
                    '$%s$ tuổi' % (str(t1 - 2)),
                    '$%s$ tuổi' % (str(t1 + 2)),
                    '$%s$ tuổi' % (str(t2)),
                    '$%s$ tuổi' % (str(t2 - 3)),
                    '$%s$ tuổi' % (str(t1 + 4))
                ]
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi sử dụng định dạng %s
                noidungcauhoi = ('''Trong một nghiên cứu tại Viện Sức khỏe Tâm thần Quốc gia, các nhà khoa học theo dõi độ dày vỏ não (cortex) của $%s$ trẻ em có IQ cao ($121 - 149$) qua tuổi $t$ (tính bằng năm), với mô hình
                                 $$S(t) = %s t^3 - %s t^2 + %s t + %s, \\quad 5 \\le t \\le 19.$$
                                 Hỏi vỏ não của trẻ có IQ siêu trí tuệ đạt độ dày cực đại vào khoảng bao nhiêu tuổi (làm tròn kết quả đến hàng đơn vị)?'''
                                 % (latex(so_tre), A_str, B_str, C_str, D_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính các hệ số đạo hàm phục vụ lời giải
                der_A_str = str(round(3 * A_val, 6)).replace('.', ',')
                der_B_str = str(round(abs(2 * B_val), 5)).replace('.', ',')
                der_C_str = str(C_val).replace('.', ',')

                # Nội dung lời giải chi tiết, đầy đủ từng bước, lập bảng biến thiên bằng TikZ
                loigiai = ('''Xét hàm số biểu thị độ dày vỏ não của trẻ:
                           $$S(t) = %s t^3 - %s t^2 + %s t + %s \\text{ trên đoạn } [5; 19].$$
                           Ta tính đạo hàm của hàm số theo biến $t$:
                           $$S'(t) = %s t^2 - %s t + %s.$$
                           Cho đạo hàm bằng $0$:
                           $$S'(t) = 0 \\Leftrightarrow %s t^2 - %s t + %s = 0 \\Leftrightarrow \\left[\\begin{aligned} & t \\approx %s \\\\ & t \\approx %s \\end{aligned}\\right.$$
                           Ta lập bảng biến thiên của hàm số $S(t)$ trên đoạn $[5; 19]$ như sau:
                           \\begin{center}
                           \\begin{tikzpicture}[scale=1]
                           \\draw[line width=1pt] (0,3) -- (10,3);
                           \\draw[line width=1pt] (0,2) -- (10,2);
                           \\draw[line width=1pt] (2,0) -- (2,4);
                           \\node at (1,3.5) {$t$};
                           \\node at (2.3,3.5) {$5$};
                           \\node at (4.5,3.5) {$%s$};
                           \\node at (7.2,3.5) {$%s$};
                           \\node at (9.5,3.5) {$19$};
                           \\node at (1,2.5) {$S'(t)$};
                           \\node at (3.4,2.5) {$+$};
                           \\node at (4.5,2.5) {$0$};
                           \\node at (5.8,2.5) {$-$};
                           \\node at (7.2,2.5) {$0$};
                           \\node at (8.5,2.5) {$+$};
                           \\node at (1,1) {$S(t)$};
                           \\draw[->,line width=1pt] (2.5,0.3) -- (4.2,1.7);
                           \\draw[->,line width=1pt] (4.8,1.7) -- (6.9,0.3);
                           \\draw[->,line width=1pt] (7.5,0.3) -- (9.2,1.7);
                           \\end{tikzpicture}
                           \\end{center}
                           Dựa vào bảng biến thiên, ta thấy trên đoạn $[5; 19]$, hàm số đạt cực đại tại điểm $t = %s$. \\\\
                           Vậy vỏ não của trẻ có IQ siêu trí tuệ đạt độ dày cực đại vào khoảng $%s$ tuổi.'''
                           % (A_str, B_str, C_str, D_str,
                              der_A_str, der_B_str, der_C_str,
                              der_A_str, der_B_str, der_C_str, latex(t1), latex(t2),
                              latex(t1), latex(t2), latex(t1), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

