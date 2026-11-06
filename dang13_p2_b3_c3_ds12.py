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


def bt_dang13_p2_b3_c3_ds12(self):
                # Khai báo biến
                x = symbols('x')

                # Thiết lập các thông số random
                h = random.choice([2, 4, 6]) 
                s1_val = (2 + 5) * h // 2
                s2_val = (1 * h) // 2
                tich_phan_tong = s1_val - s2_val
                tich_phan_tri_tuyet_doi = s1_val + s2_val

                # Mã TikZ vẽ hình
                tikz_hinh = r'''\begin{center}
                \begin{tikzpicture}[scale=0.8, >=stealth]
                    \fill[yellow!50] (-3,0) -- (-1,%s) -- (1,%s) -- (2,0) -- cycle;
                    \fill[yellow!50] (2,0) -- (3,-%s) -- (3,0) -- cycle;
                    \draw[->] (-3.5,0) -- (4,0) node[below] {$x$};
                    \draw[->] (0,-%s-0.5) -- (0,%s+0.5) node[left] {$y$};
                    \node[below left] at (0,0) {$O$};
                    \draw[thick] (-3,0) -- (-1,%s) -- (1,%s) -- (2,0) -- (3,-%s);
                    \draw[dashed] (-1,0) node[below] {$-1$} -- (-1,%s);
                    \draw[dashed] (1,0) node[below] {$1$} -- (1,%s);
                    \draw[dashed] (0,%s) node[left] {$%s$} -- (1,%s);
                    \draw[dashed] (3,0) node[above] {$3$} -- (3,-%s) -- (0,-%s) node[left] {$-%s$};
                    \node[below] at (-3,0) {$-3$};
                    \node[below left] at (2,0) {$2$};
                    \node at (0,%s/2) {$S_1$};
                    \node at (2.6,-%s/4) {$S_2$};
                \end{tikzpicture}
                \end{center}''' % (h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h)

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Cho hàm số $y=f(x)$ liên tục trên $[-3;3]$ có đồ thị như hình vẽ. 
                ''' + tikz_hinh + r'''
                Biết rằng $f(x)$ tạo với trục hoành và hai đường thẳng $x=-3, x=3$ một hình phẳng $(H)$ gồm 2 phần có diện tích lần lượt là $S_1, S_2$.''')

                ########################################################################
                # a) Nhận biết: Diện tích S1
                ########################################################################
                nb_da_1_d = r'\True Diện tích hình phẳng $S_1 = %s$.' % (s1_val)
                nb_da_1_s = r'Diện tích hình phẳng $S_1 = %s$.' % (tich_phan_tong)
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

                loigiai_nb_1 = r'''Dựa vào đồ thị, diện tích $S_1$ là diện tích hình thang giới hạn bởi đồ thị phía trên trục hoành từ $x=-3$ đến $x=2$. Ta có $S_1 = %s$.''' % (s1_val)

                ########################################################################
                # b) Thông hiểu: Tích phân trên đoạn không đổi dấu
                ########################################################################
                th_da_1_d = r'\True Giá trị của tích phân $\int_{-3}^{2} f(x) \text{d}x = %s$.' % (s1_val)
                th_da_1_s = r'Giá trị của tích phân $\int_{-3}^{2} f(x) \text{d}x = %s$.' % (s2_val)
                list_th_da_1 = [th_da_1_d, th_da_1_s]

                loigiai_th_1 = r'''Trên đoạn $[-3; 2]$, đồ thị hàm số $f(x)$ nằm phía trên trục hoành nên $\int_{-3}^{2} f(x) \text{d}x = S_1 = %s$.''' % (s1_val)

                ########################################################################
                # c) Vận dụng: Tích phân trên toàn đoạn
                ########################################################################
                vd_da_1_d = r'\True Tích phân $\int_{-3}^{3} f(x) \text{d}x = %s$.' % (tich_phan_tong)
                vd_da_1_s = r'Tích phân $\int_{-3}^{3} f(x) \text{d}x = %s$.' % (tich_phan_tri_tuyet_doi)
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

                loigiai_vd_1 = r'''Ta có $\int_{-3}^{3} f(x) \text{d}x = \int_{-3}^{2} f(x) \text{d}x + \int_{2}^{3} f(x) \text{d}x = S_1 - S_2 = %s - %s = %s$.''' % (s1_val, s2_val, tich_phan_tong)

                ########################################################################
                # d) Vận dụng cao: Tổng diện tích hình phẳng
                ########################################################################
                vdc_da_1_d = r'\True Diện tích hình phẳng $(H)$ là $S = \int_{-3}^{3} |f(x)| \text{d}x = %s$.' % (tich_phan_tri_tuyet_doi)
                vdc_da_1_s = r'Diện tích hình phẳng $(H)$ là $S = \int_{-3}^{3} |f(x)| \text{d}x = %s$.' % (tich_phan_tong)
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

                loigiai_vdc_1 = r'''Diện tích hình phẳng $(H)$ giới hạn bởi đồ thị $f(x)$ và trục hoành trên $[-3;3]$ là $S = S_1 + S_2 = %s + %s = %s$.''' % (s1_val, s2_val, tich_phan_tri_tuyet_doi)

                ########################################################################
                # Logic chọn đáp án Đúng/Sai (1-3 câu đúng)
                ########################################################################
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    ans_a = random.choice(list_nb_da_1)
                    ans_b = random.choice(list_th_da_1)
                    ans_c = random.choice(list_vd_da_1)
                    ans_d = random.choice(list_vdc_da_1)

                    if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                        shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
                        break

                # Xuất nội dung
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choiceTFn \n'
                    '{' + str(shuffled_answers[0]) + '}\n'
                    '{' + str(shuffled_answers[1]) + '}\n'
                    '{' + str(shuffled_answers[2]) + '}\n'
                    '{' + str(shuffled_answers[3]) + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + str(loigiai_nb_1) + '\n'
                    '\\item ' + str(loigiai_th_1) + '\n'
                    '\\item ' + str(loigiai_vd_1) + '\n'
                    '\\item ' + str(loigiai_vdc_1) + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage} \n\n')

                return content

