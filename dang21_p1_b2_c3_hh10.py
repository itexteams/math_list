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


def bt_dang21_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            x, y = symbols('x y')

            def sinh_bai_toan_dep():
                # Danh sách các bộ số (x0, y0, S) đảm bảo luôn có nghiệm hữu tỉ đẹp
                cac_bo_so = [
                    (2, 1, 4), (1, 2, 4), (4, 1, 1), (1, 4, 1),
                    (3, 2, 12), (2, 3, 12), (1, 1, 2), (2, 2, 8),
                    (4, 2, 16), (1, 2, 1), (2, 1, 1), (6, 3, 9)
                ]

                x0, y0, S = random.choice(cac_bo_so)
                a_sym, b_sym = symbols('a b', real=True)

                # Giải hệ bằng sympy: x0/a + y0/b = 1 và |ab| = 2S
                sol1 = solve([x0/a_sym + y0/b_sym - 1, a_sym*b_sym - 2*S], [a_sym, b_sym])
                sol2 = solve([x0/a_sym + y0/b_sym - 1, a_sym*b_sym + 2*S], [a_sym, b_sym])

                all_sols = sol1 + sol2
                ds_phuong_trinh = []
                chi_tiet_nghiem = [] # Lưu lại để trình bày lời giải

                for sa, sb in all_sols:
                    p = simplify(sb*x + sa*y - sa*sb)
                    if p.coeff(x) < 0: p = -p
                    ds_phuong_trinh.append(p)
                    chi_tiet_nghiem.append((sa, sb))

                ds_phuong_trinh = list(set(ds_phuong_trinh))
                return x0, y0, S, ds_phuong_trinh, chi_tiet_nghiem

            # --- Chạy hàm sinh dữ liệu ---
            x0, y0, S, list_pt, list_ab = sinh_bai_toan_dep()

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''Trong mặt phẳng với hệ tọa độ $Oxy$, phương trình đường thẳng $\Delta$ đi qua điểm $M(%s;%s)$ và tạo với các trục tọa độ một tam giác có diện tích bằng $%s$ là'''
                            %(latex(x0), latex(y0), latex(S)))

            # --- Đáp án đúng ---
            da_dung_str = " hoặc ".join([f"${latex(p)} = 0$" for p in list_pt])
            da_d = '\\True ' + da_dung_str

            # --- Đáp án nhiễu ---
            pt_mau = list_pt[0]
            da_s1 = f"${latex(simplify(pt_mau + random.randint(1,4)))} = 0$"
            da_s2 = f"${latex(simplify(y0*x + x0*y - x0*y0))} = 0$"
            if len(list_pt) > 1:
                da_s3 = f"${latex(simplify(list_pt[1] + 2))} = 0$"
            else:
                da_s3 = f"${latex(simplify(x - y + (x0-y0)))} = 0$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- CHI TIẾT LỜI GIẢI ---
            buoc_giai_ab = ""
            for i, (av, bv) in enumerate(list_ab):
                pt_tam = simplify(bv*x + av*y - av*bv)
                if pt_tam.coeff(x) < 0: pt_tam = -pt_tam
                buoc_giai_ab += rf" + Cặp $(a;b) = ({latex(av)}; {latex(bv)}) \Rightarrow \Delta: {latex(pt_tam)} = 0$.\\ "

            loigiai = (r'''Gọi phương trình đường thẳng $\Delta$ cần tìm có dạng: $\frac{x}{a} + \frac{y}{b} = 1$ ($a, b \neq 0$).\\
            Vì $M(%s; %s) \in \Delta$ nên ta có: $\frac{%s}{a} + \frac{%s}{b} = 1 \quad (*)$.\\
            Diện tích tam giác tạo với hai trục tọa độ là $S = \frac{1}{2}|ab| = %s \Leftrightarrow |ab| = %s \Leftrightarrow \left[\begin{aligned} &ab = %s \\ &ab = -%s \end{aligned}\right.$\\
            \textbf{Trường hợp 1:} $ab = %s \Rightarrow b = \frac{%s}{a}$. Thế vào $(*)$ ta được: \\
            $\frac{%s}{a} + \frac{%s a}{%s} = 1 \Leftrightarrow %s a^2 - %s a + %s = 0$. Giải phương trình tìm được các giá trị $a$ hữu tỉ.\\
            \textbf{Trường hợp 2:} $ab = -%s \Rightarrow b = -\frac{%s}{a}$. Thế vào $(*)$ ta được: \\
            $\frac{%s}{a} - \frac{%s a}{%s} = 1 \Leftrightarrow %s a^2 + %s a - %s = 0$. Giải phương trình tìm được các giá trị $a$ hữu tỉ.\\
            Sau khi tìm được các cặp $(a; b)$, ta có các phương trình đường thẳng thỏa mãn:\\
            %s 
            Vậy các đường thẳng cần tìm là: %s.''' 
                      %(x0, y0, x0, y0, S, 2*S, 2*S, 2*S, 
                        2*S, 2*S, x0, y0, 2*S, y0, 2*S, 2*S*x0, 
                        2*S, 2*S, x0, y0, 2*S, y0, 2*S, 2*S*x0, 
                        buoc_giai_ab, da_dung_str))

            # --- Xuất kết quả ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n')
            return content 

