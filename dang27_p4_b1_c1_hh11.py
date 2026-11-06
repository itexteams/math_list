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


def bt_dang27_p4_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ vẽ đúng 100% theo mẫu ảnh cung cấp
        # Nét vẽ 1pt, điểm 1pt, màu black
        hinh_ve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (2.4,5.2);
        \\coordinate (B) at (0,1.2);
        \\coordinate (C) at (2.2,0);
        \\coordinate (D) at (5.2,1.9);
        \\coordinate (O) at (2.9,1.3);
        \\coordinate (M) at ($(A)!0.62!(O)$);
        \\coordinate (N) at ($(B)!0.65!(C)$);
        \\coordinate (Q) at (intersection of C--O and B--D);
        \\coordinate (E) at (intersection of B--O and C--D);
        \\coordinate (P) at (intersection of D--M and A--N);
        \\coordinate (R) at (intersection of C--M and A--Q);
        \\coordinate (G) at ($(A)!0.32!(E)$);
        \\coordinate (J) at ($(B)!0.3!(D)$);
        \\coordinate (I) at ($(B)!0.42!(C)$);
        \\coordinate (F) at (intersection of I--J and C--D);
        \\coordinate (K) at (intersection of I--J and B--E);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A) (A)--(C) (A)--(N) (A)--(E) (N)--(P) (N)--(F) (C)--(F) (I)--(F);
        \\draw[line width=1pt, dashed] (B)--(D) (A)--(O) (D)--(N) (C)--(Q) (B)--(E) (A)--(Q) (D)--(M)--(P);
        \\draw[line width=1pt, dashed] (C)--(M)--(R) (D)--(R) (I)--(J) (J)--(F) (K)--(G)--(D);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (O) circle (1pt) node[below] {$O$};
        \\fill (M) circle (1pt) node[above left] {$M$};
        \\fill (N) circle (1pt) node[below left] {$N$};
        \\fill (P) circle (1pt) node[left] {$P$};
        \\fill (Q) circle (1pt) node[below right] {$Q$};
        \\fill (R) circle (1pt) node[above left] {$R$};
        \\fill (E) circle (1pt) node[below right] {$E$};
        \\fill (G) circle (1pt) node[above right] {$G$};
        \\fill (J) circle (1pt) node[above left] {$J$};
        \\fill (I) circle (1pt) node[left] {$I$};
        \\fill (K) circle (1pt) node[below] {$K$};
        \\fill (F) circle (1pt) node[below left] {$F$};
    \\end{tikzpicture}
    \\end{center}"""

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$, $O$ là một điểm thuộc miền trong tam giác $BCD$, $M$ là điểm trên đoạn $AO$. \\\\
    a) Tìm giao tuyến của mặt phẳng $(MCD)$ với các mặt phẳng $(ABC), (ABD)$. \\\\
    b) Gọi $I, J$ là các điểm tương ứng trên các cạnh $BC$ và $BD$ sao cho $IJ$ không song song với $CD$. Tìm giao tuyến của hai mặt phẳng $(IJM)$ và $(ACD)$.'''
                         % ()
                         )

        # Nội dung lời giải chi tiết giải hết các ý
        loigiai = ('''%s
    \\begin{enumEX}[a)]{1}
    \\item Trong $(BCD)$ gọi $N = DO \\cap BC$, trong $(ADN)$ gọi $P = DM \\cap AN \\Rightarrow \\begin{cases} P \\in DM \\subset (CDM) \\\\ P \\in AN \\subset (ABC) \\end{cases} \\Rightarrow P \\in (CDM) \\cap (ABC)$. \\\\
    Lại có $C \\in (CDM) \\cap (ABC) \\Rightarrow PC = (CDM) \\cap (ABC)$. \\\\
    Tương tự, trong $(BCD)$ gọi $Q = CO \\cap BD$, trong $(ACQ)$ gọi $R = CM \\cap AQ$ \\\\
    $\\Rightarrow \\begin{cases} R \\in CM \\subset (CDM) \\\\ R \\in AQ \\subset (ABD) \\end{cases} \\Rightarrow R \\in (CDM) \\cap (ABD)$. \\\\
    $\\Rightarrow D$ là điểm chung thứ hai của $(MCD)$ và $(ABD)$ nên $DR = (CDM) \\cap (ABD)$.
    \\item Trong $(BCD)$ gọi $E = BO \\cap CD, F = IJ \\cap CD, K = BE \\cap IJ$; trong $(ABE)$ gọi $G = KM \\cap AE$. \\\\
    Ta có: \\\\
    $\\begin{cases} F \\in IJ \\subset (IJM) \\\\ F \\in CD \\subset (ACD) \\end{cases} \\Rightarrow F \\in (IJM) \\cap (ACD)$, \\\\
    $\\begin{cases} G \\in KM \\subset (IJM) \\\\ G \\in AE \\subset (ACD) \\end{cases} \\Rightarrow G \\in (IJM) \\cap (ACD)$. \\\\
    Vậy $FG = (IJM) \\cap (ACD)$.
    \\end{enumEX}'''
                   % (hinh_ve)
                   )

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

