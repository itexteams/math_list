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


def bt_dang85_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Bước 1 & 3: Nghiên cứu đề bài và thiết lập các giá trị ngẫu nhiên
            # h = at^2 + bt + c
            t_sym = symbols('t')

            # Tạo ngẫu nhiên các thông số để bài toán đa dạng
            # h0: độ cao ban đầu (t=0)
            # h1: độ cao sau 1 giây (t=1)
            # h2: độ cao sau 2 giây (t=2)
            h0 = round(random.uniform(1.0, 2.0), 1)
            h1 = round(random.uniform(7.0, 9.0), 1)
            h2 = round(random.uniform(5.0, 6.5), 1)

            # Giải hệ phương trình để tìm a, b, c
            # c = h0
            # a + b + c = h1
            # 4a + 2b + c = h2
            a_val, b_val, c_val = symbols('a b c')
            eq1 = c_val - h0
            eq2 = a_val + b_val + c_val - h1
            eq3 = 4*a_val + 2*b_val + c_val - h2

            sol = solve((eq1, eq2, eq3), (a_val, b_val, c_val))
            a = float(sol[a_val])
            b = float(sol[b_val])
            c = float(sol[c_val])

            # Bước 4: Giải phương trình h = 0 để tìm thời điểm chạm đất (nghiệm dương)
            # at^2 + bt + c = 0
            delta = b**2 - 4*a*c
            t_touch = (-b - (delta**0.5)) / (2*a) 
            kq_val = round(t_touch, 2)
            kq_str = str(kq_val).replace('.', ',')

            # Tạo các phương án sai không trùng đáp án đúng
            s = set()
            while len(s) < 3:
                sai = round(kq_val + random.choice([-1.2, -0.5, 0.5, 0.8, 1.1]), 2)
                if sai > 0 and sai != kq_val:
                    s.add(str(sai).replace('.', ','))
            list_sai = list(s)

            # Nội dung câu hỏi
            noidungcauhoi = (f"Khi một quả bóng được đá lên, nó sẽ đạt đến độ cao nào đó rồi rơi xuống. "
                             f"Biết rằng quỹ đạo của quả bóng là một cung parabol trong mặt phẳng với hệ tọa độ $Oth$, "
                             f"trong đó $t$ là thời gian (tính bằng giây) kể từ khi quả bóng được đá lên; $h$ là độ cao (tính bằng mét) của quả bóng. "
                             f"Giả thiết rằng quả bóng được đá lên từ độ cao ${str(h0).replace('.', ',')}m$. Sau đó $1$ giây, nó đạt độ cao ${str(h1).replace('.', ',')}m$ "
                             f"và $2$ giây sau khi đá lên, nó đạt độ cao ${str(h2).replace('.', ',')}m$. Hỏi sau bao lâu thì quả bóng sẽ chạm đất kể từ khi được đá lên "
                             f"(tính chính xác đến hàng phần trăm)?")



            # Nội dung lời giải chi tiết
            loigiai = (# Vẽ hình bằng TikZ
            f"""\\begin{{center}}
            \\begin{{tikzpicture}}[scale=0.8, >=stealth]
                \\draw[->] (0,0) -- (4,0) node[below] {{$t$}};
                \\draw[->] (0,0) -- (0,5) node[left] {{$h$}};
                \\draw[domain=0:3.5, smooth, variable=\\x, blue, thick] plot (\\x, {{{a/2}*\\x*\\x + {b/2}*\\x + {c/2}}});
                \\draw[dashed] (1,0) node[below] {{$1$}} -- (1,{(a+b+c)/2}) -- (0,{(a+b+c)/2}) node[left] {{{str(h1).replace('.', ',')}}};
                \\draw[dashed] (2,0) node[below] {{$2$}} -- (2,{(4*a+2*b+c)/2}) -- (0,{(4*a+2*b+c)/2}) node[left] {{{str(h2).replace('.', ',')}}};
                \\node[left] at (0,{c/2}) {{{str(h0).replace('.', ',')}}};
                \\node[below left] at (0,0) {{$O$}};
            \\end{{tikzpicture}}
            \\end{{center}}"""
                f"Gọi phương trình của parabol quỹ đạo là $h = at^2 + bt + c$. \\\\ \n"
                       f"Từ giả thiết, parabol đi qua các điểm $(0; {str(h0).replace('.', ',')})$, $(1; {str(h1).replace('.', ',')})$ và $(2; {str(h2).replace('.', ',')})$. \\\\ \n"
                       f"Từ đó ta có hệ phương trình: \n"
                       f"$\\begin{{cases}} c = {str(h0).replace('.', ',')} \\\\ a + b + c = {str(h1).replace('.', ',')} \\\\ 4a + 2b + c = {str(h2).replace('.', ',')} \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} a = {str(round(a, 2)).replace('.', ',')} \\\\ b = {str(round(b, 2)).replace('.', ',')} \\\\ c = {str(h0).replace('.', ',')} \\end{{cases}}$. \\\\ \n"
                       f"Vậy phương trình quỹ đạo là $h = {str(round(a, 2)).replace('.', ',')}t^2 + {str(round(b, 2)).replace('.', ',')}t + {str(h0).replace('.', ',')}$. \\\\ \n"
                       f"Khi bóng chạm đất, $h = 0 \\Leftrightarrow {str(round(a, 2)).replace('.', ',')}t^2 + {str(round(b, 2)).replace('.', ',')}t + {str(h0).replace('.', ',')} = 0$. \\\\ \n"
                       f"Giải phương trình ta tìm được nghiệm dương $t \\approx {kq_str}$.")

            # Xuất câu trắc nghiệm
            da_d = '\\True $' + kq_str + '$'
            list_1 = [da_d, f'${list_sai[0]}$', f'${list_sai[1]}$', f'${list_sai[2]}$']
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + '\n'
                       '\\choice \n'
                       '{' + list_1[0] + '}\n'
                       '{' + list_1[1] + '}\n'
                       '{' + list_1[2] + '}\n'
                       '{' + list_1[3] + '}\n'
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

