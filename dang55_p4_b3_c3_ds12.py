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


def bt_dang55_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # B1-Nghiên cứu đề bài và B3-Suy nghĩ tìm cách random bài toán
            # Các giá trị a nên là số chính phương để căn thức đẹp: 4, 9, 16, 25
            list_a = [4, 9, 16] 
            a_val = random.choice(list_a)

            # Tỉ số V1 = k*V2. Trong đề gốc k = 2. Để m < a thì k > 1.5
            list_k = [2, 3]
            k_val = random.choice(list_k)

            # --- Tính toán giải thuật ---
            # 1. Tính V1 = pi * tích phân từ 0 đến a của (sqrt(x))^2
            v1_expr = pi * integrate(x, (x, 0, a_val))

            # 2. Gọi M(m, sqrt(m)). V2 là thể tích 2 khối nón chung đáy bán kính r=sqrt(m)
            # V2 = 1/3 * pi * r^2 * h1 + 1/3 * pi * r^2 * h2 = 1/3 * pi * m * a
            # V1 = k * V2 => v1_expr = k_val * (1/3 * pi * m * a_val)
            m_val = simplify(Rational(3, k_val * a_val) * (v1_expr / pi))

            # 3. Điểm M và phương trình đường thẳng OM: y = (sqrt(m)/m) * x
            y_m = sqrt(m_val)
            slope_om = simplify(y_m / m_val)
            line_om = slope_om * x

            # 4. Tính diện tích S giới hạn bởi (C) và OM
            # S = tích phân từ 0 đến m của (sqrt(x) - line_om)
            area_s = integrate(sqrt(x) - line_om, (x, 0, m_val))

            # --- B4-Điều chỉnh các phương án sai ---
            da_dung = '$%s$' % latex(area_s)

            def generate_distractors(correct_val):
                results = set()
                # Tạo các phương án nhiễu bằng cách thay đổi hệ số hoặc căn thức
                multipliers = [Rational(1, 2), Rational(2, 3), Rational(3, 2), Rational(1, 3)]
                for m in multipliers:
                    wrong = simplify(correct_val * m)
                    if wrong != correct_val:
                        results.add('$%s$' % latex(wrong))

                # Nếu chưa đủ 3 đáp án sai, tạo thêm bằng cách cộng trừ đơn giản
                count = 1
                while len(results) < 3:
                    wrong = simplify(correct_val + count)
                    results.add('$%s$' % latex(wrong))
                    count += 1

                return list(results)[:3]

            distractors = generate_distractors(area_s)
            da_s1, da_s2, da_s3 = distractors

            # --- Tạo mã TikZ cho hình vẽ ---
            tikz_code = r"""\begin{tikzpicture}[scale=0.5, >=stealth]
                \draw[->] (-1,0) -- (%d,0) node[below] {$x$};
                \draw[->] (0,-1) -- (0, %d) node[left] {$y$};
                \draw[smooth, samples=100, domain=0:%d] plot (\x, {sqrt(\x)}) node[right] {$(C)$};
                \coordinate (O) at (0,0);
                \coordinate (A) at (%d,0);
                \coordinate (M) at (%s, %s);
                \coordinate (H) at (%s, 0);
                \fill[yellow!40, opacity=0.5] (O) -- (M) -- (A) -- cycle;
                \draw (O) -- (M) -- (A);
                \draw[dashed] (M) -- (H);
                \draw (O) node[below left] {$O$};
                \draw (A) node[below] {$A(%d;0)$};
                \draw (M) node[above] {$M$};
                \draw (H) node[below] {$H$};
            \end{tikzpicture}""" % (a_val+2, sqrt(a_val)+2, a_val+1, a_val, float(m_val), float(y_m), float(m_val), a_val)

            # --- Xuất nội dung ---
            noidungcauhoi = r"""Cho đồ thị $(C): y = f(x) = \sqrt{x}$. Gọi $(H)$ là hình phẳng giới hạn bởi đồ thị $(C)$, đường thẳng $x = %s$ và trục $Ox$. Cho điểm $M$ thuộc đồ thị $(C)$ và điểm $A(%s;0)$. Gọi $V_1$ là thể tích khối tròn xoay khi cho $(H)$ quay quanh trục $Ox$, $V_2$ là thể tích khối tròn xoay khi cho tam giác $AOM$ quay quanh trục $Ox$. Biết rằng $V_1 = %s V_2$. Tính diện tích $S$ phần hình phẳng giới hạn bởi đồ thị $(C)$ và đường thẳng $OM$.
            \begin{center}
            %s
            \end{center}""" % (latex(a_val), latex(a_val), latex(k_val), tikz_code)

            loigiai = r"""Ta có $V_1 = \pi \int_{0}^{%s} (\sqrt{x})^2 \text{d}x = %s$. \\
            Gọi $H$ là hình chiếu của $M$ lên trục $Ox$, đặt $OH = m$ (với $0 < m \le %s$), ta có $M(m; \sqrt{m})$, $MH = \sqrt{m}$ và $AH = %s - m$. \\
            Suy ra $V_2 = \frac{1}{3} \pi \cdot MH^2 \cdot OH + \frac{1}{3} \pi \cdot MH^2 \cdot AH = \frac{1}{3} \pi \cdot MH^2 \cdot OA = \frac{%s}{3} \pi m$. \\
            Theo giả thiết, ta có $V_1 = %s V_2$ nên $%s = %s \cdot \frac{%s}{3} \pi m \Leftrightarrow m = %s$. \\
            Do đó $M\left( %s; %s \right)$. \\
            Từ đó ta có phương trình đường thẳng $OM$ là $y = %s x$. \\
            Diện tích $S$ phần hình phẳng giới hạn bởi đồ thị $(C)$ và đường thẳng $OM$ là: \\
            $S = \int_{0}^{%s} \left( \sqrt{x} - %s x \right) \text{d}x = %s$.""" % (
                latex(a_val), latex(v1_expr), latex(a_val), latex(a_val), latex(a_val), 
                latex(k_val), latex(v1_expr), latex(k_val), latex(a_val), latex(m_val),
                latex(m_val), latex(y_m), latex(slope_om),
                latex(m_val), latex(slope_om), latex(area_s))

            list_ans = [r'\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            content = (r'\begin{minipage}{\textwidth}' + '\n'
                r'\begin{ex}' + '\n' + str(noidungcauhoi) + '\n'
                r'\loigiai{' + str(loigiai) + '}\n'
                r'\end{ex}' + '\n' + r'\end{minipage}' + '\n')
            return content

