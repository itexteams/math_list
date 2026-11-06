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


def bt_dang24_p3_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tọa độ các đỉnh để tạo thành tứ giác lồi OEAC
                # O(0,0), E(xE, 0), C(0, yC), A(xA, yA)
                xE = random.randint(1, 4)
                yC = random.randint(3, 7)
                xA = xE + random.randint(1, 3)
                yA = random.randint(1, yC - 1)

                # Lập phương trình đường thẳng đi qua E(xE, 0) và A(xA, yA): a1*x + b1*y + c1 = 0
                a1 = yA
                b1 = -(xA - xE)
                c1 = -yA * xE
                g1 = math.gcd(math.gcd(abs(a1), abs(b1)), abs(c1))
                a1 //= g1; b1 //= g1; c1 //= g1

                # Lập phương trình đường thẳng đi qua C(0, yC) và A(xA, yA): a2*x + b2*y + c2 = 0
                a2 = yC - yA
                b2 = xA
                c2 = -xA * yC
                g2 = math.gcd(math.gcd(abs(a2), abs(b2)), abs(c2))
                a2 //= g2; b2 //= g2; c2 //= g2

                # Hàm định dạng phương trình đẹp (xử lý +- và hệ số 1)
                def format_eq(a, b, c):
                    terms = []
                    if a == 1: terms.append("x")
                    elif a == -1: terms.append("-x")
                    elif a != 0: terms.append(f"{a}x")

                    if b == 1: terms.append("+y" if a != 0 else "y")
                    elif b == -1: terms.append("-y")
                    elif b > 0: terms.append(f"+{b}y" if a != 0 else f"{b}y")
                    elif b < 0: terms.append(f"{b}y")

                    if c > 0: terms.append(f"+{c}")
                    elif c < 0: terms.append(f"{c}")

                    res = "".join(terms)
                    if res.startswith("+"): res = res[1:]
                    return res + " \\le 0"

                eq1 = format_eq(a1, b1, c1)
                eq2 = format_eq(a2, b2, c2)

                # Tính diện tích (Bằng tổng diện tích 2 tam giác OEA và OAC)
                S = 0.5 * (xE * yA + yC * xA)

                # Định dạng kết quả (nếu là số nguyên thì bỏ .0, nếu số thập phân thì dùng dấu phẩy)
                if S == int(S):
                    kq_str = str(int(S))
                else:
                    kq_str = str(S).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = [f'${kq_str}$']
                da = random.choice(du)


                # Câu hỏi
                noidungcauhoi = (f'''Các số $x$ và $y$ thỏa mãn hệ bất phương trình 
            $\\begin{{cases}} x \\ge 0 \\\\ y \\ge 0 \\\\ {eq1} \\\\ {eq2} \\end{{cases}}$. 
            Miền nghiệm của hệ bất phương trình là hình phẳng có diện tích bằng bao nhiêu?''')



                # Tạo mã TikZ vẽ hình cho lời giải
                # Chú ý: scale=0.8 được giữ nguyên dấu chấm để TikZ không báo lỗi
                tikz = f'''\\begin{{center}}
                \\begin{{tikzpicture}}[>=stealth, scale=0.8, line width=1pt]
                \\draw[->] (-1,0) -- ({xA + 2},0) node[below] {{$x$}};
                \\draw[->] (0,-1) -- (0,{yC + 1}) node[left] {{$y$}};
                \\node at (0,0) [below left] {{$O$}};
                \\clip (-1,-1) rectangle ({xA + 1.5},{yC + 0.5});
                \\fill[pattern=north east lines, pattern color=black] (-1,-1) rectangle ({xA + 1.5},{yC + 0.5});
                \\fill[white] (0,0) -- ({xE},0) -- ({xA},{yA}) -- (0,{yC}) -- cycle;
                \\draw[black] (-1,0) -- ({xA + 2},0);
                \\draw[black] (0,-1) -- (0,{yC + 1});
                \\draw[black, smooth, domain=-1:{xA+1.5}] plot(\\x, {{-({a1}/{b1})*\\x - {c1}/{b1}}});
                \\draw[black, smooth, domain=-1:{xA+1.5}] plot(\\x, {{-({a2}/{b2})*\\x - {c2}/{b2}}});
                \\coordinate (E) at ({xE},0);
                \\coordinate (A) at ({xA},{yA});
                \\coordinate (C) at (0,{yC});
                \\fill (0,0) circle (1pt);
                \\fill (E) circle (1pt) node[below] {{$E({xE};0)$}};
                \\fill (A) circle (1pt) node[above right] {{$A({xA};{yA})$}};
                \\fill (C) circle (1pt) node[left] {{$C(0;{yC})$}};
                \\draw[dashed, thin] ({xA},0) -- (A) -- (0,{yA});
                \\end{{tikzpicture}}
                \\end{{center}}'''

                eq1_d1 = eq1.replace(' \\le 0', ' = 0')
                eq2_d2 = eq2.replace(' \\le 0', ' = 0')

                # Xử lý các giá trị diện tích lẻ chuyển sang dấu phẩy trước khi ghép chuỗi
                val_S1 = f"{0.5 * xE * yA:g}".replace('.', ',')
                val_S2 = f"{0.5 * yC * xA:g}".replace('.', ',')

                # Nội dung lời giải (Đã bỏ lệnh .replace() ở cuối chuỗi)
                loigiai = (f'''Vẽ đường thẳng $d_1: {eq1_d1}$, $d_1$ qua $E({xE}; 0)$ và $A({xA}; {yA})$.\\\\
            Vẽ đường thẳng $d_2: {eq2_d2}$, $d_2$ qua $C(0; {yC})$ và $A({xA}; {yA})$.\\\\
            Miền nghiệm của hệ bất phương trình là tứ giác $OEAC$ với $O(0;0), E({xE}; 0), A({xA}; {yA}), C(0; {yC})$.
            {tikz}
            Ta chia tứ giác $OEAC$ thành hai tam giác $OEA$ và $OAC$.\\\\
            Diện tích tam giác $OEA$ (với đáy $OE$ và chiều cao tương ứng là $y_A$) bằng $S_1 = \\frac{{1}}{{2}} \\cdot {xE} \\cdot {yA} = {val_S1}$.\\\\
            Diện tích tam giác $OAC$ (với đáy $OC$ và chiều cao tương ứng là $x_A$) bằng $S_2 = \\frac{{1}}{{2}} \\cdot {yC} \\cdot {xA} = {val_S2}$.\\\\
            Do đó diện tích tứ giác $OEAC$ là $S = S_1 + S_2 = {val_S1} + {val_S2} = {kq_str}$.''')

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_str))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

