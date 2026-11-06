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


def bt_dang5_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khởi tạo các giá trị ngẫu nhiên======================================================================================
            a = random.randint(-6, 2)
            b = random.randint(a + 4, a + 7)
            m = random.randint(-9, 9)
            n = random.choice([x for x in range(-9, 9) if abs(m - x) > 3])
            nho, lon = min(m, n), max(m, n)
            c = random.choice([j for j in range(-9, 9) if j != 0])
            d = random.randint(-9, -1) if c > 0 else random.randint(1, 9)

            # Phần linh hoạt cho 2 kiểu BBT
            p = random.choice([['+', '-', '+', '-', '-', '+', lon, '-', nho, '+', '+'], ['-', '+', '-', '+', '+', '-', nho, '+', lon, '-', '-']]) 
            BBT = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[scale=1,transform shape]
                    \\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]
                    {{$x$/.6,$f'(x)$/.6,$f(x)$/1.8}}
                    {{$-\\infty$,${a}$,${b}$,$+\\infty$}}
                    \\tkzTabLine{{,{p[0]},d,{p[1]},0,{p[2]},}}
                    \\tkzTabVar{{{p[3]}/${p[4]}\\infty$,{p[5]}/${p[6]}$,{p[7]}/${p[8]}$,{p[9]}/${p[10]}\\infty$}}
                \\end{{tikzpicture}}
                \\end{{center}}'''
            BBT = BBT.replace("-+","-").replace("+-","-")
            # Đề bài
            de_bai = f""" Cho hàm số $y = f(x)$ liên tục trên $\\mathbb{{R}}$ và có bảng biến thiên như sau:\n {BBT}"""

            giai_chung = " " # Có thì viết, ngược lại không có lời giải chung thì cho bằng string-rỗng = ""

            # Danh sách câu hỏi. 
            '''CHÚ THÍCH: Có thể viết nhiều nhóm, để vào trong list ds_abcd phía dưới.
             Mỗi nhóm gồm 4 ý phát biểu a) b) c) d) = ứng với 4 list.
             Trong mỗi list có 2 tuple:
               +) Tuple thứ nhất chứa các ý phát biểu cùng đề cập một vấn đề, vừa có đúng vừa có sai.
               +) Tuple thứ hai chứa lời giải của phát biểu ở tuple thứ nhất.'''

            nhom_1 = (
                [(f"""\\True Hàm số $y = f(x)$ đạt cực đại tại điểm $x = {a}$""", 
                    f"""\\True Hàm số $y = f(x)$ đạt cực tiểu tại điểm $x = {b}$""", 
                    f""" Hàm số $y = f(x)$ đạt cực đại tại điểm $x = {b}$""", 
                    f""" Hàm số $y = f(x)$ đạt cực tiểu tại điểm $x = {a}$""", 
                    ),
                (f"""Vì hàm số $y = f(x)$ liên tục trên $\\mathbb{{R}}$ nên từ bảng biến thiên, ta suy ra hàm số đạt cực đại tại $x = {a}$ và đạt cực tiểu tại $x = {b}$.""")
                ],

                [(f"""\\True $f({latex(a+1)}) > f({latex(b-1)})$""", 
                    f""" $f({latex(a+1)}) < f({latex(b-1)})$"""
                    ),
                (f"""Hàm số $y = f(x)$ nghịch biến trên khoảng $({a+1}; {b-1})$ nên $f({latex(a+1)}) > f({latex(b-1)})$.""")
                ],

                [(f"""\\True Phương trình $f(x) = {random.randint(nho + 1, lon - 1)}$ có $3$ nghiệm phân biệt """, 
                    f"""\\True Phương trình $f(x) = {random.choice([nho, lon])}$ có $2$ nghiệm phân biệt """,
                    f"""\\True Phương trình $f(x) = {random.randint(nho - 5, nho - 1)}$ có $1$ nghiệm duy nhất""", 
                    f"""\\True Phương trình $f(x) = {random.randint(lon + 1, lon + 5)}$ có $1$ nghiệm duy nhất""", 
                    f""" Phương trình $f(x) = {random.randint(nho + 1, lon - 1)}$ có $2$ nghiệm phân biệt """, 
                    f""" Phương trình $f(x) = {random.choice([nho, lon])}$ có $1$ nghiệm duy nhất """,
                    f""" Phương trình $f(x) = {random.randint(nho - 5, nho - 1)}$ có $3$ nghiệm phân biệt""", 
                    f""" Phương trình $f(x) = {random.randint(lon + 1, lon + 5)}$ có $3$ nghiệm phân biệt""", 
                    ),
                (f"""Dựa vào bảng biến thiên, so sánh vế phải với các giá trị cực trị để suy ra số nghiệm của phương trình đã cho. """)
                ],

                [(f"""\\True Giá trị {'lớn' if d > 0 else 'nhỏ'} nhất của hàm số $g(x) = {c}f(x) {'' if d < 0 else '+'} {latex(d*x)} $ trên đoạn $[{a+1}; {b-1}]$ là ${c}f({b-1}) + {d*(b-1)}$""".replace('+ -', '-').replace('1f', 'f').replace('+ 0', ''),
                f"""\\True Giá trị {'nhỏ' if d > 0 else 'lớn'} nhất của hàm số $g(x) = {c}f(x) {'' if d < 0 else '+'} {latex(d*x)} $ trên đoạn $[{a+1}; {b-1}]$ là ${c}f({a+1}) + {d*(a+1)}$""".replace('+ -', '-').replace('1f', 'f').replace('+ 0', ''),  
                    f""" Giá trị {'lớn' if d < 0 else 'nhỏ'} nhất của hàm số $g(x) = {c}f(x) {'' if d < 0 else '+'} {latex(d*x)} $ trên đoạn $[{a+1}; {b-1}]$ là ${c}f({b-1}) + {d*(b-1)}$""".replace('+ -', '-').replace('1f', 'f').replace('+ 0', ''),
                f""" Giá trị {'nhỏ' if d < 0 else 'lớn'} nhất của hàm số $g(x) = {c}f(x) {'' if d < 0 else '+'} {latex(d*x)} $ trên đoạn $[{a+1}; {b-1}]$ là ${c}f({a+1}) + {d*(a+1)}$""".replace('+ -', '-').replace('1f', 'f').replace('+ 0', ''),  
                    ),
                ( f"""Trên đoạn $[{a+1}; {b-1}]$ thì $g'(x) = {c}f'(x) {'' if d < 0 else '+'} {d} {'>' if d > 0 else '<'} 0$ do $f'(x) < 0$.\\\\
                        Suy ra trên đoạn $[{a+1}; {b-1}]$ hàm số $g(x)$ {'đồng' if d > 0 else 'nghịch'} biến.\\\\
                        Do đó ${'\\max' if d > 0 else '\\min'}\\limits_{{[{a+1}; {b-1}]}}g(x) = {c}f({b-1}) + {d*(b-1)}$ 
                           và ${'\\min' if d > 0 else '\\max'}\\limits_{{[{a+1}; {b-1}]}}g(x) = {c}f({a+1}) + {d*(a+1)}$.  """.replace('+ -', '-').replace('1f', 'f').replace('+ 0', '')
                   )
                ]
            )

            nhom_2 = (
                [(f"""\\True Hàm số $y = f(x)$ đạt cực đại tại điểm $x = {b}$""", 
                    f"""\\True Hàm số $y = f(x)$ đạt cực tiểu tại điểm $x = {a}$""", 
                    f""" Hàm số $y = f(x)$ đạt cực đại tại điểm $x = {a}$""", 
                    f""" Hàm số $y = f(x)$ đạt cực tiểu tại điểm $x = {b}$""", 
                    ),
                (f"""Vì hàm số $y = f(x)$ liên tục trên $\\mathbb{{R}}$ nên từ bảng biến thiên, ta suy ra hàm số đạt cực đại tại $x = {b}$ và đạt cực tiểu tại $x = {a}$.""")
                ],

                [(f"""\\True $f({latex(b+1)}) > f({latex(b+4)})$""", 
                    f"""\\True $f({latex(a-4)}) > f({latex(a-1)})$""", 
                    f""" $f({latex(b+1)}) < f({latex(b+4)})$""",
                    f"""$f({latex(a-4)}) < f({latex(a-1)})$""", 
                    ),
                (f"""Hàm số $y = f(x)$ nghịch biến trên khoảng $({b+1}; {b+4})$ nên $f({latex(b+1)}) > f({latex(b+4)})$.""")
                ],

                [(f"""\\True Phương trình $f(x) = {random.randint(nho + 1, lon - 1)}$ có $3$ nghiệm phân biệt """, 
                    f"""\\True Phương trình $f(x) = {random.choice([nho, lon])}$ có $2$ nghiệm phân biệt """,
                    f"""\\True Phương trình $f(x) = {random.randint(nho - 5, nho - 1)}$ có $1$ nghiệm duy nhất""", 
                    f"""\\True Phương trình $f(x) = {random.randint(lon + 1, lon + 5)}$ có $1$ nghiệm duy nhất""", 
                    f""" Phương trình $f(x) = {random.randint(nho + 1, lon - 1)}$ có $2$ nghiệm phân biệt """, 
                    f""" Phương trình $f(x) = {random.choice([nho, lon])}$ có $1$ nghiệm duy nhất """,
                    f""" Phương trình $f(x) = {random.randint(nho - 5, nho - 1)}$ có $3$ nghiệm phân biệt""", 
                    f""" Phương trình $f(x) = {random.randint(lon + 1, lon + 5)}$ có $3$ nghiệm phân biệt""", 
                    ),
                (f"""Dựa vào bảng biến thiên, so sánh vế phải với các giá trị cực trị để suy ra số nghiệm của phương trình đã cho. """)
                ],

                [(f"""\\True Giá trị {'lớn' if d > 0 else 'nhỏ'} nhất của hàm số $g(x) = {c}f(x) {'' if d < 0 else '+'} {latex(d*x)} $ trên đoạn $[{b+1}; {b+4}]$ là ${c}f({b+4}) + {d*(b+4)}$""".replace('+ -', '-').replace('1f', 'f').replace('+ 0', ''),
                f"""\\True Giá trị {'nhỏ' if d > 0 else 'lớn'} nhất của hàm số $g(x) = {c}f(x) {'' if d < 0 else '+'} {latex(d*x)} $ trên đoạn $[{b+1}; {b+4}]$ là ${c}f({b+1}) + {d*(b+1)}$""".replace('+ -', '-').replace('1f', 'f').replace('+ 0', ''),  
                    f""" Giá trị {'lớn' if d < 0 else 'nhỏ'} nhất của hàm số $g(x) = {c}f(x) {'' if d < 0 else '+'} {latex(d*x)} $ trên đoạn $[{b+1}; {b+4}]$ là ${c}f({b+4}) + {d*(b+4)}$""".replace('+ -', '-').replace('1f', 'f').replace('+ 0', ''),
                f""" Giá trị {'nhỏ' if d < 0 else 'lớn'} nhất của hàm số $g(x) = {c}f(x) {'' if d < 0 else '+'} {latex(d*x)} $ trên đoạn $[{b+1}; {b+4}]$ là ${c}f({b+1}) + {d*(b+1)}$""".replace('+ -', '-').replace('1f', 'f').replace('+ 0', ''),  
                    ),
                ( f"""Trên đoạn $[{b+1}; {b+4}]$ thì $g'(x) = {c}f'(x) {'' if d < 0 else '+'} {d} {'>' if d > 0 else '<'} 0$ do $f'(x) < 0$.\\\\
                        Suy ra trên đoạn $[{b+1}; {b+4}]$ hàm số $g(x)$ {'đồng' if d > 0 else 'nghịch'} biến.\\\\
                        Do đó ${'\\max' if d > 0 else '\\min'}\\limits_{{[{b+1}; {b+4}]}}g(x) = {c}f({b+4}) + {d*(b+4)}$ 
                           và ${'\\min' if d > 0 else '\\max'}\\limits_{{[{b+1}; {b+4}]}}g(x) = {c}f({b+1}) + {d*(b+1)}$.  """.replace('+ -', '-').replace('1f', 'f').replace('+ 0', '')
                   )
                ]
            )

            # Đưa các nhóm câu hỏi vào để chọn phù hợp. Nếu các nhóm bình đẳng thì choice, ngược lại thì if ... else ...
            ds_abcd = nhom_1 if p[0] == '+' else nhom_2


            # ĐƯA NỘI DUNG VÀO FORM - Không can thiệp vào phần dưới đây ===========================================================================
            ds_hoi = [random.choice(ds_abcd[i][0]) for i in range(len(ds_abcd))]

            while all(["True" in ds_hoi[0], "True" in ds_hoi[1], "True" in ds_hoi[2], "True" in ds_hoi[3]]) or all(["True" not in ds_hoi[0], "True" not in ds_hoi[1], "True" not in ds_hoi[2], "True" not in ds_hoi[3]]):
                ds_hoi = [random.choice(ds_abcd[i][0]) for i in range(len(ds_abcd))]

            giai_a = ('Đúng. ' if 'True' in ds_hoi[0] else 'SAI. ') + ds_abcd[0][1]
            giai_b = ('Đúng. ' if 'True' in ds_hoi[1] else 'SAI. ') + ds_abcd[1][1]
            giai_c = ('Đúng. ' if 'True' in ds_hoi[2] else 'SAI. ') + ds_abcd[2][1]
            giai_d = ('Đúng. ' if 'True' in ds_hoi[3] else 'SAI. ') + ds_abcd[3][1]

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(de_bai)+ 
                '\\choiceTFn \n'
                '{' + ds_hoi[0] + '}\n'
                '{' + ds_hoi[1] + '}\n'
                '{' + ds_hoi[2] + '}\n'
                '{' + ds_hoi[3] + '}\n'
                '\\loigiai{ \n' + giai_chung + '\n'
                '\\begin{itemchoice} \n'
                '\\itemch ' + giai_a + '\n'
                '\\itemch ' + giai_b + '\n'
                '\\itemch ' + giai_c + '\n'
                '\\itemch ' + giai_d + '\n'
                '\\end{itemchoice}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

