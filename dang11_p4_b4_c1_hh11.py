
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


def bt_dang11_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k = 2
        k_plus_1 = k + 1
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình thang, đáy lớn $AD$ gấp %s lần đáy bé $BC$. Gọi $O = AC \\cap BD$, $M$ thuộc cạnh $SA$ sao cho $AM = %s MS$ và $N$ thuộc cạnh $SB$ sao cho $%s BN = NS$. \n'
                         'a) Chứng minh rằng $(OMN) \\parallel (SCD)$. \\\\ \n'
                         'b) Gọi $d = (OMN) \\cap (ABCD)$, $P = d \\cap AD$, $Q = d \\cap BC$. Chứng minh tứ giác $PQCD$ là hình bình hành. \n'
                         %(k, k, k))
        tikz_code = ( '\\begin{center} \n'
                      '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                      '\\coordinate (A) at (0,2); \n'
                      '\\coordinate (D) at (6,2); \n'
                      '\\coordinate (B) at (1.5,0); \n'
                      '\\coordinate (C) at (1.5+6/%s,0); \n'
                      '\\coordinate (S) at (2.5,6); \n'
                      '\\coordinate (O) at (intersection of A--C and B--D); \n'
                      '\\coordinate (M) at ($(S)!1/(%s+1)!(A)$); \n'
                      '\\coordinate (N) at ($(S)!%s/(%s+1)!(B)$); \n'
                      '\\coordinate (P) at (intersection of O--$(O)+(C)-(D)$ and A--D); \n'
                      '\\coordinate (Q) at (intersection of O--$(O)+(C)-(D)$ and B--C); \n'
                      '\\draw[dashed] (A) -- (D) (A) -- (C) (B) -- (D) (O) -- (M) (O) -- (N) (P) -- (Q); \n'
                      '\\draw (S) -- (A) (S) -- (B) (S) -- (C) (S) -- (D) (A) -- (B) (B) -- (C) (C) -- (D) (M) -- (N); \n'
                      '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                      '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                      '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                      '\\fill (C) circle (1.5pt) node[below] {$C$}; \n'
                      '\\fill (D) circle (1.5pt) node[right] {$D$}; \n'
                      '\\fill (O) circle (1.5pt) node[below] {$O$}; \n'
                      '\\fill (M) circle (1.5pt) node[left] {$M$}; \n'
                      '\\fill (N) circle (1.5pt) node[right] {$N$}; \n'
                      '\\fill (P) circle (1.5pt) node[above right] {$P$}; \n'
                      '\\fill (Q) circle (1.5pt) node[below] {$Q$}; \n'
                      '\\end{tikzpicture} \n'
                      '\\end{center} \n'
                      %(k, k, k, k))
        text_solution = ( '\\begin{enumEX}[a)]{1} \n'
                          '\\item Chứng minh rằng $(OMN) \\parallel (SCD)$. \\\\ \n'
                          'Ta có $AM = %s MS \\Rightarrow \\dfrac{AM}{AS} = \\dfrac{%s}{%s}$ và $%s BN = NS \\Rightarrow \\dfrac{BN}{BS} = \\dfrac{1}{%s}$. \\\\ \n'
                          'Xét $\\Delta OAD$ và $\\Delta OCB$ có $\\begin{cases} AD \\parallel BC \\\\ AD = %s BC \\end{cases} \\Rightarrow \\begin{cases} OA = %s OC \\\\ OD = %s OB \\end{cases} \\Rightarrow \\begin{cases} \\dfrac{AO}{AC} = \\dfrac{%s}{%s} \\\\ \\dfrac{BO}{BD} = \\dfrac{1}{%s} \\end{cases}$. \\\\ \n'
                          'Trong tam giác $SAC$ có $\\dfrac{AM}{AS} = \\dfrac{AO}{AC} = \\dfrac{%s}{%s}$ nên $OM \\parallel SC$. \\\\ \n'
                          'Trong tam giác $SBD$ có $\\dfrac{BN}{BS} = \\dfrac{BO}{BD} = \\dfrac{1}{%s}$ nên $ON \\parallel SD$. \\\\ \n'
                          'Như vậy $\\begin{cases} OM \\parallel SC \\\\ ON \\parallel SD \\\\ OM, ON \\subset (OMN) \\\\ SC, SD \\subset (SCD) \\\\ OM \\cap ON = O \\end{cases} \\Rightarrow (OMN) \\parallel (SCD)$. \n'
                          '\\item Chứng minh tứ giác $PQCD$ là hình bình hành. \\\\ \n'
                          'Ta có $\\begin{cases} (OMN) \\parallel (SCD) \\\\ (ABCD) \\cap (SCD) = CD \\\\ (ABCD) \\cap (OMN) = d \\end{cases} \\Rightarrow d \\parallel CD$, trong đó $d$ đi qua $O \\in (ABCD) \\cap (OMN)$. \\\\ \n'
                          'Xét tứ giác $PQCD$ có $\\begin{cases} PQ \\parallel CD \\\\ PD \\parallel CQ \\end{cases} \\Rightarrow PQCD$ là hình bình hành. \n'
                          '\\end{enumEX} \n'
                          %(k, k, k_plus_1, k, k_plus_1, k, k, k, k, k_plus_1, k_plus_1, k, k_plus_1, k_plus_1) )
        loigiai = tikz_code + text_solution
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
