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


def bt_dang38_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số
                k = randint(1, 3)
                x1, x2, x3 = -1*k, 1*k, 2*k

                # Thiết lập h(0) = f(0) - g(0)
                h0_val = 3 * k 
                g0 = k
                f0 = h0_val + g0 

                # h(x) = a(x - x1)(x - x2)(x - x3) => a = h(0) / (-x1*x2*x3)
                mau_so_a = -x1 * x2 * x3
                a_val = Rational(h0_val, mau_so_a)
                h_func = a_val * (x - x1) * (x - x2) * (x - x3)

                # Bước 2: Tính diện tích S
                S1 = integrate(h_func, (x, x1, x2))
                S2 = integrate(-h_func, (x, x2, x3))
                S_total = S1 + S2

                # Bước 3: Tính tiền
                don_gia = random.choice([100, 120, 150, 180, 200]) 
                tong_tien_raw = float(S_total * don_gia)
                kq_num = int(Decimal(str(tong_tien_raw)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                da = kq_num

                # Tạo phương án sai
                s_list = []
                while len(s_list) < 3:
                    sai = da + random.choice([-15, -10, -5, 5, 10, 15, 20])
                    if sai != da and sai > 0 and str(sai) not in s_list:
                        s_list.append(str(sai))

                # TẠO DICTIONARY CHỨA TẤT CẢ BIẾN ĐỂ TRUYỀN VÀO CHUỖI
                # Cách này giúp bạn không bao giờ phải đếm số lượng %s nữa
                d = {
                    'f0': latex(f0), 'g0': latex(g0), 
                    'x1': x1, 'x2': x2, 'x3': x3,
                    'lx1': latex(x1), 'lx2': latex(x2), 'lx3': latex(x3),
                    'don_gia': latex(don_gia),
                    'a': float(a_val), 'la': latex(a_val),
                    'xmin': x1 - 1, 'xmax': x3 + 1,
                    'dmin': x1 - 0.5, 'dmax': x3 + 0.5,
                    'h0': latex(f0 - g0), 'mau_a': latex(mau_so_a),
                    'S1': latex(S1), 'S2': latex(S2), 'Stot': latex(S_total),
                    'tien_raw': latex(S_total * don_gia), 'da': latex(da)
                }

                # Nội dung câu hỏi sử dụng đặt tên biến %(tên)s
                noidungcauhoi = (r'''\immini{Người ta dự định trồng hoa để trang trí vào phần tô đậm trong hình vẽ dưới đây. Biết rằng phần tô đậm là diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y=f\left(x\right)=ax^3+bx^2+cx+%s$ và $y=g\left(x\right)=-bx^2+mx+%s$ trong đó $a,b,c,m \in \mathbb{R}$. Biết đồ thị hai hàm số đã cho cắt nhau tại các điểm có hoành độ lần lượt bằng $%s; %s; %s$. Chi phí trồng hoa là $%s.000$ đồng/$1\text{m}^2$ và đơn vị trên mỗi trục tọa độ là mét. Tổng chi phí để trồng hoa theo dự định là bao nhiêu nghìn đồng (làm tròn kết quả đến hàng đơn vị)?}
                                 {\begin{tikzpicture}[line cap=round,line join=round,font=\footnotesize,>=stealth,scale=1.00]
            	\def\xmin{-1.23}
            	\def\xmax{3.23}
            	\def\ymin{-2.0}
            	\def\ymax{4.0}
            	\begin{scope}
            		\clip (\xmin,\ymin) rectangle (\xmax,\ymax);
            		\draw[smooth, samples=100, domain=\xmin:\xmax] plot (\x, {(\x)^3 - 3*(\x)^2 + 3});
            		\draw[smooth, samples=100, domain=\xmin:\xmax] plot (\x, {-(\x)^2 + (\x)+1});
            		\fill [pattern=north west lines,line width=2pt,draw=none]
            		plot[domain=-1:2,samples=100] (\x,{(\x)^3-3*(\x)^2+3})--plot[domain=2:-1,samples=100] (\x,{-((\x)^2)+(\x)+1})--cycle;
            	\end{scope}
            	\draw[->] (\xmin,0)--(\xmax,0) node[above] {$x$};
            	\draw[->] (0,\ymin)--(0,\ymax) node[left] {$y$};
            	\fill (0,0)  node[below right] {$O$};
            	\fill (-1,0)  node[shift={(90:2ex)}]{$%s$};
            	\fill (-1,-2)  node[]{};
            	\fill (1.00,0)  node[shift={(60:2ex)}]{$%s$};
            	\fill (2.00,0)  node[shift={(60:2ex)}]{$%s$};
            	\fill (2.73,0)  node[]{};
            	\fill (0.00,2.00)  node[]{};
            	\fill (2.00,-2.00)  node[]{};
            	\draw[dashed] (1,0)|-(1,1) (2,0)|-(2,-1) (-1,0)|-(-1,-1);
            \end{tikzpicture}}'''
                                 % (latex(f0), latex(g0),latex(x1), latex(x2), latex(x3), latex(don_gia),
                                    latex(x1),latex(x2),latex(x3)))

                # Nội dung lời giải
                loigiai = (r'''Xét hàm số hiệu $h(x) = f(x) - g(x)$. \\
                Vì đồ thị hai hàm số cắt nhau tại các điểm có hoành độ $%(lx1)s; %(lx2)s; %(lx3)s$ nên ta có: \\
                $h(x) = a(x +%(lx1)s)(x - %(lx2)s)(x - %(lx3)s)$. \\
                Mặt khác, từ đồ thị ta thấy $f(0) = %(f0)s$ và $g(0) = %(g0)s$. \\
                Suy ra $h(0) = f(0) - g(0) = %(f0)s - %(g0)s = %(h0)s$. \\
                Thay $x = 0$ vào biểu thức của $h(x)$, ta được: \\
                $a(0 +%(lx1)s)(0 - %(lx2)s)(0 - %(lx3)s) = %(h0)s \Rightarrow %(mau_a)sa = %(h0)s \Rightarrow a = %(la)s$. \\
                Diện tích phần hình phẳng tô đậm là: \\
                $S = \int_{%(lx1)s}^{%(lx3)s} \left| %(la)s (x +%(lx1)s)(x - %(lx2)s)(x - %(lx3)s) \right| \text{d}x$ \\
                $= \int_{%(lx1)s}^{%(lx2)s} %(la)s (x +%(lx1)s)(x - %(lx2)s)(x - %(lx3)s) \text{d}x + \int_{%(lx2)s}^{%(lx3)s} \left[-%(la)s (x +%(lx1)s)(x - %(lx2)s)(x - %(lx3)s) \right] \text{d}x$ \\
                $= %(S1)s + %(S2)s = %(Stot)s \text{ (m}^2)$. \\
                Tổng chi phí để trồng hoa là: \\
                $T = %(Stot)s \cdot %(don_gia)s.000 = %(tien_raw)s$ (nghìn đồng). \\
                Làm tròn đến hàng đơn vị, ta được kết quả là $%(da)s$.''' % d)

                # Xuất kết quả
                dapan = '\\shortans[0]{$%(da)s$}\n' % d
                da_d = '\\True $%(da)s$' % d
                list_1 = [da_d, '$' + s_list[0] + '$', '$' + s_list[1] + '$', '$' + s_list[2] + '$']
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '+')
            return content

