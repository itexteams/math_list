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


def bt_dang28_p4_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Mã TikZ vẽ hình theo đúng mẫu và quy tắc
        hinh_tikz = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        \\coordinate (A) at (1.5, 3.5);\n"
            "        \\coordinate (B) at (0, 0);\n"
            "        \\coordinate (C) at (1.3, -1.5);\n"
            "        \\coordinate (D) at (3.8, 0);\n"
            "        \\coordinate (M) at ($(A)!0.4!(C)$);\n"
            "        \\coordinate (N) at ($(A)!0.6!(D)$);\n"
            "        \\coordinate (I) at (intersection of M--N and C--D);\n"
            "        \\coordinate (E) at ($(B)!0.65!(C)$);\n"
            "        \\coordinate (F) at (intersection of I--E and B--D);\n"
            "        \\coordinate (O) at ($(E)!0.55!(F)$);\n"
            "        \\draw[line width=1pt] (A)--(B)--(C)--(A) (I)--(F) (A)--(D)--(C) (M)--(I) (M)--(E) (N)--(I);\n"
            "        \\draw[line width=1pt, dashed] (B)--(D)  (F)--(E) (M)--(O)--(N);\n"
            "        \\fill[black] (A) circle (1pt) node[above] {$A$};\n"
            "        \\fill[black] (B) circle (1pt) node[left] {$B$};\n"
            "        \\fill[black] (C) circle (1pt) node[below] {$C$};\n"
            "        \\fill[black] (D) circle (1pt) node[right] {$D$};\n"
            "        \\fill[black] (M) circle (1pt) node[above right] {$M$};\n"
            "        \\fill[black] (N) circle (1pt) node[above right] {$N$};\n"
            "        \\fill[black] (I) circle (1pt) node[below right] {$I$};\n"
            "        \\fill[black] (E) circle (1pt) node[below left] {$E$};\n"
            "        \\fill[black] (F) circle (1pt) node[above] {$F$};\n"
            "        \\fill[black] (O) circle (1pt) node[below] {$O$};\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$. Trên $AC$ và $AD$ lần lượt lấy các điểm $M$, $N$ sao cho $MN$ không song song với $CD$. Gọi $O$ là một điểm bên trong $\\triangle BCD$. \\\\
    a) Tìm giao tuyến của $(OMN)$ và $(BCD)$. \\\\
    b) Tìm giao điểm của $BC$ và $BD$ với mặt phẳng $(OMN)$.'''
        )

        # Nội dung lời giải
        loigiai = ('''%s
    \\begin{enumEX}[a)]{1} 
    \\item Theo hình vẽ ta có: \\\\
    - Trong mp $(ACD)$: kẻ $MN$ giao với $CD$ tại $I$. \\\\
    - Trong mp $(BCD)$: kẻ $IO$ giao $BC$ và $BD$ lần lượt tại $E$ và $F$. \\\\
    - Từ đó thì giao tuyến của $(OMN)$ và $(BCD)$ là đường $EF$. 
    \\item Theo a) thì giao của $BC$ và $BD$ với $(OMN)$ lần lượt là $E$ và $F$. 
    \\end{enumEX}'''
        %(hinh_tikz
        ))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' + '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' + '\\end{ex}\n \\end{minipage} \n\n')
    return content

