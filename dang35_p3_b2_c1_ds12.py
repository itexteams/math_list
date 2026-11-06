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


def bt_dang35_p3_b2_c1_ds12(self):
            # Khởi tạo biến
            x = symbols('x')  # x là tọa độ người chạy chậm

            ten = [
                "Minh", "Quang", "Hùng", "Tuấn", "Khôi", "Vũ", "Linh",
                "Nam", "Dũng", "Sơn", "Khoa", "Tài"
            ]
            vdv = random.sample(ten, 3)

            # Tập giá trị hợp lệ
            gtri_a = [Rational(2), Rational(22,10), Rational(5,2), Rational(14,5), Rational(3)]
            gtri_n = [Rational(3,2), Rational(2), Rational(5,2), Rational(3), Rational(7,2)]

            a = random.choice(gtri_a)
            n = random.choice(gtri_n)

            # Biểu thức góc giữa hai vận động viên từ điểm quan sát

            tangn = x/a
            tangl = tangn*n
            tu = tangl-tangn
            mau = 1+tangl*tangn
            tang = tu/mau
            # Lấy đạo hàm để tìm điểm cực trị
            dao_ham = diff(tang, x)
            nghiem = solve(dao_ham, x)

            x_max = next((x_nghiem for x_nghiem in nghiem if x_nghiem.is_real and x_nghiem > 0), None)

            if x_max is not None:
                tang_gt = tang.subs(x, x_max)
                goc = math.degrees(math.atan(float(tang_gt)))


            def roundvn(number, so_chu_so=1):
                # Làm tròn theo quy tắc ROUND_HALF_UP
                so_thap_phan = '0' * so_chu_so
                rounded = Decimal(str(number)).quantize(Decimal(f'0.{so_thap_phan}'), rounding=ROUND_HALF_UP)

                # Đổi dấu chấm thành dấu phẩy
                return str(rounded).replace('.', ',')

            def tp_vn(value):
                """Chuyển đổi số thành dạng có dấu phẩy và bỏ .0 nếu cần"""
                return str(int(value)) if value == int(value) else str(value).replace('.', ',')


            # ===== Nội dung câu hỏi =====
            noidungcauhoi = rf"""\immini{{Ông {vdv[0]}, người quan sát, đứng tại điểm $A$ cách đường chạy {tp_vn(float(a))}m. 
            Hai vận động viên {vdv[1]} và {vdv[2]} bắt đầu xuất phát từ điểm $H$ dọc theo đường chạy (như hình vẽ). 
            Biết anh {vdv[1]} chạy nhanh gấp {tp_vn(float(n))} lần anh {vdv[2]}. Tìm giá trị lớn nhất của góc nhìn $\alpha$ giữa hai vận động viên này từ vị trí của ông {vdv[0]} (làm tròn kết quả đến hàng phần mười của độ).}}
            {{	\begin{{tikzpicture}}[scale=3.2]
                    \coordinate (A) at (0,1);
                    \coordinate (H) at (0,0);
                    \coordinate (B) at (0.65,0);
                    \coordinate (C) at (1.6,0);
                    \draw (A) -- (H) -- (C);
                    \draw (A) -- (B);
                    \draw (A) -- (C);
                    \filldraw[black] (A) circle (0.5pt) node[above] {{$A$}};
                    \filldraw[black] (H) circle (0.5pt) node[below] {{$H$}};
                    \filldraw[black] (B) circle (0.5pt) node[below] {{$B$}};
                    \filldraw[black] (C) circle (0.5pt) node[below right] {{$C$}};
                    \node[left] at (0,0.4) {{{tp_vn(float(a))}m}};
                    \draw ($(H)+(0.1,0)$) -- +(0,0.1) -- +(-0.1,0.1);
                    \pic [draw, "$\alpha $", angle radius=1cm, angle eccentricity=1.2] {{angle = B--A--C}};
                \end{{tikzpicture}}}}"""
            # ===== Nội dung lời giải chi tiết =====
            loigiai = rf"""Gọi $x$ (m) là quãng đường $HB$ mà anh {vdv[1]} chạy được trong khoảng thời gian $t$, điều kiện: $x>0$.\\
            Khi đó, quãng đường $HC$ mà anh {vdv[2]} chạy được trong khoảng thời gian $t$ là ${latex(n*x)}$ (m).\\
            Ta có: $\tan \widehat{{HAB}} = \dfrac{{BH}}{{AH}}={latex(tangn)}; \tan \widehat{{HAC}} = \dfrac{{CH}}{{AH}}={latex(tangl)}$\\ 
            Suy ra $\tan \alpha =\dfrac{{{latex(tu)}}}{{{latex(mau)}}}={latex(tang)}$.\\
            Ta xét hàm số $f(x)={latex(tang)}$, với $x>0$.\\
            $f'(x)={latex(dao_ham)}$.\\
            $f'(x)=0 \Rightarrow x={latex(x_max)}$ (vì $x>0$).\\
            Dễ thấy $f(x)$ đồng biến trên khoảng $\left(0; {latex(x_max)}\right)$ và nghịch biến trên khoảng $\left({latex(x_max)};+ \infty\right)$. 
            Suy ra $\max\limits_{{(0;+\infty)}} f(x)= f\left({latex(x_max)}\right) \approx {tp_vn(round(tang_gt,3))} \Rightarrow \alpha \approx {roundvn(goc)}^{{\circ}}$\\
            Góc nhìn lớn nhất khoảng ${roundvn(goc)}^{{\circ}}$."""

            # ===== Đáp án ngắn gọn (LaTeX) =====
            dapan = r'\shortans[0]{$%s$}' % roundvn(goc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

