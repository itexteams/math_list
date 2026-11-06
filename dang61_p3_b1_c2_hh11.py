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


def bt_dang61_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số k để SA = a*sqrt(k)
                list_k = [1, 2, 3, 5, 7, 8, 11, 15]
                k = random.choice(list_k)

                # Thiết lập các giá trị SymPy
                sa_val = sqrt(k)
                ac_val = sqrt(2)
                sb_val = sqrt(k + 1)

                # cos(alpha) = 1 / (sqrt(2) * sqrt(k+1))
                cos_val = 1 / (sqrt(2) * sqrt(k+1))
                cos_val = simplify(cos_val)

                da = '$%s$' % (latex(cos_val))

                s = [
                    '$%s$' % (latex(simplify(sqrt(k) / (k+1)))),
                    '$%s$' % (latex(simplify(sqrt(2) / (k+1)))),
                    '$%s$' % (latex(simplify(sqrt(3) / 4))),
                    '$%s$' % (latex(simplify(sqrt(5) / 5))),
                    '$%s$' % (latex(simplify(sqrt(6) / 6))),
                    '$%s$' % (latex(simplify(sqrt(2) / 2)))
                ]

                if da in s:
                    s.remove(da)

                random.shuffle(s)
                das1 = s[0]; das2 = s[1]; das3 = s[2]

                sa_text = "a" if k == 1 else "a\\sqrt{%s}" % k

                noidungcauhoi = ("Cho khối chóp $S.ABCD$ có $ABCD$ là hình vuông cạnh $a$, $SA = %s$ và $SA$ vuông góc với mặt phẳng đáy. Cosin của góc giữa hai đường thẳng $SB$ và $AC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                                 % (sa_text))

                # Mã TikZ vẽ hình chóp S.ABCD
                ve_hinh = ("\\begin{center}\n"
                           "\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]\n"
                           "\\coordinate (A) at (0,2);\n"
                           "\\coordinate (B) at (4,2);\n"
                           "\\coordinate (D) at (-1.5,0);\n"
                           "\\coordinate (C) at ($(B)+(D)-(A)$);\n"
                           "\\coordinate (S) at (0,5);\n"
                           "\\coordinate (O) at ($(A)!0.5!(C)$);\n"
                           "\\draw [dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D);\n"
                           "\\draw (S)--(B)--(C)--(D)--(S) (S)--(C);\n"
                           "\\fill (A) circle (1pt) node[left] {$A$};\n"
                           "\\fill (B) circle (1pt) node[right] {$B$};\n"
                           "\\fill (C) circle (1pt) node[right] {$C$};\n"
                           "\\fill (D) circle (1pt) node[below left] {$D$};\n"
                           "\\fill (S) circle (1pt) node[above] {$S$};\n"
                           "\\fill (O) circle (1pt) node[below] {$O$};\n"
                           "\\draw (0,2.3)--(0.3,2.3)--(0.3,2);\n" # Ký hiệu góc vuông tại A
                           "\\end{tikzpicture}\n"
                           "\\end{center}")

                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                h1=cos_val
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                loigiai = (ve_hinh + "Gọi $\\alpha$ là góc giữa hai đường thẳng $AC$ và $SB$. \\\\"
                           "Ta có $ABCD$ là hình vuông cạnh $a \\Rightarrow AC = a\\sqrt{2}$. \\\\"
                           "Xét tam giác $SAB$ vuông tại $A$ (do $SA \\perp (ABCD)$), ta có: \\\\"
                           "$SB = \\sqrt{SA^2 + AB^2} = \\sqrt{(%s)^2 + a^2} = a\\sqrt{%s}$. \\\\"
                           "Sử dụng phương pháp vectơ, ta có: \\\\"
                           "$\\vec{AC} \\cdot \\vec{SB} = (\\vec{AB} + \\vec{AD}) \\cdot (\\vec{AB} - \\vec{AS}) = \\vec{AB}^2 - \\vec{AB} \\cdot \\vec{AS} + \\vec{AD} \\cdot \\vec{AB} - \\vec{AD} \\cdot \\vec{AS}$. \\\\"
                           "Vì $SA \\perp (ABCD) \\Rightarrow SA \\perp AB, SA \\perp AD$ và $ABCD$ là hình vuông nên $AB \\perp AD$. \\\\"
                           "Do đó: $\\vec{AC} \\cdot \\vec{SB} = AB^2 = a^2$. \\\\"
                           "Vậy $\\cos\\alpha = \\frac{|\\vec{AC} \\cdot \\vec{SB}|}{AC \\cdot SB} = \\frac{a^2}{a\\sqrt{2} \\cdot a\\sqrt{%s}} = \\frac{1}{\\sqrt{%s}} = %s \\approx %s$."
                           % (sa_text, k + 1, k + 1, 2 * (k + 1), latex(cos_val),str(kqz)))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kqz).replace('.',','))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

