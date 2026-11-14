
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


def bt_dang29_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình lập phương $ABCD.A\'B\'C\'D\'$ có cạnh bằng $2$. Gọi $M, N$ lần lượt là trung điểm của $BC$ và $CD$. Tính diện tích thiết diện của hình lập phương khi cắt bởi mặt phẳng $(A\'MN)$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.7, line join=round, line cap=round] \n'
                    '\\coordinate (B\') at (0,4); \n'
                    '\\coordinate (A\') at (3,6); \n'
                    '\\coordinate (C\') at (6,4); \n'
                    '\\coordinate (D\') at (9,6); \n'
                    '\\coordinate (B) at (0,0); \n'
                    '\\coordinate (A) at (3,2); \n'
                    '\\coordinate (C) at (6,0); \n'
                    '\\coordinate (D) at (9,2); \n'
                    '\\coordinate (M) at ($(B)!0.5!(C)$); \n'
                    '\\coordinate (N) at ($(C)!0.5!(D)$); \n'
                    '\\coordinate (J) at (intersection of M--N and A--B); \n'
                    '\\coordinate (I) at (intersection of M--N and A--D); \n'
                    '\\coordinate (Q) at (intersection of A\'--J and B--B\'); \n'
                    '\\coordinate (P) at (intersection of A\'--I and D--D\'); \n'
                    '\\draw[dashed] (Q) -- (B) -- (M) (P) -- (D) -- (N) (A) -- (B) (A) -- (D) (A) -- (A\') (J) -- (A) (A) -- (I) (J) -- (A\') (A\') -- (I) (M) -- (N) (A\') -- (Q) (A\') -- (P); \n'
                    '\\draw (M) -- (C) -- (N) (P) -- (D\') (C) -- (C\') (P) -- (N) (Q) -- (M) (Q) -- (B\') (A\') -- (B\') -- (C\') -- (D\') -- cycle; \n'
                    '\\draw (J) -- (M) (N) -- (I) (J) -- (Q) (I) -- (P); \n'
                    '\\fill[pattern=north east lines, pattern color=gray!80] (A\') -- (Q) -- (M) -- (N) -- (P) -- cycle; \n'
                    '\\fill (A) circle (1.5pt) node[below] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below left] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[below] {$D$}; \n'
                    '\\fill (A\') circle (1.5pt) node[above] {$A\'$}; \n'
                    '\\fill (B\') circle (1.5pt) node[left] {$B\'$}; \n'
                    '\\fill (C\') circle (1.5pt) node[right] {$C\'$}; \n'
                    '\\fill (D\') circle (1.5pt) node[right] {$D\'$}; \n'
                    '\\fill (M) circle (1.5pt) node[below] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[below right] {$N$}; \n'
                    '\\fill (I) circle (1.5pt) node[right] {$I$}; \n'
                    '\\fill (J) circle (1.5pt) node[below left] {$J$}; \n'
                    '\\fill (P) circle (1.5pt) node[right] {$P$}; \n'
                    '\\fill (Q) circle (1.5pt) node[left] {$Q$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '$MN \\cap AD = I, MN \\cap AB = J, A\'I \\cap DD\' = P, A\'J \\cap BB\' = Q$. \\\\ \n'
                    'Suy ra thiết diện là ngũ giác $A\'PNMQ$. \\\\ \n'
                    '$\\Delta DNI = \\Delta CMN = \\Delta BMJ \\Rightarrow JB = ID = BM = DN = 1 \\Rightarrow PD = BQ = \\dfrac{1}{3}AA\' = \\dfrac{2}{3}$. \\\\ \n'
                    'Ta có $QJ = QM = \\dfrac{\\sqrt{13}}{3}, JM = \\sqrt{2} \\Rightarrow S_{\\Delta QJM} = \\dfrac{\\sqrt{17}}{6}$ (áp dụng công thức Heron) \\\\ \n'
                    'Tương tự $PN = PI = \\dfrac{\\sqrt{13}}{3}, NI = \\sqrt{2} \\Rightarrow S_{\\Delta PNI} = \\dfrac{\\sqrt{17}}{6}$. \\\\ \n'
                    'Mặt khác $A\'I = A\'J = \\sqrt{13}, JI = \\sqrt{18} \\Rightarrow S_{\\Delta A\'JI} = \\dfrac{3\\sqrt{17}}{2}$. \\\\ \n'
                    'Từ đó suy ra $S_{A\'PNMQ} = S_{\\Delta A\'JI} - S_{\\Delta QJM} - S_{\\Delta PNI} = \\dfrac{3\\sqrt{17}}{2} - \\dfrac{\\sqrt{17}}{6} - \\dfrac{\\sqrt{17}}{6} = \\dfrac{7\\sqrt{17}}{6}$. \\\\ \n'
    )
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
