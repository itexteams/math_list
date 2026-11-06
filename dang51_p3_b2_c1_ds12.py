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


def bt_dang51_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ cấu hình: (hA_str, hB_str, d_int, s_str, ans_m)
                # Tương ứng: Chiều cao đỉnh A, Chiều cao đỉnh B, khoảng cách d giữa 2 đỉnh (theo km), độ dốc s, và kết quả D_max theo mét
                configs = [
                    ("1", "0,8", 2, "0,3", 100),
                    ("1,2", "0,6", 3, "0,5", 225),
                    ("1,5", "0,7", 4, "0,6", 400),
                    ("1,1", "0,8", 2, "0,55", 200),
                    ("1,4", "0,8", 3, "0,8", 450)
                ]

                hA_str, hB_str, d_int, s_str, ans_m = random.choice(configs)

                # Chuyển đổi sang float và đơn vị thực tế (mét)
                hA_f = float(hA_str.replace(',', '.'))
                hB_f = float(hB_str.replace(',', '.'))
                s_f = float(s_str.replace(',', '.'))

                d_m = d_int * 1000
                hB_m = int(hB_f * 1000)
                hA_m = int(hA_f * 1000)

                # Tọa độ x theo km
                xA = 1
                xB = xA + d_int

                # Sử dụng Sympy để tính toán chính xác các phân số
                hA_val = Rational(int(hA_f * 100), 100)
                hB_val = Rational(int(hB_f * 100), 100)
                s_val = Rational(int(s_f * 100), 100)

                a, b, c = symbols('a b c')
                eq1 = Eq(a + b + c, hA_val)
                eq2 = Eq(a*(xB)**2 + b*(xB) + c, hB_val)
                eq3 = Eq(2*a + b, -s_val)
                sol = solve((eq1, eq2, eq3), (a, b, c))

                a_val = sol[a]
                b_val = sol[b]
                c_val = sol[c]

                # Lập phương trình đường thẳng g(x)
                m_val = (hB_val - hA_val) / (xB - 1)
                n_val = hA_val - m_val * 1

                x_sym = symbols('x')
                f_expr = a_val * x_sym**2 + b_val * x_sym + c_val
                g_expr = m_val * x_sym + n_val
                D_expr = g_expr - f_expr

                # Tìm giá trị lớn nhất của D(x)
                D_a = -a_val
                D_b = m_val - b_val
                x_max = -D_b / (2 * D_a)
                D_max = D_expr.subs(x_sym, x_max)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % ans_m]
                da = du[0]

                s_options = set([
                    '$%s$' % (ans_m + 10),
                    '$%s$' % (ans_m - 10),
                    '$%s$' % (ans_m + 50),
                    '$%s$' % (ans_m - 50),
                    '$%s$' % (ans_m + 25),
                    '$%s$' % (ans_m - 25)
                ])
                if da in s_options:
                    s_options.remove(da)
                s_list = list(s_options)

                das1 = random.choice(s_list)
                s_list.remove(das1)
                das2 = random.choice(s_list)
                s_list.remove(das2)
                das3 = random.choice(s_list)

                # Câu hỏi
                noidungcauhoi = '''Hình vẽ dưới đây mô tả mặt cắt ngang của một khu du lịch sinh thái kết nối hai đỉnh núi tại $A$ và $B$ bằng một cầu treo có hình dạng là một đường cong parabol. Trong hệ trục $Oxy$, trục $Ox$ biểu thị khoảng cách theo phương ngang, trục $Oy$ biểu thị độ cao so với mực nước biển. Khoảng cách theo phương ngang giữa hai ngọn núi $A$ và $B$ bằng $%s \\text{ m}$ và chiều cao ngọn núi tại $B$ là $%s \\text{ m}$ so với mực nước biển.
            \\begin{center}
            \\begin{tikzpicture}[scale=2, >=stealth]
            \\draw[->] (0,0) -- (4,0) node[above] {$x$};
            \\draw[->] (0,0) -- (0,1.5) node[right] {$y$};
            \\fill (0,0) circle (1pt) node[left] {$O$};
            \\coordinate (A) at (1,1);
            \\coordinate (B) at (3,0.8);
            \\draw (0,0.5) -- (A) -- (2,0.3) -- (2.3,0.4) -- (2.8,0.2) -- (B) -- (3.5,0);
            \\fill[green!20] (0,0) -- (0,0.5) -- (A) -- (2,0.3) -- (2.3,0.4) -- (2.8,0.2) -- (B) -- (3.5,0) -- cycle;
            \\draw[blue, line width=1pt] (A) -- (B);
            \\draw[red, line width=1pt] (A) parabola bend (2, 0.4) (B);
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[above] {$B$};
            \\fill (0,0.5) circle (1pt);
            \\draw[<-] (1.8, 0.85) -- (2.3, 1.2) node[above] {\\small \\textbf{Cáp thẳng an toàn}};
            \\end{tikzpicture}
            \\end{center}
            Biết rằng, đỉnh núi tại $A$ có độ cao là $%s \\text{ m}$ so với mực nước biển, cách $Oy$ $1000 \\text{ m}$ và độ dốc lớn nhất của cầu treo tại đó có độ lớn bằng $%s$. Để đảm bảo an toàn, người ta lắp đặt thêm một sợi cáp an toàn căng thẳng nối trực tiếp hai đỉnh $A$ và $B$. Xác định khoảng cách lớn nhất giữa cáp an toàn và cầu treo theo phương thẳng đứng theo đơn vị mét?''' % (d_m, hB_m, hA_m, s_str)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                eq2_a = xB**2
                eq2_b = xB

                # Nội dung lời giải
                loigiai = '''Để bài làm nhìn gọn hơn, ta chuẩn hóa đơn vị về kilomet. Gọi parabol $f(x) = ax^2 + bx + c$ \\\\
            Parabol đi qua điểm $A(1; %s)$ và điểm $B(%s; %s)$ \\\\
            Độ dốc tại $A$ có độ lớn bằng $%s$ nhưng nó đang đi xuống từ trái sang phải nên độ dốc là $-%s$ \\\\
            Khi đó ta có: $y'(1) = -%s \\Leftrightarrow 2a \\cdot 1 + b = -%s \\Leftrightarrow 2a + b = -%s$ \\\\
            Từ đó ta có hệ phương trình:
            $\\begin{cases}
            a + b + c = %s \\\\
            %sa + %sb + c = %s \\\\
            2a + b = -%s
            \\end{cases} \\Leftrightarrow \\begin{cases}
            a = %s \\\\
            b = %s \\\\
            c = %s
            \\end{cases} \\Rightarrow f(x) = %s$ \\\\
            Sợi cáp an toàn là đường thẳng $g(x) = mx + n$ đi qua $A(1; %s)$ và $B(%s; %s)$ có phương trình là: \\\\
            $g(x) = %s$ \\\\
            Khoảng cách giữa cáp an toàn và cầu treo theo phương thẳng đứng là: $D(x) = g(x) - f(x)$ \\\\
            $\\Leftrightarrow D(x) = \\left(%s\\right) - \\left(%s\\right) \\Leftrightarrow D(x) = %s$ \\\\
            Khảo sát hàm số $D(x)$ để tìm khoảng cách lớn nhất. Nhận thấy, đây là đồ thị của hàm số bậc hai có hệ số $a < 0$ nên sẽ đạt giá trị lớn nhất tại $x = -\\frac{b}{2a} = -\\frac{%s}{2 \\cdot \\left(%s\\right)} = %s \\Rightarrow D_{\\max}\\left(%s\\right) = %s \\text{ (km)}$ \\\\
            Vậy khoảng cách lớn nhất giữa cáp an toàn và cầu treo theo phương thẳng đứng là $%s$ mét.''' % (
                    hA_str, xB, hB_str,
                    s_str, s_str,
                    s_str, s_str, s_str,
                    hA_str, eq2_a, eq2_b, hB_str, s_str,
                    latex(a_val), latex(b_val), latex(c_val), latex(f_expr),
                    hA_str, xB, hB_str,
                    latex(g_expr),
                    latex(g_expr), latex(f_expr), latex(D_expr),
                    latex(D_b), latex(D_a), latex(x_max), latex(x_max), str(float(D_max)).replace('.', ','),
                    ans_m
                )
                dapan='\\shortans[0]{$%s$}\n'%(ans_m)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

