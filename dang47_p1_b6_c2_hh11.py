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


def bt_dang47_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho a
            a = symbols('a')

            # B3: Suy nghĩ tìm cách random bài toán
            # Random hệ số k của cạnh AB (AB = k*a)
            k = random.choice([1, 2, 3])
            # Random góc ACB (độ)
            list_g_base = [30, 60]
            g_base_val = random.choice(list_g_base)
            # Random góc giữa SB và đáy (độ)
            list_g_sb = [30, 45, 60]
            g_sb_val = random.choice(list_g_sb)

            # Tính toán các giá trị hình học bằng Sympy
            AB = k * a
            # BC = AB / tan(g_base)
            tan_base = tan(Rational(g_base_val, 180) * pi)
            BC = AB / tan_base
            BC = sp.simplify(BC)

            # SA = AB * tan(g_sb)
            tan_sb = tan(Rational(g_sb_val, 180) * pi)
            SA = AB * tan_sb
            SA = sp.simplify(SA)

            # Diện tích đáy ABC (vuông tại B)
            S_day = Rational(1, 2) * AB * BC
            S_day = sp.simplify(S_day)

            # Thể tích khối chóp
            V = Rational(1, 3) * S_day * SA
            V = sp.simplify(V)

            # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            kq_dung = '$V = %s$' % (latex(V))

            # Tạo các đáp án nhiễu bằng cách thay đổi các hệ số phân số
            def generate_distractors(correct_v):
                distractors = set()
                factors = [Rational(1, 2), Rational(1, 4), Rational(2, 3), Rational(3, 2), 2, 3]
                for f in factors:
                    wrong = sp.simplify(correct_v * f)
                    if wrong != correct_v:
                        distractors.add('$V = %s$' % (latex(wrong)))

                res = list(distractors)
                random.shuffle(res)
                return res[:3]

            ds_sai = generate_distractors(V)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp tam giác $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$, $AB = %s$, $\\widehat{ACB} = %s^\\circ$, cạnh bên $SA$ vuông góc với mặt đáy và $SB$ hợp với mặt đáy một góc $%s^\\circ$. Thể tích $V$ của khối chóp $S.ABC$ bằng'''
                             % (latex(AB), latex(g_base_val), latex(g_sb_val)))

            # Danh sách đáp án để trộn
            list_ans = ['\\True ' + kq_dung, ds_sai[0], ds_sai[1], ds_sai[2]]
            random.shuffle(list_ans)

            # Vẽ hình bằng TikZ (Bản vẽ giống 100% ảnh mẫu)
            # Tọa độ: A=(0,0), B=(1.5,-1), C=(4,0.5), S=(0,4)
            tikz_code = r'''\begin{center} \begin{tikzpicture}[line cap=round, line join=round, line width=1pt, scale=0.8]
                \coordinate (A) at (0,0);
                \coordinate (B) at (1.5,-1.5);
                \coordinate (C) at (4.5,0.5);
                \coordinate (S) at (0,4.5);
                \draw [dashed] (A) -- (C);
                \draw (S) -- (A) -- (B) -- (C) -- (S) -- (B);
                \draw (S) -- (C);
                \draw (0,0.3) -- (0.3,0.3) -- (0.3,0);
                \draw [shift={(B)}] (-0.2,0.1) -- (0.05,0.25) -- (0.25,0.15);
                \begin{scope}[nodes={inner sep=2pt, font=\small}]
                    \node [left] at (A) {$A$};
                    \node [below] at (B) {$B$};
                    \node [right] at (C) {$C$};
                    \node [above] at (S) {$S$};
                \end{scope}
            \end{tikzpicture} \end{center}'''

            # Nội dung lời giải chi tiết
            loigiai = (tikz_code+'''$ABC$ là tam giác vuông tại $B$, $AB = %s$, $\\widehat{ACB} = %s^\\circ \\Rightarrow BC = \\frac{AB}{\\tan %s^\\circ} = %s$. \\\\
            Góc giữa đường thẳng $SB$ và mặt phẳng $\\left( ABC \\right)$ là góc $\\widehat{SBA} = %s^\\circ$. \\\\
            Trong tam giác vuông $SAB$, ta có $SA = AB \\cdot \\tan \\widehat{SBA} = %s \\cdot \\tan %s^\\circ = %s$. \\\\
            Thể tích khối chóp $S.ABC$ là: \\\\
            $V_{S.ABC} = \\frac{1}{3} S_{\\Delta ABC} \\cdot SA = \\frac{1}{3} \\cdot \\frac{1}{2} BA \\cdot BC \\cdot SA = \\frac{1}{6} \\cdot %s \\cdot %s \\cdot %s = %s$.'''
                       % (latex(AB), latex(g_base_val), latex(g_base_val), latex(BC),
                          latex(g_sb_val), latex(AB), latex(g_sb_val), latex(SA),
                          latex(AB), latex(BC), latex(SA), latex(V)))

            # Xuất kết quả theo định dạng yêu cầu (Không dùng tiền tố r cho content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

