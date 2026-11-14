
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


def bt_dang25_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình thoi cạnh $a$, tam giác $SAD$ là tam giác đều. Gọi $M$ là một điểm thuộc cạnh $AB, AM = x$ với $0 < x < a$. Mặt phẳng $(P)$ đi qua $M$ song song với $(SAD)$. Tính diện tích thiết diện của hình chóp $S.ABCD$ cắt bởi mặt phẳng $(P)$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=1, line join=round, line cap=round] \n'
                    '\\coordinate (B) at (0,0); \n'
                    '\\coordinate (C) at (3,-2); \n'
                    '\\coordinate (D) at (7,-2); \n'
                    '\\coordinate (A) at (4,0); \n'
                    '\\coordinate (S) at (4,3); \n'
                    '\\coordinate (M) at ($(A)!0.6!(B)$); \n'
                    '\\coordinate (N) at ($(D)!0.6!(C)$); \n'
                    '\\coordinate (F) at ($(S)!0.6!(C)$); \n'
                    '\\coordinate (E) at ($(S)!0.6!(B)$); \n'
                    '\\coordinate (H) at ($(M)!0.5!(N)$); \n'
                    '\\draw[dashed] (A) -- (B) (M) -- (E) (A) -- (S) (M) -- (N) (A) -- (D); \n'
                    '\\draw (S) -- (B) (S) -- (C) (S) -- (D) (B) -- (C) -- (D) (E) -- (F) -- (N) (F) -- (H); \n'
                    '\\fill[gray!30, opacity=0.8] (M) -- (N) -- (F) -- (E) -- cycle; \n'
                    '\\fill (A) circle (1.5pt) node[right] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[left] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[below] {$D$}; \n'
                    '\\fill (S) circle (1.5pt) node[above] {$S$}; \n'
                    '\\fill (M) circle (1.5pt) node[above right] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[below] {$N$}; \n'
                    '\\fill (E) circle (1.5pt) node[right] {$E$}; \n'
                    '\\fill (F) circle (1.5pt) node[left] {$F$}; \n'
                    '\\fill (H) circle (1.5pt) node[below right] {$H$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    'Do mặt phẳng $(P)$ đi qua điểm $M$ và song song với $(SAD)$ nên cắt các cạnh của hình chóp bằng các giao tuyến đi qua $M$ và song song với mặt phẳng $(SAD)$. \\\\ \n'
                    'Do $ABCD$ là hình thoi và tam giác $SAD$ đều nên thiết diện thu được là hình thang cân $MNFE$ với $MN \\parallel EF, ME = NF$. \\\\ \n'
                    'Khi đó $MN = a, \\dfrac{EF}{BC} = \\dfrac{SF}{SC} = \\dfrac{MA}{AB} = \\dfrac{x}{a} \\Rightarrow EF = x$ và $MF = a - x$. \\\\ \n'
                    'Kẻ đường cao $FH, H \\in MN$ ta có $FH = \\sqrt{MF^2 - \\left(\\dfrac{MN - EF}{2}\\right)^2} = \\dfrac{\\sqrt{3}}{2}(a - x)$. \\\\ \n'
                    'Vậy diện tích hình thang là $S = \\dfrac{\\sqrt{3}}{4}(a^2 - x^2)$. \n')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
