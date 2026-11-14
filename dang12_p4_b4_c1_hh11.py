
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


def bt_dang12_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k =2
        if k == 2:
            gt_diem = 'Gọi $M,N,P$ lần lượt là trung điểm của các cạnh $AB, AD, SB$.'
            lg_MN = '$\\Delta ABD$ có $MN$ là đường trung bình nên $MN \\parallel BD$ và $MN = \\dfrac{1}{2}BD$'

        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. ' + gt_diem + '\\\\ \n'
                         'a) Chứng minh $BD \\parallel (MNP)$. \\\\ \n'
                         'b) Tìm giao điểm của $(MNP)$ với $BC$. \\\\ \n'
                         'c) Tìm giao tuyến của hai mặt phẳng $(MNP)$ và $(SBD)$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (2,2); \n'
                    '\\coordinate (B) at (0,0); \n'
                    '\\coordinate (C) at (4,0); \n'
                    '\\coordinate (D) at (6,2); \n'
                    '\\coordinate (S) at (3,6); \n'
                    '\\coordinate (M) at ($(A)!1/'+str(k)+'!(B)$); \n'
                    '\\coordinate (N) at ($(A)!1/'+str(k)+'!(D)$); \n'
                    '\\coordinate (P) at ($(S)!1/'+str(k)+'!(B)$); \n'
                    '\\coordinate (H) at (intersection of M--N and B--C); \n'
                    '\\coordinate (Q) at ($(S)!1/'+str(k)+'!(D)$); \n'
                    '\\draw[dashed] (A) -- (B) (A) -- (D) (S) -- (A) (P) -- (M) (B) -- (D) (M) -- (N) (N) -- (P) (P) -- (Q) (N) -- (Q) (M) -- (H); \n'
                    '\\draw (S) -- (B) -- (C) -- (D) -- (S) -- (C) (B) -- (H) (H) -- (P); \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below right] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[right] {$D$}; \n'
                    '\\fill (M) circle (1.5pt) node[below right] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[above right] {$N$}; \n'
                    '\\fill (P) circle (1.5pt) node[left] {$P$}; \n'
                    '\\fill (Q) circle (1.5pt) node[right] {$Q$}; \n'
                    '\\fill (H) circle (1.5pt) node[left] {$H$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item Chứng minh $BD \\parallel (MNP)$. \\\\ \n'
                    + lg_MN + '. \\\\ \n'
                    'Ta có: $\\begin{cases} BD \\parallel MN \\\\ MN \\subset (MNP) \\Rightarrow BD \\parallel (MNP) \\\\ BD \\not\\subset (MNP) \\end{cases}$. \n'
                    '\\item Tìm giao điểm của $(MNP)$ với $BC$. \\\\ \n'
                    'Trong $(ABCD)$ dựng $H = MN \\cap BC$. \\\\ \n'
                    'Ta có $\\begin{cases} H \\in BC \\\\ H \\in MN, MN \\subset (MNP) \\end{cases} \\Rightarrow H = (MNP) \\cap BC$. \n'
                    '\\item Tìm giao tuyến của hai mặt phẳng $(MNP)$ và $(SBD)$. \\\\ \n'
                    'Gọi $\\Delta = (MNP) \\cap (SBD)$, ta có $\\begin{cases} P \\in (SBD) \\\\ P \\in (MNP) \\end{cases} \\Rightarrow P \\in \\Delta$. \\\\ \n'
                    'Ta có: $\\begin{cases} MN \\parallel BD \\\\ MN \\subset (MNP), BD \\subset (SBD) \\Rightarrow \\Delta \\parallel MN \\\\ (MNP) \\cap (SBD) = \\Delta \\end{cases}$. \\\\ \n'
                    'Vậy $\\Delta$ là đường thẳng qua $P$ và song song với $MN$. \\\\ \n'
                    'Gọi $Q = \\Delta \\cap SD$ ta được $(MNP) \\cap (SBD) = PQ$. \n'
                    '\\end{enumEX} \n')
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
