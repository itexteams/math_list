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


def bt_dang51_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Chúng ta sẽ random hệ số 'n' của cạnh AC = n*a
            n_val = random.randint(1, 4) 
            # Để giữ tính chất bài toán đẹp, ta giữ tỉ lệ AB = 2*AC và góc 60 độ

            # Tính toán các giá trị theo n (đơn vị a)
            # AC = n
            ac = n_val
            # AB = 2n
            ab = 2 * n_val
            # BC = sqrt(AB^2 - AC^2) = n*sqrt(3)
            bc_sq = ab**2 - ac**2
            bc_tex = latex(sqrt(bc_sq))

            # Diện tích đáy ABC = 1/2 * AC * BC = 1/2 * n * n*sqrt(3)
            s_abc_tex = latex(Rational(1, 2) * n_val**2 * sqrt(3))

            # Kẻ CH vuông góc AB. Trong tam giác vuông ABC:
            # BC^2 = BH * BA => BH = BC^2 / AB = (3n^2) / (2n) = 1.5n
            bh = Rational(3 * n_val, 2)
            bh_tex = latex(bh).replace('.', ',')

            # CH = sqrt(BC^2 - BH^2) = sqrt(3n^2 - 9n^2/4) = sqrt(3n^2/4) = n*sqrt(3)/2
            ch_sq = bc_sq - bh**2
            ch_tex = latex(sqrt(ch_sq))

            # Góc CKH = 60 độ. Trong tam giác vuông CKH (vuông tại H do CH vuông (SAB)):
            # HK = CH * cot(60) = (n*sqrt(3)/2) * (1/sqrt(3)) = n/2
            hk = Rational(n_val, 2)
            hk_tex = latex(hk).replace('.', ',')

            # BK = sqrt(BH^2 - HK^2) = sqrt(9n^2/4 - n^2/4) = sqrt(2n^2) = n*sqrt(2)
            bk_sq = bh**2 - hk**2
            bk_tex = latex(sqrt(bk_sq))

            # Tam giác SAB đồng dạng HKB (góc-góc) => SA/HK = AB/BK
            # SA = (AB * HK) / BK = (2n * n/2) / (n*sqrt(2)) = n / sqrt(2) = n*sqrt(2)/2
            sa_tex = latex(Rational(n_val, 2) * sqrt(2))

            # Thể tích V = 1/3 * SA * S_abc
            # V = 1/3 * (n*sqrt(2)/2) * (n^2*sqrt(3)/2) = (n^3 * sqrt(6)) / 12
            v_num = n_val**3
            v_tex = "\\frac{%s\\sqrt{6}}{12}" % (v_num if v_num > 1 else "")

            # B4: Điều chỉnh các phương án sai
            da_dung = "$%s a^3$" % v_tex
            pa_sai1 = "$%s a^3$" % ("\\frac{%s\\sqrt{2}}{6}" % (n_val**3))
            pa_sai2 = "$%s a^3$" % ("\\frac{%s\\sqrt{6}}{4}" % (n_val**3))
            pa_sai3 = "$%s a^3$" % ("\\frac{%s\\sqrt{2}}{2}" % (n_val**3))

            list_ans = ["\\True " + da_dung, pa_sai1, pa_sai2, pa_sai3]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = ("Cho hình chóp $S.ABC$ có đáy là tam giác $ABC$ vuông tại $C$, $AB=%sa$, $AC=%sa$ và $SA$ vuông góc với mặt phẳng $\\left( ABC \\right)$. Biết góc giữa hai mặt phẳng $\\left( SAB \\right)$ và $\\left( SBC \\right)$ bằng $60^\\circ$. Thể tích của khối chóp $S.ABC$ bằng"
                             % (latex(2*n_val), latex(n_val)))

            # Lời giải chi tiết
            loigiai = ("Trong $\\Delta ABC$ kẻ $CH \\perp AB \\Rightarrow CH \\perp \\left( SAB \\right) \\Rightarrow CH \\perp SB \\left( 1 \\right)$.\\\\ "
                       "$BC = \\sqrt{AB^2 - AC^2} = %sa\\sqrt{3}$.\\\\ "
                       "$BH \\cdot BA = BC^2 \\Rightarrow BH = \\frac{3a}{2} \\cdot %s = %sa$, $CH = \\sqrt{BC^2 - BH^2} = \\frac{%sa\\sqrt{3}}{2}$.\\\\ "
                       "Trong $\\Delta SAB$ kẻ $HK \\perp SB \\Rightarrow CK \\perp SB \\left( 2 \\right)$.\\\\ "
                       "Từ $\\left( 1 \\right), \\left( 2 \\right) \\Rightarrow HK \\perp SB$.\\\\ "
                       "Góc giữa hai mặt phẳng $\\left( SAB \\right)$ và $\\left( SBC \\right)$ là $\\widehat{CKH} = 60^\\circ$.\\\\ "
                       "Trong tam giác vuông $\\Delta CKH$ có $HK = CH \\cdot \\cot 60^\\circ = \\frac{%sa}{2}$, $BK = \\sqrt{BH^2 - HK^2} = %sa\\sqrt{2}$.\\\\ "
                       "$\\Delta SAB \\sim \\Delta HKB$ (g.g) nên $\\frac{SA}{HK} = \\frac{AB}{BK} = \\frac{%sa}{%sa\\sqrt{2}} \\Rightarrow SA = \\frac{%sa}{\\sqrt{2}}$.\\\\ "
                       "Thể tích hình chóp $S.ABC$ là $V = \\frac{1}{3} \\cdot SA \\cdot S_{\\Delta ABC} = \\frac{1}{3} \\cdot \\frac{%sa}{\\sqrt{2}} \\cdot \\frac{1}{2} \\cdot %sa \\cdot %sa\\sqrt{3} = %s a^3$."
                       % (latex(n_val), latex(n_val), bh_tex, latex(n_val), hk_tex, latex(n_val), latex(2*n_val), latex(n_val), latex(n_val), latex(n_val), latex(n_val), latex(n_val), v_tex))

            # TikZ Code (mô phỏng hình vẽ)
            tikz_code = ("\\begin{center} \\begin{tikzpicture}[line cap=round,line join=round,x=1.0cm,y=1.0cm, scale=0.8, line width=1pt]\n"
                         "\\coordinate (A) at (0,0); \n"
                         "\\coordinate (B) at (5,0); \n"
                         "\\coordinate (C) at (2,-1.5); \n"
                         "\\coordinate (S) at (0,5); \n"
                         "\\coordinate (H) at ($(A)!0.25!(B)$); \n"
                         "\\coordinate (K) at ($(B)!0.4!(S)$); \n"
                         "\\draw [dashed] (A)--(B) (C)--(H) (H)--(K);\n"
                         "\\draw (S)--(A) (S)--(B) (S)--(C) (A)--(C) (C)--(B) (C)--(K);\n"
                         "\\draw (0.2,0) -- (0.2,0.2) -- (0,0.2);\n" # Góc vuông tại A
                         "\\draw (1.8,-1.3) -- (1.95,-1.45) -- (2.1,-1.3);\n" # Góc vuông tại C (tương đối)
                         "\\begin{scriptsize}\n"
                         "\\draw (S) node[above left] {$S$};\n"
                         "\\draw (A) node[left] {$A$};\n"
                         "\\draw (B) node[right] {$B$};\n"
                         "\\draw (C) node[below] {$C$};\n"
                         "\\draw (H) node[above left] {$H$};\n"
                         "\\draw (K) node[above right] {$K$};\n"
                         "\\draw (1.8,0.3) node {$60^\\circ$};\n"
                         "\\end{scriptsize}\n"
                         "\\draw (H)++(0.1,0.03) -- ++(0.05,0.15) -- ++(-0.1,0); \n" # Ký hiệu vuông góc H
                         "\\draw (K)++(-0.1,-0.1) -- ++(-0.1,0.1) -- ++(0.1,0.1); \n" # Ký hiệu vuông góc K
                         "\\end{tikzpicture} \\end{center}")

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

