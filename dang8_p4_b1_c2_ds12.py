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


def bt_dang8_p4_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    def vn_num(val):
        """Định dạng số theo chuẩn Việt Nam (thay dấu chấm bằng dấu phẩy)"""
        if isinstance(val, sp.Rational):
            # Nếu mẫu số chỉ chứa ước 2 và 5 thì ra số thập phân hữu hạn
            d = val.q
            temp_d = d
            while temp_d % 2 == 0: temp_d //= 2
            while temp_d % 5 == 0: temp_d //= 5
            if temp_d == 1:
                return f"{float(val):g}".replace('.', ',')
            else:
                return sp.latex(val)
        elif isinstance(val, (int, float)):
            return f"{val:g}".replace('.', ',')
        return str(val).replace('.', ',')

    if dang=='1':
        # Thiết lập độ rộng khoảng và giá trị bắt đầu
        h = random.choice([2, 3, 4, 5])
        a1 = random.randint(4, 10)
        a2, a3, a4, a5, a6 = a1+h, a1+2*h, a1+3*h, a1+4*h, a1+5*h

        # Giá trị đại diện
        x1 = sp.Rational(a1 + a2, 2)
        x2 = sp.Rational(a2 + a3, 2)
        x3 = sp.Rational(a3 + a4, 2)
        x4 = sp.Rational(a4 + a5, 2)
        x5 = sp.Rational(a5 + a6, 2)

        # Hàm random tần số đối xứng để Q1 nằm nhóm 2, Q3 nằm nhóm 4
        def get_symmetric_freqs():
            while True:
                f1 = random.randint(10, 25)
                f2 = random.randint(20, 45)
                f3 = random.randint(30, 60)
                # Điều kiện để Q1, Q3 rơi đúng vào nhóm 2 và 4
                if (f3 < 2*f1 + 2*f2) and (2*f1 < 2*f2 + f3):
                    return f1, f2, f3

        fA1, fA2, fA3 = get_symmetric_freqs()
        fB1, fB2, fB3 = get_symmetric_freqs()

        # Đảm bảo 2 nhà máy có bộ số khác nhau
        while (fA1, fA2, fA3) == (fB1, fB2, fB3):
            fB1, fB2, fB3 = get_symmetric_freqs()

        nA = 2*fA1 + 2*fA2 + fA3
        nB = 2*fB1 + 2*fB2 + fB3

        # Trung bình cộng do tính đối xứng chắc chắn bằng x3
        mean_A = x3
        mean_B = x3

        # Hàm tính toán Q1, Q3 và các chuỗi hiển thị
        def calc_quartiles(n, f1, f2, f3):
            n4_val = n / 4
            n34_val = 3 * n / 4

            Q1_val = a2 + sp.Rational(sp.Rational(n, 4) - f1, f2) * h
            Q3_val = a4 + sp.Rational(sp.Rational(3*n, 4) - (f1 + f2 + f3), f2) * h
            Delta_Q = Q3_val - Q1_val

            return n4_val, n34_val, Q1_val, Q3_val, Delta_Q

        n4_A, n34_A, Q1_A, Q3_A, Delta_QA = calc_quartiles(nA, fA1, fA2, fA3)
        n4_B, n34_B, Q1_B, Q3_B, Delta_QB = calc_quartiles(nB, fB1, fB2, fB3)

        # So sánh khoảng biến thiên
        if float(Delta_QA) < float(Delta_QB):
            ketluan = "Vì $\\Delta_{Q_A} < \\Delta_{Q_B}$ nên mức thu nhập của người lao động nhà máy B biến động nhiều hơn."
        elif float(Delta_QA) > float(Delta_QB):
            ketluan = "Vì $\\Delta_{Q_A} > \\Delta_{Q_B}$ nên mức thu nhập của người lao động nhà máy A biến động nhiều hơn."
        else:
            ketluan = "Vì $\\Delta_{Q_A} = \\Delta_{Q_B}$ nên mức thu nhập của người lao động hai nhà máy biến động như nhau."

        # Xây dựng chuỗi hiển thị đề bài
        noidungcauhoi = f"""Thu nhập theo tháng (đơn vị: triệu đồng) của người lao động ở hai nhà máy như sau:
    \\begin{{center}}
    \\begin{{tabular}}{{|c|c|c|c|c|c|}}
    \\hline
    Thu nhập & $[{a1};{a2})$ & $[{a2};{a3})$ & $[{a3};{a4})$ & $[{a4};{a5})$ & $[{a5};{a6})$ \\\\
    \\hline
    Số người của nhà máy A & ${fA1}$ & ${fA2}$ & ${fA3}$ & ${fA2}$ & ${fA1}$ \\\\
    \\hline
    Số người của nhà máy B & ${fB1}$ & ${fB2}$ & ${fB3}$ & ${fB2}$ & ${fB1}$ \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}
    Tính mức thu nhập trung bình của người lao động ở hai nhà máy trên. Dựa vào khoảng tứ phân vị, hãy xác định xem mức thu nhập của người lao động ở nhà máy nào biến động nhiều hơn."""

        # Lời giải chi tiết
        loigiai = f"""Ta có bảng số liệu với giá trị đại diện của nhóm là:
    \\begin{{center}}
    \\begin{{tabular}}{{|c|c|c|c|c|c|}}
    \\hline
    Thu nhập & $[{a1};{a2})$ & $[{a2};{a3})$ & $[{a3};{a4})$ & $[{a4};{a5})$ & $[{a5};{a6})$ \\\\
    \\hline
    Giá trị đại diện & ${vn_num(x1)}$ & ${vn_num(x2)}$ & ${vn_num(x3)}$ & ${vn_num(x4)}$ & ${vn_num(x5)}$ \\\\
    \\hline
    Số người của nhà máy A & ${fA1}$ & ${fA2}$ & ${fA3}$ & ${fA2}$ & ${fA1}$ \\\\
    \\hline
    Số người của nhà máy B & ${fB1}$ & ${fB2}$ & ${fB3}$ & ${fB2}$ & ${fB1}$ \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}
    Mức thu nhập trung bình của người lao động nhà máy A là:\\\\ 
    \\hspace*{{3cm}}$\\frac{{{vn_num(x1)}.{fA1} + {vn_num(x2)}.{fA2} + {vn_num(x3)}.{fA3} + {vn_num(x4)}.{fA2} + {vn_num(x5)}.{fA1}}}{{{fA1} + {fA2} + {fA3} + {fA2} + {fA1}}} = {sp.latex(mean_A)}$ (triệu đồng)
    Mức thu nhập trung bình của người lao động nhà máy B là:\\\\ 
    \\hspace*{{3cm}}$\\frac{{{vn_num(x1)}.{fB1} + {vn_num(x2)}.{fB2} + {vn_num(x3)}.{fB3} + {vn_num(x4)}.{fB2} + {vn_num(x5)}.{fB1}}}{{{fB1} + {fB2} + {fB3} + {fB2} + {fB1}}} = {sp.latex(mean_B)}$ (triệu đồng)
    Nhà máy A: Ta có cỡ mẫu $n = {nA}$. Giả sử $x_1, x_2, \\dots, x_{{{nA}}}$ là mức thu nhập của người lao động nhà máy A và giả sử dãy số liệu gốc này đã được sắp xếp theo thứ tự không giảm.
    Vì $\\frac{{n}}{{4}} = {vn_num(n4_A)}$ và ${fA1} < {vn_num(n4_A)} < {fA1} + {fA2}$ nên nhóm chứa tứ phân vị thứ nhất là nhóm $[{a2};{a3})$ và tứ phân vị thứ nhất là: 
    $$Q_1 = {a2} + \\frac{{\\frac{{{nA}}}{{4}} - {fA1}}}{{{fA2}}} .{h} = {sp.latex(Q1_A)}$$
    Vì $\\frac{{3n}}{{4}} = {vn_num(n34_A)}$ và ${fA1}+{fA2}+{fA3} < {vn_num(n34_A)} < {fA1}+{fA2}+{fA3}+{fA2}$ nên nhóm chứa tứ phân vị thứ ba là nhóm $[{a4};{a5})$ và tứ phân vị thứ ba là: 
    $$Q_3 = {a4} + \\frac{{\\frac{{3.{nA}}}{{4}} - ({fA1}+{fA2}+{fA3})}}{{{fA2}}} .{h} = {sp.latex(Q3_A)}$$
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_{{Q_A}} = {sp.latex(Q3_A)} - {sp.latex(Q1_A)} = {sp.latex(Delta_QA)}$
    Nhà máy B: Ta có cỡ mẫu $n = {nB}$. Giả sử $x_1, x_2, \\dots, x_{{{nB}}}$ là mức thu nhập của người lao động nhà máy B và giả sử dãy số liệu gốc này đã được sắp xếp theo thứ tự không giảm.
    Vì $\\frac{{n}}{{4}} = {vn_num(n4_B)}$ và ${fB1} < {vn_num(n4_B)} < {fB1} + {fB2}$ nên nhóm chứa tứ phân vị thứ nhất là nhóm $[{a2};{a3})$ và tứ phân vị thứ nhất là: 
    $$Q'_1 = {a2} + \\frac{{\\frac{{{nB}}}{{4}} - {fB1}}}{{{fB2}}} .{h} = {sp.latex(Q1_B)}$$
    Vì $\\frac{{3n}}{{4}} = {vn_num(n34_B)}$ và ${fB1}+{fB2}+{fB3} < {vn_num(n34_B)} < {fB1}+{fB2}+{fB3}+{fB2}$ nên nhóm chứa tứ phân vị thứ ba là nhóm $[{a4};{a5})$ và tứ phân vị thứ ba là: 
    $$Q'_3 = {a4} + \\frac{{\\frac{{3.{nB}}}{{4}} - ({fB1}+{fB2}+{fB3})}}{{{fB2}}} .{h} = {sp.latex(Q3_B)}$$
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_{{Q_B}} = {sp.latex(Q3_B)} - {sp.latex(Q1_B)} = {sp.latex(Delta_QB)}$
    {ketluan}"""

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\n\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

