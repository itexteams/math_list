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


def bt_dang10_p3_b1_c2_ds10(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Bộ dữ liệu ngẫu nhiên được tính toán trước để đảm bảo tính chia hết và hình vẽ đẹp
                bpt_options = [
                    {"A": 20000, "B": 25000, "M": 100000, "a": 4, "b": 5, "c": 20},
                    {"A": 15000, "B": 20000, "M": 60000,  "a": 3, "b": 4, "c": 12},
                    {"A": 10000, "B": 15000, "M": 60000,  "a": 2, "b": 3, "c": 12},
                    {"A": 20000, "B": 30000, "M": 120000, "a": 2, "b": 3, "c": 12},
                    {"A": 12000, "B": 20000, "M": 60000,  "a": 3, "b": 5, "c": 15}
                ]

                config = random.choice(bpt_options)
                A = config["A"]  # Tiền phạt vật phẩm 1
                B = config["B"]  # Tiền phạt vật phẩm 2
                M = config["M"]  # Tổng số tiền phạt tối đa
                a = config["a"]  # Hệ số rút gọn của x
                b = config["b"]  # Hệ số rút gọn của y
                c = config["c"]  # Hệ số tự do rút gọn

                x_max = c // a
                y_max = c // b

                # Tính số lượng cặp nghiệm nguyên (x, y) thỏa mãn ax + by <= c
                total_cases = 0
                lattice_points_tikz = ""
                for cur_y in range(y_max + 1):
                    for cur_x in range(x_max + 1):
                        if a * cur_x + b * cur_y <= c:
                            total_cases += 1
                            # Tạo lệnh vẽ điểm nguyên cho TikZ
                            lattice_points_tikz += f"\\fill[black!70] ({cur_x}, {cur_y}) circle (2.5pt);"

                # Định nghĩa kích thước khung lưới cho hình vẽ TikZ dựa trên nghiệm lớn nhất
                max_grid = max(x_max, y_max) + 1

                # Khởi tạo mã nguồn đoạn vẽ hình TikZ theo phong cách mới
                tikz_code = f"""\\begin{{center}}
                \\begin{{tikzpicture}}[>=stealth, scale=0.6, line width=1pt]
                \\clip (-1.5, -1.5) rectangle ({max_grid + 1.5}, {max_grid + 1.5});
                \\fill[pattern=north east lines, pattern color=black] (-1.5, -1.5) rectangle ({max_grid + 1.5}, {max_grid + 1.5});
                \\fill[white] (0, 0) -- ({x_max}, 0) -- (0, {y_max}) -- cycle;
                \\draw[lightgray, dashed, line width=0.5pt] (-1,-1) grid ({max_grid},{max_grid});
                \\draw[->, black] (-1.5, 0) -- ({max_grid + 1}, 0) node[below] {{$x$}};
                \\draw[->, black] (0, -1.5) -- (0, {max_grid + 1}) node[left] {{$y$}};
                \\node at (0,0) [below left] {{$O$}};
                \\draw[black] (-1.5, {round((c + 1.5*a)/b, 2)}) -- ({round((c + 1.5*b)/a, 2)}, -1.5) node[above right] {{$d$}};
                \\draw[black] ({x_max},0.1) -- ({x_max},-0.1) node[below=2pt, font=\\footnotesize] {{${x_max}$}};
                \\draw[black] (0.1,{y_max}) -- (-0.1,{y_max}) node[left=2pt, font=\\footnotesize] {{${y_max}$}};
                {lattice_points_tikz}
                \\end{{tikzpicture}}
                \\end{{center}}"""

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (total_cases)]
                da = random.choice(du)

                # Tạo danh sách các đáp án sai xung quanh đáp án đúng
                s = [
                    '$%s$' % (total_cases + 2),
                    '$%s$' % (total_cases - 2),
                    '$%s$' % (total_cases + 4),
                    '$%s$' % (total_cases - 3),
                    '$%s$' % (total_cases + 5),
                ]
                s = [item for item in s if int(item.replace('$', '')) > 0]
                das1, das2, das3 = random.sample(s, 3)

                # Câu hỏi
                noidungcauhoi = ('''Chị Hoa là nhân viên tập sự phục vụ tại một quán ăn. Nếu làm bể mỗi cái chén sẽ bị phạt $%s$ đồng, làm bể mỗi cái ly sẽ bị phạt $%s$ đồng. Hỏi có \\textbf{tối đa} bao nhiêu trường hợp có thể xảy ra nếu tháng đó chị Hoa bị phạt không quá $%s$ đồng?''' 
                                 % (latex(A), latex(B), latex(M)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Đã chèn tikz_code vào vị trí tương ứng)
                loigiai = ('''Gọi $x, y$ lần lượt là số cái chén và số cái ly mà chị Hoa làm bể. ($x, y \\in \\mathbb{{N}}$) \\\\
                Theo đề bài ta có: $%sx + %sy \\le %s \\Rightarrow %sx + %sy \\le %s$. \\\\
                Với $x \\ge 0, y \\ge 0$, ta biểu diễn miền nghiệm của $%sx + %sy \\le %s$ như sau: \\\\
                + Vẽ đường thẳng $%sx + %sy = %s$ \\\\
                + Xét $O(0;0)$ ta có: $%s \\cdot 0 + %s \\cdot 0 \\le %s$ \\\\
                Do đó, miền nghiệm của $%sx + %sy \\le %s$ là nửa mặt phẳng bờ $d$ chứa $O(0;0)$ (miền không bị gạch)\n'''
                               % (latex(A), latex(B), latex(M), a, b, c,
                                  a, b, c, a, b, c, a, b, c,
                                  a, b, c) 
                               + tikz_code + 
                               '''\n Do $x, y \\in \\mathbb{{N}}$ nên số trường hợp tối đa có thể xảy ra nếu tháng đó chị Hoa bị phạt không quá $%s$ đồng là $%s$.'''
                               % (latex(M), total_cases))

                dapan = '\\shortans[0]{$%s$}\n' % (total_cases)

                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + dapan +
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
                return content

