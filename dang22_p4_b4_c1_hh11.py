
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


def bt_dang22_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình thang $AB \\parallel CD, AB = 2CD$. Điểm $M$ thuộc cạnh $AD$ ($M$ không trùng với $A$ và $D$) sao cho $\\dfrac{MA}{MD} = x$. Gọi $(\\alpha)$ là mặt phẳng qua $M$ và song song với $(SAB)$. Tìm $x$ để diện tích thiết diện của hình chóp cắt bởi mặt phẳng $(\\alpha)$ bằng một nửa diện tích tam giác $SAB$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=1, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (1,2); \n'
                    '\\coordinate (B) at (5,2); \n'
                    '\\coordinate (D) at (2,0); \n'
                    '\\coordinate (C) at (4,0); \n'
                    '\\coordinate (S) at (3,5); \n'
                    '\\coordinate (M) at ($(A)!0.6!(D)$); \n'
                    '\\coordinate (Q) at ($(B)!0.6!(C)$); \n'
                    '\\coordinate (N) at ($(S)!0.6!(D)$); \n'
                    '\\coordinate (P) at ($(S)!0.6!(C)$); \n'
                    '\\coordinate (E) at (intersection of M--N and Q--P); \n'
                    '\\draw[dashed] (A) -- (B) (M) -- (Q) (N) -- (P); \n'
                    '\\draw (S) -- (A) (S) -- (B) (S) -- (C) (S) -- (D) (A) -- (D) -- (C) -- (B) (M) -- (E) -- (Q); \n'
                    '\\fill[gray!30, opacity=0.8] (M) -- (N) -- (P) -- (Q) -- cycle; \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[right] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below right] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[below left] {$D$}; \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (M) circle (1.5pt) node[left] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[left] {$N$}; \n'
                    '\\fill (P) circle (1.5pt) node[right] {$P$}; \n'
                    '\\fill (Q) circle (1.5pt) node[right] {$Q$}; \n'
                    '\\fill (E) circle (1.5pt) node[above] {$E$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    'Dễ thấy thiết diện là hình thang $MNPQ$ (như hình vẽ) \\\\ \n'
                    'Khi đó $MN \\parallel SA$, $NP \\parallel CD$, $PQ \\parallel SB$, $QM \\parallel AB$. \\\\ \n'
                    'Gọi $E$ là giao điểm của $MN$ và $PQ$. \\\\ \n'
                    'Ta có: $QM = \\dfrac{MD}{AD} \\cdot AB + \\dfrac{AM}{AD} \\cdot CD = \\dfrac{1}{x+1} AB + \\dfrac{x}{x+1} \\cdot \\dfrac{CD}{1} = \\dfrac{x+2}{2(x+1)} AB$. \\\\ \n'
                    'Hai tam giác $SAB$ và $EMQ$ đồng dạng nên $\\dfrac{S_{EMQ}}{S_{SAB}} = \\left(\\dfrac{MQ}{AB}\\right)^2 = \\dfrac{(x+2)^2}{4(x+1)^2}$. \\\\ \n'
                    'Vì $\\dfrac{NP}{CD} = \\dfrac{NS}{SD} = \\dfrac{AM}{AD} = \\dfrac{x}{x+1}$ suy ra $NP = \\dfrac{x}{x+1} CD = \\dfrac{x}{2(x+1)} AB$. \\\\ \n'
                    'Do đó $\\dfrac{NP}{QM} = \\dfrac{x}{x+2}$ và $\\dfrac{S_{EPN}}{S_{EMQ}} = \\left(\\dfrac{NP}{MQ}\\right)^2 = \\dfrac{x^2}{(x+2)^2} \\Rightarrow \\dfrac{S_{MNPQ}}{S_{EMQ}} = 1 - \\dfrac{x^2}{(x+2)^2} = \\dfrac{4x+4}{(x+2)^2}$. \\\\ \n'
                    'Từ đó suy ra $\\dfrac{S_{MNPQ}}{S_{SAB}} = \\dfrac{4x+4}{4(x+1)^2} = \\dfrac{1}{x+1} \\Rightarrow S_{MNPQ} = \\dfrac{1}{2} S_{SAB} \\Leftrightarrow \\dfrac{1}{x+1} = \\dfrac{1}{2} \\Leftrightarrow x = 1$. \n')

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
