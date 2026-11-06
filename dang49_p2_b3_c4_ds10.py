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


def bt_dang49_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến SymPy
            x, y = symbols('x y')

            # --- BƯỚC 1: RANDOM CÁC THÔNG SỐ CƠ BẢN ---
            # Chọn cạnh hình vuông L là số nguyên chẵn để tính toán đẹp (ví dụ từ 6 đến 12)
            L = random.choice([6, 8, 10, 12])

            # Chọn AE (ae) và BF (bf) sao cho hình ảnh cân đối
            ae = random.randint(2, L // 3) 
            bf = random.randint(L // 2 - 1, L // 2 + 1)

            # Các đoạn phụ thuộc
            eb = L - ae
            cf = L - bf

            # --- BƯỚC 2: TỰ ĐỘNG TÍNH TOÁN BIỂU THỨC ---
            # Diện tích 4 tam giác góc:
            # S1 (AEH) = 1/2 * ae * x
            # S2 (BEF) = 1/2 * eb * bf
            # S3 (CFG) = 1/2 * cf * y
            # S4 (DGH) = 1/2 * (L-y) * (L-x)

            # Biểu thức 2S = 2*(L^2 - (S1+S2+S3+S4))
            # Sau khi khai triển: 2S = L^2 - eb*bf + eb*x + bf*y - x*y
            const_term = L**2 - eb * bf
            expr_2S_dung = -x*y + eb*x + bf*y + const_term
            expr_2S_sai = x*y - eb*x - bf*y + const_term + random.randint(2, 5)

            # Điều kiện EH // FG (Hình thang): ae/y = x/cf => xy = ae * cf
            k_val = ae * cf # hằng số k trong xy = k

            # Tính giá trị x, y để S min (theo BĐT Cauchy cho: eb*x + bf*y)
            # Ta có y = k/x => f(x) = eb*x + bf*(k/x)
            # f(x) min khi eb*x = bf*k/x => x^2 = (bf*k)/eb
            x_min_sq = Rational(bf * k_val, eb)
            x_val = sqrt(x_min_sq)
            y_val = k_val / x_val
            tong_xy_min = simplify(x_val + y_val)

            # --- BƯỚC 3: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = r'''Cho một tấm nhôm hình vuông cạnh $%s$ cm. Người ta muốn cắt một hình thang như hình vẽ. Ký hiệu $S$ là diện tích hình thang $EFGH$.
            \begin{center}
            \begin{tikzpicture}[scale=0.6, font=\footnotesize]
                \draw[thick] (0,4) node[above left]{$A$} -- (4,4) node[above right]{$B$} -- (4,0) node[below right]{$C$} -- (0,0) node[below left]{$D$} -- cycle;
                \coordinate (E) at (1.2,4);
                \coordinate (H) at (0,2.8);
                \coordinate (F) at (4,2.2);
                \coordinate (G) at (2.5,0);
                \fill[orange!30] (E) -- (F) -- (G) -- (H) -- cycle;
                \draw[thick] (E) -- (F) -- (G) -- (H) -- cycle;
                \node[above] at (E) {$E$}; \node[right] at (F) {$F$}; \node[below] at (G) {$G$}; \node[left] at (H) {$H$};
                \node[above] at (0.6,4) {$%s$ cm};
                \node[right] at (4,3.1) {$%s$ cm};
                \node[left, blue] at (0,3.4) {$x$ cm};
                \node[below, blue] at (3.2,0) {$y$ cm};
            \end{tikzpicture}
            \end{center}''' % (L, ae, bf)

            # --- BƯỚC 4: CÁC ĐÁP ÁN ---
            # NHẬN BIẾT
            nb_da_1_d = r'\True Biểu thức diện tích hình thang theo $x, y$ là $2S = %s$' % latex(expr_2S_dung)
            nb_da_1_s = r'Biểu thức diện tích hình thang theo $x, y$ là $2S = %s$' % latex(expr_2S_sai)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = r'''Diện tích hình vuông $S_{ABCD} = %s^2 = %s$. Tổng diện tích 4 tam giác trắng ở góc là: \\
            $S_1+S_2+S_3+S_4 = \frac{1}{2}%sx + \frac{1}{2}(%s \cdot %s) + \frac{1}{2}%sy + \frac{1}{2}(%s-x)(%s-y)$. \\
            Rút gọn ta được $2S = 2S_{ABCD} - 2(S_1+S_2+S_3+S_4) = %s$.''' % (L, L**2, ae, eb, bf, cf, L, L, latex(expr_2S_dung))

            # THÔNG HIỂU
            th_da_1_d = r'\True Để $EFGH$ là hình thang ($EH \parallel FG$) thì $xy = %s$' % k_val
            th_da_1_s = r'Để $EFGH$ là hình thang ($EH \parallel FG$) thì $x + y = %s$' % k_val
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = r'''Để $EH \parallel FG$, theo định lý Ta-lét trong tam giác hoặc tọa độ hóa, ta cần tỉ lệ: \\ $\frac{AE}{AH} = \frac{CG}{CF} \Rightarrow \frac{%s}{x} = \frac{y}{%s} \Rightarrow xy = %s$.''' % (ae, cf, k_val)

            # VẬN DỤNG
            vd_da_1_d = r'\True Khi diện tích $S$ nhỏ nhất thì tổng $x + y = %s$' % latex(tong_xy_min)
            vd_da_1_s = r'Khi diện tích $S$ nhỏ nhất thì tổng $x + y = %s$' % latex(tong_xy_min + 1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = r'''Thay $y = \dfrac{%s}{x}$ vào $2S$, ta có $2S = %s + %sx + %s \left(\frac{%s}{x} \right) - %s$. \\
            Áp dụng BĐT Cauchy cho hai số dương $%sx$ và $\frac{%s}{x}$, dấu "=" xảy ra khi $x = %s$, suy ra $y = %s$. \\
            Vậy $x+y = %s$.''' % (k_val, const_term, eb, bf, k_val, k_val, eb, bf*k_val, latex(x_val), latex(y_val), latex(tong_xy_min))

            # VẬN DỤNG CAO
            vdc_da_1_d = r'\True Giá trị nhỏ nhất của diện tích $S$ là một số vô tỉ'
            vdc_da_1_s = r'Giá trị nhỏ nhất của diện tích $S$ là một số nguyên'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            # Tính S_min để đưa vào lời giải
            s_min_val = (const_term - k_val + 2*sqrt(eb*bf*k_val))/2
            loigiai_vdc_1 = r'''Từ biểu thức $2S$, ta tính được $S_{min} = \frac{%s - %s + 2\sqrt{%s \cdot %s \cdot %s}}{2} \approx %s$. Đây là một số vô tỉ.''' % (const_term, k_val, eb, bf, k_val, round(float(s_min_val), 2))

            # --- BƯỚC 5: XỬ LÝ ĐÁP ÁN ĐÚNG/SAI & XUẤT BẢN ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

