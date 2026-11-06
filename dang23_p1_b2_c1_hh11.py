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


def bt_dang23_p1_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = [
        (2, 3, "2"),
        (3, 4, "3"),
        (4, 5, "4"),
        (5, 6, "5")
    ]
    # Random các số tỷ lệ trong bài toán
    tu, mau, an_nd_val = random.choice(lisdang)

    td = 'ABCD'

    # Câu hỏi
    noidungcauhoi = ('''Cho tứ diện $%s$, gọi $M$ là điểm thuộc cạnh $AB$ sao cho $AM = \\frac{%s}{%s}AB$, $N$ là điểm thuộc cạnh $AD$ sao cho $AN = %s ND$, $P, Q$ lần lượt là trung điểm $BC, CD$. Giao tuyến của hai mặt phẳng $(ABD)$ và $(MPQ)$ là'''
                     % (td, tu, mau, an_nd_val))

    # Các đáp án
    da_d = ('\\True $%s$' % 'MN')
    da_s1 = ('$%s$' % 'MD')
    da_s2 = ('$%s$' % 'MB')
    da_s3 = ('$%s$' % 'MP')

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Nội dung lời giải
    loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (2.5,3.5);
    \\coordinate (B) at (0.5,1.2);
    \\coordinate (D) at (4.5,1.2);
    \\coordinate (C) at (1.8,0);
    \\coordinate (M) at ($(A)!2/3!(B)$);
    \\coordinate (N) at ($(A)!2/3!(D)$);
    \\coordinate (P) at ($(B)!0.5!(C)$);
    \\coordinate (Q) at ($(C)!0.5!(D)$);
    \\draw[line width=1pt] (A)--(B) (B)--(C) (C)--(D) (D)--(A) (A)--(C) (M)--(P) (N)--(Q);
    \\draw[line width=1pt, dashed] (B)--(D) (M)--(N) (P)--(Q);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\fill (P) circle (1pt) node[below left] {$P$};
    \\fill (Q) circle (1pt) node[below right] {$Q$};
    \\end{tikzpicture}
    \\end{center} Vì $AM = \\frac{%s}{%s}AB \\Rightarrow \\frac{AM}{AB} = \\frac{%s}{%s}$ và $AN = %s ND \\Rightarrow \\frac{AN}{ND} = %s \\Rightarrow \\frac{AN}{AN+ND} = \\frac{%s}{%s+1} \\Rightarrow \\frac{AN}{AD} = \\frac{%s}{%s}$ \\\\ Suy ra
    $\\frac{AM}{AB} = \\frac{AN}{AD} \\Rightarrow MN // BD \\ (1)$. \\\\
    Vì $P, Q$ lần lượt là trung điểm $BC, CD$ suy ra $PQ // BD \\ (2)$. \\\\
    Từ $(1),(2) \\Rightarrow MN // PQ \\Rightarrow N \\in (MPQ)$. Hai mặt phẳng $(MPQ)$ và $(ABD)$ có hai điểm chung $M$ và $N$. Vậy $(MPQ) \\cap (ABD) = MN$.'''
    % (tu, mau, tu, mau, an_nd_val, an_nd_val, tu, tu, tu, mau))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\choice \n'
               '{'+str(list_1[1])+'}\n'
               '{'+str(list_1[2])+'}\n'
               '{'+str(list_1[3])+'}\n'
               '{'+str(list_1[0])+'}\n'
               '\\loigiai{'+str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

