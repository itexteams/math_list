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


def bt_dang50_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: MẸO RANDOM ĐỂ a, b, c LÀ SỐ NGUYÊN
                # Các bộ cấu hình này đã được tính toán ngược từ a,b,c nguyên để suy ra tỷ lệ P
                configs = [
                    (4, 2, Rational(1, 2), Rational(3, 4)), # Sinh ra a=-3, b=6, c=-4
                    (4, 2, Rational(1, 4), Rational(3, 8)), # Sinh ra a=-3, b=13, c=-16
                    (6, 3, Rational(1, 3), Rational(5, 8)), # Sinh ra a=-4, b=17, c=-24
                    (6, 3, Rational(1, 3), Rational(7, 8))  # Sinh ra a=-3, b=8, c=-6
                ]
                L_val, R_val, k_val, P_val = random.choice(configs)

                a, b, c = symbols('a b c')
                f = k_val * x**3 + a * x**2 + b * x + c

                # Phương trình 1: Đi qua A(R, 0)
                eq1_lhs = a*R_val**2 + b*R_val + c
                eq1_rhs = -k_val*R_val**3

                # Phương trình 2: Đi qua B(L, L)
                eq2_lhs = a*L_val**2 + b*L_val + c
                eq2_rhs = L_val - k_val*L_val**3

                # Tính toán diện tích (Sử dụng hình vuông ngoại tiếp)
                S_hv = (2 * L_val)**2
                S_square_inner = (2 * R_val)**2
                S_shaded = P_val * S_hv

                # Phương trình 3: Tích phân diện tích
                integ_eval = integrate(x - f, (x, R_val, L_val))
                I_val = (S_shaded - S_square_inner) / 8

                const_term = integ_eval.subs({a:0, b:0, c:0})
                lhs_abc = integ_eval - const_term
                rhs_val = I_val - const_term

                # Giải hệ phương trình
                sol = solve((Eq(eq1_lhs, eq1_rhs), Eq(eq2_lhs, eq2_rhs), Eq(lhs_abc, rhs_val)), (a, b, c))
                a_val, b_val, c_val = sol[a], sol[b], sol[c]

                # Tính kết quả a+b+c
                kq_val = sp.simplify(a_val + b_val + c_val)
                kq = str(kq_val) # Vì a,b,c nguyên nên kết quả chắc chắn là chuỗi số nguyên đẹp

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # B4: Điều chỉnh các phương án sai (cộng trừ các số nguyên để không bị trùng)
                s_raw = [
                    kq_val + 1,
                    kq_val + 2,
                    kq_val + 3,
                    kq_val - 1,
                    kq_val - 2,
                    kq_val - 3
                ]
                s = ['$%s$' % (latex(val)) for val in s_raw]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Để chào mừng Ngày Quốc tế phụ nữ 8/3, bạn Bình muốn tự làm một món quà tặng mẹ. Từ một tấm bìa hình vuông cạnh $%s$ (dm), Bình dùng các đồ thị của hàm số $y=f\\left(x\\right)$ và $x=f\\left(y\\right)$ để vẽ hoa tặng mẹ, nhụy hoa được vẽ bằng đường tròn có tâm là tâm hình vuông và bán kính bằng $%s$ (dm). Khi đặt trong hệ trục tọa độ $Oxy$ thì điểm $A\\left(%s;0\\right)$ và đường cong $AB$ là một phần của đồ thị hàm đa thức bậc ba $y=f\\left(x\\right)=%sx^3+ax^2+bx+c$. Biết rằng tỷ lệ phần tô màu (gồm cánh và nhụy hoa) chiếm $%s$ diện tích hình vuông. Tổng $a+b+c$ bằng bao nhiêu?}
            {\\begin{tikzpicture}[scale=0.4, >=stealth, line width=1pt]
                \\def\\L{%s}
                \\def\\R{%s}
                \\draw (-\\L,-\\L) rectangle (\\L,\\L);
                \\fill[yellow!80] (\\R,0) to[out=0, in=225] (\\L,\\L) to[out=225, in=90] (0,\\R) arc (90:0:\\R);
                \\fill[yellow!80] (-\\R,0) to[out=180, in=-45] (-\\L,\\L) to[out=-45, in=90] (0,\\R) arc (90:180:\\R);
                \\fill[yellow!80] (-\\R,0) to[out=180, in=45] (-\\L,-\\L) to[out=45, in=-90] (0,-\\R) arc (270:180:\\R);
                \\fill[yellow!80] (\\R,0) to[out=0, in=135] (\\L,-\\L) to[out=135, in=-90] (0,-\\R) arc (270:360:\\R);
                \\fill[orange!40] (0,0) circle (\\R);
                \\draw (0,0) circle (\\R);
                \\draw (\\R,0) to[out=0, in=225] (\\L,\\L);
                \\draw (0,\\R) to[out=90, in=225] (\\L,\\L);
                \\draw (-\\R,0) to[out=180, in=-45] (-\\L,\\L);
                \\draw (0,\\R) to[out=90, in=-45] (-\\L,\\L);
                \\draw (-\\R,0) to[out=180, in=45] (-\\L,-\\L);
                \\draw (0,-\\R) to[out=-90, in=45] (-\\L,-\\L);
                \\draw (\\R,0) to[out=0, in=135] (\\L,-\\L);
                \\draw (0,-\\R) to[out=-90, in=135] (\\L,-\\L);
                \\node[left] at (\\R, 0) {$A$};
                \\node[above right] at (\\L, \\L) {$B$};
            \\end{tikzpicture}}''' % (2*L_val, R_val, R_val, latex(k_val), latex(P_val), L_val, R_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Diện tích hình vuông là $S = %s^2 = %s$ (dm$^2$).\\\\
            Diện tích hình vuông ngoại tiếp đường tròn (nhụy hoa) là $S_1 = %s^2 = %s$ (dm$^2$).\\\\
            Diện tích phần tô màu là $S_{td} = %s \\cdot %s = %s$ (dm$^2$).\\\\
            Diện tích phần tô màu nằm ngoài $S_1$ là $S_2 = S_{td} - S_1 = %s - %s = %s$ (dm$^2$).\\\\
            Gọi $B\\left(%s; %s\\right)$ là đỉnh của hình vuông ở góc phần tư thứ nhất.\\\\
            Do tính đối xứng, diện tích một mảnh của phần nằm ngoài $S_1$ dưới phân giác $y=x$ trên đoạn $\\left[%s; %s\\right]$ là $\\int_{%s}^{%s} \\left[ x - f\\left(x\\right) \\right] \\text{d}x$.\\\\
            Phần diện tích $S_2$ gồm $8$ mảnh như vậy, do đó ta có:
            $$S_2 = 8 \\int_{%s}^{%s} \\left[ x - f\\left(x\\right) \\right] \\text{d}x = 8 \\int_{%s}^{%s} \\left[ x - \\left(%sx^3+ax^2+bx+c\\right) \\right] \\text{d}x$$
            $$\\Rightarrow \\int_{%s}^{%s} \\left[ x - f\\left(x\\right) \\right] \\text{d}x = \\frac{%s}{8}$$
            Tính tích phân ta được phương trình: $%s = %s$ (1).\\\\
            Mặt khác, đồ thị hàm số đi qua $A\\left(%s; 0\\right)$ nên $f\\left(%s\\right) = 0 \\Leftrightarrow %s = %s$ (2).\\\\
            Đồ thị hàm số đi qua $B\\left(%s; %s\\right)$ nên $f\\left(%s\\right) = %s \\Leftrightarrow %s = %s$ (3).\\\\
            Từ (1), (2) và (3) ta có hệ phương trình. Giải hệ ta được $a = %s$, $b = %s$, $c = %s$.\\\\
            Vậy $a+b+c = %s$.''' % (
                    2*L_val, S_hv,
                    2*R_val, S_square_inner,
                    latex(P_val), S_hv, latex(S_shaded),
                    latex(S_shaded), S_square_inner, latex(S_shaded - S_square_inner),
                    L_val, L_val,
                    R_val, L_val, R_val, L_val,
                    R_val, L_val, R_val, L_val, latex(k_val),
                    R_val, L_val, latex(S_shaded - S_square_inner),
                    latex(lhs_abc), latex(rhs_val),
                    R_val, R_val, latex(eq1_lhs), latex(eq1_rhs),
                    L_val, L_val, L_val, L_val, latex(eq2_lhs), latex(eq2_rhs),
                    latex(a_val), latex(b_val), latex(c_val),
                    kq
                ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

