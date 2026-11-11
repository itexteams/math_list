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


def bt_dang12_p4_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành và $M,N,E$ lần lượt là trung điểm của các đoạn thẳng $AB,CD,SA$ (hình dưới). Chứng minh rằng\\\\ \n'
                         'a) $MN$ song song với hai mặt phẳng $(SBC)$ và $(SAD)$.\\\\ \n'
                         'b) $SB$ và $SC$ song song với mặt phẳng $(MNE)$. \n')
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[>=stealth,scale=0.7, line join = round, line cap = round] \n'
                   '\\tkzDefPoints{0/0/B, 4/0/C, 2/2/A} \n'
                   '\\coordinate (D) at ($(A)+(C)-(B)$); \n'
                   '\\coordinate (S) at ($(A)+(1,3)$); \n'
                   '\\tkzDefMidPoint(A,B) \\tkzGetPoint{M} \n'
                   '\\tkzDefMidPoint(C,D) \\tkzGetPoint{N} \n'
                   '\\tkzDefMidPoint(S,A) \\tkzGetPoint{E} \n'
                   '\\tkzDrawSegments(S,B S,C S,D B,C C,D) \n'
                   '\\tkzDrawSegments[dashed](S,A A,B A,D M,N M,E E,N) \n'
                   '\\tkzDrawPoints(S,A,B,C,D,M,N,E) \n'
                   '\\tkzLabelPoints[above](S) \n'
                   '\\tkzLabelPoints[left](E) \n'
                   '\\tkzLabelPoints[below](C) \n'
                   '\\tkzLabelPoints[right](D) \n'
                   '\\tkzLabelPoints[below left](B) \n'
                   '\\tkzLabelPoints[below right](N,M) \n'
                   '\\tkzLabelPoints[above right](A) \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'a) Do $M, N$ lần lượt là trung điểm của $AB, CD$ suy ra $MN \\parallel BC, MN \\parallel AD$. \n'
                   'Ta có $MN$ không nằm trong $(SBC)$ và song song với $BC$ nằm trong $(SBC)$ \n'
                   'Suy ra $MN \\parallel (SBC)$ và chứng minh tương tự $MN \\parallel (SAD)$.\\\\ \n'
                   'b) Do $M, E$ lần lượt là trung điểm của $AB, SA$ suy ra $ME$ là đường trung bình tam giác $SAB$ hay $ME \\parallel SB$. \n'
                   'Ta có $SB$ không nằm trong $(MNE)$ và song song với $ME$ nằm trong $(MNE) \\Rightarrow SB \\parallel (MNE)$. \n'
                   'Gọi $O$ là giao điểm của $AC$ và $BD$ do $ABCD$ là hình bình hành nên $O$ là trung điểm của $AC$ mà $E$ là trung điểm của $SA$ nên $OE$ là đường trung bình của tam giác $SAC \\Rightarrow OE \\parallel SC$ \n'
                   'Ta có $SC$ không nằm trong $(MNE)$ và song song với $OE$ nằm trong $(MNE) \\Rightarrow SC \\parallel (MNE)$. \n')
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+
               '\\loigiai{ \n'
               +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content  

