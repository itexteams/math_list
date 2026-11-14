
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


def bt_dang16_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k=2
        if k==2:
            gt_M = "Gọi $M$ là trung điểm của $A'B'$."
            lg_N = "tại trung điểm $N$ của $B'C'$"
            lg_P = "tại trung điểm $P$ của $BC$"
            lg_Q = "tại trung điểm $Q$ của $AB$"
        noidungcauhoi = ('Cho hình hộp $ABCD.A\'B\'C\'D\'$. ' + gt_M + ' Tìm thiết diện của hình hộp cắt bởi mặt phẳng $(P)$ đi qua $M$ và song song với mặt phẳng $(A\'C\'C)$. Thiết diện là hình gì? \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate (A) at (2,2); \n'
                    '\\coordinate (B) at (0,0); \n'
                    '\\coordinate (C) at (5,0); \n'
                    '\\coordinate (D) at (7,2); \n'
                    '\\coordinate (A\') at ($(A)+(0,4)$); \n'
                    '\\coordinate (B\') at ($(B)+(0,4)$); \n'
                    '\\coordinate (C\') at ($(C)+(0,4)$); \n'
                    '\\coordinate (D\') at ($(D)+(0,4)$); \n'
                    '\\coordinate (M) at ($(A\')!1/'+str(k)+'!(B\')$); \n'
                    '\\coordinate (N) at ($(B\')!1/'+str(k)+'!(C\')$); \n'
                    '\\coordinate (P) at ($(B)!1/'+str(k)+'!(C)$); \n'
                    '\\coordinate (Q) at ($(A)!1/'+str(k)+'!(B)$); \n'
                    '\\draw[dashed] (A) -- (B) (A) -- (D) (A) -- (A\') (A) -- (C) (M) -- (Q) (Q) -- (P); \n'
                    '\\draw (B) -- (C) -- (D) (B) -- (B\') (C) -- (C\') (D) -- (D\') (A\') -- (C\') (A\') -- (B\') -- (C\') -- (D\') -- (A\') (M) -- (N) -- (P); \n'
                    '\\fill[gray!30, opacity=0.8] (M) -- (N) -- (P) -- (Q) -- cycle; \n'
                    '\\fill (A) circle (1.5pt) node[below] {$A$}; \n'
                    '\\fill (B) circle (1.5pt) node[below] {$B$}; \n'
                    '\\fill (C) circle (1.5pt) node[below] {$C$}; \n'
                    '\\fill (D) circle (1.5pt) node[right] {$D$}; \n'
                    '\\fill (A\') circle (1.5pt) node[above] {$A\'$}; \n'
                    '\\fill (B\') circle (1.5pt) node[left] {$B\'$}; \n'
                    '\\fill (C\') circle (1.5pt) node[right] {$C\'$}; \n'
                    '\\fill (D\') circle (1.5pt) node[right] {$D\'$}; \n'
                    '\\fill (M) circle (1.5pt) node[above left] {$M$}; \n'
                    '\\fill (N) circle (1.5pt) node[above right] {$N$}; \n'
                    '\\fill (P) circle (1.5pt) node[below] {$P$}; \n'
                    '\\fill (Q) circle (1.5pt) node[left] {$Q$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    'Vì $(P)$ song song với $(A\'C\'C)$ nên $(P)$ song song với $(A\'C\'CA)$. \\\\ \n'
                    'Suy ra giao tuyến của $(P)$ với $(A\'B\'C\'D\')$ là đường thẳng đi qua $M$, song song với $A\'C\'$ và cắt $B\'C\'$ ' + lg_N + '. \\\\ \n'
                    'Tương tự, giao tuyến của $(P)$ với $(B\'C\'CB)$ là đường thẳng đi qua $N$, song song với $C\'C$ và cắt $BC$ ' + lg_P + '. \\\\ \n'
                    'Giao tuyến của $(P)$ với $(A\'B\'BA)$ là đường thẳng đi qua $M$, song song với $A\'A$ và cắt $AB$ ' + lg_Q + '. \\\\ \n'
                    'Vậy thiết diện cần tìm là tứ giác $MNPQ$. \\\\ \n'
                    'Do $NP$ song song và bằng $CC\'$; $MQ$ song song và bằng $AA\'$ nên tứ giác $MNPQ$ là hình bình hành. \n'
                    )
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content
