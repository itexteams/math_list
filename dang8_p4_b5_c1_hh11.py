
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


def bt_dang8_p4_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        a = random.choice([2, 3, 4, 6])
        k1 = random.choice([1, 2, 3])
        k2 = random.choice([2, 3, 4])
        if k1 == 1:
            dk_M = "SM = MB"
        else:
            dk_M = f"SM = {k1}MB"
        dk_N = f"SN = \\frac{{1}}{{{k2}}}SD"
        bm_bs = Rational(1, k1 + 1)
        op_ob = Rational(k1, k1 + 1)
        op_bd = Rational(k1, 2 * (k1 + 1))
        op_val = op_bd * a * sqrt(2)
        nd_sd = Rational(k2 - 1, k2)
        oq_do = Rational(1, k2)
        oq_bd = Rational(1, 2 * k2)
        oq_val = oq_bd * a * sqrt(2)
        pq_val = simplify(op_val + oq_val)
        ao_val = Rational(a, 2) * sqrt(2)
        s_apq = simplify(Rational(1, 2) * ao_val * pq_val)
        m_ratio = round(k1 / (k1 + 1), 3)
        n_ratio = round(1 / k2, 3)
        tikz_code = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.85]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (3.8,0);
    \\coordinate (A) at (1.4,1.3);
    \\coordinate (D) at (5.2,1.3);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (S) at (2.1,4.5);
    \\coordinate (M) at ($(S)!{m_ratio}!(B)$);
    \\coordinate (N) at ($(S)!{n_ratio}!(D)$);
    \\coordinate (P) at ($(O)!{m_ratio}!(B)$);
    \\coordinate (Q) at ($(O)!{n_ratio}!(D)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (A)--(M) (A)--(N) (M)--(N) (M)--(P) (N)--(Q) (A)--(P);
    \\fill (A) circle (1.5pt) node[left] {{$A$}};
    \\fill (B) circle (1.5pt) node[below left] {{$B$}};
    \\fill (C) circle (1.5pt) node[below right] {{$C$}};
    \\fill (D) circle (1.5pt) node[right] {{$D$}};
    \\fill (O) circle (1.5pt) node[below] {{$O$}};
    \\fill (S) circle (1.5pt) node[above] {{$S$}};
    \\fill (M) circle (1.5pt) node[left] {{$M$}};
    \\fill (N) circle (1.5pt) node[above right] {{$N$}};
    \\fill (P) circle (1.5pt) node[below right] {{$P$}};
    \\fill (Q) circle (1.5pt) node[below right] {{$Q$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        noidungcauhoi = f"Cho hình chóp $S.ABCD$ đáy là hình vuông tâm $O$ cạnh ${a}$. Trên cạnh $SB, SD$ lần lượt lấy điểm $M, N$ sao cho ${dk_M}$ và ${dk_N}$. Diện tích hình chiếu song song của tam giác $\\Delta AMN$ lên mặt phẳng $(ABCD)$ theo phương của đường thẳng $SO$ bằng bao nhiêu?"
        loigiai = f"""{tikz_code}
    Trong $(SBD)$ vẽ $MP \\parallel SO \\Rightarrow P$ là hình chiếu song song của $M$ lên $(ABCD)$ theo phương $SO$. \\\\
    Trong $(SBD)$ vẽ $NQ \\parallel SO \\Rightarrow Q$ là hình chiếu song song của $N$ lên $(ABCD)$ theo phương $SO$. \\\\
    $\\Rightarrow$ Hình chiếu song song của tam giác $\\Delta AMN$ lên mặt phẳng $(ABCD)$ theo phương của đường thẳng $SO$ là $\\Delta APQ$. \\\\
    + Vì $MP \\parallel SO \\Rightarrow \\frac{{BM}}{{BS}} = \\frac{{BP}}{{BO}}$. \\\\
    + Ta có ${dk_M} \\Rightarrow BM = {latex(bm_bs)}BS \\Rightarrow \\frac{{BM}}{{BS}} = {latex(bm_bs)}$ \\\\
    $\\Rightarrow \\frac{{BP}}{{BO}} = {latex(bm_bs)} \\Rightarrow OP = {latex(op_ob)}OB \\Rightarrow OP = {latex(op_bd)}BD = {latex(op_val)}$ $(1)$. \\\\
    + Vì $NQ \\parallel SO \\Rightarrow \\frac{{DN}}{{DS}} = \\frac{{DQ}}{{DO}}$. \\\\
    + Ta có ${dk_N} \\Rightarrow ND = {latex(nd_sd)}SD \\Rightarrow \\frac{{ND}}{{SD}} = {latex(nd_sd)}$ \\\\
    $\\Rightarrow \\frac{{DQ}}{{DO}} = {latex(nd_sd)} \\Rightarrow DQ = {latex(nd_sd)}DO \\Rightarrow OQ = {latex(oq_do)}DO = {latex(oq_bd)}BD = {latex(oq_val)}$ $(2)$. \\\\
    Từ $(1)$ và $(2)$ suy ra $PQ = OP + OQ = {latex(pq_val)}$. \\\\
    $\\Rightarrow S_{{\\Delta APQ}} = \\frac{{1}}{{2}} AO \\cdot PQ = \\frac{{1}}{{2}} \\cdot {latex(ao_val)} \\cdot {latex(pq_val)} = {latex(s_apq)}$."""
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
