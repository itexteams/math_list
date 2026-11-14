
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


def bt_dang7_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k=randint(2,3)
        k_plus_1 = k + 1
        if k == 2:
            gt_M = 'Gọi $M$ là trọng tâm của tam giác $ABE$.'
            lg_M = ('Vì $M$ là trọng tâm của tam giác $ABE$ nên $M$ thuộc trung tuyến $BO$ (với $O$ là tâm hình bình hành $ABEF$). '
                    'Khi đó $\\dfrac{BM}{BO} = \\dfrac{2}{3}$. \\\\ \n'
                    'Vì $ABEF$ là hình bình hành nên $\\dfrac{BO}{BF} = \\dfrac{1}{2}$. Suy ra $\\dfrac{BM}{BF} = \\dfrac{1}{3}$. Do đó $\\dfrac{BM}{MF} = \\dfrac{1}{2}$. \\\\ \n')
        else:
            gt_M = 'Trên đường chéo $BF$ lấy điểm $M$ sao cho $MF = '+str(k)+' BM$.'
            lg_M = 'Theo giả thiết ta có $MF = '+str(k)+' BM \\Rightarrow \\dfrac{BM}{MF} = \\dfrac{1}{'+str(k)+'}$. \\\\ \n'
        noidungcauhoi = ('Cho hai hình bình hành $ABCD$ và $ABEF$ không cùng nằm trong một mặt phẳng.\\\\ \n'
                         'a) Chứng minh rằng $(AFD) \\parallel (BEC)$. \\\\ \n'
                         'b) '+gt_M+' Gọi $(P)$ là mặt phẳng đi qua $M$ và song song với mặt phẳng $(AFD)$. Lấy $N$ là giao điểm của $(P)$ và $AC$. Tính $\\dfrac{AN}{NC}$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate (D) at (0,0); \n'
                    '\\coordinate (C) at (6,0); \n'
                    '\\coordinate (A) at (1.5,2); \n'
                    '\\coordinate (B) at (7.5,2); \n'
                    '\\coordinate (F) at (2.5,5); \n'
                    '\\coordinate (E) at (8.5,5); \n'
                    '\\coordinate (M) at ($(B)!1/'+str(k_plus_1)+'!(F)$); \n'
                    '\\coordinate (H) at ($(B)!1/'+str(k_plus_1)+'!(A)$); \n'
                    '\\coordinate (N) at ($(C)!1/'+str(k_plus_1)+'!(A)$); \n'
                    '\\coordinate (Q) at ($(F)!1/'+str(k_plus_1)+'!(A)$); \n'
                    '\\draw[dashed] (D) -- (A) -- (B) (A) -- (F) (A) -- (C) (B) -- (F) (H) -- (M) (H) -- (N) (M) -- (N); \n'
                    '\\draw (F) -- (E) -- (B) -- (C) -- (D) -- (F) (D) -- (C) (E) -- (B) (E) -- (C); \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[right] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[right] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[left] {$D$}; \n'
                    '\\fill (E) circle (1.5pt) node[above] {$E$}; \n'
                    '\\fill (F) circle (1.5pt) node[above] {$F$}; \n'
                    '\\fill (M) circle (1.5pt) node[above right] {$M$}; \n'
                    '\\fill (H) circle (1.5pt) node[below] {$H$}; \n'
                    '\\fill (N) circle (1.5pt) node[below] {$N$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item Chứng minh rằng $(AFD) \\parallel (BEC)$. \\\\ \n'
                    'Ta có $AD \\parallel BC$, suy ra $AD \\parallel (BCE)$. Tương tự $AF \\parallel (BCE)$. \\\\ \n'
                    'Khi đó $(ADF) \\parallel (BCE)$. \n'
                    '\\item Tính $\\dfrac{AN}{NC}$. \\\\ \n'
                    'Ta có $(P) \\parallel (AFD)$ nên $(P) \\cap (ABF) = MH$ với $H \\in AB$ và $MH \\parallel AF$. \\\\ \n'
                    +lg_M+
                    'Khi đó $\\dfrac{BH}{AH} = \\dfrac{1}{'+str(k)+'}$ (vì $AF \\parallel MH$). \\\\ \n'
                    'Mà $(P) \\parallel (AFD)$ nên $(P) \\cap (ABC) = NH$ với $N \\in AC$ và $NH \\parallel AD \\Rightarrow NH \\parallel BC$. \\\\ \n'
                    'Do đó $\\dfrac{AN}{NC} = \\dfrac{AH}{BH} = '+str(k)+'$. \n'
                    '\\end{enumEX} \n')
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
