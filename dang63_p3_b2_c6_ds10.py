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


def bt_dang63_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- RANDOM CÁC THÔNG SỐ BÀI TOÁN ---
                # Random số lần gieo xúc xắc (các số chẵn để luôn có khả năng quay về điểm ban đầu)
                N_list = [8, 10, 12]
                N = random.choice(N_list)

                # Random các mặt của xúc xắc quy định chiều kim đồng hồ (xác suất luôn là 2/6 = 1/3)
                faces_list = ["1 hoặc 2", "5 hoặc 6", "1 hoặc 6"]
                faces = random.choice(faces_list)

                if faces == "1 hoặc 2":
                    cw_label = "1; 2"
                    ccw_label = "3; 4; 5; 6"
                elif faces == "5 hoặc 6":
                    cw_label = "5; 6"
                    ccw_label = "1; 2; 3; 4"
                elif faces == "1 hoặc 6":
                    cw_label = "1; 6"
                    ccw_label = "2; 3; 4; 5"

                # --- TÍNH TOÁN KẾT QUẢ ---
                valid_cases = []
                total_prob = Rational(0, 1)

                # Giải hệ phương trình x + y = N và y - x = 6m
                for m in range(-5, 6):
                    if (N + 6*m) % 2 == 0:
                        y = (N + 6*m) // 2
                        x = N - y
                        if 0 <= x <= N and 0 <= y <= N:
                            prob = math.comb(N, x) * (Rational(1, 3)**x) * (Rational(2, 3)**y)
                            valid_cases.append((m, x, y, prob))
                            total_prob += prob

                k = int(total_prob.p)
                den = int(total_prob.q)
                factors = factorint(den)
                M = factors.get(3, 0) # Lấy số mũ của 3 ở mẫu số

                # --- TẠO CÁC ĐÁP ÁN TRẮC NGHIỆM ---
                da = k
                offsets = [10, 20, 30, -10, -20, -30, 15, -15, 5, -5]
                random.shuffle(offsets)

                # Đảm bảo các phương án sai (distractors) không bị âm và khác nhau
                o1 = k + offsets[0]
                o2 = k + offsets[1]
                o3 = k + offsets[2]
                if o1 <= 0: o1 = k + 7
                if o2 <= 0: o2 = k + 11
                if o3 <= 0: o3 = k + 13

                du = ['$%s$' % (k)]
                da = random.choice(du)
                s = ['$%s$' % (o1), '$%s$' % (o2), '$%s$' % (o3)]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- HÌNH VẼ TIKZ ĐỀ BÀI ---
                tikz_question = '''\\begin{tikzpicture}[scale=1.2, line width=1pt]
                \\draw (0,0) circle (1cm);
                \\fill (0,0) circle (1.5pt) node[below] {$O$};
                \\fill (0,1) circle (1.5pt) node[above] {$P$};
            \\end{tikzpicture}'''

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = ('''\\immini{Trên đường tròn tâm $O$ bán kính bằng $1$ có một điểm $P$ chuyển động (như hình bên). Khi gieo một con xúc xắc, nếu số chấm xuất hiện là %s thì điểm $P$ chuyển động theo chiều kim đồng hồ một góc $60^\\circ$, còn trong các trường hợp khác thì điểm $P$ chuyển động theo chiều ngược chiều kim đồng hồ một góc $60^\\circ$. Khi gieo xúc xắc %s lần, xác suất để điểm $P$ trở về đúng vị trí ban đầu là $\\frac{k}{3^{%s}}$. Khi đó, giá trị của $k$ là bao nhiêu? (biết rằng $k$ là số tự nhiên).}
            {%s}''' % (faces, N, M, tikz_question))

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- CHUẨN BỊ CHUỖI LỜI GIẢI ĐỘNG ---
                cases_text = ""
                sum_expr_text = ""
                for m, x, y, prob in valid_cases:
                    cases_text += '''\\indent $\\bullet\\ m = %s \\Rightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases} \\Rightarrow \\text{Xác suất: } C_{%s}^{%s} \\left(\\frac{1}{3}\\right)^{%s} \\left(\\frac{2}{3}\\right)^{%s}$.\\\\''' % (m, x, y, N, x, x, y)
                    sum_expr_text += '''C_{%s}^{%s} \\left(\\frac{1}{3}\\right)^{%s} \\left(\\frac{2}{3}\\right)^{%s} + ''' % (N, x, x, y)

                sum_expr_text = sum_expr_text[:-3] # Xóa " + " dư ở cuối

                # --- HÌNH VẼ TIKZ LỜI GIẢI ---
                tikz_solution = '''\\begin{center}
            \\begin{tikzpicture}[scale=1.5, line width=1pt]
                \\draw (0,0) circle (1cm);
                \\fill (0,0) circle (1.5pt) node[below] {$O$};
                \\foreach \\a in {90, 30, -30, -90, -150, 150} {
                    \\fill ({cos(\\a)},{sin(\\a)}) circle (1.5pt);    }
                \\node[above] at (0,1) {$P$};
                \\node[right] at ({cos(30)},{sin(30)}) {$%s$};
                \\node[left] at ({cos(150)},{sin(150)}) {$%s$};
                \\draw[red] (0,0) -- (0,1);
                \\draw[red] (0,0) -- ({cos(30)},{sin(30)});
                \\draw[red] (0,0) -- ({cos(150)},{sin(150)});
                \\draw[<->, red] ({0.3*cos(90)},{0.3*sin(90)}) arc (90:30:0.3);
                \\node[red] at ({0.5*cos(60)},{0.5*sin(60)}) {$60^\\circ$};
                \\draw[<->, red] ({0.3*cos(90)},{0.3*sin(90)}) arc (90:150:0.3);
                \\node[red] at ({0.5*cos(120)},{0.5*sin(120)}) {$60^\\circ$};
            \\end{tikzpicture}
            \\end{center}''' % (cw_label, ccw_label)

                # --- NỘI DUNG LỜI GIẢI ---
                loigiai = ('''Khi gieo một con xúc xắc, xác suất xuất hiện %s chấm là: $\\frac{2}{6} = \\frac{1}{3}$.\\\\
            Khi gieo một con xúc xắc, xác suất xuất hiện các chấm còn lại là: $\\frac{4}{6} = \\frac{2}{3}$.\\\\
            %s
            Gọi $x$ là số lần điểm $P$ chuyển động theo chiều kim đồng hồ ($\\circlearrowright 60^\\circ$).\\\\
            Gọi $y$ là số lần điểm $P$ chuyển động ngược chiều kim đồng hồ ($\\circlearrowleft 60^\\circ$).\\\\
            Điều kiện: $x, y \\in \\mathbb{N}; 0 \\le x \\le %s, 0 \\le y \\le %s$.\\\\
            Từ giả thiết: $x + y = %s \\quad (1)$\\\\
            Sau $%s$ lần chuyển động, điểm $P$ trở về đúng vị trí ban đầu khi:\\\\
            $y \\cdot 60^\\circ - x \\cdot 60^\\circ = m \\cdot 360^\\circ$, với $m$ là số nguyên.\\\\
            Suy ra: $y - x = 6m \\quad (2)$\\\\
            Từ (1), (2) ta xét các giá trị $m$ có thể có:\\\\
            %s Vậy xác suất để điểm $P$ trở về đúng vị trí ban đầu là:\\\\
            $%s = \\frac{%s}{3^{%s}} = \\frac{k}{3^{%s}}$.\\\\
            Kết luận: $k = %s$.''' % (faces, tikz_solution, N, N, N, N, cases_text, sum_expr_text, k, M, M, k))
                dapan='\\shortans[0]{$%s$}\n'%(k)
                # --- XUẤT CÂU TRẮC NGHIỆM ---
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                    '\\loigiai{\n'+str(loigiai)+'}\n'
                    '\\end{ex}\n\\end{minipage} \n\n')
            return content

