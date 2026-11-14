
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


def bt_dang13_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình bình hành tâm $O$. Gọi $M,N$ lần lượt là trung điểm của $SA, SB$.\\\\ \n'
                         'a) Chứng minh $(OMN) \\parallel (SCD)$. \\\\ \n'
                         'b) Gọi $K$ là điểm bất kỳ trên $MN$. Chứng minh $OK \\parallel (SCD)$. \n'
                         %())
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (1,2); \n'
                    '\\coordinate (B) at (6,2); \n'
                    '\\coordinate (C) at (4,-1); \n'
                    '\\coordinate (D) at (-1,-1); \n'
                    '\\coordinate (S) at (1,6); \n'
                    '\\coordinate (O) at ($(A)!0.5!(C)$); \n'
                    '\\coordinate (M) at ($(S)!0.5!(A)$); \n'
                    '\\coordinate (N) at ($(S)!0.5!(B)$); \n'
                    '\\coordinate (K) at ($(M)!0.4!(N)$); \n'
                    '\\draw[dashed] (D) -- (A) -- (B) (S) -- (A) (A) -- (C) (B) -- (D) (O) -- (M) (O) -- (N) (M) -- (N) (O) -- (K); \n'
                    '\\draw (S) -- (D) -- (C) -- (B) -- (S) (S) -- (C); \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[right] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[right] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[left] {$D$}; \n'
                    '\\fill (O) circle (1.5pt) node[below] {$O$}; \n'
                    '\\fill (M) circle (1.5pt) node[left] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[right] {$N$}; \n'
                    '\\fill (K) circle (1.5pt) node[above] {$K$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item Chứng minh $(OMN) \\parallel (SCD)$. \n'
                    'Ta có $OM$ là đường trung bình của $\\Delta SAC$ nên $OM \\parallel SC$. \n'
                    'Khi đó $\\begin{cases} OM \\parallel SC \\\\ SC \\subset (SCD) \\\\ OM \\not\\subset (SCD) \\end{cases} \\Rightarrow OM \\parallel (SCD)$. '
                    'Tương tự $\\begin{cases} ON \\parallel SD \\\\ SD \\subset (SCD) \\\\ ON \\not\\subset (SCD) \\end{cases} \\Rightarrow ON \\parallel (SCD)$. \n'
                    'Vậy $\\begin{cases} OM, ON \\parallel (SCD) \\\\ OM, ON \\subset (OMN) \\\\ OM \\cap ON = O \\end{cases} \\Rightarrow (OMN) \\parallel (SCD)$. \n'
                    '\\item Chứng minh $OK \\parallel (SCD)$. \n'
                    'Ta có $\\begin{cases} (OMN) \\parallel (SCD) \\\\ OK \\subset (OMN) \\end{cases} \\Rightarrow OK \\parallel (SCD)$. \n'
                    '\\end{enumEX} \n'
                    %())
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
