
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


def bt_dang13_p4_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k = random.choice([2, 4, 5, 8])
        p_m, p_n = random.choice([('M', 'N'), ('E', 'F'), ('P', 'Q')])
        am_as = Rational(k, k + 1)
        ac_an = 2 * am_as
        an_ac = Rational(1, ac_an)
        cn_ca = 1 - an_ac
        kq_dec = str(round(float(cn_ca), 4)).replace('.', ',')
        m_pos = round(1 / (k + 1), 3)
        n_pos = round(float(an_ac), 3)
        tikz_code = f"""\\begin{{center}}
    \\begin{{tikzpicture}}[font=\\footnotesize, line join=round, line cap=round, >=stealth, scale=0.85]
    \\coordinate (A) at (0,0);
    \\coordinate (D) at (3.6,0);
    \\coordinate (B) at (1.3,1.3);
    \\coordinate (C) at (4.9,1.3);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (S) at (1.8,4.2);
    \\coordinate (M) at ($(S)!{m_pos}!(A)$);
    \\coordinate (N) at ($(A)!{n_pos}!(C)$);
    \\draw[line width=1pt] (S)--(A)--(D)--(C)--(S)--(D);
    \\draw[line width=1pt, dashed] (S)--(B)--(A) (B)--(C) (A)--(C) (B)--(D) (S)--(O) (M)--(O) (S)--(N);
    \\fill (A) circle (1.5pt) node[below left] {{$A$}};
    \\fill (B) circle (1.5pt) node[left] {{$B$}};
    \\fill (C) circle (1.5pt) node[right] {{$C$}};
    \\fill (D) circle (1.5pt) node[below] {{$D$}};
    \\fill (O) circle (1.5pt) node[below] {{$O$}};
    \\fill (S) circle (1.5pt) node[above] {{$S$}};
    \\fill (M) circle (1.5pt) node[left] {{${p_m}$}};
    \\fill (N) circle (1.5pt) node[below right] {{${p_n}$}};
    \\end{{tikzpicture}}
    \\end{{center}}"""
        noidungcauhoi = f"Cho hình chóp $S.ABCD$ có đáy là hình bình hành, trên cạnh $SA$ lấy điểm ${p_m}$ sao cho ${p_m}A = {k}{p_m}S$. Gọi $O$ là tâm của hình bình hành $ABCD$. Một phép chiếu song song theo phương ${p_m}O$ lên mặt phẳng $(ABCD)$ biến điểm $S$ thành điểm ${p_n}$. Tỉ số $\\frac{{C{p_n}}}{{CA}}$ bằng bao nhiêu?"
        loigiai = f"""{tikz_code}
    Trong mặt phẳng $(SAC)$ kẻ $S{p_n}$ song song $O{p_m}$ với ${p_n}$ thuộc $AC$. \\\\
    Khi đó ${p_n} \\in (ABCD)$ nên ${p_n}$ là hình chiếu song song của $S$ lên $(ABCD)$ theo phương $O{p_m}$. \\\\
    Xét $\\Delta SA{p_n}$ ta có $O{p_m} \\parallel S{p_n} \\Rightarrow \\frac{{A{p_m}}}{{AS}} = \\frac{{AO}}{{A{p_n}}} = {latex(am_as)}$ (định lí Thalès). \\\\
    $\\Rightarrow \\frac{{\\frac{{1}}{{2}}AC}}{{A{p_n}}} = {latex(am_as)} \\Rightarrow \\frac{{AC}}{{A{p_n}}} = {latex(ac_an)} \\Rightarrow \\frac{{A{p_n}}}{{AC}} = {latex(an_ac)} \\Rightarrow \\frac{{C{p_n}}}{{CA}} = {latex(cn_ca)} = {kq_dec}$."""
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
