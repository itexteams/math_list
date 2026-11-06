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


def bt_dang26_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Bước 1: Khởi tạo dữ liệu ngẫu nhiên
            list_names_all = ['Phát', 'Phong', 'Đức', 'Kiên', 'Dương', 'Khoa', 'Hải', 'An', 'Bình', 'Chi', 'Dũng', 'Giang', 'Hương', 'Khánh', 'Minh', 'Nam', 'Quân']
            chosen_names = random.sample(list_names_all, 7)
            name1, name2 = chosen_names[5], chosen_names[6] # Hai bạn được hỏi
            danh_sach_ten = ", ".join(chosen_names[:-1]) + " và " + chosen_names[-1]

            # Tạo bộ số (x, y, z) sao cho x+y+z = 7 và x, y, z >= 1
            # Bộ (2, 2, 3) là bộ trong hình. Ta có thể random các hoán vị hoặc bộ khác.
            sets = [(2, 2, 3), (1, 3, 3), (1, 2, 4)]
            x, y, z = random.choice(sets)
            xyz_list = [x, y, z]
            random.shuffle(xyz_list)
            x, y, z = xyz_list

            # Tính số sách mỗi loại
            # n1: Đa thức, n2: Tổ hợp, n3: Hình học
            # Mỗi hs 2 quyển khác chủ đề -> x (ĐT-TH), y (ĐT-HH), z (HH-TH)
            n1 = x + y # Tổng sách Đa thức
            n2 = x + z # Tổng sách Tổ hợp
            n3 = y + z # Tổng sách Hình học

            # Bước 2: Tính toán lời giải
            # Không gian mẫu: Xếp 7 học sinh vào 3 nhóm x, y, z
            n_omega = binomial(7, x) * binomial(7 - x, y)

            # Biến cố A: Khoa và Dương có phần thưởng giống nhau
            # TH1: Cùng nhận ĐT-TH (nhóm x)
            if x >= 2:
                case1 = binomial(5, x - 2) * binomial(7 - x, y)
            else:
                case1 = 0

            # TH2: Cùng nhận ĐT-HH (nhóm y)
            if y >= 2:
                case2 = binomial(5, y - 2) * binomial(7 - y, x)
            else:
                case2 = 0

            # TH3: Cùng nhận HH-TH (nhóm z)
            if z >= 2:
                case3 = binomial(5, z - 2) * binomial(7 - z, x)
            else:
                case3 = 0

            n_A = case1 + case2 + case3
            prob = float(n_A) / float(n_omega)

            # Làm tròn đến hàng phần trăm theo kiểu Việt Nam (dấu ,)
            kq_decimal = Decimal(str(prob)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_decimal).replace('.', ',')

            # Bước 3: Tạo các phương án sai
            def generate_wrong_answers(correct_val):
                wrongs = set()
                while len(wrongs) < 3:
                    offset = random.choice([-0.05, -0.03, 0.02, 0.04, 0.07, 0.11, -0.08])
                    w = Decimal(str(correct_val + offset)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    w_str = str(w).replace('.', ',')
                    if w_str != str(correct_val).replace('.', ',') and float(w) > 0:
                        wrongs.add('$%s$' % w_str)
                return list(wrongs)

            wrong_ans = generate_wrong_answers(prob)

            # Bước 4: Nội dung câu hỏi và lời giải
            noidungcauhoi = ('''Tổng kết năm học 2025-2026, đội HSG toán của CLB chuyên Gia Lai có 7 bạn được khen thưởng: %s. 
            Phần thưởng cho tất cả các bạn gồm có %s quyển sách Đa Thức, %s quyển sách Tổ Hợp, %s quyển sách Hình Học (các quyển sách cùng chủ đề là giống nhau) sao cho mỗi học sinh được 2 quyển sách khác chủ đề. Xác suất để bạn %s và %s có phần thưởng giống nhau bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                             % (danh_sach_ten, latex(n1), latex(n2), latex(n3), name1, name2))

            # Tạo phần text lời giải chi tiết
            loigiai = ('''Gọi $x$ là số học sinh nhận sách Đa Thức và Tổ Hợp. \\\\
            Gọi $y$ là số học sinh nhận sách Đa Thức và Hình Học. \\\\
            Gọi $z$ là số học sinh nhận sách Hình Học và Tổ Hợp. \\\\
            Ta có hệ phương trình: $\\begin{cases} x + y = %s \\\\ x + z = %s \\\\ y + z = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases}$. \\\\
            Số phần tử của không gian mẫu là: $n_{\\Omega} = C_7^{%s} \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s} = %s$. \\\\
            Gọi $A$ là biến cố: "%s và %s có phần thưởng giống nhau". \\\\
            - Trường hợp 1: Cùng nhận sách Đa Thức và Tổ Hợp: có $C_2^2 \\cdot C_5^{%s} \\cdot C_{%s}^{%s} = %s$ cách. \\\\
            - Trường hợp 2: Cùng nhận sách Đa Thức và Hình Học: có $C_2^2 \\cdot C_5^{%s} \\cdot C_{%s}^{%s} = %s$ cách. \\\\
            - Trường hợp 3: Cùng nhận sách Hình Học và Tổ Hợp: có $C_2^2 \\cdot C_5^{%s} \\cdot C_{%s}^{%s} = %s$ cách. \\\\
            Số phần tử của biến cố $A$ là: $n_A = %s + %s + %s = %s$. \\\\
            Xác suất để %s và %s có phần thưởng giống nhau là $P_A = \\frac{n_A}{n_{\\Omega}} = \\frac{%s}{%s} \\approx %s$.'''
                       % (latex(n1), latex(n2), latex(n3), latex(x), latex(y), latex(z),
                          latex(x), latex(7-x), latex(y), latex(7-x-y), latex(z), latex(n_omega),
                          name1, name2,
                          latex(x-2 if x>=2 else 0), latex(5-(x-2) if x>=2 else 5), latex(y), latex(case1),
                          latex(y-2 if y>=2 else 0), latex(5-(y-2) if y>=2 else 5), latex(x), latex(case2),
                          latex(z-2 if z>=2 else 0), latex(5-(z-2) if z>=2 else 5), latex(x), latex(case3),
                          latex(case1), latex(case2), latex(case3), latex(n_A),
                          name1, name2, latex(n_A), latex(n_omega), kq_str))
            dapan=' \\shortans[0]{$%s$} '%(kq_str)
            # Các đáp án trắc nghiệm
            da_d = ('\\True $%s$' % kq_str)
            list_ans = [da_d, wrong_ans[0], wrong_ans[1], wrong_ans[2]]
            random.shuffle(list_ans)

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

