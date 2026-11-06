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


def bt_dang24_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            t = symbols('t')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random biên độ của vận tốc (a) từ 2 đến 9
                a = random.randint(2, 9)

                # Biểu thức vận tốc v(t) = a*cos(t)
                v_t = a * cos(t)
                v_t_latex = latex(v_t)

                # Tính nguyên hàm để tìm s(t)
                # s(t) = integral(v(t) dt) = a*sin(t) + C
                # Với t=0, s(0)=0 => C=0
                s_t_dung = a * sin(t)

                # --- B4: Điều chỉnh các phương án sai ---
                # Tạo các phương án nhiễu (sai về dấu hoặc hàm lượng giác)
                da_sai_1 = -a * sin(t)
                da_sai_2 = a * cos(t)
                da_sai_3 = -a * cos(t)

                # Đáp án đúng
                da_d = '\\True $' + 's(t) = ' + latex(s_t_dung) + '$'
                da_s1 = '$s(t) = ' + latex(da_sai_1) + '$'
                da_s2 = '$s(t) = ' + latex(da_sai_2) + '$'
                da_s3 = '$s(t) = ' + latex(da_sai_3) + '$'

                # Đưa các đáp án vào danh sách và trộn
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # --- Hình vẽ TikZ ---
                hinh_ve = r'''\begin{tikzpicture}[>=stealth, scale=1]
                \draw[thick] (0,0) -- (0,1.5);
                \foreach \i in {0,0.2,0.4,0.6,0.8,1,1.2,1.4} \draw (0,\i) -- (-0.2,\i+0.2);
                \draw[decorate,decoration={aspect=0.3, segment length=2mm, amplitude=3mm,coil}] (0,0.7) -- (2.5,0.7);
                \draw[fill=blue!30] (2.5,0.2) rectangle (3.2,1.2);
                \draw[->] (-0.5,0) -- (5,0) node[below] {$x$};
                \draw[dashed] (1.5,1.5) -- (1.5,0) node[below] {$O$};
                \draw[<-] (1.5,1.6) -- (1.5,2) node[above] {vị trí cân bằng};
                \draw (2.85,0) -- (2.85,-0.1) node[below] {$x(t)$};
            \end{tikzpicture}'''

                # --- B2: Viết lại đề bài và lời giải ---
                noidungcauhoi = (r'''Một con lắc lò xo dao động điều hòa theo phương ngang trên mặt phẳng không ma sát như Hình vẽ, có vận tốc tức thời cho bởi $v(t) = %s$, trong đó $t$ tính bằng giây và $v(t)$ tính bằng centimét/giây. Tại thời điểm $t = 0$, con lắc đó ở vị trí cân bằng.
            \begin{center}
            %s
            \end{center}
            Tìm phương trình chuyển động $s(t)$ của con lắc đó.''' % (v_t_latex, hinh_ve))

                loigiai = (r'''Giả sử con lắc chuyển động theo phương trình $s = s(t)$. \\
            Suy ra $s'(t) = v(t)$, do đó $s(t)$ là một nguyên hàm của $v(t)$. Ta có:\\
            $$\int v(t) \text{d}t = \int %s \text{d}t = %s \sin t + C.$$
            Suy ra $s(t) = %s \sin t + C$.\\
            Tại thời điểm $t = 0$, ta có $s(0) = 0$, tức là $%s \sin 0 + C = 0 \Rightarrow C = 0$.\\
            Vậy phương trình chuyển động của con lắc là $s(t) = %s \sin t$.''' 
                % (v_t_latex, latex(a), latex(a), latex(a), latex(a)))

            # Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

