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


def bt_dang7_p3_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                t = symbols('t')

                # Random thời điểm t_i (gia tốc bắt đầu dương - điểm uốn của đồ thị)
                t_i = randint(2, 5)

                # Random tổng thời gian T (T > t_i)
                T = t_i + randint(4, 8)

                # Random hệ số a (để phương trình có nghiệm đẹp)
                a_denom = random.choice([2, 3, 6, 12])
                a = Rational(1, a_denom)

                # Xây dựng các hệ số b, c để vật luôn có vận tốc v(t) >= 0 và gia tốc a(t) > 0 khi t > t_i
                # Chọn b, c sao cho v(t) = 3a(t - t_i)^2 >= 0
                b = -3 * a * t_i
                c = 3 * a * t_i**2

                # Các hàm số
                s_func = a * t**3 + b * t**2 + c * t
                v_func = sp.diff(s_func, t)
                a_func = sp.diff(v_func, t)

                # Chọn 2 mốc thời gian hiển thị trên đồ thị (khác t_i và T)
                x_choices = []
                while len(x_choices) < 2:
                    val = randint(1, T - 1)
                    if val not in x_choices and val != t_i:
                        x_choices.append(val)
                x_choices.sort()
                x1, x2 = x_choices[0], x_choices[1]

                # Tính giá trị quãng đường tại các mốc thời gian
                s1 = s_func.subs(t, x1)
                s2 = s_func.subs(t, x2)
                s_T = s_func.subs(t, T)

                # Kết quả bài toán
                kq = T - t_i

                # Hàm hỗ trợ định dạng số thập phân dùng trong TikZ
                def fmt(val):
                    return str(round(float(val), 4))

                # Tạo chuỗi TikZ vẽ đồ thị
                tikz_str = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, x=0.6cm, y=%scm]
            \\draw[->] (-1,0) -- (%s,0) node[below] {$t(s)$};
            \\draw[->] (0,-0.5) -- (0,%s) node[right] {$s(t) (m)$};
            \\node at (0,0) [below left] {$O$};
            \\draw[domain=0:%s, smooth, variable=\\t, thick] plot ({\\t}, {%s*\\t*\\t*\\t + %s*\\t*\\t + %s*\\t});
            \\draw[dashed] (%s,0) node[below]{$%s$} -- (%s,%s) -- (0,%s) node[left]{$%s$};
            \\draw[dashed] (%s,0) node[below]{$%s$} -- (%s,%s) -- (0,%s) node[left]{$%s$};
            \\draw[dashed] (%s,0) node[below]{$%s$} -- (%s,%s) -- (0,%s) node[left]{$%s$};
            \\fill (0,0) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}''' % (
                    fmt(6.0 / float(s_T)),
                    T + 1, fmt(1.1 * float(s_T)),
                    T, fmt(a), fmt(b), fmt(c),
                    x1, x1, x1, fmt(s1), fmt(s1), latex(s1),
                    x2, x2, x2, fmt(s2), fmt(s2), latex(s2),
                    T, T, T, fmt(s_T), fmt(s_T), latex(s_T),
                    x1, fmt(s1),
                    x2, fmt(s2),
                    T, fmt(s_T)
                ))

                # Đáp án đúng
                du = ['$%s$' % (kq)]
                da = du[0]

                # Tạo các phương án nhiễu
                s_set = set()
                for offset in [1, 2, 3, 4]:
                    s_set.add('$%s$' % (kq + offset))
                    if kq - offset > 0:
                        s_set.add('$%s$' % (kq - offset))
                s_set.add('$%s$' % (T))
                s_set.discard(da)
                s = list(s_set)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một vật chuyển động quãng đường $s(t)$ (tính theo mét) vật đi được sau khoảng thời gian $t$ (tính theo giây), $t \\ge 0$, được mô tả là một hàm số bậc ba có đồ thị như hình vẽ dưới đây:
            %s
            Hỏi trong $%s$ giây đầu tiên, khoảng thời gian vật chuyển động nhanh dần kéo dài bao nhiêu giây?''' 
                                 % (tikz_str, T))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hệ phương trình
                eq1_str = "%s a + %s b + %s c = %s" % (x1**3, x1**2, x1, latex(s1))
                eq2_str = "%s a + %s b + %s c = %s" % (x2**3, x2**2, x2, latex(s2))
                eq3_str = "%s a + %s b + %s c = %s" % (T**3, T**2, T, latex(s_T))

                # Lời giải
                loigiai = ('''Gọi phương trình chuyển động của vật là $s(t) = at^3 + bt^2 + ct + d$ ($a \\ne 0$).\\\\
            Đồ thị đi qua gốc tọa độ $O(0; 0)$ nên $d = 0$.\\\\
            Theo đồ thị, ta có $s(%s) = %s$, $s(%s) = %s$, $s(%s) = %s$. Ta có hệ phương trình:\\\\
            $\\left\\{\\begin{matrix} %s \\\\ %s \\\\ %s \\end{matrix}\\right. \\iff \\left\\{\\begin{matrix} a = %s \\\\ b = %s \\\\ c = %s \\end{matrix}\\right.$\\\\
            Suy ra phương trình chuyển động là $s(t) = %s$.\\\\
            Vận tốc của vật là $v(t) = s'(t) = %s = %s \\ge 0 \\, \\forall t \\ge 0$.\\\\
            Gia tốc của vật là $a(t) = v'(t) = %s$.\\\\
            Vật chuyển động nhanh dần khi vận tốc tăng, tức là gia tốc $a(t) > 0$ (vì $v(t) \\ge 0$).\\\\
            Ta có $a(t) > 0 \\iff %s > 0 \\iff t > %s$.\\\\
            Do đó, trong $%s$ giây đầu tiên, khoảng thời gian vật chuyển động nhanh dần là $t \\in (%s; %s]$.\\\\
            Thời gian kéo dài là $%s - %s = %s$ giây.'''
                           % (
                               x1, latex(s1), x2, latex(s2), T, latex(s_T),
                               eq1_str, eq2_str, eq3_str,
                               latex(a), latex(b), latex(c),
                               latex(s_func),
                               latex(v_func), latex(factor(v_func)),
                               latex(a_func),
                               latex(a_func), t_i,
                               T, t_i, T,
                               T, t_i, kq
                           ))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

