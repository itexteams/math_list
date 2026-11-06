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


def bt_dang30_p1_b3_c3_ds12(self):
            # Khai báo biến
            list_a = [1, 2, 3]
            a = random.choice(list_a)

            # Phương trình hoành độ giao điểm: a|x| = x^2 <=> x = 0 hoặc |x| = a => x = +/- a
            # Khi đó y = a^2.
            y_limit = a**2

            # Khi quay quanh Oy, ta đổi biến x theo y (xét bên x > 0)
            # y = ax => x = y/a
            # y = x^2 => x = sqrt(y)
            f1 = y/a
            f2 = sqrt(y)

            # Thể tích V = pi * tích phân từ 0 đến a^2 của |f2^2 - f1^2| dy
            # V = pi * integral(y - (y/a)^2, (y, 0, a**2))
            integral_expr = y - (y**2 / a**2)
            val_v = integrate(integral_expr, (y, 0, y_limit))
            kq_dung = val_v * pi

            # B4: Tạo các phương án sai không trùng với đáp án đúng
            options_set = set()
            while len(options_set) < 3:
                # Tạo các biến thể sai dựa trên các lỗi phổ biến (quên pi, sai hệ số, sai số mũ)
                wrong_val = random.choice([
                    Rational(a**4, 3), 
                    Rational(a**4, 2), 
                    Rational(a**4, 4), 
                    Rational(a**4, 12),
                    Rational(a**2, 6),
                    Rational(a**2, 3)
                ]) * pi
                if wrong_val != kq_dung:
                    options_set.add('$%s$' % latex(wrong_val))

            list_wrong = list(options_set)

            # Tạo TikZ cho hình vẽ
            # Điều chỉnh scale dựa trên giá trị của a
            tikz_scale = 0.8 if a == 1 else (0.5 if a == 2 else 0.3)
            tikz_code = r"""
            \begin{center}
            \begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, scale=""" + str(tikz_scale) + r"""]
                \draw[->] (-"""+str(a+1)+r""",0) -- ("""+str(a+1)+r""",0) node[below] {$x$};
                \draw[->] (0,-1) -- (0,"""+str(y_limit+1)+r""") node[left] {$y$};
                \draw[dashed] (-"""+str(a)+r""", """+str(y_limit)+r""") -- ("""+str(a)+r""", """+str(y_limit)+r""");
                \draw[samples=100, domain=-"""+str(sqrt(y_limit+0.5))+r""":"""+str(sqrt(y_limit+0.5))+r"""] plot (\x, {(\x)^2});
                \draw (-"""+str(a+0.5)+r""", """+str(a*(a+0.5))+r""") -- (0,0) -- ("""+str(a+0.5)+r""", """+str(a*(a+0.5))+r""");
                \fill[pattern=north west lines, opacity=0.5] plot[domain=0:"""+str(a)+r"""] (\x, {(\x)^2}) -- (0,0) -- cycle;
                \fill[pattern=north east lines, opacity=0.5] plot[domain=-"""+str(a)+r""":0] (\x, {(\x)^2}) -- (0,0) -- cycle;
                \node at (0.3,-0.3) {$O$};
                \node at ("""+str(a)+r""", -0.3) {$"""+str(a)+r"""$};
                \node at (-"""+str(a)+r""", -0.3) {$-"""+str(a)+r"""$};
                \node at (-0.3, """+str(y_limit)+r""") {$"""+str(y_limit)+r"""$};
            \end{tikzpicture}
            \end{center}"""

            # Nội dung câu hỏi
            noidungcauhoi = r"Hình phẳng giới hạn bởi hai đồ thị $y = %s|x|$ và $y = x^2$ quay quanh trục tung tạo nên một vật thể tròn xoay có thể tích bằng" % (latex(a) if a != 1 else "")

            # Nội dung lời giải
            loigiai = r"""Phương trình hoành độ giao điểm: $%s|x| = x^2 \Leftrightarrow \left[\begin{aligned} &x = 0 \Rightarrow y = 0 \\ &x = \pm %s \Rightarrow y = %s \end{aligned}\right.$. \\
            %s
            Ta có đồ thị hai hàm số $y = %s|x|$ và $y = x^2$ đều đối xứng qua $Oy$ nên hình phẳng giới hạn bởi hai đồ thị quay quanh trục tung tạo nên một vật thể tròn xoay có thể tích bằng thể tích vật thể tròn xoay khi quay hình phẳng giới hạn bởi hai đường $x = \frac{y}{%s}$ và $x = \sqrt{y}$ quay xung quanh trục $Oy$. \\
            Thể tích vật thể tròn xoay cần tìm là:
            $$V = \pi \int_{0}^{%s} \left| \left(\sqrt{y}\right)^2 - \left(\frac{y}{%s}\right)^2 \right| \text{d}y = \pi \int_{0}^{%s} \left( y - \frac{y^2}{%s} \right) \text{d}y = \pi \left. \left( \frac{1}{2}y^2 - \frac{1}{3%s}y^3 \right) \right|_{0}^{%s} = %s.$$""" % (
                latex(a) if a != 1 else "", latex(a), latex(y_limit),
                tikz_code,
                latex(a) if a != 1 else "",
                latex(a),
                latex(y_limit), latex(a), latex(y_limit), latex(a**2), latex(a**2), latex(y_limit),
                latex(kq_dung)
            )

            # Xuất kết quả
            da_d = '\\True $%s$' % latex(kq_dung)
            list_1 = [da_d, list_wrong[0], list_wrong[1], list_wrong[2]]
            random.shuffle(list_1)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choice \n'
                '{' + list_1[0] + '}\n'
                '{' + list_1[1] + '}\n'
                '{' + list_1[2] + '}\n'
                '{' + list_1[3] + '}\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

