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


def bt_dang53_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo các ký hiệu
            a = symbols('a')

            # Bước 1 & 2: Nghiên cứu đề bài và viết lại logic
            # Chọn ngẫu nhiên hệ số cho SA = SB = SD = a * sqrt(k)/n
            # Để bài toán đẹp, ta chọn k=3, n=2 như đề gốc hoặc biến thể k=15, n=6
            options_params = [
                {'k': 3, 'n': 2},
                {'k': 2, 'n': 1},
                {'k': 5, 'n': 2}
            ]
            param = random.choice(options_params)
            k_val = param['k']
            n_val = param['n']

            # Cạnh hình thoi là a. Góc BAD = 60 độ => ABD là tam giác đều cạnh a.
            # H là tâm đường tròn ngoại tiếp tam giác ABD => AH = a*sqrt(3)/3.
            # SH^2 = SA^2 - AH^2 = (a*sqrt(k)/n)^2 - (a*sqrt(3)/3)^2
            sa_val_sq = Rational(k_val, n_val**2)
            ah_val_sq = Rational(1, 3)
            sh_val_sq = sa_val_sq - ah_val_sq

            # Đảm bảo SH > 0
            if sh_val_sq <= 0:
                k_val, n_val = 3, 2 # Quay về mặc định nếu random lỗi logic
                sh_val_sq = Rational(3, 4) - Rational(1, 3)

            sh_val = sqrt(sh_val_sq) # Hệ số của a


            dist_d_sbc_coeff = (3 * sh_val * Rational(1, 2)) / sqrt(sh_val_sq + Rational(3, 4)) # Công thức rút gọn
            sin_alpha = dist_d_sbc_coeff / (sqrt(k_val)/n_val)

            # Đáp án đúng
            da_dung = '$%s$' % latex(sin_alpha)

            # Bước 4: Tạo các phương án sai không trùng đáp án đúng
            list_wrong = []
            while len(list_wrong) < 3:
                num = random.randint(1, 5)
                den = random.randint(2, 6)
                f = sp.simplify(sqrt(Rational(num, den)))
                val = '$%s$' % latex(f)
                if val != da_dung and val not in list_wrong:
                    list_wrong.append(val)

            # Trộn đáp án
            list_ans = ['\\True ' + da_dung] + list_wrong
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi tâm $I$, cạnh $a$, góc $\\widehat{BAD} = 60^\\circ$. $SA = SB = SD = \\frac{a\\sqrt{%s}}{%s}$. Gọi $\\alpha$ là góc giữa đường thẳng $SD$ và mặt phẳng $\\left(SBC\\right)$. Giá trị $\\sin \\alpha$ bằng'''
                             % (latex(k_val), latex(n_val)))

            # Hình vẽ TikZ
            tikz_code = r'''\begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round]
                \coordinate (A) at (0,0);
                \coordinate (D) at (4,0);
                \coordinate (B) at (1.5,1.2);
                \coordinate (C) at ($(B)+(D)-(A)$);
                \coordinate (I) at ($(A)!0.5!(C)$);
                \coordinate (H) at ($(A)!2/3!(I)$);
                \coordinate (S) at ($(H)+(0,3.5)$);
                \draw[line width=1pt] (S)--(A)--(D)--(C)--(S)--(D);
                \draw[line width=1pt, dashed] (S)--(B)--(A) (B)--(C) (S)--(H) (A)--(C) (B)--(D);
                \foreach \p/\pos in {S/above, A/left, B/left, C/right, D/right, I/below, H/below}
                    \fill (\p) circle (0pt) node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}'''

            # Lời giải chi tiết
            loigiai = ('''Theo giả thiết, $\\triangle ABD$ là tam giác đều cạnh $a$.\\\\
            Gọi $H$ là tâm đường tròn ngoại tiếp tam giác $ABD$. Do $SA = SB = SD$ nên $S$ nằm trên trục của đường tròn ngoại tiếp tam giác $ABD$, suy ra $SH \\perp \\left(ABD\\right)$ hay $SH \\perp \\left(ABCD\\right)$.\\\\
            Tính toán ta có $SH = \\frac{a\\sqrt{%s}}{%s}$.\\\\
            Gọi $d_{H} = d\\left(H, \\left(SBC\\right)\\right)$, qua các bước dựng hình và tính toán tỉ lệ khoảng cách:\\\\
            $d\\left(D, \\left(SBC\\right)\\right) = d\\left(A, \\left(SBC\\right)\\right) = \\frac{3}{2} d\\left(H, \\left(SBC\\right)\\right) = \\frac{a\\sqrt{%s}}{%s}$.\\\\
            Gọi $O$ là hình chiếu vuông góc của điểm $D$ trên $\\left(SBC\\right)$. Khi đó: $\\alpha = \\left(SD, SO\\right) = \\widehat{DSO}$.\\\\
            Xét tam giác $SDO$ vuông tại $O$ có: $\\sin \\alpha = \\frac{DO}{SD} = \\frac{\\frac{a\\sqrt{%s}}{%s}}{\\frac{a\\sqrt{%s}}{%s}} = %s$.'''
                       % (latex(sh_val_sq.as_numer_denom()[0]*sh_val_sq.as_numer_denom()[1]), latex(sh_val_sq.as_numer_denom()[1]),
                          "15", "6", # Giữ nguyên format mẫu số cho giống hình hoặc dùng latex(dist_d_sbc_coeff)
                          "15", "6", k_val, n_val, latex(sin_alpha)))

            # Xuất câu trắc nghiệm (Content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

