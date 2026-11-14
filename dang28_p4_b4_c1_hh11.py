
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


def bt_dang28_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k = 1
        k_str = str(k)
        kp1_str = str(k+1)
        if k == 1:
            ratio_text = ''
        else:
            ratio_text = ' = ' + k_str
        noidungcauhoi = ('Cho hình hộp $ABCD \\cdot A\'B\'C\'D\'$. Hai điểm $M,N$ lần lượt nằm trên hai cạnh $AD,CC\'$ sao cho $\\dfrac{AM}{MD} = \\dfrac{CN}{NC\'}' + ratio_text + '$. Xác định thiết diện của hình hộp cắt bởi mặt phẳng qua $MN$ và song song với $(ACB\') $. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate (B) at (0,0); \n'
                    '\\coordinate (C) at (6,0); \n'
                    '\\coordinate (A) at (2,2); \n'
                    '\\coordinate (D) at (8,2); \n'
                    '\\coordinate (B\') at (0,4); \n'
                    '\\coordinate (C\') at (6,4); \n'
                    '\\coordinate (A\') at (2,6); \n'
                    '\\coordinate (D\') at (8,6); \n'
                    '\\coordinate (M) at ($(A)!'+k_str+'/'+kp1_str+'!(D)$); \n'
                    '\\coordinate (N) at ($(C)!'+k_str+'/'+kp1_str+'!(C\')$); \n'
                    '\\coordinate (I) at ($(A)!'+k_str+'/'+kp1_str+'!(A\')$); \n'
                    '\\coordinate (E) at ($(D)!1/'+kp1_str+'!(C)$); \n'
                    '\\coordinate (F) at ($(C\')!1/'+kp1_str+'!(B\')$); \n'
                    '\\coordinate (K) at ($(A\')!1/'+kp1_str+'!(B\')$); \n'
                    '\\draw[dashed] (B) -- (A) -- (D) (A) -- (A\') (A) -- (C) (A\') -- (D) (B\') -- (A); \n'
                    '\\draw[dashed] (K) -- (I) -- (M) -- (E); \n'
                    '\\draw (B) -- (C) -- (D) (B) -- (B\') (C) -- (C\') (D) -- (D\') (A\') -- (B\') -- (C\') -- (D\') -- cycle; \n'
                    '\\draw (B\') -- (C); \n'
                    '\\draw (E) -- (N) -- (F) -- (K); \n'
                    '\\fill[gray!30, opacity=0.6] (I) -- (M) -- (E) -- (N) -- (F) -- (K) -- cycle; \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below left] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[right] {$D$}; \n'
                    '\\fill (A\') circle (1.5pt) node[above] {$A\'$}; \n'
                    '\\fill (B\') circle (1.5pt) node[left] {$B\'$}; \n'
                    '\\fill (C\') circle (1.5pt) node[right] {$C\'$}; \n'
                    '\\fill (D\') circle (1.5pt) node[right] {$D\'$}; \n'
                    '\\fill (M) circle (1.5pt) node[below] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[right] {$N$}; \n'
                    '\\fill (I) circle (1.5pt) node[left] {$I$}; \n'
                    '\\fill (E) circle (1.5pt) node[right] {$E$}; \n'
                    '\\fill (F) circle (1.5pt) node[above] {$F$}; \n'
                    '\\fill (K) circle (1.5pt) node[left] {$K$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    'Gọi $I$ là điểm trên $AA\'$ sao cho $\\dfrac{AI}{IA\'} = \\dfrac{AM}{MD}' + ratio_text + '$ suy ra $IM \\parallel A\'D$ suy ra $IM \\parallel CB\'$. \\\\ \n'
                    'Lại có $\\dfrac{AI}{IA\'} = \\dfrac{CN}{NC\'}' + ratio_text + '$ suy ra $IN \\parallel AC$ suy ra $(MNI) \\parallel (ACB\') $. \\\\ \n'
                    'Do đó mặt phẳng $(MNI)$ là mặt phẳng đi qua $M,N$ và song song với mặt phẳng $(ACB\') $. \\\\ \n'
                    'Qua $M$ kẻ $ME \\parallel AC$ ; qua $N$ kẻ $NF \\parallel B\'C\'$ , qua $F$ kẻ $FK \\parallel A\'C\'$ . \\\\ \n'
                    'Khi đó thiết diện cần tìm là đa giác $MENFKI$. \n'
                    )
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
