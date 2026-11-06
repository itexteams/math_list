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


def bt_dang6_p3_b2_c2_ds10(self):
            # Khai báo biến
            # Định nghĩa hàm
            def hien_phan_so(t):
                m=Rational(t).limit_denominator(1000000000000)
                return m
            def lam_tron(number, digits):
                decimal_number = Decimal(str(number))
                return decimal_number.quantize(Decimal(10) ** -digits, rounding=ROUND_HALF_UP)
            def hien_phan_thuc(t):
                t = sp.nsimplify(t)
                if t.is_rational:
                    return latex(Rational(t))
                else:
                    return latex(t)
            def is_integer(number):
                return isinstance(number, int)
            def tach_phan_nguyen_va_phan_thap(num):
                # Tách phần nguyên
                phan_nguyen = int(num)
                # Tách phần thập phân
                phan_thap_phan = num - phan_nguyen
                return phan_nguyen, phan_thap_phan
            def key(so):
                # Kiểm tra nếu số là số nguyên
                if isinstance(so, int) or (isinstance(so, float) and so.is_integer()):
                    return str(int(so))  # Chuyển đổi thành chuỗi mà không làm tròn

                # Nếu không phải số nguyên, thực hiện các thao tác ban đầu
                txt = str(float(lam_tron(so, 1))) if len(str(float(lam_tron(so, 2)))) > 4 else str(float(lam_tron(so, 2)))
                return txt.replace('.', ',')
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                #Khai báo biến
                x, y = symbols('x y')
                while True:
                    # Tạo ngẫu nhiên các hệ số
                    a1 = 1
                    b1 = 1
                    c1 = random.randint(20, 100)
                    a2 = random.randint(5, 10)
                    b2 = random.randint(5, 10)
                    c2 = b2*random.randint(5, 33)
                    loinhuan_A=random.randint(2, 4)
                    loinhuan_B=loinhuan_A+random.randint(1, 2)
                    # Giải hệ phương trình
                    nghiem = sp.solve([sp.Eq(a1*x + b1*y, c1), sp.Eq(a2*x + b2*y, c2)], (x, y))

                    # Kiểm tra xem nghiệm có tồn tại và có phải là số nguyên dương không
                    if c2/a2 > c1 and c2/b2 < c1 and (c1/a1).is_integer and (c2/b2).is_integer and nghiem and all(n.is_integer and n > 0 for n in (nghiem[x], nghiem[y])):
                        break
                ymax = max(c1/b1, c2/b2)
                ymin = min(c1/b1, c2/b2)
                xmax = max(c1/a1, c2/a2)
                xmin = min(c1/a1, c2/a2)
                # Xuất ra mã TikZ
                tikz_code = f'''\\begin{{center}}
                \\begin{{tikzpicture}}[>=stealth, scale=0.8, line width=1pt]
                    \\draw[->] (-1, 0) -- ({hien_phan_so(xmax/10 + 2)}, 0) node[below] {{$x$}};
                    \\draw[->] (0, -1) -- (0, {hien_phan_so(ymax/10 + 2)}) node[left] {{$y$}};
                    \\node at (0,0) [below left] {{$O$}};
                    \\clip (-1,-1) rectangle ({hien_phan_so(xmax/10 + 1)}, {hien_phan_so(ymax/10 + 1)});
                    \\fill[pattern=north east lines, pattern color=black] (-1,-1) rectangle ({hien_phan_so(xmax/10 + 1)}, {hien_phan_so(ymax/10 + 1)});
                    \\fill[white] (0,0) -- ({hien_phan_so(c1/(10*a1))},0) -- ({hien_phan_so(nghiem[x]/10)},{hien_phan_so(nghiem[y]/10)}) -- (0,{hien_phan_so(c2/(10*b2))}) -- cycle;
                    \\draw[black] (-1,0) -- ({hien_phan_so(xmax/10 + 2)},0);
                    \\draw[black] (0,-1) -- (0,{hien_phan_so(ymax/10 + 2)});
                    \\draw[black, smooth, domain=-1:{hien_phan_so(xmax/10 + 1)}] plot(\\x, {{-({a1}/{b1})*\\x+{hien_phan_so(c1/(10*b1))}}});
                    \\draw[black, smooth, domain=-1:{hien_phan_so(xmax/10 + 1)}] plot(\\x, {{-({a2}/{b2})*\\x+{hien_phan_so(c2/(10*b2))}}});
                    \\coordinate (A) at ({hien_phan_so(c1/(10*a1))},0);
                    \\coordinate (B) at ({hien_phan_so(nghiem[x]/10)},{hien_phan_so(nghiem[y]/10)});
                    \\coordinate (C) at (0,{hien_phan_so(c2/(10*b2))});
                    \\fill (0,0) circle (0.5pt);
                    \\fill (A) circle (0.5pt) node[above right] {{$A$}};
                    \\fill (B) circle (0.5pt) node[above right] {{$B$}};
                    \\fill (C) circle (0.5pt) node[above right] {{$C$}};
                    \\draw[dashed, thin] ({hien_phan_so(nghiem[x]/10)},0) -- (B) -- (0,{hien_phan_so(nghiem[y]/10)});
                \\end{{tikzpicture}}
                \\end{{center}}'''
                # In ra phương trình và mã TikZ
                #print(f"Hệ phương trình:\n${a1} x + {b1} y = {c1}$\\\\")
                #print(f"${a2} x + {b2} y = {c2}$\\\\")
                #print(nghiem[x], nghiem[y])
                #print(tikz_code)

                # Khai báo hàm F và các điểm A, B, C, D, E
                def F(x, y):
                    return 2*loinhuan_A * x + 2*loinhuan_B * y

                # Danh sách các điểm với tọa độ tương ứng
                points = {
                    "A": (c1/a1, 0),
                    "B": (nghiem[x], nghiem[y]),
                    "C": (0, c2/b2),
                }

                # Tính giá trị của F tại mỗi điểm và tìm giá trị lớn nhất, nhỏ nhất
                max_F = None
                min_F = None
                point_max = None
                point_min = None
                coords_max = None  # Lưu tọa độ khi F đạt giá trị lớn nhất
                coords_min = None  # Lưu tọa độ khi F đạt giá trị nhỏ nhất

                for point, (x, y) in points.items():
                    value = F(x, y)

                    # Cập nhật giá trị lớn nhất và điểm tương ứng
                    if max_F is None or value > max_F:
                        max_F = value
                        point_max = point
                        coords_max = (x, y)

                    # Cập nhật giá trị nhỏ nhất và điểm tương ứng
                    if min_F is None or value < min_F:
                        min_F = value
                        point_min = point
                        coords_min = (x, y)

                # Kết quả
                #print(f"Giá trị F lớn nhất là {hien_phan_so(max_F)} tại điểm {point_max} với x = {hien_phan_so(coords_max[0])} và y = {hien_phan_so(coords_max[1])}")
                #print(f"Giá trị F nhỏ nhất là {hien_phan_so(min_F)} tại điểm {point_min} với x = {hien_phan_so(coords_min[0])} và y = {hien_phan_so(coords_min[1])}")
                von_ban_dau=key(2*c2/1000)
                kq = key(coords_max[1]).replace(",0","")

                # Câu hỏi
                noidungcauhoi=f"""Một đại lý xe máy có kế hoạch nhập về hai dòng xe máy $A$ và $B$, 
                giá mỗi chiếc lần lượt là ${hien_phan_so(2*a2)}$ triệu đồng và ${hien_phan_so(2*b2)}$ triệu đồng 
                với số vốn ban đầu không vượt quá ${von_ban_dau}$ tỉ đồng. 
                Xe máy $A$ mang lợi nhuận ${hien_phan_so(2*loinhuan_A)}$ triệu đồng cho mỗi chiếc 
                và xe máy $B$ mang lợi nhuận ${hien_phan_so(2*loinhuan_B)}$ triệu đồng cho mỗi chiếc. 
                Đại lý ước tính rằng tổng nhu cầu hàng tháng sẽ không vượt quá ${hien_phan_so(c1)}$ chiếc cả hai loại. 
                Chủ đại lý cần đầu tư kinh doanh bao nhiêu chiếc loại $B$ để thu được lợi nhuận lớn nhất?"""
                # Nội dung lời giải
                loigiai=f'''Gọi số xe máy loại $A$ và $B$ cần đầu tư lần lượt là $x$ và $y$. ($x, y\\in\\mathbb{{N}}$).\\\\
                    Do tổng số vốn ban đầu không vượt quá ${von_ban_dau}$ tỉ đồng nên ta có $${hien_phan_so(2*a2)}\\cdot 10^6x+{hien_phan_so(2*b2)}\\cdot 10^6y\\leq {von_ban_dau}\\cdot 10^9
                    \\Leftrightarrow {a2} x + {b2} y  \\leq {c2}.$$
                    Vì tổng nhu cầu hàng tháng sẽ không vượt quá ${hien_phan_so(c1)}$ chiếc cả hai loại nên $x+y\\leq {hien_phan_so(c1)}$.\\\\
                    Lợi nhuận thu được là $F={2*loinhuan_A}\\cdot 10^6x+{2*loinhuan_B}\\cdot 10^6y=2\\cdot10^6\\cdot({loinhuan_A}x+{loinhuan_B}y) $.\\\\
                    Ta có hệ bất phương trình $\\heva{{&x+y\\leq {hien_phan_so(c1)}\\\\&{a2} x + {b2} y \\leq {c2}\\\\&x\\geq 0\\\\&y\\geq 0.}} $
                    {tikz_code}
                    Miền nghiệm của hệ bất phương trình là miền tứ giác $OABC$ kể cả các cạnh của tứ giác. 
                    Trong đó: $O(0;0)$; 
                    $A\\left({hien_phan_so(xmin)};0\\right)$; 
                    $B\\left({hien_phan_so((c1*b2 - c2*b1)/(a1*b2-a2*b1))};{hien_phan_so((a1*c2 - a2*c1)/(a1*b2-a2*b1))}\\right)$ 
                    và $C\\left(0; {hien_phan_so(ymin)}\\right)$.\\\\
                    Tại $O(0;0)$, $F(0;0) = 2\\cdot10^6\\cdot({loinhuan_A}\\cdot 0 +{loinhuan_B} \\cdot 0) = 0$.\\\\
                    Tại $A({hien_phan_so(xmin)};0)$, $F({hien_phan_so(xmin)};0) = 2\\cdot10^6\\cdot({loinhuan_A}\\cdot {hien_phan_so(xmin)}+{loinhuan_B}\\cdot 0) = {hien_phan_so(2*(loinhuan_A * xmin))} \\cdot 10^6$.\\\\
                    Tại $B({hien_phan_thuc(coords_max[0])};{hien_phan_thuc(coords_max[1])})$, $F({hien_phan_thuc(coords_max[0])};{hien_phan_thuc(coords_max[1])}) = 2\\cdot10^6\\cdot({loinhuan_A}\\cdot {hien_phan_thuc(coords_max[0])}+{loinhuan_B}\\cdot {hien_phan_thuc(coords_max[1])}) = {hien_phan_so(2*(loinhuan_A * coords_max[0]+loinhuan_B * coords_max[1]))} \\cdot 10^6$.\\\\
                    Tại $C(0;{hien_phan_so(ymin)})$, $F(0;{hien_phan_so(ymin)}) = 2\\cdot10^6\\cdot({loinhuan_A}\\cdot 0 +{loinhuan_B}\\cdot {hien_phan_so(ymin)}) = {hien_phan_so(2*(loinhuan_B * ymin))} \\cdot 10^6$.\\\\
                    Vậy cần đầu tư kinh doanh ${hien_phan_thuc(coords_max[0])}$ xe máy loại $A$ và ${hien_phan_thuc(coords_max[1])}$ xe máy loại $B$ để thu được lợi nhuận lớn nhất.'''.replace("1x","x").replace("1y","y")
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            if dang=='2':
                #Khai báo biến
                x, y = symbols('x y')
                while True:
                    # Tạo ngẫu nhiên các hệ số
                    a1 = 1
                    b1 = 1
                    c1 = random.randint(20, 100)
                    a2 = random.randint(5, 10)
                    b2 = random.randint(5, 10)
                    c2 = b2*random.randint(5, 33)
                    loinhuan_A=random.randint(2, 4)
                    loinhuan_B=loinhuan_A+random.randint(1, 2)
                    # Giải hệ phương trình
                    nghiem = sp.solve([sp.Eq(a1*x + b1*y, c1), sp.Eq(a2*x + b2*y, c2)], (x, y))

                    # Kiểm tra xem nghiệm có tồn tại và có phải là số nguyên dương không
                    if c2/a2 > c1 and c2/b2 < c1 and (c1/a1).is_integer and (c2/b2).is_integer and nghiem and all(n.is_integer and n > 0 for n in (nghiem[x], nghiem[y])):
                        break
                ymax = max(c1/b1, c2/b2)
                ymin = min(c1/b1, c2/b2)
                xmax = max(c1/a1, c2/a2)
                xmin = min(c1/a1, c2/a2)
                # Xuất ra mã TikZ
                tikz_code = f'''\\begin{{center}}
                \\begin{{tikzpicture}}[scale=1, line join=round, line cap=round,>=stealth,thick]
                    \\fill[pattern=north east lines] (0,0)--(0,{hien_phan_so(ymax/10+1)})--({hien_phan_so(xmax/10+1)},{hien_phan_so(ymax/10+1)})--({hien_phan_so(xmax/10+1)},0)--cycle;
                    \\fill[color = white] (0,0)--(0,{hien_phan_so(ymin/10)})--({hien_phan_so(nghiem[x]/10)},{hien_phan_so(nghiem[y]/10)})--({hien_phan_so(xmin/10)},0)--cycle;
                    \\draw (0,0) node[below left]{{$O$}};
                    \\draw[thin] ({hien_phan_so(c1/(10*a1))},1pt)--({hien_phan_so(c1/(10*a1))},-1pt) node [below] {{${latex(hien_phan_so(c1/(a1)))}$}};
                    \\draw[thin] ({hien_phan_so(c2/(10*a2))},1pt)--({hien_phan_so(c2/(10*a2))},-1pt) node [below] {{${latex(hien_phan_so(c2/(a2)))}$}};
                    \\draw[thin] (1pt,{hien_phan_so(c1/(10*b1))})--(-1pt,{hien_phan_so(c1/(10*b1))}) node [left] {{${latex(hien_phan_so(c1/(b1)))}$}};
                    \\draw[thin] (1pt,{hien_phan_so(c2/(10*b2))})--(-1pt,{hien_phan_so(c2/(10*b2))}) node [left] {{${latex(hien_phan_so(c2/(b2)))}$}};
                    \\draw[red, thick] (0, {hien_phan_so(c1/(10*b1))}) -- ({hien_phan_so(c1/(10*a1))}, 0) node[pos=0.7, above, sloped] {{ x + y = {c1}}};
                    \\draw[blue, thick] (0, {hien_phan_so(c2/(10*b2))}) -- ({hien_phan_so(c2/(10*a2))}, 0) node[pos=0.7, above, sloped] {{{a2} x + {b2} y = {c2}}};
                    \\draw[dashed, thin] ({nghiem[x]/10},0)node[below]{{${latex(nghiem[x])}$}}--({nghiem[x]/10}, {nghiem[y]/10})--(0, {nghiem[y]/10})node[left]{{${latex(nghiem[y])}$}};
                    \\draw ({hien_phan_so(c1/(10*a1))},0)node[above right, fill=white]{{$A$}} 
                    ({nghiem[x]/10},{nghiem[y]/10})node[above right, fill=white]{{$B$}} 
                    (0,{hien_phan_so(c2/(10*b2))})node[above right, fill=white]{{$C$}};
                    \\draw[->] (-0.5,0) -- ({xmax/10 + 1},0) node[right] {{$x$}};
                    \\draw[->] (0,-0.5) -- (0,{ymax/10 + 1}) node[above] {{$y$}};
                \\end{{tikzpicture}}
                \\end{{center}}'''

                # Khai báo hàm F và các điểm A, B, C, D, E
                def F(x, y):
                    return 2*loinhuan_A * x + 2*loinhuan_B * y

                # Danh sách các điểm với tọa độ tương ứng
                points = {
                    "A": (c1/a1, 0),
                    "B": (nghiem[x], nghiem[y]),
                    "C": (0, c2/b2),
                }

                # Tính giá trị của F tại mỗi điểm và tìm giá trị lớn nhất, nhỏ nhất
                max_F = None
                min_F = None
                point_max = None
                point_min = None
                coords_max = None  # Lưu tọa độ khi F đạt giá trị lớn nhất
                coords_min = None  # Lưu tọa độ khi F đạt giá trị nhỏ nhất

                for point, (x, y) in points.items():
                    value = F(x, y)

                    # Cập nhật giá trị lớn nhất và điểm tương ứng
                    if max_F is None or value > max_F:
                        max_F = value
                        point_max = point
                        coords_max = (x, y)

                    # Cập nhật giá trị nhỏ nhất và điểm tương ứng
                    if min_F is None or value < min_F:
                        min_F = value
                        point_min = point
                        coords_min = (x, y)

                von_ban_dau=key(2*c2/1000)
                kq = key(2*(loinhuan_A * coords_max[0]+loinhuan_B * coords_max[1])).replace(",0","")
                # Câu hỏi
                noidungcauhoi=f"""Một đại lý xe máy có kế hoạch nhập về hai dòng xe máy $A$ và $B$, 
                giá mỗi chiếc lần lượt là ${hien_phan_so(2*a2)}$ triệu đồng và ${hien_phan_so(2*b2)}$ triệu đồng 
                với số vốn ban đầu không vượt quá ${von_ban_dau}$ tỉ đồng. 
                Xe máy $A$ mang lợi nhuận ${hien_phan_so(2*loinhuan_A)}$ triệu đồng cho mỗi chiếc 
                và xe máy $B$ mang lợi nhuận ${hien_phan_so(2*loinhuan_B)}$ triệu đồng cho mỗi chiếc. 
                Đại lý ước tính rằng tổng nhu cầu hàng tháng sẽ không vượt quá ${hien_phan_so(c1)}$ chiếc cả hai loại. 
                Nếu đầu từ số lượng xe phù hợp, chủ đại lý sẽ thu được lợi nhuận là $a \\cdot 10^6$ đồng. Tìm $a$."""
                # Nội dung lời giải
                loigiai=f'''Gọi số xe máy loại $A$ và $B$ cần đầu tư lần lượt là $x$ và $y$. ($x, y\\in\\mathbb{{N}}$).\\\\
                    Do tổng số vốn ban đầu không vượt quá ${von_ban_dau}$ tỉ đồng nên ta có $${hien_phan_so(2*a2)}\\cdot 10^6x+{hien_phan_so(2*b2)}\\cdot 10^6y\\leq {von_ban_dau}\\cdot 10^9
                    \\Leftrightarrow {a2} x + {b2} y  \\leq {c2}.$$
                    Vì tổng nhu cầu hàng tháng sẽ không vượt quá ${hien_phan_so(c1)}$ chiếc cả hai loại nên $x+y\\leq {hien_phan_so(c1)}$.\\\\
                    Lợi nhuận thu được là $F={2*loinhuan_A}\\cdot 10^6x+{2*loinhuan_B}\\cdot 10^6y=2\\cdot10^6\\cdot({loinhuan_A}x+{loinhuan_B}y) $.\\\\
                    Ta có hệ bất phương trình $\\heva{{&x+y\\leq {hien_phan_so(c1)}\\\\&{a2} x + {b2} y \\leq {c2}\\\\&x\\geq 0\\\\&y\\geq 0.}} $
                    {tikz_code}
                    Miền nghiệm của hệ bất phương trình là miền tứ giác $OABC$ kể cả các cạnh của tứ giác. 
                    Trong đó: $O(0;0)$; 
                    $A\\left({hien_phan_so(xmin)};0\\right)$; 
                    $B\\left({hien_phan_so((c1*b2 - c2*b1)/(a1*b2-a2*b1))};{hien_phan_so((a1*c2 - a2*c1)/(a1*b2-a2*b1))}\\right)$ 
                    và $C\\left(0; {hien_phan_so(ymin)}\\right)$.\\\\
                    Tại $O(0;0)$, $F(0;0) = 2\\cdot10^6\\cdot({loinhuan_A}\\cdot 0 +{loinhuan_B} \\cdot 0) = 0$.\\\\
                    Tại $A({hien_phan_so(xmin)};0)$, $F({hien_phan_so(xmin)};0) = 2\\cdot10^6\\cdot({loinhuan_A}\\cdot {hien_phan_so(xmin)}+{loinhuan_B}\\cdot 0) = {hien_phan_so(2*(loinhuan_A * xmin))} \\cdot 10^6$.\\\\
                    Tại $B({hien_phan_thuc(coords_max[0])};{hien_phan_thuc(coords_max[1])})$, $F({hien_phan_thuc(coords_max[0])};{hien_phan_thuc(coords_max[1])}) = 2\\cdot10^6\\cdot({loinhuan_A}\\cdot {hien_phan_thuc(coords_max[0])}+{loinhuan_B}\\cdot {hien_phan_thuc(coords_max[1])}) = {hien_phan_so(2*(loinhuan_A * coords_max[0]+loinhuan_B * coords_max[1]))} \\cdot 10^6$.\\\\
                    Tại $C(0;{hien_phan_so(ymin)})$, $F(0;{hien_phan_so(ymin)}) = 2\\cdot10^6\\cdot({loinhuan_A}\\cdot 0 +{loinhuan_B}\\cdot {hien_phan_so(ymin)}) = {hien_phan_so(2*(loinhuan_B * ymin))} \\cdot 10^6$.\\\\
                    Lợi nhuận lớn nhất đại lý thu được là ${hien_phan_so(2*(loinhuan_A * coords_max[0]+loinhuan_B * coords_max[1]))} \\cdot 10^6$ đồng.
                    Vậy $a= {kq}$'''.replace("1x","x").replace("1y","y")

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('zz', '.').replace('\\text{-', '\\text{$-$')
            return content

