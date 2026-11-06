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


def bt_dang21_p3_b1_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tọa độ điểm A trên cột đèn và bóng đèn I
                # Đảm bảo S không phải là số chính phương để giữ lại dấu căn giống mẫu
                x_a = random.choice([1, 2, 3, 4])
                y_a = random.choice([1, 2, 3, 4])
                z_a = random.choice([1, 2])

                # dz là khoảng cách từ A đến I (đơn vị 100m)
                dz = random.choice([3, 4, 5])
                z_i = z_a + dz

                # Bán kính R_int phải lớn hơn khoảng cách d(I, P)
                # d(I,P) xấp xỉ dz, nên chọn R_int lớn hơn dz
                R_int = dz + random.choice([1, 2, 3])

                # Các giá trị đề bài
                R_cover = R_int * 100
                dist_IA_m = dz * 100
                S = x_a**2 + y_a**2 + z_a**2

                # Tính toán Vector bằng SymPy
                OA = sp.Matrix([x_a, y_a, z_a])
                k_vec = sp.Matrix([0, 0, 1])

                ud = OA.cross(k_vec)
                nP = ud.cross(OA)

                # Biểu diễn phương trình mặt phẳng (P)
                x_sym, y_sym, z_sym = sp.symbols('x y z')
                eq_P = nP[0]*x_sym + nP[1]*y_sym + nP[2]*z_sym
                eq_P_latex = sp.latex(eq_P)

                # Tính khoảng cách d(I, (P))
                num_d = abs(nP[0]*x_a + nP[1]*y_a + nP[2]*z_i)
                den_d_sq = nP[0]**2 + nP[1]**2 + nP[2]**2

                d_val_sym = sp.Rational(num_d, 1) / sp.sqrt(den_d_sq)
                d_latex = sp.latex(sp.simplify(d_val_sym))

                # Tính bán kính đường tròn giao tuyến r
                d_val_float = float(num_d) / float(sp.sqrt(den_d_sq).evalf())
                r_val = sp.sqrt(R_int**2 - d_val_float**2)

                # Bán kính thực tế (m)
                r_meter = r_val * 100
                kq_int = int(Decimal(str(float(r_meter))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                r_approx_comma = f"{float(r_val):.2f}".replace('.', ',')

                # Các đáp án trắc nghiệm
                da = str(kq_int)
                wrong_offsets = [1, -1, 2, -2, 5, -5, 10, -10, 15, -15]
                s_list = []
                for offset in wrong_offsets:
                    w_val = kq_int + offset
                    if w_val > 0 and w_val != kq_int:
                        s_list.append(str(w_val))

                # Lọc trùng và chọn 3 phương án sai
                s_list = list(set(s_list))
                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Vẽ mặt cắt bằng TikZ
                tikz_code = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=0.8, line width=1pt]\n'
                    '    \\draw (0,0) circle (2.5);\n'
                    '    \\draw (-3,-1) -- (3,-1) node[above left, pos=0.1] {$(P)$};\n'
                    '    \\coordinate (I) at (0,0.5);\n'
                    '    \\fill (I) circle (1.5pt) node[above] {$I$};\n'
                    '    \\coordinate (H) at (0,-1);\n'
                    '    \\fill (H) circle (1.5pt);\n'
                    '    \\draw (I) -- (H) node[midway, right] {$d$};\n'
                    '    \\coordinate (M) at (-2.14,-1);\n'
                    '    \\fill (M) circle (1.5pt);\n'
                    '    \\draw (I) -- (M) node[midway, above left] {$R$};\n'
                    '    \\draw (M) -- (H) node[midway, below] {$r$};\n'
                    '    \\draw (0,-0.8) -- (0.2,-0.8) -- (0.2,-1);\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một chiếc đèn đường có bán kính phủ sáng là $%s$ m (ánh sáng phát ra từ đèn là các chùm ánh sáng toả ra từ bóng đèn) và vị trí của bóng đèn được xác định trên hệ trục toạ độ $Oxyz$ (đơn vị trên mỗi trục là $100$ mét) là $I(%s; %s; %s)$ và gốc toạ độ $O$ là một điểm trên mặt đất. Giả sử cột đèn có dạng đường thẳng đứng, hướng lên và mặt đất là mặt phẳng $(Oxy)$. Người đặt một tấm bạt hứng sáng đủ lớn sao cho tấm bạt đi qua gốc toạ độ và một điểm nằm trên cột đèn, cách bóng đèn $%s$ m, đồng thời tấm bạt tạo với mặt đất một góc $\\alpha$ có $\\sin \\alpha = \\frac{%s}{\\sqrt{%s}}$. Xem tấm bạt là một mặt phẳng. Khi đó, ánh sáng từ đèn được tấm bạt hứng vào tạo thành một hình tròn. Bán kính của hình tròn đó bằng bao nhiêu mét? (Kết quả làm tròn đến hàng đơn vị).'''
                                 % (R_cover, x_a, y_a, z_i, dist_IA_m, z_a, S))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi tấm bạt là một mặt phẳng $(P)$, theo đề ta có $(P)$ đi qua điểm $O(0; 0; 0)$, điểm $A(%s; %s; %s)$ và tạo với mặt phẳng $(Oxy)$ một góc $\\alpha$ có $\\sin \\alpha = \\frac{%s}{\\sqrt{%s}}$. \\\\
            Ta có đường thẳng $OA$ có vectơ chỉ phương $\\overrightarrow{OA} = (%s; %s; %s)$ và mặt phẳng $(Oxy)$ có vectơ pháp tuyến $\\vec{k} = (0; 0; 1)$. \\\\
            Khi đó: $\\sin(OA; (Oxy)) = \\frac{|%s \\cdot 0 + %s \\cdot 0 + %s \\cdot 1|}{\\sqrt{%s^2 + %s^2 + %s^2}} = \\frac{%s}{\\sqrt{%s}}$ suy ra $(OA; (Oxy)) = ((P); (Oxy))$. \\\\
            Suy ra giao tuyến của $(P)$ và $(Oxy)$ vuông góc với $OA$. \\\\
            Gọi $d = (P) \\cap (Oxy) \\Rightarrow \\begin{cases} \\vec{u_d} \\perp \\overrightarrow{OA} \\\\ \\vec{u_d} \\perp \\vec{k} \\end{cases} \\Rightarrow \\vec{u_d} = [\\overrightarrow{OA}, \\vec{k}] = (%s; %s; %s)$. \\\\
            Ta có $\\begin{cases} d \\subset (P) \\\\ OA \\subset (P) \\end{cases} \\Rightarrow \\begin{cases} \\vec{n_P} \\perp \\vec{u_d} \\\\ \\vec{n_P} \\perp \\overrightarrow{OA} \\end{cases} \\Rightarrow \\vec{n_P} = [\\vec{u_d}, \\overrightarrow{OA}] = (%s; %s; %s)$ nên $(P): %s = 0$. \\\\
            Do bóng đèn có bán kính phủ sáng là $%s$ m nên vùng ánh sáng chiếu ra có dạng một hình cầu tâm $I(%s; %s; %s)$, bán kính $R = %s$. Ta có: \\\\
            $d(I; (P)) = \\frac{|%s \\cdot %s + %s \\cdot %s + %s \\cdot %s|}{\\sqrt{(%s)^2 + (%s)^2 + %s^2}} = %s$.
            %s
            Gọi bán kính đường tròn giao tuyến là $r$ rồi áp dụng định lý Pytago, ta có: \\\\
            $r = \\sqrt{R^2 - d^2} = \\sqrt{%s^2 - \\left(%s\\right)^2} \\approx %s$. \\\\
            Vậy bán kính đường tròn thu được trên tấm bạt là $%s$ (m).'''
                           % (x_a, y_a, z_a, z_a, S,
                              x_a, y_a, z_a, 
                              x_a, y_a, z_a, x_a, y_a, z_a, z_a, S,
                              ud[0], ud[1], ud[2],
                              nP[0], nP[1], nP[2], eq_P_latex,
                              R_cover, x_a, y_a, z_i, R_int,
                              nP[0], x_a, nP[1], y_a, nP[2], z_i, nP[0], nP[1], nP[2], d_latex,
                              tikz_code,
                              R_int, d_latex, r_approx_comma, kq_int))
                dapan='\\shortans[0]{$%s$}\n'%(kq_int)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

