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


def bt_dang43_p1_b6_c2_hh11(self):
            # Khai báo biến
            # --- Khởi tạo biến ký hiệu ---
            a = symbols('a')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Biến n đại diện cho tỉ số SA/AB. Trong đề gốc SA = a nên n = 1.
            # Ta sẽ chọn ngẫu nhiên n để thay đổi khoảng cách d(A, (SBC)) và Thể tích.
            list_n = [Rational(1, 1), Rational(1, 2), Rational(2, 1), sp.sqrt(3), Rational(3, 2)]
            n = random.choice(list_n)

            # 1. Cạnh hình vuông đáy AB = a
            # 2. Chiều cao SA = n * a
            # 3. Tính khoảng cách AH từ A đến mặt phẳng (SBC)
            # Công thức: 1/AH^2 = 1/SA^2 + 1/AB^2
            # => AH = (SA * AB) / sqrt(SA^2 + AB^2)
            AH_expr = (n * a * a) / sqrt((n*a)**2 + a**2)
            AH_val = simplify(AH_expr)

            # 4. Tính diện tích đáy và thể tích
            S_day = a**2
            V_val = simplify(Rational(1, 3) * S_day * (n * a))

            # --- B4: Điều chỉnh các phương án sai ---
            kq_dung = '$%s$' % latex(V_val).replace('.', ',')

            # Tạo danh sách đáp án nhiễu
            list_distractors = [
                '$%s$' % latex(V_val * 3).replace('.', ','),
                '$%s$' % latex(V_val * Rational(3, 2)).replace('.', ','),
                '$%s$' % latex(V_val * Rational(1, 2)).replace('.', ','),
                '$%s$' % latex(simplify(V_val * sqrt(3) / 3)).replace('.', ','),
                '$%s$' % latex(simplify(V_val * 2)).replace('.', ','),
                '$%s$' % latex(a**3).replace('.', ','),
                '$%s$' % latex(Rational(1, 6) * n * a**3).replace('.', ',')
            ]

            # Lọc bỏ trùng lặp và bỏ đáp án đúng nếu lỡ trùng
            list_distractors = list(set([x for x in list_distractors if x != kq_dung]))
            random.shuffle(list_distractors)

            das1 = list_distractors[0]
            das2 = list_distractors[1]
            das3 = list_distractors[2]

            # --- Nội dung câu hỏi ---
            # Thay thế dấu chấm bằng dấu phẩy cho các số thập phân nếu có trong latex
            dist_text = latex(AH_val).replace('.', ',')

            noidungcauhoi = ('''Cho khối chóp $S.ABCD$ có đáy là hình vuông cạnh $a$, $SA$ vuông góc với đáy và khoảng cách từ $A$ đến mặt phẳng $\\left(SBC\\right)$ bằng $%s$. Thể tích của khối chóp đã cho bằng'''
                             % (dist_text))

            # --- Hình vẽ TikZ (Bản sao 100% phong cách ảnh) ---
            tikz_code = r''' \begin{center}
            \begin{tikzpicture}[scale=0.8, line width=1pt, >=stealth]
                \coordinate (A) at (0,4);
                \coordinate (D) at (-1.5,1.5);
                \coordinate (B) at (4,4);
                \coordinate (C) at ($(B)+(D)-(A)$);
                \coordinate (S) at (0,8);
                \coordinate (H) at ($(S)!0.5!(B)$); 
                \draw [dashed] (S)--(A)--(B);
                \draw [dashed] (A)--(D);
                \draw [dashed] (A)--(H);
                \draw (S)--(D)--(C)--(B)--(S);
                \draw (S)--(C);
                \draw (D)--(C);
                \draw (0,4.3)--(0.3,4.3)--(0.3,4); % Góc S-A-B
                \draw (0.2,4.2)--(-0.1,3.9)--(-0.3,4.1); % Góc S-A-D (tương đối)
                \draw (S) node[above] {$S$};
                \draw (A) node[left] {$A$};
                \draw (B) node[right] {$B$};
                \draw (C) node[right] {$C$};
                \draw (D) node[left] {$D$};
                \draw (H) node[above right] {$H$};
                \foreach \p in {S,A,B,C,D,H} \fill (\p) circle (1.5pt);
            \end{tikzpicture}
            \end{center}'''

            # --- B2: Nội dung lời giải chi tiết ---
            loigiai = (tikz_code + '''Ta có $BC \\perp AB$ (do $ABCD$ là hình vuông) và $BC \\perp SA$ (do $SA$ vuông góc với mặt đáy). \\\\
            Suy ra $BC \\perp \\left(SAB\\right)$. \\\\
            Trong mặt phẳng $\\left(SAB\\right)$, kẻ $AH \\perp SB$ tại $H$. \\\\
            Vì $BC \\perp \\left(SAB\\right)$ nên $BC \\perp AH$. \\\\
            Từ đó ta có $AH \\perp SB$ và $AH \\perp BC$, suy ra $AH \\perp \\left(SBC\\right)$. \\\\
            Do đó $d\\left(A; \\left(SBC\\right)\\right) = AH = %s$. \\\\
            Xét tam giác $SAB$ vuông tại $A$, ta có hệ thức lượng: \\\\
            $\\frac{1}{AH^2} = \\frac{1}{SA^2} + \\frac{1}{AB^2} \\Rightarrow \\frac{1}{SA^2} = \\frac{1}{AH^2} - \\frac{1}{AB^2}$. \\\\
            Thay số: $\\frac{1}{SA^2} = \\frac{1}{\\left(%s\\right)^2} - \\frac{1}{a^2} = %s$. \\\\
            Từ đó suy ra $SA = %s$. \\\\
            Diện tích đáy $S_{ABCD} = a^2$. \\\\
            Vậy thể tích khối chóp là $V_{S.ABCD} = \\frac{1}{3} \\cdot SA \\cdot S_{ABCD} = \\frac{1}{3} \\cdot %s \\cdot a^2 = %s$.'''
                       % (dist_text, dist_text, latex(simplify(1/AH_val**2 - 1/a**2)), 
                          latex(n*a), latex(n*a), latex(V_val).replace('.', ',')))

            # --- Xuất câu trắc nghiệm ---
            da_d = '\\True ' + kq_dung
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

