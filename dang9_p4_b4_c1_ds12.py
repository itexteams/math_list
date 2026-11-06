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


def bt_dang9_p4_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Danh sách các cấu hình thông số ngẫu nhiên đảm bảo tính toán đẹp và nghiệm nguyên
                configs = [
                    {
                        'OA': Rational(15, 8),
                        'AB': Rational(9, 8),
                        'h_doi': 243
                    },
                    {
                        'OA': Rational(15, 8),
                        'AB': Rational(9, 8),
                        'h_doi': 486
                    },
                    {
                        'OA': Rational(15, 4),
                        'AB': Rational(9, 4),
                        'h_doi': 972
                    },
                    {
                        'OA': Rational(15, 4),
                        'AB': Rational(9, 4),
                        'h_doi': 243
                    },
                    {
                        'OA': Rational(3, 4),
                        'AB': Rational(5, 4),
                        'h_doi': 100
                    },
                    {
                        'OA': Rational(9, 4),
                        'AB': Rational(15, 4),
                        'h_doi': 400
                    },
                    {
                        'OA': Rational(2, 1),
                        'AB': Rational(7, 4),
                        'h_doi': 1225
                    }
                ]

                cfg = random.choice(configs)
                OA = cfg['OA']
                AB = cfg['AB']
                h_doi = cfg['h_doi']

                xB = OA + AB

                # Biến số và hàm số
                f_poly = x * (x - OA) * (x - xB)
                f_exp = sp.expand(f_poly)
                df_exp = sp.diff(f_exp, x)

                # Tìm hoành độ các điểm cực trị
                x_roots = sp.solve(df_exp, x)
                x1 = x_roots[0] # Hoành độ ngọn đồi (cực đại)
                x2 = x_roots[1] # Hoành độ đáy hồ (cực tiểu)

                val1 = f_poly.subs(x, x1)
                val2 = f_poly.subs(x, x2)

                h_doi_km = Rational(h_doi, 1000)
                k = h_doi_km / val1

                f_x2 = k * val2
                kq_m = abs(int(f_x2 * 1000)) # Kết quả độ sâu tính bằng mét

                # Đáp án đúng
                du = ['$%s$' % (kq_m)]
                da = random.choice(du)

                # Tạo các đáp án sai
                s_set = set([
                    '$%s$' % (kq_m + 50),
                    '$%s$' % (kq_m + 100),
                    '$%s$' % (kq_m + 150),
                    '$%s$' % (abs(kq_m - 50)) if abs(kq_m - 50) > 0 else '$%s$' % (kq_m + 200),
                    '$%s$' % (abs(kq_m - 100)) if abs(kq_m - 100) > 0 else '$%s$' % (kq_m + 250),
                    '$%s$' % (h_doi)
                ])
                s_set.discard(da)
                s = list(s_set)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # TikZ vẽ hình minh họa
                tikz_str = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, x=1.2cm, y=1.2cm, scale=0.9]
            \\draw[->] (-0.6,0) -- (4.2,0) node[below] {$x$};
            \\draw[->] (0,-1.2) -- (0,2.2) node[right] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\fill[pattern=dots, pattern color=gray!80] 
              plot[domain=0:1.875, smooth] (\\x, {0.8*\\x*(\\x-1.875)*(\\x-3)}) -- (1.875,0) -- (0,0) -- cycle;
            \\fill[blue!20] 
              plot[domain=1.875:3, smooth] (\\x, {0.8*\\x*(\\x-1.875)*(\\x-3)}) -- (3,0) -- (1.875,0) -- cycle;
            \\fill[pattern=dots, pattern color=gray!80] 
              (3,0) -- plot[domain=3:3.6, smooth] (\\x, {0.8*\\x*(\\x-1.875)*(\\x-3)}) -- (3.6,0) -- cycle;
            \\draw[red!80!black, line width=1pt, domain=-0.2:3.6, smooth] 
              plot (\\x, {0.8*\\x*(\\x-1.875)*(\\x-3)});
            \\fill (0,0) circle (1.5pt);
            \\fill (1.875,0) circle (1.5pt) node[above right] {$A$};
            \\fill (3,0) circle (1.5pt) node[above right] {$B$};
            \\node at (-0.4,0.2) {Biển};
            \\node at (0.75,1.2) {Đồi};
            \\node at (2.4375,-1) {Hồ};
            \\node at (3.6,0.6) {Núi};
            \\end{tikzpicture}
            \\end{center}''')

                # Nội dung câu hỏi
                noidungcauhoi = ('''Lát cắt ngang của một vùng đất ven biển được mô hình hóa thành một hàm số bậc ba $y = f(x)$ có đồ thị như hình vẽ (đơn vị trên các trục là $km$). Biết khoảng cách hai bên chân đồi $OA = %s$ km, độ rộng của hồ $AB = %s$ km và chiều cao của ngọn đồi là $%s$ m. Tính độ sâu của hồ tại điểm sâu nhất theo đơn vị mét.
            %s'''
                                 % (
                                     latex(OA).replace('.', ','),
                                     latex(AB).replace('.', ','),
                                     latex(h_doi),
                                     tikz_str
                                 ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Tọa độ các giao điểm của đồ thị với trục hoành là $O(0; 0)$, $A(%s; 0)$ và $B(%s; 0)$ (vì $x_B = OA + AB = %s + %s = %s$).\\\\
            Do đồ thị hàm số bậc ba $y = f(x)$ đi qua gốc tọa độ $O$ và cắt trục hoành tại $A$, $B$ nên hàm số có dạng:\\\\
            $f(x) = kx(x - %s)(x - %s) = k\\left(%s\\right)$ (với $k > 0$).\\\\
            Đạo hàm:\\\\
            $f'(x) = k\\left(%s\\right)$.\\\\
            Cho $f'(x) = 0 \\iff %s = 0 \\iff \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$\\\\
            Đỉnh ngọn đồi ứng với điểm cực đại của hàm số tại hoành độ $x = %s \\in (0; %s)$.\\\\
            Chiều cao của ngọn đồi là $%s$ m = $%s$ km.\\\\
            Do đó $f(%s) = %s \\iff k \\cdot \\left(%s\\right) = %s \\iff k = %s$.\\\\
            Suy ra $f(x) = %s \\cdot \\left(%s\\right)$.\\\\
            Độ sâu lớn nhất của hồ ứng với điểm cực tiểu của hàm số tại hoành độ $x = %s \\in (%s; %s)$.\\\\
            Giá trị cực tiểu tại điểm sâu nhất của hồ là:\\\\
            $f(%s) = %s \\cdot \\left(%s\\right) = %s$ km = $%s$ mét.\\\\
            Vậy độ sâu của hồ tại điểm sâu nhất bằng $%s$ mét.'''
                           % (
                               latex(OA).replace('.', ','),
                               latex(xB).replace('.', ','),
                               latex(OA).replace('.', ','),
                               latex(AB).replace('.', ','),
                               latex(xB).replace('.', ','),
                               latex(OA).replace('.', ','),
                               latex(xB).replace('.', ','),
                               latex(f_exp).replace('.', ','),
                               latex(df_exp).replace('.', ','),
                               latex(df_exp).replace('.', ','),
                               latex(x1).replace('.', ','),
                               latex(x2).replace('.', ','),
                               latex(x1).replace('.', ','),
                               latex(OA).replace('.', ','),
                               latex(h_doi),
                               latex(h_doi_km).replace('.', ','),
                               latex(x1).replace('.', ','),
                               latex(h_doi_km).replace('.', ','),
                               latex(val1).replace('.', ','),
                               latex(h_doi_km).replace('.', ','),
                               latex(k).replace('.', ','),
                               latex(k).replace('.', ','),
                               latex(f_exp).replace('.', ','),
                               latex(x2).replace('.', ','),
                               latex(OA).replace('.', ','),
                               latex(xB).replace('.', ','),
                               latex(x2).replace('.', ','),
                               latex(k).replace('.', ','),
                               latex(val2).replace('.', ','),
                               latex(f_x2).replace('.', ','),
                               latex(f_x2 * 1000).replace('.', ','),
                               latex(kq_m).replace('.', ',')
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

