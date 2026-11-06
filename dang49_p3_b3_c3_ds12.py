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


def bt_dang49_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân sang dấu phẩy
            def format_num(val):
                if int(val) == val:
                    return str(int(val))
                return str(val).replace('.', ',')

            # Hàm hỗ trợ định dạng biểu thức LaTeX theo quy tắc
            def format_latex(expr):
                s = latex(expr)
                s = s.replace('.', ',')
                s = s.replace('(', '\\left(').replace(')', '\\right)')
                return s

            # Hàm làm tròn kết quả đến hàng phần 10 và định dạng dấu phẩy
            def round_to_10th(val):
                val_float = float(val)
                val_dec = Decimal(str(val_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                return str(val_dec).replace('.', ',')

            # Khai báo biến và thiết lập các giá trị ngẫu nhiên có điều kiện
            # Điều kiện: 4*h_M > h_E để parabol luôn có đỉnh không nằm quá cao hoặc đi xuống dưới
            valid_pairs = [
                (3.5, 1),
                (4, 1.5),
                (5, 1.5),
                (5, 2),
                (6, 2),
                (6, 2.5)
            ]
            h_E_val, h_M_val = random.choice(valid_pairs)
            w_val = random.choice([4, 6, 8])
            d_val = random.randint(3, 6)

            h_E = Rational(str(h_E_val))
            h_M = Rational(str(h_M_val))
            w = Rational(w_val)
            d = Rational(d_val)

            w_text = format_num(w_val)
            d_text = format_num(d_val)
            h_E_text = format_num(h_E_val)
            h_M_text = format_num(h_M_val)

            a, b, c, x_var = symbols('a b c x')

            # Lập hệ phương trình tìm a, b (c = 0)
            # a*w^2 + b*w = h_E
            # a*(w/2)^2 + b*(w/2) = h_M
            a_val = (2*h_E - 4*h_M) / (w**2)
            b_val = (4*h_M - h_E) / w

            parabola_eq = a_val * x_var**2 + b_val * x_var

            # Tính diện tích thiết diện và thể tích
            S_val = a_val * (w**3) / 3 + b_val * (w**2) / 2
            V_val = S_val * d

            # Áp dụng làm tròn hàng phần mười cho đáp án đúng
            da_text = round_to_10th(V_val)

            # Tạo các phương án sai (nhầm diện tích tam giác, quên nhân chiều sâu d, hoặc tính toán sai)
            S_tri = Rational(1, 2) * w * h_E
            V_tri = S_tri * d
            V_wrong1 = V_val * 2
            V_wrong2 = V_val / 2
            V_wrong3 = V_val + 1
            V_wrong4 = V_val - 1

            da = '$%s$' % da_text
            s_list = [
                '$%s$' % round_to_10th(S_val),
                '$%s$' % round_to_10th(V_tri),
                '$%s$' % round_to_10th(V_wrong1),
                '$%s$' % round_to_10th(V_wrong2),
                '$%s$' % round_to_10th(V_wrong3),
                '$%s$' % round_to_10th(V_wrong4)
            ]

            # Đảm bảo các phương án sai không bị trùng với đáp án đúng và không trùng nhau
            s_unique = []
            for ans in s_list:
                if ans != da and ans not in s_unique:
                    s_unique.append(ans)

            random.shuffle(s_unique)
            das1 = s_unique[0]
            das2 = s_unique[1]
            das3 = s_unique[2]

            # Các đáp án
            da_d = '\\True ' + str(da)
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Xây dựng hình vẽ TikZ 3D mô phỏng khối tường cong
            cx = float(w_val / 2)
            cy = float(b_val * w_val / 2)

            tikz_str = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt, scale=0.8, x={(1cm,0cm)}, y={(0cm,1cm)}, z={(-0.5cm,0.5cm)}]
            \\coordinate (A) at (0,0,0);
            \\coordinate (C) at (%s,0,0);
            \\coordinate (E) at (%s,%s,0);
            \\coordinate (M) at (%s,0,0);
            \\coordinate (Mt) at (%s,%s,0);
            \\coordinate (B) at (0,0,%s);
            \\coordinate (Cb) at (%s,0,%s);
            \\coordinate (Eb) at (%s,%s,%s);
            \\draw[dashed] (A) -- (C) -- (E);
            \\draw[dashed] (A) -- (B) -- (Cb) -- (Eb);
            \\draw[dashed] (C) -- (Cb);
            \\draw[dashed] (M) -- ++(0,0,%s);
            \\draw[dashed] (M) -- (Mt);
            \\draw[fill=yellow!40] (A) -- (B) .. controls (%s, %s, %s) .. (Eb) -- (E) .. controls (%s, %s, 0) .. (A);
            \\draw (B) .. controls (%s, %s, %s) .. (Eb);
            \\node[below] at (A) {$A$};
            \\node[below] at (C) {$C$};
            \\node[right] at (E) {$E$};
            \\node[left] at (B) {$B$};
            \\node[below] at (M) {$M$};
            \\node[below] at (%s,0,0) {$%s\\text{ m}$};
            \\node[right] at (%s, %s, 0) {$%s\\text{ m}$};
            \\node[below left] at (0,0,%s) {$%s\\text{ m}$};
            \\node[right] at (%s,%s,0) {$%s\\text{ m}$};
            \\end{tikzpicture}
            \\end{center}''' % (
                w_val, w_val, h_E_val, w_val/2, w_val/2, h_M_val, d_val, w_val, d_val, w_val, h_E_val, d_val,
                d_val,
                cx, cy, d_val, cx, cy,
                cx, cy, d_val,
                w_val/4, format_num(w_val/2),
                w_val, h_E_val/2, h_E_text,
                d_val/2, d_text,
                w_val/2, h_M_val/2, h_M_text
            ))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Ông A dự định xây "tường cong" trong sân trượt patin là một khối bê tông có chiều cao từ mặt đất lên là $%s\\text{ m}$. Giao của mặt tường cong và mặt đất là đoạn thẳng $AB=%s\\text{ m}$. Thiết diện của khối tường cong cắt bởi mặt phẳng vuông góc với $AB$ tại $A$ là một hình tam giác vuông cong $ACE$ với $AC=%s\\text{ m}$, $CE=%s\\text{ m}$ và cạnh cong $AE$ nằm trên một đường parabol có trục đối xứng vuông góc với mặt đất. Tại vị trí $M$ là trung điểm của $AC$ thì tường cong có độ cao $%s\\text{ m}$ (xem hình minh họa bên). Thể tích bê tông cần sử dụng để tạo nên khối tường cong đó bằng bao nhiêu mét khối? (làm tròn kết quả đến hàng phần mười).
            %s''' % (h_E_text, d_text, w_text, h_E_text, h_M_text, tikz_str))

            # Nội dung lời giải
            loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho $A \\equiv O\\left(0;0\\right)$, $C\\left(%s;0\\right)$, $E\\left(%s;%s\\right)$.\\\\
            Khi đó $M$ là trung điểm của $AC$ nên $M\\left(%s;0\\right)$. Tại $M$ tường cong có độ cao $%s\\text{ m}$ nên parabol đi qua điểm $M'\\left(%s;%s\\right)$.\\\\
            Giả sử phương trình đường parabol là $y = ax^2 + bx + c$.\\\\
            Vì parabol đi qua $A\\left(0;0\\right)$, $E\\left(%s;%s\\right)$ và $M'\\left(%s;%s\\right)$ nên ta có hệ phương trình:\\\\
            $\\left\\{\\begin{aligned} & c=0 \\\\ & %s a + %s b + c = %s \\\\ & %s a + %s b + c = %s \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & a = %s \\\\ & b = %s \\\\ & c = 0 \\end{aligned}\\right.$\\\\
            Suy ra phương trình parabol là $y = %s$.\\\\
            Diện tích thiết diện của khối tường cong là:\\\\
            $S = \\int\\limits_0^{%s} \\left(%s\\right) \\mathrm{d}x = %s \\text{ m}^2$.\\\\
            Thể tích bê tông cần sử dụng là:\\\\
            $V = S \\cdot AB = %s \\cdot %s = %s \\text{ m}^3 \\approx %s \\text{ m}^3$.''' % (
                w_text, w_text, h_E_text,
                format_num(w_val/2), h_M_text, format_num(w_val/2), h_M_text,
                w_text, h_E_text, format_num(w_val/2), h_M_text,
                format_latex(w**2), w_text, h_E_text,
                format_latex((w/2)**2), format_num(w_val/2), h_M_text,
                format_latex(a_val), format_latex(b_val),
                format_latex(parabola_eq),
                w_text, format_latex(parabola_eq), format_latex(S_val),
                format_latex(S_val), d_text, format_latex(V_val), da_text
            ))
            dapan='\\shortans[0]{$%s$}\n'%(da_text)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

