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


def bt_dang20_p4_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ vẽ đúng 100% theo mẫu ảnh cung cấp
        # Nét vẽ 1pt, điểm 1pt, màu black
        hinh_ve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (1.5,-1.4);
        \\coordinate (D) at (5,0);
        \\coordinate (A) at (2.2,3.1);
        \\coordinate (E) at ($(B)!0.55!(C)$);
        \\coordinate (F) at ($(C)!0.6!(D)$);
        \\coordinate (G) at ($(A)!0.6!(B)$);
        \\coordinate (H) at ($(A)!0.55!(D)$);
        \\coordinate (M) at (intersection of A--E and D--G);
        \\coordinate (N) at (intersection of A--F and C--H);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A) (A)--(C) (A)--(E) (A)--(F) (C)--(G) (C)--(H);
        \\draw[line width=1pt, dashed] (B)--(D) (G)--(H);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[below right] {$D$};
        \\fill (E) circle (1pt) node[below left] {$E$};
        \\fill (F) circle (1pt) node[below right] {$F$};
        \\fill (G) circle (1pt) node[above left] {$G$};
        \\fill (H) circle (1pt) node[above right] {$H$};
        \\fill (M) circle (1pt) node[below left] {$M$};
        \\fill (N) circle (1pt) node[right] {$N$};
    \\end{tikzpicture}
    \\end{center}"""

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$. $M$ là một điểm bên trong $\\triangle ABD$, $N$ là điểm bên trong của $\\triangle ACD$. Tìm giao tuyến của các cặp mặt phẳng \\\\
    a) $(AMN)$ và $(BCD)$. \\\\
    b) $(DMN)$ và $(ABC)$.'''
                         % ()
                         )

        # Nội dung lời giải chi tiết đầy đủ từng bước
        loigiai = ('''%s
    \\begin{enumEX}[a)]{1}
    \\item Trong mặt phẳng $(ABD)$, gọi $E = AM \\cap BD$. Trong mặt phẳng $(ACD)$, gọi $F = AN \\cap CD$. \\\\
    Ta có: \\\\
    $\\begin{cases} E \\in AM \\Rightarrow E \\in (AMN) \\\\ F \\in AN \\Rightarrow F \\in (AMN) \\end{cases} \\Rightarrow EF \\subset (AMN)$ (1). \\\\
    Mặt khác: \\\\
    $\\begin{cases} E \\in BD \\Rightarrow E \\in (BCD) \\\\ F \\in CD \\Rightarrow F \\in (BCD) \\end{cases} \\Rightarrow EF \\subset (BCD)$ (2). \\\\
    Từ (1) và (2) suy ra $EF = (BCD) \\cap (AMN)$.
    \\item Trong mặt phẳng $(ABD)$, gọi $G = DM \\cap AB$. Trong mặt phẳng $(ACD)$, gọi $H = DN \\cap AC$. \\\\
    Ta có: \\\\
    $\\begin{cases} G \\in DM \\Rightarrow G \\in (DMN) \\\\ H \\in DN \\Rightarrow H \\in (DMN) \\end{cases} \\Rightarrow GH \\subset (DMN)$ (3). \\\\
    Mặt khác: \\\\
    $\\begin{cases} G \\in AB \\Rightarrow G \\in (ABC) \\\\ H \\in AC \\Rightarrow H \\in (ABC) \\end{cases} \\Rightarrow GH \\subset (ABC)$ (4). \\\\
    Từ (3) và (4) suy ra $GH = (DMN) \\cap (ABC)$.
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

