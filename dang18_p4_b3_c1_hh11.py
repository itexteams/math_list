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


def bt_dang18_p4_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$. Gọi $M, N$ là hai điểm trên cạnh $AB, CD$. Mặt phẳng $(P)$ qua $MN$ và song song với $SA$. Xác định thiết diện của $(P)$ với hình chóp. \n')
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[>=stealth,scale=1, line join = round, line cap = round] \n'
                   '\\tkzDefPoints{0/0/A, 5/0/D, 2/-2/B, 6/-3/C} \n'
                   '\\coordinate (S) at ($(A)+(1,3)$); \n'
                   '\\coordinate (M) at ($(A)!0.6!(B)$); \n'
                   '\\coordinate (N) at ($(D)!0.7!(C)$); \n'
                   '\\tkzInterLL(A,C)(M,N) \\tkzGetPoint{E} \n'
                   '\\tkzDefLine[parallel=through M](S,A) \\tkzGetPoint{m} \n'
                   '\\tkzInterLL(M,m)(S,B) \\tkzGetPoint{K} \n'
                   '\\tkzDefLine[parallel=through E](S,A) \\tkzGetPoint{e} \n'
                   '\\tkzInterLL(E,e)(S,C) \\tkzGetPoint{H} \n'
                   '\\tkzDrawSegments(S,B S,C S,D A,B B,C C,D S,A M,K K,H H,N) \n'
                   '\\tkzDrawSegments[dashed](A,D A,C M,N E,H S,E) \n'
                   '\\tkzFillPolygon[black, opacity=0.3](M,K,H,N) \n'
                   '\\tkzDrawPoints(S,A,B,C,D,M,N,E,K,H) \n'
                   '\\tkzLabelPoints[above](S,H) \n'
                   '\\tkzLabelPoints[below](B,C,E) \n'
                   '\\tkzLabelPoints[left](A,M,K) \n'
                   '\\tkzLabelPoints[right](D,N) \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Ta có $\\begin{cases} M \\in (P) \\cap (SAB) \\\\ SA \\parallel (P) \\\\ SA \\subset (SAB) \\end{cases}$ nên giao tuyến của mặt phẳng $(P)$ và $(SAB)$ là đường thẳng đi qua $M$ song song với $SA$ và cắt $SB$ tại $K$. \n'
                   'Trong $(ABCD)$ gọi $E = AC \\cap MN \\Rightarrow E \\in (P)$. \n'
                   'Ta có $\\begin{cases} E \\in (P) \\cap (SAC) \\\\ SA \\parallel (P) \\\\ SA \\subset (SAC) \\end{cases}$ nên giao tuyến của mặt phẳng $(P)$ và $(SAC)$ là đường thẳng đi qua $E$ song song với $SA$ và cắt $SC$ tại $H$. \n'
                   'Vì $\\begin{cases} (P) \\cap (ABCD) = MN \\\\ (P) \\cap (SAB) = MK \\\\ (P) \\cap (SBC) = KH \\\\ (P) \\cap (SCD) = HN \\end{cases}$ nên thiết diện của hình chóp cắt bởi $(P)$ là tứ giác $MNHK$. \n')
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+
               '\\loigiai{ \n'
               +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content  

