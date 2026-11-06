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


def bt_dang21_p4_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ vẽ đúng 100% theo mẫu ảnh cung cấp
        # Nét vẽ 1pt, điểm 1pt, màu black
        hinh_ve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (1.5,1.8);
        \\coordinate (B) at (0.6,0.6);
        \\coordinate (C) at (5,0.7);
        \\coordinate (D) at (5.9,1.9);
        \\coordinate (S) at (2,4.8);
        \\coordinate (O) at (intersection of A--C and B--D);
        \\coordinate (M) at ($(S)!0.5!(B)$);
        \\coordinate (N) at ($(S)!0.5!(D)$);
        \\coordinate (P) at ($(S)!0.75!(C)$);
        \\coordinate (K) at (intersection of M--N and S--O);
        \\coordinate (E) at (intersection of P--K and S--A);
        \\coordinate (I) at (intersection of E--M and A--B);
        \\coordinate (J) at (intersection of E--P and A--C);
        \\draw[line width=1pt] (S)--(M)--(I) (S)--(N)--(D) (S)--(P) (N)--(P)--(M) (I)--(J);
        \\draw[line width=1pt] (M)--(P) (D)--(C) (D)--(J) (P)--(J);
        \\draw[line width=1pt, dashed] (S)--(A) (S)--(O) (A)--(B) (B)--(C) (C)--(D) (D)--(A) (C)--(J);
        \\draw[line width=1pt, dashed] (A)--(C) (B)--(D) (M)--(B) (P)--(C);
        \\draw[line width=1pt, dashed] (M)--(N) (E)--(P) (E)--(M) (E)--(N) (B)--(I) (C)--(J);
        \\fill (A) circle (1pt) node[below] {$A$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (O) circle (1pt) node[below] {$O$};
        \\fill (M) circle (1pt) node[left] {$M$};
        \\fill (N) circle (1pt) node[above right] {$N$};
        \\fill (P) circle (1pt) node[right] {$P$};
        \\fill (K) circle (1pt) node[above] {$K$};
        \\fill (E) circle (1pt) node[right] {$E$};
        \\fill (I) circle (1pt) node[below left] {$I$};
        \\fill (J) circle (1pt) node[right] {$J$};
    \\end{tikzpicture}
    \\end{center}"""

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $M, N$ lần lượt là trung điểm của $SB, SD$. Lấy điểm $P$ trên cạnh $SC$ sao cho $PC < PS$. Tìm giao tuyến của các cặp mặt phẳng \\\\
    a) $(SAD)$ và $(SBD)$. \\\\
    b) $(MNP)$ và $(SBD)$. \\\\
    c) $(MNP)$ và $(SAC)$. \\\\
    d) $(MNP)$ và $(SAB)$. \\\\
    e) $(SAD)$ và $(MNP)$. \\\\
    f) $(MNP)$ và $(ABCD)$.'''
                         % ()
                         )

        # Nội dung lời giải chi tiết giải hết các ý
        loigiai = ('''%s
    \\begin{enumEX}[a)]{1}
    \\item Trong mặt phẳng $(ABCD)$ gọi $O$ là giao điểm của $AC, BD$. \\\\
    Do $S, O$ đều thuộc $2$ mặt phẳng $(SAC), (SBD) \\Rightarrow SO = (SAC) \\cap (SBD)$.
    \\item Ta có: $\\begin{cases} M \\in SB \\subset (SBD) \\\\ N \\in SD \\subset (SBD) \\end{cases} \\Rightarrow MN \\subset (SBD)$. \\\\
    Lại có $MN \\subset (MNP)$. \\\\
    Vậy $MN = (SBD) \\cap (MNP)$.
    \\item Trong $(SBD)$ gọi $K = MN \\cap SO$. \\\\
    Đường thẳng $PK$ nằm trong $(SAC)$ cắt $SA$ tại $E$. \\\\
    Ta có: $PE = (SAC) \\cap (MNP)$.
    \\item Ta có $E, M$ là $2$ điểm chung của mặt phẳng $(SAB), (MNP)$. \\\\
    $\\Rightarrow ME = (SAB) \\cap (MNP)$.
    \\item Tương tự, $N, E$ là $2$ điểm chung của $(SAD)$ và $(MNP)$. \\\\
    $\\Rightarrow NE = (SAD) \\cap (MNP)$.
    \\item Trong mặt phẳng $(SAC)$ gọi $J = EP \\cap AC$, trong mặt phẳng $(SAB)$ gọi $I = EM \\cap AB$. \\\\
    Do $I, J$ là $2$ điểm chung của $2$ mặt phẳng $(MNP), (ABCD) \\Rightarrow IJ = (MNP) \\cap (ABCD)$.
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

