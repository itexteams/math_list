
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


def bt_dang6_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k=randint(2,5)
        if k==2:
            gt_M = 'Gọi $M$ là trung điểm $SA$.'
            lg_N = 'trung điểm $N$ của $SB$'
            lg_P = 'trung điểm $P$ của $SC$'
        else:
            gt_M = 'Gọi $M$ là một điểm trên cạnh $SA$ sao cho $SA = ' + str(k) + ' SM$.'
            lg_N = 'điểm $N$ thuộc $SB$ sao cho $SB = ' + str(k) + ' SN$'
            lg_P = 'điểm $P$ thuộc $SC$ sao cho $SC = ' + str(k) + ' SP$'
        noidungcauhoi = ('Cho hình chóp $S.ABC$. ' + gt_M + ' Xác định thiết diện của hình chóp cắt bởi mặt phẳng $(P)$ đi qua $M$ và song song với mặt phẳng $(ABC)$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=1, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (0,0); \n'
                    '\\coordinate (C) at (5,0); \n'
                    '\\coordinate (B) at (2.5,-2); \n'
                    '\\coordinate (S) at (2.5,4); \n'
                    '\\coordinate (M) at ($(S)!1/'+str(k)+'!(A)$); \n'
                    '\\coordinate (N) at ($(S)!1/'+str(k)+'!(B)$); \n'
                    '\\coordinate (P) at ($(S)!1/'+str(k)+'!(C)$); \n'
                    '\\draw[dashed] (A) -- (C) (M) -- (P); \n'
                    '\\draw (S) -- (A) (S) -- (B) (S) -- (C) (A) -- (B) (B) -- (C) (M) -- (N) -- (P); \n'
                    '\\fill[gray!30, opacity=0.8] (M) -- (N) -- (P) -- cycle; \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[right] {$C$}; \n'
                    '\\fill (M) circle (1.5pt) node[left] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[below right] {$N$}; \n'
                    '\\fill (P) circle (1.5pt) node[right] {$P$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    'Ta có $M$ là một điểm chung của $(P)$ và $(SAB)$. \\\\ \n'
                    'Do $\\begin{cases} (P) \\parallel (ABC) \\\\ (SAB) \\cap (ABC) = AB \\end{cases}$ nên giao tuyến của $(P)$ và $(SAB)$ là đường thẳng đi qua $M$ song song với $AB$ và cắt $SB$ tại ' + lg_N + '. \\\\ \n'
                    'Tương tự, giao tuyến của $(P)$ và $(SAC)$ là đường thẳng đi qua $M$, song song với $AC$ và cắt $SC$ tại ' + lg_P + '. \\\\ \n'
                    'Vậy thiết diện của hình chóp $S.ABC$ cắt bởi mặt phẳng $(P)$ là tam giác $MNP$. \n')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
