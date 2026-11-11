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


def bt_dang22_p4_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Lấy điểm $M$ trên cạnh $AD$ sao cho $AD = 3AM$. Gọi $G, N$ lần lượt là trọng tâm của tam giác $SAB, ABC$.\\\\ \n'
                         'a) Tìm giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$. \\\\ \n'
                         'b) Chứng minh rằng $MN$ song song với mặt phẳng $(SCD)$ và $NG$ song song với mặt phẳng $(SAC)$. \n')
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[>=stealth,scale=1, line join = round, line cap = round] \n'
                   '\\tkzDefPoints{0/0/D, 4/0/C, 2/2/A} \n'
                   '\\coordinate (B) at ($(A)+(C)-(D)$); \n'
                   '\\coordinate (S) at ($(A)+(1,3)$); \n'
                   '\\coordinate (M) at ($(A)!0.333!(D)$); \n'
                   '\\tkzDefMidPoint(A,B) \\tkzGetPoint{I} \n'
                   '\\tkzCentroid(S,A,B) \\tkzGetPoint{G} \n'
                   '\\tkzCentroid(A,B,C) \\tkzGetPoint{N} \n'
                   '\\tkzDefLine[parallel=through S](A,B) \\tkzGetPoint{d} \n'
                   '\\tkzDrawSegments(S,D S,C S,B D,C C,B S,d) \n'
                   '\\tkzDrawSegments[dashed](S,A A,D A,B M,N I,C S,I N,G) \n'
                   '\\tkzDrawPoints(S,A,B,C,D,M,N,I,G) \n'
                   '\\tkzLabelPoints[above](S,d) \n'
                   '\\tkzLabelPoints[below](D,C) \n'
                   '\\tkzLabelPoints[left](A,M) \n'
                   '\\tkzLabelPoints[right](B,G) \n'
                   '\\tkzLabelPoints[above right](I) \n'
                   '\\tkzLabelPoints[below right](N) \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là đường thẳng $d$ đi qua $S$ và song song với $AB$ và $CD$. \n'
                   '\\item Gọi $I$ là trung điểm của $AB$. \n'
                   'Xét hình bình hành $ABCD$ có $\\dfrac{DM}{DA} = \\dfrac{CN}{CI} = \\dfrac{2}{3} \\Rightarrow MN \\parallel CD$. \n'
                   'Mà $CD \\subset (SCD)$ và $MN \\not\\subset (SCD)$ nên $MN \\parallel (SCD)$. \n'
                   'Ta có $\\dfrac{IG}{IS} = \\dfrac{IN}{IC} = \\dfrac{1}{3} \\Rightarrow NG \\parallel SC$ mà $SC \\subset (SAC)$ và $NG \\not\\subset (SAC)$ nên $NG \\parallel (SAC)$. \n'
                   '\\end{enumEX} \n')
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+
               '\\loigiai{ \n'
               +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content  

