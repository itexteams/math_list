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


def bt_dang25_p3_b2_c1_ds12(self):
            # Khai báo biến 
            a_choices = [round(2.0 + 0.2 * i, 1) for i in range(16)]     # từ 2.0 đến 5.0
            n_choices = [round(1.5 + 0.5 * i, 1) for i in range(7)]      # từ 1.5 đến 4.5

            # Chọn ngẫu nhiên
            a = random.choice(a_choices)
            n = random.choice(n_choices)

            # Số thập phân Việt Nam
            def tp_vn(value):
                """Chuyển đổi số thành dạng có dấu phẩy và bỏ .0 nếu cần"""
                return str(int(value)) if value == int(value) else str(value).replace('.', ',')

            # Tính kết quả
            x = sp.Symbol('x', positive=True)
            kq_expr = a * sp.cbrt(n) / (1 + sp.cbrt(n))
            kq = tp_vn(round(float(kq_expr), 2))  # làm tròn kết quả đến hàng phần trăm



            # ===== Nội dung câu hỏi =====
            noidungcauhoi = f"""Giả sử hai nguồn sáng $S_1$, $S_2$ đặt cách nhau {tp_vn(a)} mét, trong đó nguồn $S_1$ mạnh gấp {tp_vn(n)} lần nguồn $S_2$.
            Cường độ chiếu sáng của một vật do một nguồn sáng gây ra tỉ lệ thuận với độ mạnh của nguồn sáng và tỉ lệ nghịch với bình phương khoảng cách từ vật đến nguồn sáng.
            Hỏi nên đặt vật trên đoạn nối hai nguồn và gần $S_1$ bao nhiêu mét để vật nhận được ít ánh sáng nhất? (kết quả làm tròn đến hàng phần trăm)."""

            # ===== Nội dung lời giải chi tiết =====
            loigiai = rf"""Gọi $x$ (mét) là khoảng cách từ vật đến nguồn sáng $S_1$. Khi đó khoảng cách từ vật đến $S_2$ là ${tp_vn(a)}-x$. Điều kiện: $0<x<{tp_vn(a)}$.\\
            Giả sử nguồn $S_2$ có cường độ chiếu sáng là $I$ ($I>0$). Khi đó nguồn $S_1$ có cường độ chiếu sáng là ${tp_vn(n)}I$. \\
            Tổng cường độ chiếu sáng đến vật là:
            \[S(x) = \frac{{{tp_vn(n)}I}}{{x^2}} + \frac{{I}}{{({tp_vn(a)} - x)^2}}\]
            Do $I$ là hằng số nên ta xét hàm số $f(x)=\frac{{{tp_vn(n)}}}{{x^2}} + \frac{{1}}{{({tp_vn(a)} - x)^2}}$.
            Ta có: 
            \[f'(x) = \frac{{-2 \cdot {tp_vn(n)}}}{{x^3}} + \frac{{2}}{{({tp_vn(a)} - x)^3}} = 0
            \Rightarrow \left(\frac{{x}}{{{tp_vn(a)} - x}}\right)^3 = {tp_vn(n)}\]
            hay
            \[\frac{{x}}{{{tp_vn(a)} - x}} = \sqrt[3]{{{tp_vn(n)}}} \Rightarrow x = \frac{{{tp_vn(a)} \cdot \sqrt[3]{{{tp_vn(n)}}}}}{{1 + \sqrt[3]{{{tp_vn(n)}}}}} \approx {kq}\]
            Bảng biến thiên:
            \begin{{center}}
            \begin{{tikzpicture}}
                \foreach \x/\t in {{1.2/x, 3/{{0}}, 5/{{{kq}}}, 7/{{{tp_vn(a)}}}}}
                \node at (\x,4.2) {{$\t$}};
                \foreach \x/\t in {{3.8/{{-}}, 5/{{0}}, 6.2/{{+}}}}
                \node at (\x,3.5) {{$\t$}};
                \foreach \x/\t in {{3/+\infty,7/+\infty}}
                \node at (\x,2.6) {{$\t$}};
                \node at (1.2,3.5) {{$f'(x)$}};  
                \node at (1.2,2.6) {{$f(x)$}};
                \node (A) at (5,0.5) {{$f({kq})$}};
                \draw[-stealth] (3,2.4) -- (A);
                \draw[-stealth] (A) -- (7,2.4);
                \draw (0,4.5) rectangle (8,0);
                \draw (0,3.9) -- (8,3.9);
                \draw (0,3.2) -- (8,3.2);
                \draw (2.2,4.5) -- (2.2,0);    
            \end{{tikzpicture}}
            \end{{center}}
            Suy ra giá trị nhỏ nhất của hàm số $y=f(x)$ trên khoảng $(0;{tp_vn(a)})$ là $f({kq})$.\\
            Vậy ta nên đặt vật gần $S_1$ khoảng {kq} mét để vật nhận được ít ánh sáng nhất."""

            # ===== Đáp án ngắn gọn (LaTeX) =====
            dapan = r'\shortans[0]{$%s$}' % sp.latex(kq)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

