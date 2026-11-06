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


def bt_dang26_p3_b2_c1_ds12(self):
            # Khai báo biến 
            # Tập giá trị phân số có thể chọn
            a_values = [Rational(5, 2), 3, Rational(3, 2), 4]
            b_values = [1, Rational(5, 4), Rational(3, 2), Rational(7, 4), 2]

            # Lấy ngẫu nhiên
            a = random.choice(a_values)
            b = random.choice(b_values)

            # Định nghĩa hàm f(x)
            f = (a**2 * (x + b)**2) / x**2 + (x + b)**2

            # Tính đạo hàm
            dh_f = sp.diff(f, x)

            # Rút gọn thành một phân số duy nhất
            dh_gon = sp.together(sp.simplify(dh_f))

            # Giải phương trình f'(x) = 0
            solutions = sp.solve(dh_f, x)

            # Lọc nghiệm thực và sắp xếp thứ tự
            nghiem_dh = [sol for sol in solutions if sp.im(sol) == 0]
            sap_xep = sorted(nghiem_dh, key=lambda sol: sol.evalf())
            AB_min = round(sp.sqrt(f.subs(x, sap_xep[-1])),2)

            # Số thập phân Việt Nam
            def tp_vn(value):
                """Chuyển đổi số thành dạng có dấu phẩy và bỏ .0 nếu cần"""
                return str(int(value)) if value == int(value) else str(value).replace('.', ',')

            # ===== Nội dung câu hỏi =====
            noidungcauhoi = rf""" Một hàng rào $CD$ cao {tp_vn(float(a))} m được đặt song song với toà nhà và cách tòa nhà một đoạn $ED={tp_vn(float(b))}$ m (hình vẽ minh hoạ). 
            \begin{{center}}
            \begin{{tikzpicture}}[scale=0.8]
                \draw[thick] (-2,0) -- (8,0);
                \fill[gray!30] (-1.6,0) rectangle (1.6,7.5);     
                \fill[gray!60] (-1.8,7.5) rectangle (1.8,7.8);    
                \fill[gray!50] (-0.8,0) rectangle (0.8,1.2);      
                \foreach \x in {{-1.2, -0.4, 0.4}}
                \foreach \y in {{1.6, 3.0, 4.4, 5.8}}
                \fill[cyan!50] (\x,\y) rectangle ++(0.6,0.9);
                \coordinate (E) at (1.6,0);                
                \coordinate (A) at (1.6,2.5);              
                \coordinate (B) at (7.2,0);                
                \coordinate (C) at ($(A)!0.35!(B)$);       
                \coordinate (D) at (C |- E);               
                \draw[thick] (A) -- (B);                 
                \draw[dashed] (C) -- (D);                  
                \fill (A) circle (1.5pt) node[above right] {{$A$}};
                \fill (E) circle (1.5pt) node[below] {{$E$}};
                \fill (B) circle (1.5pt) node[below] {{$B$}};
                \fill (C) circle (1.5pt) node[above] {{$C$}};
                \fill (D) circle (1.5pt) node[below] {{$D$}};
            \end{{tikzpicture}}
            \end{{center}}
            Tìm chiều dài ngắn nhất của thang $AB$ được đặt từ mặt đất qua đỉnh hàng rào đến tường (kết quả làm tròn đến hàng phần trăm của mét).\\ """
            # ===== Nội dung lời giải chi tiết =====
            loigiai = rf""" Đặt $BD=x,\ x>0$. Khi đó: $EB=x+{tp_vn(float(b))}$.\\ 
            Ta có tam giác $BCD$ đồng dạng tam giác $BAE$ nên:\\
            $\frac{{AE}}{{CD}} = \frac{{EB}}{{BD}} \Rightarrow AE = \frac{{EB \cdot CD}}{{BD}} = \frac{{(x+{tp_vn(float(b))}) \cdot {latex(a)}}}{{x}}$.\\
            Mà: $AB^2=AE^2+EB^2={latex(a**2)}\left(\frac{{x+{tp_vn(float(b))}}}{{{x}}}\right)^2 + \left(x+{tp_vn(float(b))}\right)^2$.\\
            Nhận xét: $AB$ nhỏ nhất khi và chỉ khi $AB^2$ nhỏ nhất.\\ 
            Do đó, ta tìm giá trị nhỏ nhất của hàm số:
            Ta có: $f(x)=AB^2={latex(a**2)}\left(\frac{{x+{tp_vn(float(b))}}}{{{x}}}\right)^2 + \left(x+{tp_vn(float(b))}\right)^2$ trên khoảng $(0; +\infty)$.\\
            $f'(x) = {latex(dh_gon)}$.\\
            $f'(x)=0$ có các nghiệm $x_1={latex(sap_xep[0])}$ (loại), $x_2 \approx {tp_vn(round(sap_xep[-1],4))}$ (nhận).\\
            Bảng biến thiên:
            \begin{{center}}
            \begin{{tikzpicture}}
                \foreach \x/\t in {{1.2/x, 3/{{0}}, 5/x_2, 7/+\infty}}
                \node at (\x,4.2) {{$\t$}};
                \foreach \x/\t in {{3.8/{{-}}, 5/{{0}}, 6.2/{{+}}}}
                \node at (\x,3.5) {{$\t$}};
                \foreach \x/\t in {{3/+\infty,7/+\infty}}
                \node at (\x,2.6) {{$\t$}};
                \node at (1.2,3.5) {{$f'(x)$}};  
                \node at (1.2,2.6) {{$f(x)$}};
                \node (A) at (5,0.5) {{$f(x_2)$}};
                \draw[-stealth] (3,2.4) -- (A);
                \draw[-stealth] (A) -- (7,2.4);
                \draw (0,4.5) rectangle (8,0);
                \draw (0,3.9) -- (8,3.9);
                \draw (0,3.2) -- (8,3.2);
                \draw (2.2,4.5) -- (2.2,0);    
            \end{{tikzpicture}}
            \end{{center}}
            Vậy độ dài ngắn nhất của cây thang là $\sqrt{{f(x_2)}} \approx {tp_vn(AB_min)}$ m."""

            # ===== Đáp án ngắn gọn (LaTeX) =====
            dapan = r'\shortans[0]{$%s$}' % sp.latex(tp_vn(AB_min))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

