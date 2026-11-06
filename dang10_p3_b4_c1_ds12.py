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


def bt_dang10_p3_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ cấu hình cho đồ thị tàu lượn (x1, x_end, k_denom, h_min)
                # x1 là hoành độ điểm cực đại, x2 (cực tiểu) luôn bằng 3*x1
                configs = [
                    (20, 90, 1000, 6),
                    (20, 90, 800, 6),
                    (10, 50, 100, 5),
                    (15, 65, 500, 10),
                    (30, 150, 2700, 12),
                    (25, 115, 500, 4),
                    (20, 70, 1000, 6)
                ]
                config = random.choice(configs)
                x1, x_end, k_denom, h_min = config
                x2 = 3 * x1
                k = Rational(1, k_denom)

                y_A = h_min
                y_C = h_min

                # Tính toán tọa độ Y tại cực đại (B) và điểm cuối (D)
                y_B_val = float(k * x1 * (x1 - x2)**2 + h_min)
                y_D_val = float(k * x_end * (x_end - x2)**2 + h_min)

                y_B = int(y_B_val) if y_B_val.is_integer() else y_B_val
                y_D = int(y_D_val) if y_D_val.is_integer() else y_D_val

                y_B_str = str(y_B).replace('.', ',')
                y_D_str = str(y_D).replace('.', ',')

                max_height = max(y_B_val, y_D_val)

                diff_y_val = y_D_val - y_A
                diff_y = int(diff_y_val) if diff_y_val.is_integer() else diff_y_val
                diff_y_str = str(diff_y).replace('.', ',')

                coef_a = x_end * (x_end - x2)**2

                # Làm tròn đến hàng đơn vị theo yêu cầu
                kq_str = str(Decimal(max_height).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                du = ['$%s$' % kq_str]
                da = du[0]

                # Các đáp án nhiễu (cộng/trừ số nguyên)
                s = [
                    '$%s$' % str(Decimal(max_height + 1).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),
                    '$%s$' % str(Decimal(max_height - 1).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),
                    '$%s$' % str(Decimal(max_height + 2).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),
                    '$%s$' % str(Decimal(max_height - 2).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),
                    '$%s$' % str(Decimal(max_height + 3).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),
                    '$%s$' % str(Decimal(max_height - 3).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),
                ]

                # Thêm giá trị nhiễu là điểm cực đại/cực trị còn lại (cũng làm tròn tới hàng đơn vị)
                distractor_val = min(y_B_val, y_D_val)
                dist_str = str(Decimal(distractor_val).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                s.append('$%s$' % dist_str)

                # Lọc trùng và chọn ngẫu nhiên
                s = list(set(s) - set(du))
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Tỉ lệ cho hình vẽ TikZ tùy biến theo dữ liệu random
                x_unit = 6.0 / float(x_end)
                y_unit = 4.0 / float(max(max_height, 10))

                tikz_str = '''\\begin{center}
            \\begin{tikzpicture}[>=stealth, x=%scm, y=%scm]
            \\draw[->] (-%s,0) -- (%s,0) node[below] {$x$};
            \\draw[->] (0,-%s) -- (0,%s) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\draw[thick, blue, smooth, samples=100, domain=0:%s] plot (\\x, {%s * \\x * (\\x - %s) * (\\x - %s) + %s});
            \\fill (0,%s) circle (1.5pt) node[left] {$A$};
            \\fill (%s,%s) circle (1.5pt) node[above right] {$C$};
            \\fill (%s,%s) circle (1.5pt) node[above left] {$D$};
            \\draw[dashed] (%s,0) node[below]{$%s$} -- (%s,%s);
            \\draw[dashed] (%s,0) node[below]{$%s$} -- (%s,%s) -- (0,%s) node[left]{$%s$};
            \\end{tikzpicture}
            \\end{center}''' % (
                    round(x_unit, 4), round(y_unit, 4),
                    round(x_end * 0.1, 1), round(x_end * 1.1, 1),
                    round(max_height * 0.1, 1), round(max_height * 1.1, 1),
                    x_end, float(k), x2, x2, h_min,
                    y_A, x2, y_C, x_end, y_D,
                    x2, x2, x2, y_C,
                    x_end, x_end, x_end, y_D, y_D, y_D_str
                )

                # Câu hỏi (sửa lại hàng đơn vị)
                noidungcauhoi = ('''Một phần đường chạy của tàu lượn siêu tốc khi gắn hệ trục toạ độ $Oxy$ được mô phỏng như hình vẽ, đơn vị trên mỗi trục là mét. Biết đường chạy của nó là một phần đồ thị hàm bậc ba $y = ax^3 + bx^2 + cx + d \\, (0 \\le x \\le %s)$ và đi qua các điểm $A(0; %s)$, $C(%s; %s)$, $D(%s; %s)$ đồng thời đạt độ cao nhỏ nhất so với mặt đất là $%s$ m tại điểm $C$. Độ cao lớn nhất mà tàu lượn siêu tốc đạt được là bao nhiêu mét? (Kết quả làm tròn đến hàng đơn vị).
            %s''' % (x_end, y_A, x2, y_C, x_end, y_D_str, h_min, tikz_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi phương trình hàm số bậc ba là $y = f(x) = ax^3 + bx^2 + cx + d$.\\\\
            Đồ thị hàm số đi qua điểm $A(0; %s)$ nên $f(0) = %s \\Rightarrow d = %s$.\\\\
            Đồ thị hàm số đạt cực tiểu tại $C(%s; %s)$ (vì $C$ là điểm có độ cao nhỏ nhất) nên:\\\\
            \\begin{itemize}
                \\item $f(%s) = %s \\Rightarrow a(%s)^3 + b(%s)^2 + c(%s) + %s = %s \\Rightarrow %s a + %s b + %s c = 0$ (1)
                \\item $f'(%s) = 0$. Ta có $f'(x) = 3ax^2 + 2bx + c \\Rightarrow 3a(%s)^2 + 2b(%s) + c = 0 \\Rightarrow %s a + %s b + c = 0$ (2)
            \\end{itemize}
            Từ (1) suy ra: $c = -%s a - %s b$.\\\\
            Thay vào (2) ta được: $%s a + %s b - %s a - %s b = 0 \\Rightarrow %s a + %s b = 0 \\Rightarrow b = %s a$.\\\\
            Thay $b$ lại vào công thức $c$: $c = -%s a - %s(%s a) = %s a$.\\\\
            Vậy $f(x) = ax^3 + (%s a)x^2 + (%s a)x + %s = ax(x^2 - %s x + %s) + %s = ax(x - %s)^2 + %s$.\\\\
            Đồ thị đi qua điểm $D(%s; %s)$ nên $f(%s) = %s \\Rightarrow a \\cdot %s \\cdot (%s - %s)^2 + %s = %s \\Rightarrow %s a = %s \\Rightarrow a = %s$.\\\\
            Từ đó ta có phương trình hàm số: $f(x) = %s x(x - %s)^2 + %s$.\\\\
            Để tìm độ cao lớn nhất, ta xét hàm số $f(x)$ trên đoạn $[0; %s]$.\\\\
            $f'(x) = %s [ (x - %s)^2 + 2x(x - %s) ] = %s (x - %s)(3x - %s)$. \\\\
            Cho $f'(x) = 0 \\iff x = %s$ hoặc $x = %s$.\\\\
            Tính các giá trị:\\\\
            $f(0) = %s$; $f(%s) = %s$; $f(%s) = %s$.\\\\
            Vậy độ cao lớn nhất tàu lượn đạt được là $%s$ mét.''' % (
                    y_A, y_A, y_A,
                    x2, y_C,
                    x2, y_C, x2, x2, x2, y_A, y_C, x2**3, x2**2, x2,
                    x2, x2, x2, 3*x2**2, 2*x2,
                    x2**2, x2,
                    3*x2**2, 2*x2, x2**2, x2, 2*x2**2, x2, -2*x2,
                    x2**2, x2, -2*x2, x2**2,
                    -2*x2, x2**2, y_A, 2*x2, x2**2, y_A, x2, y_A,
                    x_end, y_D_str, x_end, y_D_str, x_end, x_end, x2, y_A, y_D_str, coef_a, diff_y_str, latex(k),
                    latex(k), x2, y_A,
                    x_end,
                    latex(k), x2, x2, latex(k), x2, x2,
                    x2, x1,
                    y_A, x1, y_B_str, x_end, y_D_str,
                    kq_str
                ))
            dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

