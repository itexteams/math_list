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


def bt_dang24_p4_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        a = 3
        b = a + 1
        noidungcauhoi = ('Cho hình hộp $ABCD.A\'B\'C\'D\'$. Gọi $M$ là điểm trên cạnh $AC$ sao cho $AM = %s MC$. Lấy $N$ trên cạnh $C\'D$ sao cho $C\'N = x C\'D$. Với giá trị nào của $x$ thì $MN \\parallel BD\'$. \n'
                         %(a))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[>=stealth,scale=1, line join = round, line cap = round] \n'
                   '\\tkzDefPoints{0/0/B, 4/0/C, 1/1/A} \n'
                   '\\coordinate (D) at ($(A)+(C)-(B)$); \n'
                   '\\coordinate (A\') at ($(A)+(0,3)$); \n'
                   '\\coordinate (B\') at ($(B)+(0,3)$); \n'
                   '\\coordinate (C\') at ($(C)+(0,3)$); \n'
                   '\\coordinate (D\') at ($(D)+(0,3)$); \n'
                   '\\coordinate (M) at ($(A)!%s!(C)$); \n'
                   '\\coordinate (O) at ($(A)!1/2!(C)$); \n'
                   '\\coordinate (I) at ($(D)!1/2!(D\')$); \n'
                   '\\tkzDefMidPoint(D,D\') \\tkzGetPoint{I} \n'
                   '\\tkzInterLL(C,I)(C\',D) \\tkzGetPoint{N} \n'
                   '\\tkzDrawSegments(B,C C,D D,D\' C,C\' B,B\' B\',C\' C\',D\' D\',A\' A\',B\' C\',D D,N C,I C,D\') \n'
                   '\\tkzDrawSegments[dashed](A,B A,D A,A\' B,D\' A,C M,N O,I B,D I,A) \n'
                   '\\tkzDrawPoints(O, I, A,B,C,D,A\',B\',C\',D\',M,N) \n'
                   '\\tkzLabelPoints[above](A\',D\',C\') \n'
                   '\\tkzLabelPoints[left](B\',B) \n'
                   '\\tkzLabelPoints[right](D,N,I) \n'
                   '\\tkzLabelPoints[below](C,O,M) \n'
                   '\\tkzLabelPoints[above right](A) \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Từ giả thiết, ta có $M$ là trọng tâm tam giác $BCD$. \n'
                   'Gọi $O, I$ lần lượt là trung điểm của $AC$ và $DD\'$. Khi đó, ta có $BD\' \\parallel (IAC)$. \n'
                   'Trong $(CDD\'C\')$ gọi $N\' = CI \\cap C\'D$ khi đó $N\'$ là trọng tâm tam giác $CDD\'$. \n'
                   'Do đó $\\dfrac{CM}{CO} = \\dfrac{2}{3} = \\dfrac{CN\'}{CI} \\Rightarrow MN\' \\parallel OI$ mà $OI \\parallel BD\'$ nên $MN \\parallel BD\'$. Vậy $N\' \\equiv N$ và $x = \\dfrac{2}{3}$. \n'
                   %(Rational(a,b)))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+
               '\\loigiai{ \n'
               +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content  

