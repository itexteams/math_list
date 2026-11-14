
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


def bt_dang23_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình thang $ABCD$ có $AD \\parallel BC, AD = 2BC$. Gọi $E$ là trung điểm $AD$ và $O$ giao điểm của $AC$ và $BE$; $I$ là một điểm di động trên $AC$ khác $A$ và $C$. Qua $I$ vẽ mặt phẳng $(\\alpha)$ song song với $(SBE)$. Tìm thiết diện tạo bởi $(\\alpha)$ và hình chóp $S.ABCD$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.9, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (1,2); \n'
                    '\\coordinate (B) at (3,0); \n'
                    '\\coordinate (C) at (7,0); \n'
                    '\\coordinate (D) at (9,2); \n'
                    '\\coordinate (S) at (5,6); \n'
                    '\\coordinate (E) at ($(A)!0.5!(D)$); \n'
                    '\\coordinate (O) at (intersection of A--C and B--E); \n'
                    '\\coordinate (I1) at ($(A)!0.5!(O)$); \n'
                    '\\coordinate (M) at (intersection of I1--$(I1)+(E)-(B)$ and A--B); \n'
                    '\\coordinate (N) at (intersection of I1--$(I1)+(B)-(E)$ and A--D); \n'
                    '\\coordinate (P) at (intersection of M--$(M)+(S)-(B)$ and S--A); \n'
                    '\\coordinate (I2) at ($(C)!0.4!(O)$); \n'
                    '\\coordinate (H) at (intersection of I2--$(I2)+(E)-(B)$ and B--C); \n'
                    '\\coordinate (U) at (intersection of I2--$(I2)+(B)-(E)$ and A--D); \n'
                    '\\coordinate (K) at (intersection of H--$(H)+(S)-(B)$ and S--C); \n'
                    '\\coordinate (V) at (intersection of U--$(U)+(S)-(E)$ and S--D); \n'
                    '\\draw[dashed] (A) -- (D) (A) -- (C) (B) -- (E) (S) -- (E) (M) -- (N) -- (P) (H) -- (U) -- (V); \n'
                    '\\draw (S) -- (A) (S) -- (B) (S) -- (C) (S) -- (D) (A) -- (B) -- (C) -- (D) (M) -- (P) (H) -- (K) -- (V); \n'
                    '\\fill[gray!30, opacity=0.8] (M) -- (N) -- (P) -- cycle; \n'
                    '\\fill[gray!30, opacity=0.8] (H) -- (U) -- (V) -- (K) -- cycle; \n'
                    '\\fill (A) circle (1.5pt) node[left] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[right] {$D$}; \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (E) circle (1.5pt) node[below] {$E$}; \n'
                    '\\fill (O) circle (1.5pt) node[below] {$O$}; \n'
                    '\\fill (I1) circle (1.5pt) node[below right] {$I$}; \n'
                    '\\fill (M) circle (1.5pt) node[left] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[right] {$N$}; \n'
                    '\\fill (P) circle (1.5pt) node[above left] {$P$}; \n'
                    '\\fill (H) circle (1.5pt) node[below] {$H$}; \n'
                    '\\fill (U) circle (1.5pt) node[below right] {$U$}; \n'
                    '\\fill (K) circle (1.5pt) node[right] {$K$}; \n'
                    '\\fill (V) circle (1.5pt) node[right] {$V$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '\\textbf{Trường hợp 1:} Điểm $I$ nằm giữa $A$ và $O$. \\\\ \n'
                    'Qua $I$ kẻ đường thẳng song song với $BE$ cắt $AB, AD$ lần lượt tại $M$ và $N$. \\\\ \n'
                    'Qua $M$ kẻ đường thẳng song song với $SB$ cắt $SA$ tại $P$. \\\\ \n'
                    'Suy ra $(MNP)$ là mặt phẳng đi qua $I$ và song song với $(SBE)$. \\\\ \n'
                    'Do đó, thiết diện của hình chóp cắt bởi mặt phẳng $(\\alpha)$ là tam giác $MNP$. \\\\ \n'
                    '\\textbf{Trường hợp 2:} Điểm $I$ nằm giữa $C$ và $O$. \\\\ \n'
                    'Qua $I$ kẻ đường thẳng song song với $BE$ cắt $BC, AD$ lần lượt tại $H$ và $U$. \\\\ \n'
                    'Qua $H$ kẻ đường thẳng song song với $SB$ cắt $SC$ tại $K$. \\\\ \n'
                    'Qua $U$ kẻ đường thẳng song song với $SE$ cắt $SD$ tại $V$. \\\\ \n'
                    'Suy ra $(HKVU)$ là mặt phẳng đi qua $I$ và song song với $(SBE)$. \\\\ \n'
                    'Do đó thiết diện của hình chóp cắt bởi mặt phẳng $(\\alpha)$ là tứ giác $HKVU$. \n')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
