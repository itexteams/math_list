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


def bt_dang26_p4_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ vẽ đúng 100% theo mẫu ảnh cung cấp
        # Nét vẽ 1pt, điểm 1pt, màu black
        hinh_ve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,-0.5);
        \\coordinate (C) at (3,-1.8);
        \\coordinate (D) at (6.2,0.3);
        \\coordinate (A) at (1.7,3.1);
        \\coordinate (E) at ($(B)!0.3!(D)$);
        \\coordinate (F) at ($(C)!0.52!(D)$);
        \\coordinate (P) at ($(A)!0.38!(B)$);
        \\coordinate (Q) at ($(A)!0.62!(C)$);
        \\coordinate (M) at (intersection of A--E and D--P);
        \\coordinate (N) at (intersection of A--F and D--Q);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A) (A)--(C) (A)--(F) (A)--(Q) (P)--(Q) (Q)--(D);
        \\draw[line width=1pt, dashed] (B)--(D) (A)--(E) (D)--(P) (E)--(F);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (E) circle (1pt) node[below left] {$E$};
        \\fill (F) circle (1pt) node[below right] {$F$};
        \\fill (P) circle (1pt) node[above left] {$P$};
        \\fill (Q) circle (1pt) node[left] {$Q$};
        \\fill (M) circle (1pt) node[above right] {$M$};
        \\fill (N) circle (1pt) node[above right] {$N$};
    \\end{tikzpicture}
    \\end{center}"""

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$, $M$ là một điểm bên trong tam giác $ABD$, $N$ là một điểm bên trong tam giác $ACD$. Tìm giao tuyến của các cặp mặt phẳng sau: \\\\
    a) $(AMN)$ và $(BCD)$. \\\\
    b) $(DMN)$ và $(ABC)$.'''
                         % ()
                         )

        # Nội dung lời giải chi tiết giải hết các ý
        loigiai = ('''%s
    \\begin{enumEX}[a)]{1}
    \\item Tìm giao tuyến của $(AMN)$ và $(BCD)$ \\\\
    Trong $(ABD)$, gọi $E = AM \\cap BD$ \\\\
    $E \\in AM$ mà $AM \\subset (AMN) \\Rightarrow E \\in (AMN)$ \\\\
    $E \\in BD$ mà $BD \\subset (BCD) \\Rightarrow E \\in (BCD)$ \\\\
    $\\Rightarrow E$ là điểm chung của $(AMN)$ và $(BCD)$ \\\\
    Trong $(ACD)$, gọi $F = AN \\cap CD$ \\\\
    $F \\in AN$ mà $AN \\subset (AMN) \\Rightarrow F \\in (AMN)$ \\\\
    $F \\in CD$ mà $CD \\subset (BCD) \\Rightarrow F \\in (BCD)$ \\\\
    $\\Rightarrow F$ là điểm chung của $(AMN)$ và $(BCD)$ \\\\
    Vậy $EF$ là giao tuyến của $(AMN)$ và $(BCD)$.
    \\item Tìm giao tuyến của $(DMN)$ và $(ABC)$ \\\\
    Trong $(ABD)$, gọi $P = DM \\cap AB$ \\\\
    $P \\in DM$ mà $DM \\subset (DMN) \\Rightarrow P \\in (DMN)$ \\\\
    $P \\in AB$ mà $AB \\subset (ABC) \\Rightarrow P \\in (ABC)$ \\\\
    $\\Rightarrow P$ là điểm chung của $(DMN)$ và $(ABC)$ \\\\
    Trong $(ACD)$, gọi $Q = DN \\cap AC$ \\\\
    $Q \\in DN$ mà $DN \\subset (DMN) \\Rightarrow Q \\in (DMN)$ \\\\
    $Q \\in AC$ mà $AC \\subset (ABC) \\Rightarrow Q \\in (ABC)$ \\\\
    $\\Rightarrow Q$ là điểm chung của $(DMN)$ và $(ABC)$ \\\\
    Vậy $PQ$ là giao tuyến của $(DMN)$ và $(ABC)$.
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

