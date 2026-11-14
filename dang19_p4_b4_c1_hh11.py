
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


def bt_dang19_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M,N,Q$ lần lượt là trung điểm của các cạnh $AB,AD,SC$. Thiết diện của hình chóp với mặt phẳng $(MNQ)$ là đa giác có bao nhiêu cạnh? \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.6, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (6,2); \n'
                    '\\coordinate (B) at (2,-1); \n'
                    '\\coordinate (C) at (7,-1); \n'
                    '\\coordinate (D) at (11,2); \n'
                    '\\coordinate (S) at (4,6); \n'
                    '\\coordinate (M) at ($(A)!0.5!(B)$); \n'
                    '\\coordinate (N) at ($(A)!0.5!(D)$); \n'
                    '\\coordinate (Q) at ($(S)!0.5!(C)$); \n'
                    '\\coordinate (E) at (intersection of M--N and C--B); \n'
                    '\\coordinate (F) at (intersection of M--N and C--D); \n'
                    '\\coordinate (L) at (intersection of E--Q and S--B); \n'
                    '\\coordinate (K) at (intersection of F--Q and S--D); \n'
                    '\\draw[dashed] (A) -- (B) (K) -- (N) (L) -- (M) (A) -- (D) (A) -- (S) (E) -- (M) (M) -- (N) (N) -- (F); \n'
                    '\\draw (S) -- (B) (S) -- (C) (S) -- (D) (E) -- (B) -- (C) -- (D) -- (F) (E) -- (L) -- (Q) -- (K) -- (F); \n'
                    '\\fill[pattern=north east lines, pattern color=gray!80] (M) -- (L) -- (Q) -- (K) -- (N) -- cycle; \n'
                    '\\fill (A) circle (1.5pt) node[below left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[right] {$D$}; \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (M) circle (1.5pt) node[below] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[below right] {$N$}; \n'
                    '\\fill (Q) circle (1.5pt) node[left] {$Q$}; \n'
                    '\\fill (E) circle (1.5pt) node[below left] {$E$}; \n'
                    '\\fill (F) circle (1.5pt) node[right] {$F$}; \n'
                    '\\fill (L) circle (1.5pt) node[left] {$L$}; \n'
                    '\\fill (K) circle (1.5pt) node[above right] {$K$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    'Trong mặt phẳng $(ABCD)$ gọi $E = MN \\cap CB, F = MN \\cap CD$. \\\\ \n'
                    'Trong mặt phẳng $(SBC)$ gọi $L = EQ \\cap SB$. \\\\ \n'
                    'Trong mặt phẳng $(SCD)$ gọi $K = FQ \\cap SD$. \\\\ \n'
                    'Khi đó mặt phẳng $(MNQ)$ cắt các mặt của hình chóp theo các đoạn giao tuyến $MN, NL, LQ, QK, KM$. \\\\ \n'
                    'Vậy thiết diện là ngũ giác $MNLKQ$ có 5 cạnh. \n')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
