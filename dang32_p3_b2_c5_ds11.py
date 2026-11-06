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


def bt_dang32_p3_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random dữ liệu bài toán
                # N là số lượng số tự nhiên liên tiếp trong tập hợp A
                N = randint(48, 55)

                # Số ô trong hình vẽ là tổng từ 1 đến 6 (hàng 1 có 1 ô, ..., hàng 6 có 6 ô)
                # Tổng số ô = 21. Các vị trí A, B, C, D, E, F tương ứng với các chỉ số trong dãy tăng dần x_1...x_21
                # A = x_1, B = x_3, C = x_6, D = x_10, E = x_15, F = x_21

                T = 0
                loigiai_chi_tiet = ""

                # Bước 2: Tính toán các trường hợp của công sai d
                # Giữa E (x_15) và F (x_21) có 5 số nên d = F - E >= 6
                # Điều kiện F = A + 5d <= N
                d_min = 6
                d_max = (N - 1) // 5

                for d in range(d_min, d_max + 1):
                    # Số cách chọn các số nằm giữa các mốc AP
                    # Giữa A-B: C(d-1, 1), B-C: C(d-1, 2), C-D: C(d-1, 3), D-E: C(d-1, 4), E-F: C(d-1, 5)
                    ways_between = math.comb(d-1, 1) * math.comb(d-1, 2) * math.comb(d-1, 3) * math.comb(d-1, 4) * math.comb(d-1, 5)

                    # Số giá trị có thể có của A sao cho F = A + 5d <= N => A <= N - 5d
                    max_A = N - 5 * d
                    T_d = max_A * ways_between
                    T += T_d

                    # Chuỗi LaTeX cho từng trường hợp để đưa vào lời giải
                    loigiai_chi_tiet += (
                        '\\text{Trường hợp } $d = %s: A + 5 \\cdot %s \\le %s \\Rightarrow A \\le %s$. \\\\'
                        '\\text{Số cách chọn các số ở giữa là } $%s \\cdot C_{%s}^{1} \\cdot C_{%s}^{2} \\cdot C_{%s}^{3} \\cdot C_{%s}^{4} \\cdot C_{%s}^{5} = %s$. \\\\'
                        % (latex(d), latex(d), latex(N), latex(max_A), latex(max_A), latex(d-1), latex(d-1), latex(d-1), latex(d-1), latex(d-1), latex(T_d))
                    )

                # Tính log(T)
                kq_val = math.log10(T)
                kq_rounded = Decimal(float(kq_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                da_dung = str(kq_rounded).replace('.', ',')

                # Tạo các phương án sai
                s = [
                    str(round(kq_val + 0.5, 1)).replace('.', ','),
                    str(round(kq_val - 0.7, 1)).replace('.', ','),
                    str(round(kq_val + 1.2, 1)).replace('.', ','),
                    str(round(kq_val - 0.3, 1)).replace('.', ','),
                    str(round(kq_val + 0.8, 1)).replace('.', ','),
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (
                    '''\\immini{Từ tập hợp $A = \\left\\{ 1; 2; 3; \\dots; %s \\right\\}$ gồm $%s$ số tự nhiên liên tiếp, cần chọn ra $21$ số phân biệt để gắn vào $21$ ô đơn vị như hình vẽ. Gọi $T$ là số cách chọn số sao cho mọi số ở hàng trên luôn nhỏ hơn mọi số ở hàng dưới, mọi số bên trái luôn nhỏ hơn mọi số bên phải cùng hàng, đồng thời các số thuộc các ô $A, B, C, D, E, F$ theo thứ tự lập thành cấp số cộng. Giá trị $\\log \\left( T \\right)$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục).}
            {\\begin{tikzpicture}[scale=0.5, line width=1pt]
            \\draw (0,6) -- (1,6) -- (1,5) -- (2,5) -- (2,4) -- (3,4) -- (3,3) -- (4,3) -- (4,2) -- (5,2) -- (5,1) -- (6,1) -- (6,0) -- (0,0) -- cycle;
            \\draw (0,5) -- (1,5); \\draw (0,4) -- (2,4); \\draw (0,3) -- (3,3); \\draw (0,2) -- (4,2); \\draw (0,1) -- (5,1);
            \\draw (1,6) -- (1,0); \\draw (2,5) -- (2,0); \\draw (3,4) -- (3,0); \\draw (4,3) -- (4,0); \\draw (5,2) -- (5,0);
            \\node at (0.5, 5.5) {A}; \\node at (1.5, 4.5) {B}; \\node at (2.5, 3.5) {C}; \\node at (3.5, 2.5) {D}; \\node at (4.5, 1.5) {E}; \\node at (5.5, 0.5) {F};
            \\end{tikzpicture} }'''
                    % (latex(N), latex(N))
                )

                # Các đáp án
                da_d = ('\\True $%s$' % (da_dung))
                da_s1 = ('$%s$' % (das1))
                da_s2 = ('$%s$' % (das2))
                da_s3 = ('$%s$' % (das3))

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải
                loigiai = (
                    '''Do điều kiện mọi số hàng trên nhỏ hơn hàng dưới và trái nhỏ hơn phải, nên khi chọn được bộ $21$ số, các số này phải được sắp xếp theo thứ tự tăng dần vào các ô theo quy tắc từ trái sang phải, từ trên xuống dưới. \\\\
                    Gọi $21$ số được chọn là $x_1 < x_2 < \\dots < x_{21}$. Khi đó, các ô tương ứng là: \\\\
                    $A = x_1, B = x_3, C = x_6, D = x_{10}, E = x_{15}, F = x_{21}$. \\\\
                    Vì $A, B, C, D, E, F$ lập thành cấp số cộng với công sai $d$, ta có: \\\\
                    $B = A + d, C = A + 2d, D = A + 3d, E = A + 4d, F = A + 5d$. \\\\
                    Giữa $E$ và $F$ có $21 - 15 - 1 = 5$ số nên $d - 1 \\ge 5 \\Rightarrow d \\ge 6$. \\\\
                    Mặt khác, $F \\le %s \\Rightarrow A + 5d \\le %s$. \\\\
                    %s
                    Tổng số cách chọn là $T = %s$. \\\\
                    Vậy $\\log \\left( T \\right) = \\log \\left( %s \\right) \\approx %s$.'''
                    % (latex(N), latex(N), loigiai_chi_tiet, latex(T), latex(T), da_dung)
                )
                dapan='\\shortans[0]{$%s$}\n'%(da_dung)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

