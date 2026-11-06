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


def bt_dang18_p4_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ chính xác 100% theo hình ảnh cung cấp
        # Nét vẽ 1pt, điểm 1pt, màu black, đúng đường liền và đứt nét
        hinh_ve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (D) at (0,0);
        \\coordinate (A) at (1,1.5);
        \\coordinate (C) at (4.6,0);
        \\coordinate (B) at (5.6,1.5);
        \\coordinate (O) at (intersection of A--C and B--D);
        \\coordinate (S) at (1.5,5.4);
        \\coordinate (M) at ($(B)!0.5!(C)$);
        \\coordinate (N) at ($(C)!0.5!(D)$);
        \\coordinate (P) at ($(S)!0.5!(O)$);
        \\coordinate (E) at (intersection of N--O and A--B);
        \\coordinate (F) at (intersection of N--P and S--E);
        \\coordinate (G) at (intersection of M--N and A--B);
        \\draw[line width=1pt] (S)--(D) (S)--(C) (S)--(G) (D)--(N)--(C)--(G);
        \\draw[line width=1pt, dashed] (S)--(A) (S)--(B) (S)--(O) (S)--(E);
        \\draw[line width=1pt, dashed] (A)--(D) (A)--(B)--(G) (A)--(C) (B)--(D);
        \\draw[line width=1pt, dashed] (N)--(P)--(F) (E)--(F) (M)--(N)--(E) (F)--(G);
        \\draw[line width=1pt, dashed] (N)--(O) (O)--(C) (B)--(C);
        \\fill (D) circle (1pt) node[below left] {$D$};
        \\fill (A) circle (1pt) node[above left] {$A$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (B) circle (1pt) node[above] {$B$};
        \\fill (O) circle (1pt) node[below right] {$O$};
        \\fill (S) circle (1pt) node[above right] {$S$};
        \\fill (M) circle (1pt) node[below left] {$M$};
        \\fill (N) circle (1pt) node[below] {$N$};
        \\fill (P) circle (1pt) node[left] {$P$};
        \\fill (E) circle (1pt) node[below right] {$E$};
        \\fill (F) circle (1pt) node[right] {$F$};
        \\fill (G) circle (1pt) node[right] {$G$};
    \\end{tikzpicture}
    \\end{center}"""

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$, có đáy $ABCD$ là hình bình hành tâm $O$. $M, N, P$ lần lượt là trung điểm của $BC, CD, SO$. Tìm giao tuyến của $(MNP)$ với các mặt phẳng $(SAB), (SAD), (SBC)$ và $(SCD)$.'''
                         % ()
                         )

        # Nội dung lời giải chi tiết giải hết các ý
        loigiai = ('''%s
    Gọi $E = NO \\cap AB$; $F = NP \\cap SE$, $MN \\cap AB = G$. \\\\
    + Giao tuyến của $(MNP)$ và $(SAB)$: \\\\
    $\\begin{cases} G \\in AB \\Rightarrow G \\in (SAB) \\\\ F \\in SE \\subset (SAB) \\Rightarrow F \\in (SAB) \\end{cases} \\Rightarrow GF \\subset (SAB)$. \\\\
    $\\begin{cases} G \\in MN \\Rightarrow G \\in (MNP) \\\\ F \\in NP \\Rightarrow F \\in (MNP) \\end{cases} \\Rightarrow GF \\subset (MNP)$. \\\\
    Vậy $(MNP) \\cap (SAB) = GF$. \\\\
    + Giao tuyến của $(MNP)$ và $(SBC)$: \\\\
    Trong $(SAB)$, gọi $H = GF \\cap SB$. \\\\
    Khi đó: $\\begin{cases} H \\in GF \\subset (MNP) \\Rightarrow H \\in (MNP) \\\\ H \\in SB \\subset (SBC) \\Rightarrow H \\in (SBC) \\end{cases}$ và $M \\in BC \\subset (SBC)$, $M \\in (MNP)$. \\\\
    Vậy $(MNP) \\cap (SBC) = MH$. \\\\
    + Giao tuyến của $(MNP)$ và $(SCD)$: \\\\
    Ta có $N \\in CD \\subset (SCD)$ và $N \\in (MNP)$. \\\\
    Mặt khác, trong $(ABCD)$, $MN // BD$. Trong tam giác $SBD$, đường trung bình ứng với cạnh $BD$ đi qua $P$ nên thiết diện qua $P$ song song với $BD$. \\\\
    Hoặc kéo dài $NP$ cắt $SD$ tại $K$, khi đó $K \\in SD \\subset (SCD)$ và $K \\in NP \\subset (MNP)$. \\\\
    Vậy $(MNP) \\cap (SCD) = NK$. \\\\
    + Giao tuyến của $(MNP)$ và $(SAD)$: \\\\
    Gọi $I = MN \\cap AD$. Trong $(SAD)$, đoạn thẳng nối $I$ và $K$ chính là giao tuyến của $(MNP)$ và $(SAD)$. \\\\
    Vậy $(MNP) \\cap (SAD) = IK$.'''
                   % (hinh_ve)
                   )

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

