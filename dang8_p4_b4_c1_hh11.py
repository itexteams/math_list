
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


def bt_dang8_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k = 2
        if k == 2:
            gt_M_N = 'Gọi $M, N$ lần lượt là trung điểm của $SA$ và $AD$'
            lg_MN = 'Ta có $M, N$ lần lượt là trung điểm của $SA$ và $AD \\Rightarrow MN$ là đường trung bình của $\\Delta SAD \\Rightarrow MN \\parallel SD$'
            lg_BN = 'Mà có $2ND = AD = 2BC$ và $ND \\parallel BC$ nên suy ra $BNDC$ là hình bình hành $\\Rightarrow BN \\parallel CD$'
        else:
            k_minus_1 = k - 1
            gt_M_N = f'Gọi $N$ thuộc cạnh $AD$ sao cho $AD = {k}DN$, $M$ thuộc cạnh $SA$ sao cho $SA = {k}SM$'
            lg_MN = f'Ta có $SA = {k}SM \\Rightarrow \\dfrac{{AM}}{{AS}} = \\dfrac{{{k_minus_1}}}{{{k}}}$ và $AD = {k}DN \\Rightarrow \\dfrac{{AN}}{{AD}} = \\dfrac{{{k_minus_1}}}{{{k}}}$. Trong $\\Delta SAD$ có $\\dfrac{{AM}}{{AS}} = \\dfrac{{AN}}{{AD}}$ nên $MN \\parallel SD$'
            lg_BN = f'Ta có $AD = {k}DN$ mà $AD = {k}BC \\Rightarrow DN = BC$. Lại có $DN \\parallel BC$ (do $AD \\parallel BC$) nên tứ giác $BNDC$ là hình bình hành $\\Rightarrow BN \\parallel CD$'
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ với đáy $ABCD$ là hình thang mà $AD \\parallel BC$ và $AD = %s BC$. %s. Chứng minh: $(BMN) \\parallel (SCD)$ từ đó suy ra $BM \\parallel (SCD)$. \n'
                         %(k, gt_M_N))
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (0,2); \n'
                    '\\coordinate (D) at (6,2); \n'
                    '\\coordinate (B) at (1.5,0); \n'
                    '\\coordinate (C) at (1.5+6/%s,0); \n'
                    '\\coordinate (S) at (2.5,6); \n'
                    '\\coordinate (N) at ($(D)!1/%s!(A)$); \n'
                    '\\coordinate (M) at ($(S)!1/%s!(A)$); \n'
                    '\\draw[dashed] (A) -- (D) (A) -- (C) (B) -- (D) (M) -- (N) (B) -- (N) (N) -- (C); \n'
                    '\\draw (S) -- (A) (S) -- (B) (S) -- (C) (S) -- (D) (A) -- (B) (B) -- (C) (C) -- (D) (B) -- (M); \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[right] {$D$}; \n'
                    '\\fill (M) circle (1.5pt) node[left] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[above right] {$N$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '%s. Ta có $\\begin{cases} MN \\parallel SD \\\\ SD \\subset (SCD) \\\\ MN \\not\\subset (SCD) \\end{cases} \\Rightarrow MN \\parallel (SCD)$. \\\\ \n'
                    '%s. \\\\ \n'
                    'Ta có $\\begin{cases} NB \\parallel CD \\\\ CD \\subset (SCD) \\\\ NB \\not\\subset (SCD) \\end{cases} \\Rightarrow NB \\parallel (SCD)$. '
                    'Khi đó $\\begin{cases} MN, NB \\parallel (SCD) \\\\ MN, NB \\subset (BMN) \\\\ MN \\cap NB = N \\end{cases} \\Rightarrow (BMN) \\parallel (SCD)$. \\\\ \n'
                    'Mặt khác do $BM \\subset (BMN)$ nên $BM \\parallel (SCD)$. \n'
                    %(k, k, k, lg_MN, lg_BN))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
