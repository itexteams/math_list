
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


def bt_dang23_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k_map = {2: 'gấp đôi', 3: 'gấp $3$ lần', 4: 'gấp $4$ lần'}
        k = random.choice([2, 3, 4])
        alpha = random.choice([30, 45, 60])
        F = random.choice([10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 60])
        if alpha == 45:
            he_so_goc = sqrt(2)
            loai_hinh = 'hình vuông'
        elif alpha == 30:
            he_so_goc = sqrt(3)
            loai_hinh = 'hình thoi có $\\widehat{COD} = 60^\\circ$'
        else:
            he_so_goc = Rational(1)
            loai_hinh = 'hình thoi có $\\widehat{COD} = 120^\\circ$'
        OE_val = simplify(F * he_so_goc)
        F1_val = simplify(OE_val / (k - 1))
        F2_val = simplify(k * F1_val)
        F2_dec = Decimal(str(float(F2_val.evalf()))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        F2_round_str = str(F2_dec).replace('.', ',')
        if F2_val.is_integer:
            ketqua_F2 = f'{latex(F2_val)}\\text{{ N}}'
        else:
            ketqua_F2 = f'{latex(F2_val)}\\text{{ N}} \\approx {F2_round_str}\\text{{ N}}'
        hs_k1 = '' if (k - 1) == 1 else str(k - 1)
        half_alpha = alpha / 2
        r_label = 0.85 if alpha == 30 else 0.72
        hinhve_de = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\draw (O) circle (1.25);\n'
            '\\draw[-latex] (O)--(2.4,0) node[pos=0.78, above] {$\\vec{F}_1$};\n'
            '\\draw[-latex] (O)--(-4.2,0) node[pos=0.85, above] {$\\vec{F}_2$};\n'
            f'\\draw[dashed, -latex] (O)--({alpha}:2.1) node[above] {{$\\vec{{F}}_3$}};\n'
            f'\\draw[dashed, -latex] (O)--(-{alpha}:2.1) node[below] {{$\\vec{{F}}_4$}};\n'
            '\\fill (O) circle (1.5pt) node[above left] {$O$};\n'
            f'\\node at ({half_alpha}:{r_label}) {{${alpha}^\\circ$}};\n'
            f'\\node at (-{half_alpha}:{r_label}) {{${alpha}^\\circ$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        hinhve_lg = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\draw (O) circle (1.25);\n'
            '\\draw[-latex] (O)--(2.4,0) node[pos=0.78, above] {$\\vec{F}_1$} node[right] {$A$};\n'
            '\\draw[-latex] (O)--(-4.2,0) node[pos=0.85, above] {$\\vec{F}_2$} node[left] {$B$};\n'
            f'\\draw[dashed, -latex] (O)--({alpha}:2.1) node[pos=0.75, right] {{$\\vec{{F}}_3$}} node[above right] {{$C$}};\n'
            f'\\draw[dashed, -latex] (O)--(-{alpha}:2.1) node[pos=0.75, right] {{$\\vec{{F}}_4$}} node[below right] {{$D$}};\n'
            '\\fill (O) circle (1.5pt) node[above left] {$O$};\n'
            f'\\node at ({half_alpha}:{r_label}) {{${alpha}^\\circ$}};\n'
            f'\\node at (-{half_alpha}:{r_label}) {{${alpha}^\\circ$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        noidungcauhoi = (
            f'Một vật đang ở vị trí $O$ chịu hai lực tác dụng ngược chiều nhau là $\\vec{{F}}_1$ và $\\vec{{F}}_2$, trong đó độ lớn lực $\\vec{{F}}_2$ lớn {k_map[k]} độ lớn lực $\\vec{{F}}_1$. Người ta muốn vật dừng lại nên cần tác dụng vào vật hai lực $\\vec{{F}}_3, \\vec{{F}}_4$ có phương hợp với lực $\\vec{{F}}_1$ các góc ${alpha}^\\circ$ như hình vẽ, chúng có độ lớn bằng nhau và bằng ${F}\\text{{ N}}$. Tìm độ lớn của lực $\\vec{{F}}_2$ (kết quả làm tròn đến một chữ số sau dấu phẩy).\n'
            + hinhve_de
        )
        if k == 2:
            buoc_hinh = (
                'Đặt $\\vec{F}_1 = \\overrightarrow{OA}, \\vec{F}_2 = \\overrightarrow{OB}, \\vec{F}_3 = \\overrightarrow{OC}, \\vec{F}_4 = \\overrightarrow{OD}$.\\\\\n'
                'Ta có: $\\vec{F}_3 + \\vec{F}_4 = \\vec{F}_1 \\Leftrightarrow \\overrightarrow{OC} + \\overrightarrow{OD} = \\overrightarrow{OA}$ do đó $OCAD$ là hình bình hành.\\\\\n'
                f'Mặt khác: $OC = OD = {F}$ và $\\widehat{{COD}} = {alpha}^\\circ + {alpha}^\\circ = {2*alpha}^\\circ$ nên $OCAD$ là {loai_hinh}.\\\\\n'
                f'Khi đó: $\\left|\\vec{{F}}_1\\right| = OA = {latex(F1_val)}\\text{{ N}}$, $\\left|\\vec{{F}}_2\\right| = 2\\left|\\vec{{F}}_1\\right| = {ketqua_F2}$.\n'
            )
        else:
            buoc_hinh = (
                'Đặt $\\vec{F}_1 = \\overrightarrow{OA}, \\vec{F}_2 = \\overrightarrow{OB}, \\vec{F}_3 = \\overrightarrow{OC}, \\vec{F}_4 = \\overrightarrow{OD}$ và $\\overrightarrow{OE} = \\overrightarrow{OC} + \\overrightarrow{OD}$.\\\\\n'
                f'Ta có $OCED$ là hình bình hành. Mặt khác $OC = OD = {F}$ và $\\widehat{{COD}} = {alpha}^\\circ + {alpha}^\\circ = {2*alpha}^\\circ$ nên $OCED$ là {loai_hinh}.\\\\\n'
                f'Suy ra $OE = {latex(OE_val)}\\text{{ N}}$. Vì ${hs_k1}\\vec{{F}}_1 = \\vec{{F}}_3 + \\vec{{F}}_4 = \\overrightarrow{{OE}}$ nên $\\left|\\vec{{F}}_1\\right| = \\dfrac{{OE}}{{{k-1}}} = {latex(F1_val)}\\text{{ N}}$.\\\\\n'
                f'Khi đó: $\\left|\\vec{{F}}_2\\right| = {k}\\left|\\vec{{F}}_1\\right| = {ketqua_F2}$.\n'
            )
        loigiai = (
            hinhve_lg +
            f'Ta có: $\\vec{{F}}_2 = -{k}\\vec{{F}}_1$. Để vật trở về trạng thái cân bằng thì hợp lực bằng $\\vec{{0}}$.\\\\\n'
            f'$\\Leftrightarrow \\vec{{F}}_1 + \\vec{{F}}_2 + \\vec{{F}}_3 + \\vec{{F}}_4 = \\vec{{0}} \\Leftrightarrow \\vec{{F}}_1 - {k}\\vec{{F}}_1 + \\vec{{F}}_3 + \\vec{{F}}_4 = \\vec{{0}} \\Leftrightarrow \\vec{{F}}_3 + \\vec{{F}}_4 = {hs_k1}\\vec{{F}}_1$.\\\\\n'
            + buoc_hinh
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
