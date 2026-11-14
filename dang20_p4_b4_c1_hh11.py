
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


def bt_dang20_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ đáy là hình bình hành tâm $O$ có $AC = a, BD = b$. Tam giác $SBD$ là tam giác đều. Một mặt phẳng $(\\alpha)$ di động song song với mặt phẳng $(SBD)$ và đi qua điểm $I$ trên đoạn $AC$.\\\\ \n'
                         'a) Xác định thiết diện của hình chóp với mặt phẳng $(\\alpha)$. \\\\ \n'
                         'b) Tính diện tích thiết diện theo $a, b$ và $x = AI$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (1,2.5); \n'
                    '\\coordinate (B) at (-1,0); \n'
                    '\\coordinate (C) at (5,0); \n'
                    '\\coordinate (D) at (7,2.5); \n'
                    '\\coordinate (S) at (1,6); \n'
                    '\\coordinate (O) at (intersection of A--C and B--D); \n'
                    '\\coordinate (I1) at ($(A)!0.4!(O)$); \n'
                    '\\coordinate (M) at (intersection of I1--$(I1)+(D)-(B)$ and A--D); \n'
                    '\\coordinate (N) at (intersection of I1--$(I1)+(B)-(D)$ and A--B); \n'
                    '\\coordinate (P) at (intersection of M--$(M)+(S)-(D)$ and S--A); \n'
                    '\\coordinate (I2) at ($(C)!0.35!(O)$); \n'
                    '\\coordinate (H) at (intersection of I2--$(I2)+(D)-(B)$ and C--D); \n'
                    '\\coordinate (L) at (intersection of I2--$(I2)+(B)-(D)$ and B--C); \n'
                    '\\coordinate (K) at (intersection of H--$(H)+(S)-(D)$ and S--C); \n'
                    '\\draw[dashed] (A) -- (D) (A) -- (B) (A) -- (C) (B) -- (D) (S) -- (O) (M) -- (N) (M) -- (P) (P) -- (N); \n'
                    '\\draw[dashed] (H) -- (L) (S) -- (A) ; \n'
                    '\\draw (H) -- (K) (K) -- (L) (S) -- (B) (S) -- (C) (S) -- (D) (B) -- (C) -- (D); \n'
                    '\\fill[gray!30, opacity=0.8] (M) -- (N) -- (P) -- cycle; \n'
                    '\\fill[gray!30, opacity=0.8] (H) -- (L) -- (K) -- cycle; \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below right] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[right] {$D$}; \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (O) circle (1.5pt) node[below] {$O$}; \n'
                    '\\fill (M) circle (1.5pt) node[above] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[left] {$N$}; \n'
                    '\\fill (P) circle (1.5pt) node[above left] {$P$}; \n'
                    '\\fill (H) circle (1.5pt) node[below right] {$H$}; \n'
                    '\\fill (L) circle (1.5pt) node[below] {$L$}; \n'
                    '\\fill (K) circle (1.5pt) node[right] {$K$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item Xác định thiết diện của hình chóp với mặt phẳng $(\\alpha)$. \\\\ \n'
                    'Nếu $I \\in OA$ thì ta có $\\begin{cases} (\\alpha) \\parallel (SBD) \\\\ (ABD) \\cap (SBD) = BD \\\\ I \\in (\\alpha) \\cap (ABD) \\end{cases} \\Rightarrow (\\alpha) \\cap (ABD) = MN$ với $MN$ qua $I$ và $MN \\parallel BD$. \\\\ \n'
                    'Tương tự $(\\alpha)$ cắt $(SAB)$ theo đoạn giao tuyến $MP$ song song với $SB$ cắt $(SAD)$ theo đoạn giao tuyến $NP \\parallel SD$. Thiết diện là tam giác đều $MNP$ (vì đồng dạng với tam giác đều $SBD$). \\\\ \n'
                    'Nếu $I \\in OC$ thì thiết diện là tam giác đều $HKL$ có các cạnh tương ứng song song với cạnh tam giác $SBD$. \n'
                    '\\item Tính diện tích thiết diện theo $a, b$ và $x = AI$. \\\\ \n'
                    'Ta có $S_{\\Delta SBD} = \\dfrac{b^2\\sqrt{3}}{4}$. \\\\ \n'
                    'Nếu $I$ nằm giữa $O$ và $A$ thì $0 < x < \\dfrac{a}{2}$. \\\\ \n'
                    'Khi đó $\\dfrac{S_{\\Delta MNP}}{S_{\\Delta SBD}} = \\left(\\dfrac{MN}{BD}\\right)^2$. Do $MN \\parallel BD$ suy ra $\\dfrac{MN}{BD} = \\dfrac{AI}{AO} = \\dfrac{2x}{a} \\Rightarrow S_{\\Delta MNP} = \\dfrac{b^2 x^2 \\sqrt{3}}{a^2}$. \\\\ \n'
                    'Nếu $I$ nằm giữa $O$ và $C$ thì $\\dfrac{a}{2} < x < a$. \\\\ \n'
                    'Khi đó $\\dfrac{S_{\\Delta HKL}}{S_{\\Delta SBD}} = \\left(\\dfrac{HL}{BD}\\right)^2$. Do $HL \\parallel BD \\Rightarrow \\dfrac{HL}{BD} = \\dfrac{CI}{CO} = \\dfrac{2(a - x)}{a} \\Rightarrow S_{\\Delta HKL} = \\dfrac{b^2(a - x)^2\\sqrt{3}}{a^2}$. \n'
                    '\\end{enumEX} \n')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
