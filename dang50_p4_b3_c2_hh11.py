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


def bt_dang50_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Để các giá trị trung điểm đẹp, ta chọn k là số chẵn.
            k_val = random.choice([2, 4, 6, 8])
            side_str = f"{k_val}a" if k_val > 1 else "a"

            # Các đại lượng tính toán theo k
            # Đường cao SH của tam giác SAB đều cạnh ka: SH = (ka * sqrt(3)) / 2
            sh_val = Rational(k_val, 2) # hệ số của a*sqrt(3)

            # M là trung điểm SC -> MP là đường trung bình tam giác SHC (P là trung điểm HC)
            # MP = SH / 2 = (ka * sqrt(3)) / 4
            mp_num = k_val
            mp_den = 4
            mp_hieu = Rational(mp_num, mp_den) # hệ số của a*sqrt(3)

            # Tính PN: Sử dụng hệ trục tọa độ hoặc hình học phẳng trên đáy
            # H là trung điểm AB, N là trung điểm AD, P là trung điểm HC.
            # PN = 3/4 * cạnh = 3/4 * ka = (3k/4) * a
            pn_val = Rational(3 * k_val, 4)

            # tan(MNP) = MP / PN = [(k*sqrt(3))/4] / [3k/4] = sqrt(3)/3
            # Vậy góc luôn là 30 độ cho cấu trúc này.

            # B4-Điều chỉnh các phương án
            da_dung = '30^\\circ'
            cac_phuong_an_sai = ['45^\\circ', '60^\\circ', '90^\\circ', '15^\\circ']
            random.shuffle(cac_phuong_an_sai)

            list_ans = ['\\True $' + da_dung + '$', 
                        '$' + cac_phuong_an_sai[0] + '$', 
                        '$' + cac_phuong_an_sai[1] + '$', 
                        '$' + cac_phuong_an_sai[2] + '$']
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $%s$. Tam giác $SAB$ đều và nằm trong mặt phẳng vuông góc với đáy. Gọi $M$, $N$ lần lượt là trung điểm của $SC$ và $AD$. Tính góc giữa $MN$ và mặt đáy $(ABCD)$.' 
                             % (side_str))

            # Nội dung lời giải chi tiết
            # Tính toán các chuỗi latex để đưa vào lời giải
            sh_latex = f"\\frac{{{k_val}a\\sqrt{{3}}}}{{2}} = {latex(sh_val)}a\\sqrt{{3}}"
            mp_latex = f"\\frac{{1}}{{2}}SH = \\frac{{{latex(sh_val)}a\\sqrt{{3}}}}{{2}} = \\frac{{{k_val}a\\sqrt{{3}}}}{{4}}"
            pn_latex = f"\\frac{{3}}{4} \\cdot {k_val}a = {latex(pn_val)}a"

            loigiai = (    '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, line join=round, line cap=round, >=stealth, line width=1pt]\n'
                '\\coordinate (A) at (0,0);\n'
                '\\coordinate (B) at (-1.5,-1.5);\n'
                '\\coordinate (C) at (2.5,-1.5);\n'
                '\\coordinate (D) at (4,0);\n'
                '\\coordinate (H) at ($(A)!0.5!(B)$);\n'
                '\\coordinate (S) at ($(H)+(0,3.5)$);\n'
                '\\coordinate (M) at ($(S)!0.5!(C)$);\n'
                '\\coordinate (N) at ($(A)!0.5!(D)$);\n'
                '\\coordinate (P) at ($(H)!0.5!(C)$);\n'
                '\\draw [dashed] (S)--(A)--(B) (A)--(D) (S)--(H) (M)--(P)--(N) (A)--(C) (H)--(C) (M)--(N);\n'
                '\\draw (S)--(B)--(C)--(D)--(S) (S)--(C) ;\n'
                '\\node [left] at (A) {$A$};\n'
                '\\node [below left] at (B) {$B$};\n'
                '\\node [below right] at (C) {$C$};\n'
                '\\node [right] at (D) {$D$};\n'
                '\\node [above] at (S) {$S$};\n'
                '\\node [left] at (H) {$H$};\n'
                '\\node [above right] at (M) {$M$};\n'
                '\\node [above] at (N) {$N$};\n'
                '\\node [below] at (P) {$P$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                '''Gọi $H$ là trung điểm $AB$. Vì $\\triangle SAB$ đều và nằm trong mặt phẳng vuông góc với đáy nên $SH \\perp (ABCD)$ và $SH = ''' + sh_latex + '$' '''.\\\\
            Gọi $P$ là trung điểm $CH$. Trong $\\triangle SHC$, $MP$ là đường trung bình nên $MP // SH$. \\\\
            Mà $SH \\perp (ABCD) \\Rightarrow MP \\perp (ABCD)$.\\\\
            Khi đó, góc giữa $MN$ và mặt đáy $(ABCD)$ là góc $\\widehat{MNP}$ (do $\\widehat{MPN} = 90^\\circ$).\\\\
            Ta có: $MP = ''' + mp_latex + '$' '''.\\\\
            Xét hình vuông $ABCD$, bằng cách sử dụng hệ trục tọa độ hoặc tính toán hình học phẳng, ta tính được độ dài hình chiếu $PN = ''' + pn_latex + '$' '''.\\\\
            Trong tam giác vuông $MNP$:
            $$\\tan \\widehat{MNP} = \\frac{MP}{PN} = \\frac{\\frac{''' + str(k_val) + '''a\\sqrt{3}}{4}}{\\frac{''' + str(3*k_val) + '''a}{4}} = \\frac{\\sqrt{3}}{3}.$$
            Suy ra $\\widehat{MNP} = 30^\\circ$.''')

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

