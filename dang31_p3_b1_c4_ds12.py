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


def bt_dang31_p3_b1_c4_ds12(self):
            # Khai báo biến
            def format_frac(num, den):
                f = frac(num, den)
                if f.denominator == 1:
                    return str(f.numerator)
                return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng ngăn sách K (từ 3 đến 6)
                K_val = random.choice([3, 4, 5, 6])

                # Để giữ nguyên logic 2 trường hợp (ngăn max=4 và ngăn max=3), tổng số sách phải là K + 3
                N_val = K_val + 3

                # Tính toán các giá trị tổ hợp và hệ số
                case1_ways = K_val
                case2_ways = K_val * (K_val - 1)
                nA_coeff = case1_ways + case2_ways

                # Tính các phân số cho xác suất
                frac_4_N = format_frac(4, N_val)
                frac_fav1 = format_frac(4 * case1_ways, N_val)

                frac_3_N = format_frac(3, N_val)
                frac_fav2 = format_frac(3 * case2_ways, N_val)

                frac_fav_sum = format_frac(4 * case1_ways + 3 * case2_ways, N_val)

                P_exact = frac(4 * case1_ways + 3 * case2_ways, N_val * nA_coeff)
                P_exact_str = format_frac(P_exact.numerator, P_exact.denominator)

                P_approx = round(float(P_exact), 2)
                kq_str = str(P_approx).replace('.', ',')

                # Xử lý chuỗi văn bản cho phù hợp với số lượng K
                n_str = ', '.join([f'n_{i}' for i in range(1, K_val + 1)])
                rem_case1 = f"{K_val - 1} ngăn còn lại mỗi ngăn 1 cuốn"

                if K_val - 2 == 1:
                    rem_case2 = "ngăn còn lại chứa 1 cuốn"
                    rem_case2_sent = "Ngăn còn lại chứa 1 cuốn."
                else:
                    rem_case2 = f"{K_val - 2} ngăn còn lại mỗi ngăn 1 cuốn"
                    rem_case2_sent = f"{K_val - 2} ngăn còn lại mỗi ngăn chứa 1 cuốn."

                # Vẽ hình TikZ minh họa (động theo K_val)
                tikz_code = "\\begin{center}\n\\begin{tikzpicture}[scale=0.8, line width=1pt]\n"
                colors = ["green!15", "orange!15", "blue!15", "cyan!40", "purple!15", "yellow!15"]
                for i in range(K_val):
                    color = colors[i % len(colors)]
                    tikz_code += f"\\draw[fill={color}] ({i*1.5},0) rectangle ({(i+1)*1.5},2.5);\n"

                    # Sắp xếp giống case 2 để minh hoạ
                    count = 1
                    if i == K_val - 1:
                        count = 3
                    elif i == K_val - 2:
                        count = 2

                    start_x = i*1.5 + 0.75 - (count*0.3)/2
                    for j in range(count):
                        bx = start_x + j*0.3
                        by = 0.5
                        tikz_code += f"\\draw[fill=white, thin, line join=round] ({bx},{by}) rectangle ++(0.15,1.2);\n"
                        tikz_code += f"\\draw[fill=white, thin, line join=round] ({bx+0.15},{by}) -- ++(0.08,0.1) -- ++(0,1.2) -- ++(-0.08,-0.1) -- cycle;\n"
                        tikz_code += f"\\draw[fill=white, thin, line join=round] ({bx},{by+1.2}) -- ++(0.08,0.1) -- ++(0.15,0) -- ++(-0.08,-0.1) -- cycle;\n"
                tikz_code += "\\end{tikzpicture}\n\\end{center}\n"

                # Các đáp án trắc nghiệm
                da = kq_str
                s_set = set()
                while len(s_set) < 3:
                    offset = round(random.choice([-0.12, -0.05, -0.02, -0.01, 0.02, 0.03, 0.05, 0.11]), 2)
                    wrong = round(P_approx + offset, 2)
                    if 0 < wrong < 1 and wrong != P_approx:
                        s_set.add(str(wrong).replace('.', ','))

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Xếp ngẫu nhiên $%s$ cuốn sách khác nhau có tính thứ tự, trong đó có một cuốn là sách Toán vào một giá sách có $%s$ ngăn. Biết rằng sau khi xếp, mỗi ngăn đều có ít nhất một cuốn sách. Gọi $A$ là biến cố trong $%s$ ngăn sách, có đúng một ngăn chứa số lượng sách nhiều hơn hẳn các ngăn còn lại” và $B$ là biến cố cuốn sách Toán học nằm ở ngăn có nhiều sách nhất đó. Xác suất $P(B|A)$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).' % (N_val, K_val, K_val))
                noidungcauhoi += tikz_code

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = ('$%s$' % das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải
                loigiai_args = (
                    K_val, n_str, N_val,
                    rem_case1, K_val, K_val, case1_ways,
                    N_val, N_val, case1_ways, N_val,
                    rem_case2, K_val, K_val, K_val,
                    K_val - 1, K_val - 1, K_val - 1, rem_case2_sent,
                    N_val, N_val, K_val, K_val - 1, N_val, case2_ways, N_val,
                    case1_ways, N_val, case2_ways, N_val, nA_coeff, N_val,
                    N_val, N_val,
                    frac_4_N, frac_4_N, frac_4_N, case1_ways, N_val, frac_fav1, N_val,
                    frac_3_N, frac_3_N, frac_3_N, case2_ways, N_val, frac_fav2, N_val,
                    frac_fav1, frac_fav2, N_val, frac_fav_sum, N_val,
                    frac_fav_sum, N_val, nA_coeff, N_val, P_exact_str, kq_str
                )

                loigiai = (
                    'Gọi số sách trong $%s$ ngăn lần lượt là $%s$. Khi đó, tổng số sách bằng $%s$ và mỗi ngăn có ít nhất một cuốn sách. '
                    'Để có duy nhất một ngăn nhiều sách nhất thì ta có các trường hợp sau:\\\\\n'
                    '\\textbf{Trường hợp 1:} Ngăn nhiều nhất có 4 cuốn, %s và 4 là số lớn nhất duy nhất, chọn 1 ngăn (trong $%s$ ngăn) để chứa 4 cuốn có $C_{%s}^1 = %s$ cách.\\\\\n'
                    'Xếp $%s$ cuốn sách vào có $%s!$ cách nên số cách xếp trong trường hợp này là $n(A_1) = %s.%s!$ cách.\\\\\n'
                    '\\textbf{Trường hợp 2:} Ngăn nhiều nhất có 3 cuốn, ngăn nhiều thứ hai có 2 cuốn, %s, chọn 1 ngăn (trong $%s$ ngăn) để chứa 3 cuốn có $C_{%s}^1 = %s$ cách.\\\\\n'
                    'Chọn 1 ngăn (trong $%s$ ngăn còn lại) để chứa 2 cuốn có $C_{%s}^1 = %s$ cách. %s\\\\\n'
                    'Xếp $%s$ cuốn sách vào có $%s!$ cách nên số cách xếp là $n(A_2) = %s.%s.%s! = %s.%s!$ cách.\\\\\n'
                    'Vậy số cách xếp thỏa mãn là: $n(A) = n(A_1) + n(A_2) = %s.%s! + %s.%s! = %s.%s!$\\\\\n'
                    'Biến cố $B$ yêu cầu sách Toán phải nằm trong ngăn nhiều sách nhất.\\\\\n'
                    'Vì vai trò của các cuốn sách là như nhau nên xác suất để cuốn sách Toán rơi vào một nhóm $k$ vị trí trong tổng số $%s$ vị trí là $\\frac{k}{%s}$.\\\\\n'
                    '\\textbf{Trong trường hợp 1:} Ngăn nhiều nhất có 4 cuốn nên xác suất sách Toán nằm ở ngăn này là: $%s$\\\\\n'
                    'Vậy số cách thuận lợi cho trường hợp này là: $%s.n(A_1) = %s.%s.%s! = %s.%s!$.\\\\\n'
                    '\\textbf{Trong trường hợp 2:} Ngăn nhiều nhất có 3 cuốn nên xác suất sách Toán nằm ở ngăn này là: $%s$\\\\\n'
                    'Vậy số cách thuận lợi cho trường hợp này là: $%s.n(A_2) = %s.%s.%s! = %s.%s!$\\\\\n'
                    'Tổng số cách thuận lợi: $n(A \\cap B) = \\left( %s + %s \\right).%s! = %s.%s!$\\\\\n'
                    'Vậy xác suất cần tính là: $P(B|A) = \\frac{n(A \\cap B)}{n(A)} = \\frac{%s.%s!}{%s.%s!} = %s \\approx %s$.'
                    % loigiai_args
                )
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

