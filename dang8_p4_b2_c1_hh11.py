
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


def bt_dang8_p4_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ với đáy $ABCD$ là hình thang với đáy $AD$ và $BC$. '
                         'Biết $AD = a$, $BC = b$. Gọi $I, J$ lần lượt là trọng tâm tam giác $SAD$ và $SBC$. '
                         'Mặt phẳng $(ADJ)$ cắt $SB, SC$ lần lượt tại $M, N$. Mặt phẳng $(BCI)$ cắt $SA, SD$ tại $P, Q$. '
                         'Chứng minh $MN \\parallel PQ$. \n')
        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]\n'
            '\\coordinate (A) at (-2,1.5);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (3,0);\n'
            '\\coordinate (D) at (5,1.5);\n'
            '\\coordinate (S) at (1,6);\n'
            '\\coordinate (M1) at ($(A)!0.5!(D)$);\n'
            '\\coordinate (M2) at ($(B)!0.5!(C)$);\n'
            '\\coordinate (I) at ($(S)!2/3!(M1)$);\n'
            '\\coordinate (J) at ($(S)!2/3!(M2)$);\n'
            '\\coordinate (P) at ($(S)!2/3!(A)$);\n'
            '\\coordinate (Q) at ($(S)!2/3!(D)$);\n'
            '\\coordinate (M) at ($(S)!2/3!(B)$);\n'
            '\\coordinate (N) at ($(S)!2/3!(C)$);\n'
            '\\draw (S)--(B)--(C)--(D)--(S)--(C);\n'
            '\\draw (S)--(M)--(N);\n'
            '\\draw (S)--(J)--(M2);\n'
            '\\draw (S)--(A)--(B);\n'
            '\\draw (A)--(M);\n'
            '\\draw (D)--(N);\n'
            '\\draw (B)--(P);\n'
            '\\draw (C)--(Q);\n'
            '\\draw[dashed] (A)--(D);\n'
            '\\draw[dashed] (P)--(Q) (P)--(I)--(Q) (M)--(J)--(N);\n'
            '\\draw[dashed] (M)--(N) (I)--(C) (I)--(B);\n'
            '\\fill (S) circle (1.5pt) node[above] {$S$};\n'
            '\\fill (A) circle (1.5pt) node[left] {$A$};\n'
            '\\fill (B) circle (1.5pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1.5pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1.5pt) node[right] {$D$};\n'
            '\\fill (I) circle (1.5pt) node[above right] {$I$};\n'
            '\\fill (J) circle (1.5pt) node[below right] {$J$};\n'
            '\\fill (P) circle (1.5pt) node[left] {$P$};\n'
            '\\fill (Q) circle (1.5pt) node[right] {$Q$};\n'
            '\\fill (M) circle (1.5pt) node[left] {$M$};\n'
            '\\fill (N) circle (1.5pt) node[right] {$N$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        loigiai = (
            tikz_code +
            'Ta có: $I \\in (SAD) \\Rightarrow I \\in (SAD) \\cap (IBC)$ \\\\ \n'
            'Lại có $\\begin{cases} AD \\subset (SAD) \\\\ BC \\subset (IBC) \\\\ AD \\parallel BC \\end{cases}$ \\\\ \n'
            'Do đó giao tuyến của hai mặt phẳng $(SAD)$ và $(IBC)$ là đường thẳng qua $I$ và song song với $AD, BC$. \\\\ \n'
            'Khi đó trong $(SAD)$, qua $I$ kẻ đường thẳng song song với $AD$, cắt $SA$ tại $P$ và cắt $SD$ tại $Q$. \\\\ \n'
            '$\\Rightarrow (SAD) \\cap (IBC) = PQ$ \\\\ \n'
            '$\\Rightarrow PQ \\parallel AD \\parallel BC \\quad (1)$ \\\\ \n'
            'Chứng minh tương tự: $J \\in (SBC) \\Rightarrow J \\in (SBC) \\cap (ADJ)$ \\\\ \n'
            '$\\begin{cases} AD \\subset (ADJ) \\\\ BC \\subset (SBC) \\\\ AD \\parallel BC \\\\ (SBC) \\cap (ADJ) = MN \\end{cases}$ \\\\ \n'
            '$\\Rightarrow MN \\parallel AD \\parallel BC \\quad (2)$ \\\\ \n'
            'Do đó, từ $(1)$ và $(2)$ suy ra: $MN \\parallel PQ$. \n'
        )
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
