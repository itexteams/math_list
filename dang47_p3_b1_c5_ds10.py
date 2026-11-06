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


def bt_dang47_p3_b1_c5_ds10(self):
            # Chọn ngẫu nhiên 5 chữ số khác nhau từ 1 đến 9
            # Khai báo biến
            # Khai báo biến
            # Random vị trí điểm A bị chắn (các vị trí làm bài toán có ý nghĩa)
            A_positions = [(1,1), (2,1), (3,1), (1,2), (2,2), (3,2)]
            Ax, Ay = random.choice(A_positions)

            # Khởi tạo các cạnh của đồ thị dạng (từ_điểm, đến_điểm)
            edges = [
                # Các cạnh đi ngang (sang phải)
                ((0,0),(1,0)), ((1,0),(2,0)), ((2,0),(3,0)), ((3,0),(4,0)), ((4,0),(5,0)),
                ((0,1),(1,1)), ((1,1),(2,1)), ((2,1),(3,1)), ((3,1),(4,1)), ((4,1),(5,1)),
                ((0,2),(1,2)), ((1,2),(2,2)), ((2,2),(3,2)),
                ((0,3),(2,3)), ((2,3),(3,3)), ((3,3),(5,3)),
                # Các cạnh đi dọc (đi lên)
                ((0,0),(0,1)), ((0,1),(0,2)), ((0,2),(0,3)),
                ((1,0),(1,1)), ((1,1),(1,2)),
                ((2,0),(2,1)), ((2,1),(2,2)), ((2,2),(2,3)),
                ((3,0),(3,1)), ((3,1),(3,2)), ((3,2),(3,3)),
                ((4,0),(4,1)),
                ((5,0),(5,1)), ((5,1),(5,3))
            ]

            # Tập hợp các nút
            nodes = set([u for u,v in edges] + [v for u,v in edges])
            val = {n: 0 for n in nodes}
            val[(0,0)] = 1 # Nút bắt đầu (M) có 1 cách

            # Sắp xếp các nút từ dưới lên, từ trái qua phải để tính toán quy hoạch động
            sorted_nodes = sorted(list(nodes), key=lambda p: p[0]+p[1])

            # Tính số cách đi đến mỗi nút
            for n in sorted_nodes:
                if n == (0,0): continue
                # Nếu là vị trí A bị chặn, số cách đi qua bằng 0
                if n == (Ax, Ay):
                    val[n] = 0
                    continue
                # Cộng dồn số cách từ các nút kề trước đó
                for u, v in edges:
                    if v == n:
                        val[n] += val[u]

            # Kết quả đúng là giá trị tại điểm C(5,3)
            kq = val[(5,3)]

            # Các đáp án trắc nghiệm
            du = ['$%s$' % (kq)]
            da = random.choice(du)

            # Tạo các đáp án sai gần với đáp án đúng
            s_opts = list(set([kq-1, kq+1, kq+2, kq-2, kq+3, kq-3, kq+4, kq-4]))
            if kq in s_opts: s_opts.remove(kq)
            if 0 in s_opts: s_opts.remove(0)

            s = ['$%s$' % (latex(opt)) for opt in random.sample(s_opts, 3)]

            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Tạo nội dung ảnh TikZ cho đề bài
            tikz_q = ('\\begin{center}\n'
                      '\\begin{tikzpicture}[scale=0.8, font=\\small, line width=1pt]\n'
                      '\\draw (0,0) -- (5,0);\n'
                      '\\draw (0,1) -- (5,1);\n'
                      '\\draw (0,2) -- (3,2);\n'
                      '\\draw (0,3) -- (2,3);\n'
                      '\\draw (2,3) -- (5,3);\n'
                      '\\draw (0,0) -- (0,3);\n'
                      '\\draw (1,0) -- (1,2);\n'
                      '\\draw (2,0) -- (2,3);\n'
                      '\\draw (3,0) -- (3,3);\n'
                      '\\draw (4,0) -- (4,1);\n'
                      '\\draw (5,0) -- (5,3);\n'
                      # Đã sửa: Thêm màu đỏ [red] và tăng kích thước lên 2.5pt cho M, C, A
                      '\\fill[red] (0,0) circle (2.5pt) node[below, black] {$M$};\n'
                      '\\fill[red] (5,3) circle (2.5pt) node[right, black] {$C$};\n'
                      '\\fill[red] (%s,%s) circle (2.5pt) node[below right, black] {$A$};\n'
                      '\\end{tikzpicture}\n'
                      '\\end{center}' % (Ax, Ay))

            # Câu hỏi
            noidungcauhoi = ('Trên đường đi từ nhà Mạnh (M) đến công ty (C) có điểm $A$ người ta đang thi công sửa chữa đường nên không thể đi qua vị trí điểm $A$. Biết rằng toàn bộ cung đường theo bản đồ từ dưới lên trên và từ trái qua phải là đường một chiều nên vì vậy nên Mạnh chỉ được phép đi lên hoặc đi sang phải. Vậy Mạnh có bao nhiêu cách đi từ nhà đến công ty?\n%s' % (tikz_q))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xây dựng các Node hiển thị lời giải
            node_str = ""
            for (x,y), v in val.items():
                if (x,y) == (Ax, Ay): continue
                if v == 0: continue

                pos_str = "above right"
                if x == 0 and y != 0: pos_str = "above left"
                if y == 0 and x != 0: pos_str = "below right"
                if x == 0 and y == 0: pos_str = "below right"
                if x == 5 and y == 3: pos_str = "above left"

                node_str += '\\node[%s, inner sep=1.5pt] at (%s,%s) {$%s$};\n' % (pos_str, x, y, v)

            # Tạo nội dung ảnh TikZ cho lời giải
            tikz_sol = ('\\begin{center}\n'
                        '\\begin{tikzpicture}[scale=0.8, font=\\small, line width=1pt]\n'
                        '\\draw (0,0) -- (5,0);\n'
                        '\\draw (0,1) -- (5,1);\n'
                        '\\draw (0,2) -- (3,2);\n'
                        '\\draw (0,3) -- (2,3);\n'
                        '\\draw (2,3) -- (5,3);\n'
                        '\\draw (0,0) -- (0,3);\n'
                        '\\draw (1,0) -- (1,2);\n'
                        '\\draw (2,0) -- (2,3);\n'
                        '\\draw (3,0) -- (3,3);\n'
                        '\\draw (4,0) -- (4,1);\n'
                        '\\draw (5,0) -- (5,3);\n'
                        # Đã sửa: Thêm màu đỏ [red] và tăng kích thước lên 2.5pt cho M, C, A
                        '\\fill[red] (0,0) circle (2.5pt) node[below, black] {$M$};\n'
                        '\\fill[red] (5,3) circle (2.5pt) node[right, black] {$C$};\n'
                        '\\fill[red] (%s,%s) circle (2.5pt) node[below right, black] {$A$};\n'
                        '%s'
                        '\\end{tikzpicture}\n'
                        '\\end{center}' % (Ax, Ay, node_str))

            # Nội dung lời giải
            loigiai = ('Từ sơ đồ ta có thể suy ra từ nhà Mạnh đến công ty có $%s$ cách.\n%s' % (kq, tikz_sol))
            dapan='\\shortans[0]{$%s$}\n'%(da)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

