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


def bt_dang52_p3_b1_c2_hh11(self):
            # Khai báo tỉ lệ
            list_ratios = [Rational(1, 2), Rational(1, 3), Rational(2, 3)]
            m_ratio = random.choice(list_ratios)
            n_ratio = random.choice(list_ratios)

            # Tính toán Cosin bằng SymPy
            # Tích vô hướng: dot = 1 - m + n
            dot_product = 1 - m_ratio + n_ratio
            # Độ dài: |MN|^2 = 1 + m^2 + n^2
            len_mn_sq = 1 + m_ratio**2 + n_ratio**2
            # Độ dài: |AC'|^2 = 3
            len_ac_sq = 3

            cos_val = Abs(dot_product) / (sqrt(len_mn_sq) * sqrt(len_ac_sq))
            cos_val = sp.simplify(cos_val)

            # Tạo đáp án đúng dạng LaTeX
            da_dung_latex = "$%s$" % latex(cos_val)

            # Tạo các đáp án nhiễu
            s = []
            while len(s) < 3:
                num = random.randint(1, 7)
                den = random.randint(2, 6)
                val = "$%s$" % latex(sp.simplify(sqrt(num)/den))
                if val != da_dung_latex and val not in s:
                    s.append(val)

            # Nội dung câu hỏi
            m_text = "trung điểm" if m_ratio == Rational(1, 2) else "điểm sao cho $AM = \\frac{%s}{%s}AD$" % (m_ratio.p, m_ratio.q)
            n_text = "trung điểm" if n_ratio == Rational(1, 2) else "điểm sao cho $BN = \\frac{%s}{%s}BB'$" % (n_ratio.p, n_ratio.q)

            noidungcauhoi = ("Cho hình lập phương $ABCD.A'B'C'D'$. Gọi $M, N$ lần lượt là " + m_text + " của $AD$ và " + n_text + " của $BB'$. Cosin của góc hợp bởi $MN$ và $AC'$ bằng")

            # TikZ Code
            tikz_code = ("\\begin{center}\n\\begin{tikzpicture}[scale=1.5, line join=round, line cap=round, >=stealth, font=\\footnotesize]\n"
                "\\coordinate (A) at (0,1);\n"
                "\\coordinate (B) at (0.8,1.4);\n"
                "\\coordinate (C) at (2.3,1.4);\n"
                "\\coordinate (D) at (1.5,1);\n"
                "\\coordinate (A1) at (0,0);\n"
                "\\coordinate (B1) at (0.8,0.4);\n"
                "\\coordinate (C1) at (2.3,0.4);\n"
                "\\coordinate (D1) at (1.5,0);\n"
                "\\draw (A) -- (D) -- (D1) -- (A1) -- (A);\n"
                "\\draw (D) -- (C) -- (C1) -- (D1);\n"
                "\\draw (C) -- (B) -- (A);\n"
                "\\draw[dashed] (A1) -- (B1) -- (C1);\n"
                "\\draw[dashed] (B) -- (B1);\n"
                "\\coordinate (M) at ($(A)!" + str(float(m_ratio)) + "!(D)$);\n"
                "\\coordinate (N) at ($(B)!" + str(float(n_ratio)) + "!(B1)$);\n"
                "\\draw[blue, thick, dashed] (M) -- (N);\n"
                "\\draw[red, thick, dashed] (A) -- (C1);\n"
                "\\fill (M) circle (1pt) node[above] {$M$};\n"
                "\\fill (N) circle (1pt) node[right] {$N$};\n"
                "\\node[left] at (A) {$A$};\n"
                "\\node[above] at (B) {$B$};\n"
                "\\node[right] at (C) {$C$};\n"
                "\\node[right] at (D) {$D$};\n"
                "\\node[left] at (A1) {$A'$};\n"
                "\\node[below] at (B1) {$B'$};\n"
                "\\node[right] at (C1) {$C'$};\n"
                "\\node[right] at (D1) {$D'$};\n"
                "\\end{tikzpicture}\n\\end{center}")

            # SỬA LỖI TẠI ĐÂY: Sử dụng đối tượng cos_val của SymPy để tính toán, không dùng chuỗi LaTeX
            val_float = float(cos_val.evalf())
            number = Decimal(str(val_float))
            # Làm tròn đến 2 chữ số thập phân thay vì hàng đơn vị cho Cosin (hợp lý hơn)
            kqz = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            loigiai = ("Xét hình lập phương $ABCD.A'B'C'D'$ cạnh $a$. \\\\\n"
                "Đặt $\\vec{AB}=\\vec{a}, \\vec{AD}=\\vec{b}, \\vec{AA'}=\\vec{c}$. Khi đó $|\\vec{a}| = |\\vec{b}| = |\\vec{c}| = a$ và các tích vô hướng bằng $0$. \\\\\n"
                "Ta có: $\\vec{MN} = \\vec{a} + " + latex(n_ratio) + "\\vec{c} - " + latex(m_ratio) + "\\vec{b}$. \\\\\n"
                "$\\Rightarrow |\\vec{MN}| = \\sqrt{a^2 + (" + latex(m_ratio) + "a)^2 + (" + latex(n_ratio) + "a)^2} = \\frac{a\\sqrt{" + str(len_mn_sq.p) + "}}{" + str(len_mn_sq.q if len_mn_sq.q != 1 else "1") + "}$. \\\\\n"
                "$\\vec{AC'} = \\vec{a} + \\vec{b} + \\vec{c} \\Rightarrow |\\vec{AC'}| = a\\sqrt{3}$. \\\\\n"
                "Tích vô hướng: $\\vec{AC'} \\cdot \\vec{MN} = " + latex(dot_product) + "a^2$. \\\\\n"
                "Gọi $\\alpha$ là góc giữa $MN$ và $AC'$, ta có: \\\\\n"
                "$\\cos \\alpha = \\frac{|\\vec{MN} \\cdot \\vec{AC'}|}{|\\vec{MN}| \\cdot |\\vec{AC'}|} = $" + da_dung_latex + "$ \\approx " + str(kqz).replace('.', ',') + "$.")

            # Đáp án
            dapan = '\\shortans[0]{$%s$}'%(str(kqz).replace('.', ','))

            # Trộn đáp án trắc nghiệm
            da_d = "\\True " + da_dung_latex
            list_1 = [da_d, s[0], s[1], s[2]]
            random.shuffle(list_1)

            # Xuất nội dung
            content = ("\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + str(dapan) +
                "\\loigiai{" + tikz_code + str(loigiai) + "}\n" +
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

