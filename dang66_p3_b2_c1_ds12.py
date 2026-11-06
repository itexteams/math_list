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


def bt_dang66_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                params = [
                    (2000, 16, 0.005, 5, 4, "bốn"),
                    (2500, 20, 0.004, 5, 5, "năm"),
                    (1500, 15, 0.006, 10, 3, "ba"),
                    (2000, 18, 0.005, 10, 4, "bốn"),
                    (3000, 22, 0.005, 5, 5, "năm")
                ]

                N, a, b, t_pct, c, c_text = random.choice(params)

                t_rate = t_pct / 100.0
                factor = 1.0 - t_rate

                coeff_x = factor * a - c          # Hệ số bậc 1 của P(x)
                coeff_x2 = factor * b         # Hệ số bậc 2 của P(x) (P(x) = -coeff_x2 * x^2 + coeff_x * x)

                # Điểm cực trị x_peak = coeff_x / (2 * coeff_x2)
                x_peak = coeff_x / (2 * coeff_x2)

                x_floor = math.floor(x_peak)
                x_ceil = math.ceil(x_peak)

                P_floor = coeff_x * x_floor - coeff_x2 * (x_floor**2)
                P_ceil = coeff_x * x_ceil - coeff_x2 * (x_ceil**2)

                if P_ceil >= P_floor:
                    x_opt = x_ceil
                else:
                    x_opt = x_floor

                # Chuyển đổi định dạng số thập phân sang dấu phẩy theo quy tắc
                a_str = str(a).replace('.', ',')
                b_str = str(b).replace('.', ',')
                factor_str = str(round(factor, 4)).replace('.', ',')
                coeff_x_str = str(round(coeff_x, 4)).replace('.', ',')
                coeff_x2_str = str(round(coeff_x2, 6)).replace('.', ',')
                coeff_2x2_str = str(round(2 * coeff_x2, 6)).replace('.', ',')
                x_peak_str = str(round(x_peak, 2)).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (x_opt)]
                da = du[0]

                s = [
                    '$%s$' % (x_opt + 10),
                    '$%s$' % (x_opt - 10),
                    '$%s$' % (x_opt + 20),
                    '$%s$' % (x_opt - 20),
                    '$%s$' % (x_opt + 50),
                    '$%s$' % (x_opt - 50),
                    '$%s$' % (N),
                    '$%s$' % (x_floor if x_opt == x_ceil else x_ceil)
                ]
                s = [ans for ans in s if ans != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Bảng biến thiên vẽ bằng TikZ (đã thêm khung bao quanh)
                bbt_tikz = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, >=stealth, line width=1pt]
            \\draw (0,0.8) rectangle (7.5,-2.6);
            \\draw (0,0) -- (7.5,0);
            \\draw (0,-0.8) -- (7.5,-0.8);
            \\draw (1.5,0.8) -- (1.5,-2.6);
            \\node at (0.75,0.4) {$x$};
            \\node at (1.8,0.4) {$0$};
            \\node at (4.5,0.4) {$%s$};
            \\node at (7.0,0.4) {$%s$};
            \\node at (0.75,-0.4) {$P'(x)$};
            \\node at (3.15,-0.4) {$+$};
            \\node at (4.5,-0.4) {$0$};
            \\node at (5.75,-0.4) {$-$};
            \\node at (0.75,-1.7) {$P(x)$};
            \\node (min1) at (1.8,-2.3) {$0$};
            \\node (max) at (4.5,-1.1) {$P(%s)$};
            \\node (min2) at (7.0,-2.3) {$P(%s)$};
            \\draw[->] (min1) -- (max);
            \\draw[->] (max) -- (min2);
            \\end{tikzpicture}
            \\end{center}''' % (x_peak_str, N, x_peak_str, N))

                # Câu hỏi
                noidungcauhoi = ('''Một doanh nghiệp dự kiến sản xuất không quá $%s$ sản phẩm cùng loại. Giả sử rằng doanh thu của doanh nghiệp khi sản xuất $x$ sản phẩm ($x \\in \\mathbb{N}; 0 \\le x \\le %s$) là $R(x) = %sx - %sx^2$ (triệu đồng) và doanh nghiệp phải nộp một khoản thuế là $%s\\%%$ của doanh thu $R(x)$. Chi phí để sản xuất mỗi sản phẩm là %s triệu đồng. Lợi nhuận của doanh nghiệp (khi sản xuất $x$ sản phẩm) được tính theo công thức: Lợi nhuận bằng doanh thu trừ đi thuế và chi phí. Doanh nghiệp phải sản xuất bao nhiêu sản phẩm để thu được lợi nhuận lớn nhất?'''
                                 % (N, N, a_str, b_str, t_pct, c_text))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (xét hàm, đạo hàm, lập bảng biến thiên TikZ)
                loigiai = ('''Doanh thu của doanh nghiệp sau khi nộp thuế $%s\\%%$ là:\\\\
            $R_{\\text{sau thuế}}(x) = (1 - %s\\%%) R(x) = %s \\cdot (%sx - %sx^2) = %sx - %sx^2$ (triệu đồng).\\\\
            Chi phí sản xuất $x$ sản phẩm là:\\\\
            $C(x) = %sx$ (triệu đồng).\\\\
            Lợi nhuận của doanh nghiệp khi sản xuất $x$ sản phẩm là:\\\\
            $P(x) = R_{\\text{sau thuế}}(x) - C(x) = (%sx - %sx^2) - %sx = -%sx^2 + %sx$ (triệu đồng).\\\\
            Xét hàm số $P(x) = -%sx^2 + %sx$ trên đoạn $[0; %s]$.\\\\
            Ta có đạo hàm:\\\\
            $P'(x) = -%sx + %s$.\\\\
            Cho $P'(x) = 0 \\Leftrightarrow -%sx + %s = 0 \\Leftrightarrow x = \\frac{%s}{%s} \\approx %s$.\\\\
            Ta có bảng biến thiên của hàm số $P(x)$ trên đoạn $[0; %s]$ như sau:\\\\
            %s
            Dựa vào bảng biến thiên, hàm số $P(x)$ đạt giá trị lớn nhất tại điểm $x_0 \\approx %s$.\\\\
            Vì $x \\in \\mathbb{N}$, ta xét hai số nguyên gần $x_0$ nhất là $x = %s$ và $x = %s$.\\\\
            So sánh giá trị $P(%s)$ và $P(%s)$, ta được giá trị lợi nhuận lớn nhất đạt tại $x = %s$.\\\\
            Vậy doanh nghiệp phải sản xuất $%s$ sản phẩm để thu được lợi nhuận lớn nhất.'''
                           % (t_pct, t_pct, factor_str, a_str, b_str, str(round(factor * a, 4)).replace('.', ','), str(round(factor * b, 6)).replace('.', ','),
                              c,
                              str(round(factor * a, 4)).replace('.', ','), str(round(factor * b, 6)).replace('.', ','), c, coeff_x2_str, coeff_x_str,
                              coeff_x2_str, coeff_x_str, N,
                              coeff_2x2_str, coeff_x_str,
                              coeff_2x2_str, coeff_x_str, coeff_x_str, coeff_2x2_str, x_peak_str,
                              N,
                              bbt_tikz,
                              x_peak_str,
                              x_floor, x_ceil,
                              x_floor, x_ceil, x_opt,
                              x_opt))
            dapan='\\shortans[0]{$%s$}\n'%(x_opt)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

