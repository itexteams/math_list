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


def bt_dang11_p2_b1_c4_ds10(self):
            # Khai báo biến
            # --- Khởi tạo các biến ngẫu nhiên ---
            # k là giá trị cực đại/cực tiểu của hàm số (trong hình là 1)
            k = randint(1, 4)
            x_val = 2024 + randint(0, 10) # Năm ngẫu nhiên cho câu c

            # --- Nội dung câu hỏi và Hình vẽ TikZ ---
            # Vẽ đồ thị hàm số hằng y=-k khi x<=0, y=k khi x>=1 và đoạn nối ở giữa
            tikz_code = r"""\begin{tikzpicture}[>=stealth, x=1cm, y=1cm, scale=0.8]
                \draw[->] (-3,0) -- (3,0) node[below] {$x$};
                \draw[->] (0,-%s) -- (0,%s) node[left] {$y$};
                \draw (0,0) node[below left] {$O$};
                \draw[thick, blue] (-2.5,-%s) -- (0,-%s) -- (1,%s) -- (2.5,%s);
                \fill (0,-%s) circle (0pt) node[right] {$-%s$};
                \fill (1,%s) circle (0pt);
                \draw[dashed] (1,0) -- (1,%s) -- (0,%s);
                \node at (1,0) [below] {$1$};
                \node at (0,%s) [left] {$%s$};
                \fill (-1,0) circle (0pt) node[below] {$-1$};
                \fill (-2,0) circle (0pt) node[below] {$-2$};
                \fill (2,0) circle (0pt) node[below] {$2$};
            \end{tikzpicture}""" % (k+1, k+1, k, k, k, k, k, k, k, k, k, k, k)

            noidungcauhoi = r"Cho hàm số $y = f(x)$ có đồ thị như hình vẽ bên." + "\n" + r"\begin{center}" + tikz_code + r"\end{center}"

            ########################################################################
            # Nhận biết: Giá trị tại điểm x = 1
            nb_da_1_d = r'\True $f(1) = %s$' % k
            nb_da_1_s = r'$f(1) = 0$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r"Dựa vào đồ thị, tại điểm $x=1$ ta dóng lên đồ thị và dóng sang trục $Oy$ được $y=%s$. Vậy $f(1)=%s$." % (k, k)

            ########################################################################
            # Thông hiểu: So sánh giá trị f(-2) và f(2)
            th_da_1_d = r'\True $f(-2) < f(2)$'
            th_da_1_s = r'$f(-2) > f(2)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r"Ta có $f(-2) = -%s$ và $f(2) = %s$. Vì $-%s < %s$ nên $f(-2) < f(2)$." % (k, k, k, k)

            ########################################################################
            # Vận dụng: Điểm thuộc đồ thị (nhánh vô cực)
            vd_da_1_d = r'\True Điểm $(-%s; -%s)$ thuộc đồ thị hàm số.' % (x_val, k)
            vd_da_1_s = r'Điểm $(-%s; %s)$ thuộc đồ thị hàm số.' % (x_val, k)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r"Với $x \le 0$, đồ thị hàm số là đường thẳng $y = -%s$. Do đó với $x = -%s$ thì $y = -%s$. Vậy điểm $(-%s; -%s)$ thuộc đồ thị." % (k, x_val, k, x_val, k)

            ########################################################################
            # Vận dụng cao: Tập giá trị/Bất phương trình f(x)
            vdc_da_1_d = r'\True $-%s \le f(x), \forall x \in \mathscr{D}$' % k
            vdc_da_1_s = r'$f(x) \le -%s, \forall x \in \mathscr{D}$' % k
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r"Dựa vào đồ thị, ta thấy điểm thấp nhất của đồ thị có tung độ bằng $-%s$. Do đó $f(x) \ge -%s$ với mọi $x \in \mathbb{R}$." % (k, k)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp xáo trộn và đảm bảo số câu đúng từ 1-3
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + nb_sel + '}\n'
                '{' + th_sel + '}\n'
                '{' + vd_sel + '}\n'
                '{' + vdc_sel + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

