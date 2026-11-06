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


def bt_dang45_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các kịch bản kích thước để hình vẽ TikZ luôn hợp lý và giữ tỷ lệ đẹp như gốc
                configs = [
                    {'L': 54, 'L1': 24, 'H': 28, 'H1': 12, 'W': 36, 'lg': 20, 'wg': 16, 'R': 11},
                    {'L': 60, 'L1': 30, 'H': 30, 'H1': 10, 'W': 40, 'lg': 25, 'wg': 20, 'R': 15},
                    {'L': 50, 'L1': 20, 'H': 26, 'H1': 14, 'W': 30, 'lg': 15, 'wg': 10, 'R': 10},
                    {'L': 56, 'L1': 26, 'H': 25, 'H1': 10, 'W': 34, 'lg': 22, 'wg': 14, 'R': 12}
                ]
                cfg = random.choice(configs)

                L = cfg['L']
                L1 = cfg['L1']
                H = cfg['H']
                H1 = cfg['H1']
                W = cfg['W']
                lg = cfg['lg']
                wg = cfg['wg']
                R = cfg['R']
                H2 = H - H1

                # Tính toán thể tích
                V_base_full = L * W * H1
                V_groove = lg * wg * H1
                V1 = V_base_full - V_groove

                V_top_full = L1 * W * H2
                V_cyl_coeff = int((R**2) * H2 / 2) # Hệ số của pi

                V_total_num = V1 + V_top_full
                V_val = V_total_num - V_cyl_coeff * math.pi
                kq_ratio = V_val / 2025
                kq_final = int(round(kq_ratio))

                # Các đáp án trắc nghiệm
                da = kq_final
                du = ['$%s$' % (da)]
                da_d = random.choice(du)

                # Sinh các phương án sai ngẫu nhiên
                s = ['$%s$' % (da + 1),
                     '$%s$' % (da + 2),
                     '$%s$' % (da + 3),
                     '$%s$' % (da - 1),
                     '$%s$' % (da - 2),
                     '$%s$' % (da - 3)]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi (Bao gồm mã vẽ TikZ với các tham số tương ứng)
                noidungcauhoi = ('''Một chi tiết máy có các hình chiếu đứng, hình chiếu cạnh và hình chiếu bằng như hình vẽ sau (các kích thước cho như trong hình vẽ). Gọi $V$ là thể tích kim loại cần để đúc chi tiết máy đó. Tính giá trị của $\\frac{V}{2025}$ (kết quả làm tròn đến hàng đơn vị).
            \\begin{center} \\scalebox{0.6}{ 
            \\begin{tikzpicture}[scale=0.15, font=\\footnotesize, line width=1pt]
            \\def\\L{%s}
            \\def\\Lone{%s}
            \\def\\H{%s}
            \\def\\Hone{%s}
            \\def\\W{%s}
            \\def\\lg{%s}
            \\def\\wg{%s}
            \\def\\R{%s}
            \\def\\Dgap{15}
            \\pgfmathsetmacro{\\Ltwo}{\\L - \\Lone}
            \\pgfmathsetmacro{\\Htwo}{\\H - \\Hone}
            \\pgfmathsetmacro{\\Whalf}{\\W / 2}
            \\pgfmathsetmacro{\\wghalf}{\\wg / 2}
            \\pgfmathsetmacro{\\Wgap}{\\Dgap + \\W}
            \\pgfmathsetmacro{\\cx}{\\Ltwo}
            \\pgfmathsetmacro{\\cy}{-\\Dgap - \\Whalf}
            \\draw (0,0) -- (\\L,0) -- (\\L,\\H) -- (\\Ltwo,\\H) -- (\\Ltwo,\\Hone) -- (0,\\Hone) -- cycle;
            \\draw[dashed] (\\lg, 0) -- (\\lg, \\Hone);
            \\draw[dashed] (\\Ltwo+\\R, \\Hone) -- (\\Ltwo+\\R, \\H);
            \\draw[dash dot, thin, magenta] (\\Ltwo, \\Hone - 2) -- (\\Ltwo, \\H + 2);
            \\draw (0, -\\Dgap) rectangle (\\L, -\\Dgap-\\W);
            \\draw (\\Ltwo, -\\Dgap) -- (\\Ltwo, \\cy+\\R);
            \\draw (\\Ltwo, \\cy-\\R) -- (\\Ltwo, -\\Dgap-\\W);
            \\draw (0, \\cy+\\wghalf) -- (\\lg, \\cy+\\wghalf) -- (\\lg, \\cy-\\wghalf) -- (0, \\cy-\\wghalf);
            \\draw (\\lg, \\cy+\\wghalf) -- (\\lg, \\cy-\\wghalf);
            \\draw (\\Ltwo, \\cy-\\R) arc (-90:90:\\R);
            \\draw[dash dot, thin, magenta] (-2, \\cy) -- (\\L+2, \\cy);
            \\draw[dash dot, thin, magenta] (\\Ltwo, \\cy+\\R+2) -- (\\Ltwo, \\cy-\\R-2);
            \\def\\Sx{\\L + \\Dgap}
            \\draw (\\Sx, 0) rectangle (\\Sx+\\W, \\H);
            \\draw (\\Sx, \\Hone) -- (\\Sx+\\Whalf-\\wghalf, \\Hone);
            \\draw (\\Sx+\\Whalf+\\wghalf, \\Hone) -- (\\Sx+\\W, \\Hone);
            \\draw (\\Sx+\\Whalf-\\wghalf, \\Hone) -- (\\Sx+\\Whalf-\\wghalf, 0);
            \\draw (\\Sx+\\Whalf+\\wghalf, \\Hone) -- (\\Sx+\\Whalf+\\wghalf, 0);
            \\draw (\\Sx+\\Whalf-\\wghalf, \\Hone) -- (\\Sx+\\Whalf+\\wghalf, \\Hone);
            \\draw[dashed] (\\Sx+\\Whalf-\\R, \\Hone) -- (\\Sx+\\Whalf-\\R, \\H);
            \\draw[dashed] (\\Sx+\\Whalf+\\R, \\Hone) -- (\\Sx+\\Whalf+\\R, \\H);
            \\draw[dash dot, thin, magenta] (\\Sx+\\Whalf, -2) -- (\\Sx+\\Whalf, \\H+2);
            \\begin{scope}[draw=magenta, thin, solid]
            \\draw (\\Sx, -\\Dgap) -- (\\Sx+\\W, -\\Dgap-\\W);
            \\draw (\\L, -\\Dgap) -- (\\Sx, -\\Dgap) -- (\\Sx, 0);
            \\draw (\\L, -\\Dgap-\\W) -- (\\Sx+\\W, -\\Dgap-\\W) -- (\\Sx+\\W, 0);
            \\draw (\\L, \\cy) -- (\\Sx+\\Whalf, \\cy) -- (\\Sx+\\Whalf, 0);
            \\draw (\\lg, \\cy+\\wghalf) -- (\\Sx+\\Whalf-\\wghalf, \\cy+\\wghalf) -- (\\Sx+\\Whalf-\\wghalf, 0);
            \\draw (\\lg, \\cy-\\wghalf) -- (\\Sx+\\Whalf+\\wghalf, \\cy-\\wghalf) -- (\\Sx+\\Whalf+\\wghalf, 0);
            \\draw (\\Ltwo, \\cy+\\R) -- (\\Sx+\\Whalf-\\R, \\cy+\\R) -- (\\Sx+\\Whalf-\\R, \\Hone);
            \\draw (\\Ltwo, \\cy-\\R) -- (\\Sx+\\Whalf+\\R, \\cy-\\R) -- (\\Sx+\\Whalf+\\R, \\Hone);
            \\end{scope}
            \\begin{scope}[>=stealth, thin]
            \\draw[<->] (0, \\H+5) -- (\\L, \\H+5) node[midway, above] {$\\L$};
            \\draw[dashed] (0, \\H) -- (0, \\H+6);
            \\draw[dashed] (\\L, \\H) -- (\\L, \\H+6);
            \\draw[<->] (\\Ltwo, \\H+2.5) -- (\\L, \\H+2.5) node[midway, above] {$\\Lone$};
            \\draw[dashed] (\\Ltwo, \\H) -- (\\Ltwo, \\H+3.5);
            \\draw[<->] (-5, 0) -- (-5, \\Hone) node[midway, left] {$\\Hone$};
            \\draw[dashed] (0, 0) -- (-6, 0);
            \\draw[dashed] (0, \\Hone) -- (-6, \\Hone);
            \\draw[<->] (0, -\\Dgap/2) -- (\\lg, -\\Dgap/2) node[midway, above] {$\\lg$};
            \\draw[dashed] (0, -\\Dgap) -- (0, -\\Dgap/2+1);
            \\draw[dashed] (\\lg, -\\Dgap) -- (\\lg, -\\Dgap/2+1);
            \\draw[<->] (-5, -\\Dgap) -- (-5, -\\Dgap-\\W) node[midway, left] {$\\W$};
            \\draw[dashed] (0, -\\Dgap) -- (-6, -\\Dgap);
            \\draw[dashed] (0, -\\Dgap-\\W) -- (-6, -\\Dgap-\\W);
            \\draw[<->] (-2.5, \\cy+\\wghalf) -- (-2.5, \\cy-\\wghalf) node[midway, fill=white, inner sep=1pt] {$\\wg$};
            \\draw[dashed] (0, \\cy+\\wghalf) -- (-3.5, \\cy+\\wghalf);
            \\draw[dashed] (0, \\cy-\\wghalf) -- (-3.5, \\cy-\\wghalf);
            \\draw[<-] ( \\Ltwo + \\R*0.707, \\cy + \\R*0.707 ) -- (\\Ltwo - 2, \\cy + \\R + 16) -- (\\Ltwo - 12, \\cy + \\R + 16) node[midway, above, inner sep=1pt] {R$\\R$};
            \\draw[<->] (\\Sx+\\W+5, 0) -- (\\Sx+\\W+5, \\H) node[midway, right] {$\\H$};
            \\draw[dashed] (\\Sx+\\W, 0) -- (\\Sx+\\W+6, 0);
            \\draw[dashed] (\\Sx+\\W, \\H) -- (\\Sx+\\W+6, \\H);
            \\draw[<->] (\\Sx+\\W+2.5, 0) -- (\\Sx+\\W+2.5, \\Hone) node[midway, right] {$\\Hone$};
            \\draw[dashed] (\\Sx+\\W, \\Hone) -- (\\Sx+\\W+3.5, \\Hone);
            \\draw[<->] (\\Sx, -\\Dgap/2) -- (\\Sx+\\W, -\\Dgap/2) node[midway, below] {$\\W$};
            \\draw[dashed] (\\Sx, 0) -- (\\Sx, -\\Dgap/2-1);
            \\draw[dashed] (\\Sx+\\W, 0) -- (\\Sx+\\W, -\\Dgap/2-1);
            \\draw[<->] (\\Sx+\\Whalf-\\wghalf, -\\Dgap/4) -- (\\Sx+\\Whalf+\\wghalf, -\\Dgap/4) node[midway, below] {$\\wg$};
            \\draw[dashed] (\\Sx+\\Whalf-\\wghalf, 0) -- (\\Sx+\\Whalf-\\wghalf, -\\Dgap/4-1);
            \\draw[dashed] (\\Sx+\\Whalf+\\wghalf, 0) -- (\\Sx+\\Whalf+\\wghalf, -\\Dgap/4-1);
            \\end{scope}
            \\end{tikzpicture} }
            \\end{center}''' % (L, L1, H, H1, W, lg, wg, R))

                # Xử lý format mảng đáp án
                da_d = ('\\True ' + str(da_d))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (có đổi dấy chấm thập phân sang dấu phẩy)
                loigiai = ('''Chia chi tiết máy thành $2$ khối để tính thể tích: khối phần đế (phía dưới) và khối phần trên. \\\\
            - Khối phần đế: Là một khối hộp chữ nhật có kích thước $L \\times W \\times H_1 = %s \\times %s \\times %s$, bị khoét đi một khối hộp chữ nhật ở giữa có kích thước $l_g \\times w_g \\times H_1 = %s \\times %s \\times %s$. \\\\
            $\\Rightarrow$ Thể tích phần đế là: 
            $V_1 = %s \\cdot %s \\cdot %s - %s \\cdot %s \\cdot %s = %s - %s = %s$. \\\\
            - Khối phần trên: Là một khối hộp chữ nhật có kích thước $L_1 \\times W \\times H_2 = %s \\times %s \\times %s$ (với $H_2 = H - H_1 = %s - %s = %s$), bị khoét đi một nửa khối trụ đứng có bán kính đáy $R = %s$ và chiều cao $H_2 = %s$. \\\\
            $\\Rightarrow$ Thể tích phần trên là:
            $V_2 = %s \\cdot %s \\cdot %s - \\frac{1}{2} \\pi R^2 H_2 = %s - \\frac{1}{2} \\pi \\cdot %s^2 \\cdot %s = %s - %s\\pi$. \\\\
            Thể tích của toàn bộ chi tiết máy là: \\\\
            $V = V_1 + V_2 = %s + %s - %s\\pi = %s - %s\\pi \\approx %s$. \\\\
            Giá trị cần tính là: $\\frac{V}{2025} \\approx \\frac{%s}{2025} \\approx %s$. \\\\
            Làm tròn kết quả đến hàng đơn vị, ta được $%s$.''' %
                (L, W, H1, lg, wg, H1,
                 L, W, H1, lg, wg, H1, V_base_full, V_groove, V1,
                 L1, W, H2, H, H1, H2, R, H2,
                 L1, W, H2, V_top_full, R, H2, V_top_full, V_cyl_coeff,
                 V1, V_top_full, V_cyl_coeff, V_total_num, V_cyl_coeff, str(round(V_val, 2)).replace('.', ','),
                 str(round(V_val, 2)).replace('.', ','), str(round(kq_ratio, 3)).replace('.', ','),
                 kq_final))
                dapan='\\shortans[0]{$%s$}\n'%(kq_final)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

