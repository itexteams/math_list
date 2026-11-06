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


def bt_dang10_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        val = Decimal('0.5')
        kq = val.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(val).replace('.', ',')

        # Hình vẽ TikZ vẽ đúng 100% như ảnh cung cấp, bỏ lưới ô vuông, nét 1pt, điểm 1pt, màu black
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        \\coordinate (S) at (1.8, 4.2);\n"
            "        \\coordinate (D) at (1.0, 0.0);\n"
            "        \\coordinate (C) at (4.5, 0.0);\n"
            "        \\coordinate (A) at (2.5, 1.2);\n"
            "        \\coordinate (B) at (6.0, 1.2);\n"
            "        \\coordinate (O) at (3.5, 0.6);\n"
            "        \\coordinate (M) at ($(S)!0.5!(B)$);\n"
            "        \\coordinate (N) at ($(S)!0.5!(D)$);\n"
            "        \\coordinate (I) at ($(S)!0.5!(O)$);\n"
            "        \\coordinate (K) at ($(S)!0.5!(C)$);\n"
            "        \\coordinate (E) at ($(A)!0.6!(I)$);\n"
            "        \\draw[line width=1pt] (S)--(D)--(C)--(B)--(S) (S)--(C) (M)--(K);\n"
            "        \\draw[line width=1pt, dashed] (D)--(A)--(B) (S)--(A) (A)--(C) (B)--(D) (S)--(O) (M)--(N)--(A) (A)--(K) (O)--(E);\n"
            "        \\fill (S) circle (1pt) node[above left] {$S$};\n"
            "        \\fill (D) circle (1pt) node[below left] {$D$};\n"
            "        \\fill (C) circle (1pt) node[below right] {$C$};\n"
            "        \\fill (A) circle (1pt) node[left] {$A$};\n"
            "        \\fill (B) circle (1pt) node[above right] {$B$};\n"
            "        \\fill (O) circle (1pt) node[above right] {$O$};\n"
            "        \\fill (M) circle (1pt) node[above right] {$M$};\n"
            "        \\fill (N) circle (1pt) node[left] {$N$};\n"
            "        \\fill (I) circle (1pt) node[above right] {$I$};\n"
            "        \\fill (K) circle (1pt) node[above right] {$K$};\n"
            "        \\fill (E) circle (1pt) node[left] {$E$};\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M, N$ lần lượt là trung điểm của các $SB, SD$; $K$ là giao điểm của mặt phẳng $(AMN)$ và đường thẳng $SC$. Tỉ số $\\frac{SK}{SC}$ bằng bao nhiêu? ''')

        # Nội dung lời giải
        loigiai = ('''\\begin{center}
        	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
        		\\draw [line width=1]    (345.97,240.67) -- (209.97,240.67) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (384.98,189.65) -- (248.98,189.65) ;
        		\\draw [line width=1]    (345.97,240.67) -- (384.98,189.65) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (209.97,240.67) -- (248.98,189.65) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (209.97,240.67) -- (384.98,189.65) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (345.97,240.67) -- (248.98,189.65) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (225.6,64.9) -- (248.98,189.65) ;
        		\\draw [line width=1]    (225.6,64.9) -- (209.97,240.67) ;
        		\\draw [line width=1]    (384.98,189.65) -- (225.6,64.9) ;
        		\\draw [line width=1]    (345.97,240.67) -- (225.6,64.9) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (225.6,64.9) -- (297.48,215.16) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (217.79,152.78) -- (305.29,127.28) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (248.98,189.65) -- (264.6,121.9) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (297.48,215.16) -- (254.1,165.4) ;
        		\\draw (231.5,179.67) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$A$};
        		\\draw (385.83,179) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$B$};
        		\\draw (344.33,238) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$C$};
        		\\draw (194.83,236) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$D$};
        		\\draw (287.83,215.33) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$O$};
        		\\draw (215.67,52) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$S$};
        		\\draw (303.33,113) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$M$};
        		\\draw (202.83,145) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$N$};
        		\\draw (247.33,127.5) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$I$};
        		\\draw (261.33,107) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$K$};
        		\\draw (243.83,154.5) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$E$};
        	\\end{tikzpicture}
        \\end{center} Gọi $O = AC \\cap BD$.\\\\
    Trong $(SBD)$, gọi $I = SO \\cap MN$.\\\\
    Trong $(SAC)$:\\\\
    $\\begin{cases} K = AI \\cap SC \\\\ K \\in AI \\subset (AMN) \\Rightarrow K \\in (AMN) \\\\ K \\in SC \\end{cases}$\\\\
    $\\Rightarrow K = SC \\cap (AMN)$.\\\\
    Kẻ $OE // SC$. Theo định lý Thales, ta có:\\\\
    $\\frac{AC}{AO} = \\frac{KC}{OE}$. (1)\\\\
    $\\frac{IO}{IS} = \\frac{OE}{KS}$. (2)\\\\
    Ta có (1) $\\cdot$ (2):\\\\
    $\\frac{AC}{AO} \\cdot \\frac{IO}{IS} = \\frac{KC}{OE} \\cdot \\frac{OE}{KS}$\\\\
    $\\Leftrightarrow \\frac{AC}{AO} \\cdot \\frac{IO}{IS} = \\frac{KC}{KS}$\\\\
    $\\Leftrightarrow 2 \\cdot 1 = \\frac{KC}{KS}$\\\\
    $\\Leftrightarrow \\frac{SK}{SC} = \\frac{1}{2} = %s$.\\\\
    Vậy tỉ số $\\frac{SK}{SC} = %s$.'''
                   % (kq_str, kq_str)
                   )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n' )
    return content

