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


def bt_dang13_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        val = Decimal(3) / Decimal(4)
        kq = val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Hình vẽ TikZ vẽ đúng 100% như ảnh, nét 1pt, điểm 1pt, màu black, không lưới ô vuông
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        \\coordinate (A) at (0.0, 0.0);\n"
            "        \\coordinate (B) at (4.2, -0.1);\n"
            "        \\coordinate (D) at (1.8, 1.7);\n"
            "        \\coordinate (C) at (6.0, 1.6);\n"
            "        \\coordinate (S) at (1.9, 4.3);\n"
            "        \\coordinate (O) at ($(A)!0.5!(C)$);\n"
            "        \\coordinate (M) at ($(S)!0.667!(B)$);\n"
            "        \\coordinate (N) at ($(S)!0.667!(D)$);\n"
            "        \\coordinate (I) at ($(S)!0.667!(O)$);\n"
            "        \\coordinate (P) at ($(S)!0.5!(C)$);\n"
            "        \\coordinate (J) at ($(S)!0.75!(C)$);\n"
            "        \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S) (S)--(B) (M)--(P) (P)--(J)--(B);\n"
            "        \\draw[line width=1pt, dashed] (A)--(D)--(C) (S)--(D) (A)--(C) (B)--(D) (S)--(O) (A)--(M) (A)--(N)--(P) (M)--(N) (A)--(P) (O)--(J) (O)--(M) (O)--(N);\n"
            "        \\fill (S) circle (1pt) node[above] {$S$};\n"
            "        \\fill (A) circle (1pt) node[below left] {$A$};\n"
            "        \\fill (B) circle (1pt) node[below] {$B$};\n"
            "        \\fill (C) circle (1pt) node[right] {$C$};\n"
            "        \\fill (D) circle (1pt) node[left] {$D$};\n"
            "        \\fill (O) circle (1pt) node[below] {$O$};\n"
            "        \\fill (M) circle (1pt) node[right] {$M$};\n"
            "        \\fill (N) circle (1pt) node[left] {$N$};\n"
            "        \\fill (I) circle (1pt) node[above right] {$I$};\n"
            "        \\fill (P) circle (1pt) node[above right] {$P$};\n"
            "        \\fill (J) circle (1pt) node[above right] {$J$};\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Trên các cạnh $SB, SD$ lần lượt lấy các điểm $M, N$ sao cho $\\frac{SM}{SB} = \\frac{SN}{SD} = \\frac{2}{3}$. Mặt phẳng $(\\alpha)$ đi qua điểm $O$ và song song với mặt phẳng $(AMN)$ cắt $SC$ tại $J$. Tỉ số $\\frac{SJ}{SC}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).''')

        # Nội dung lời giải
        loigiai = (hinhve+'''Ta có: $\\frac{SM}{SB} = \\frac{SN}{SD} = \\frac{2}{3} \\Rightarrow MN // BD$.\\\\
    Trong mặt phẳng $(SBD)$ gọi $I = MN \\cap SO$. Ta có $MI // BD \\Rightarrow \\frac{SM}{SB} = \\frac{SI}{SO} = \\frac{2}{3}$.\\\\
    Trong mặt phẳng $(SAC)$ gọi $P = AI \\cap SC \\Rightarrow P = SC \\cap (AMN)$ và $(SAC) \\cap (AMN) = AP$\\\\
    ($P$ là trung điểm $SC$).\\\\
    Hai mặt phẳng song song $(AMN)$ và $(\\alpha)$ bị cắt bởi mặt phẳng $(SAC)$ theo hai giao tuyến $AP$ và $OJ$ nên $AP // OJ$.\\\\
    Ta có: $IP // OJ \\Rightarrow \\frac{SI}{SO} = \\frac{SP}{SJ} = \\frac{2}{3} \\Rightarrow SJ = \\frac{3}{2} SP = \\frac{3}{2} \\cdot \\frac{1}{2} SC = \\frac{3}{4} SC \\Rightarrow \\frac{SJ}{SC} = \\frac{3}{4} = %s$.\\\\
    Vậy tỉ số $\\frac{SJ}{SC} = %s$.'''
                   % (kq_str, kq_str)
                   )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

