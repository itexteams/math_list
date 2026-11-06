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


def bt_dang10_p1_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':

        # Các đáp án trắc nghiệm (không có dấu chấm ở cuối, thay || bằng //)
        da_d = ('\\True $(ABC)$ cắt $(MNP)$')
        da_s1 = '$(MNP)//(ABC)$'
        da_s2 = '$(A\'B\'C\')//(ABC)$'
        da_s3 = '$(A\'B\'C\')//(MNP)$'

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung câu hỏi
        noidungcauhoi = ('''%s''' % ('Cho hình chóp $S.ABC$. Gọi $M$, $N$, $P$ lần lượt là trung điểm của các cạnh $SA$, $SB$, $SC$. Gọi $A\'$, $B\'$, $C\'$ lần lượt là giao điểm của các cặp đường thẳng $BP$ và $CN$, $CM$ và $AP$, $AN$ và $BM$. Khẳng định nào sau đây \\textbf{sai}?'))

        # Hình vẽ TikZ vẽ đúng 100% theo mẫu, nét vẽ 1pt, điểm 1pt, màu nét vẽ và điểm: black
        hinhve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (S) at (2.5,4.5);
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (3.5,-1.5);
            \\coordinate (C) at (5,0);
            \\coordinate (M) at ($(S)!0.5!(A)$);
            \\coordinate (N) at ($(S)!0.5!(B)$);
            \\coordinate (P) at ($(S)!0.5!(C)$);
            \\coordinate (A') at (intersection of B--P and C--N);
            \\coordinate (B') at (intersection of C--M and A--P);
            \\coordinate (C') at (intersection of A--N and B--M);
            \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S)--(B) (B)--(M) (B)--(P) (A)--(N) (C)--(N) (M)--(N)--(P);
            \\draw[line width=1pt, dashed] (A)--(C) (S)--(N)  (C)--(M) (A)--(P)  (P)--(M) (A')--(B')--(C')--(A');
            \\fill (S) circle (1pt) node[above] {$S$};
            \\fill (A) circle (1pt) node[left] {$A$};
            \\fill (B) circle (1pt) node[below] {$B$};
            \\fill (C) circle (1pt) node[right] {$C$};
            \\fill (M) circle (1pt) node[left] {$M$};
            \\fill (N) circle (1pt) node[below] {$N$};
            \\fill (P) circle (1pt) node[above right] {$P$};
            \\fill (A') circle (1pt) node[above right] {$A\'$};
            \\fill (B') circle (1pt) node[above] {$B\'$};
            \\fill (C') circle (1pt) node[left] {$C\'$};
            \\end{tikzpicture}
            \\end{center}''')

        # Nội dung lời giải (trình bày chi tiết, đầy đủ từng bước như ảnh gốc, thay || bằng //)
        loigiai = ('''%s
    Từ tính chất đường trung bình ta có $\\begin{cases} MN//AB \\\\ MP//AC \\end{cases}$.\\\\
    Ta có:
    $\\begin{cases} MN//AB \\\\ MN \\not\\subset (ABC) \\\\ AB \\subset (ABC) \\end{cases} \\Rightarrow MN//(ABC)$ và $\\begin{cases} MP//AC \\\\ MP \\not\\subset (ABC) \\\\ AC \\subset (ABC) \\end{cases} \\Rightarrow MP//(ABC)$
    $\\begin{cases} MN//(ABC) \\\\ MP//(ABC) \\\\ MN \\cap MP = \\{M\\} \\\\ MN, MP \\subset (MNP) \\end{cases} \\Rightarrow (MNP)//(ABC)$.'''
                   % (hinhve))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n\\choice \n' '{'+str(list_1[0])+'}\n' '{'+str(list_1[1])+'}\n' '{'+str(list_1[2])+'}\n' '{'+str(list_1[3])+'}\n' '\\loigiai{\n'+str(loigiai)+'\n}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

