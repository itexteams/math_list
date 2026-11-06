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


def bt_dang23_p4_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ vẽ đúng 100% theo mẫu ảnh cung cấp
        # Nét vẽ 1pt, điểm 1pt, màu black
        hinh_ve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (1.8,1.6);
        \\coordinate (B) at (0.6,0.3);
        \\coordinate (C) at (3.8,0.3);
        \\coordinate (D) at (7.2,1.6);
        \\coordinate (S) at (1.9,5.8);
        \\coordinate (I) at ($(S)!0.5!(A)$);
        \\coordinate (J) at ($(D)!0.25!(A)$);
        \\coordinate (K) at ($(S)!0.66667!(B)$);
        \\coordinate (E) at (intersection of K--I and B--A);
        \\coordinate (F) at (intersection of J--E and B--C);
        \\coordinate (P) at (intersection of J--E and B--D);
        \\draw[line width=1pt] (S)--(K) (S)--(C) (S)--(D) (K)--(E)  (C)--(F)--(E) (F)--(C)  (C)--(D);
        \\draw[line width=1pt, dashed] (S)--(A) (S)--(I) (A)--(B) (A)--(D) (B)--(D) (B)--(C);
        \\draw[line width=1pt, dashed] (I)--(K) (I)--(J) (K)--(J) (K)--(P) (K)--(F) (P)--(D);
        \\draw[line width=1pt, dashed] (E)--(F) (F)--(P) (P)--(J) (B)--(F) (K)--(B) (B)--(E);
        \\fill (A) circle (1pt) node[below right] {$A$};
        \\fill (B) circle (1pt) node[below right] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (I) circle (1pt) node[above right] {$I$};
        \\fill (J) circle (1pt) node[above] {$J$};
        \\fill (K) circle (1pt) node[left] {$K$};
        \\fill (E) circle (1pt) node[below left] {$E$};
        \\fill (F) circle (1pt) node[below] {$F$};
        \\fill (P) circle (1pt) node[below right] {$P$};
    \\end{tikzpicture}
    \\end{center}"""

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$, có đáy $ABCD$ là hình thang có đáy lớn $AD$. Gọi $I$ là trung điểm của $SA$, $J$ là điểm nằm trên $AD$ sao cho $JD = \\frac{1}{4}AD$, $K \\in SB: SK = 2BK$. Tìm giao tuyến của hai mặt phẳng: \\\\
    a) $(IJK)$ và $(ABCD)$. \\\\
    b) $(IJK)$ và $(SBD)$. \\\\
    c) $(IJK)$ và $(SCB)$.'''
                         % ()
                         )

        # Nội dung lời giải chi tiết giải hết các ý
        loigiai = ('''%s
    \\begin{enumEX}[a)]{1}
    \\item Trong mặt phẳng $(SAB)$ gọi $E = KI \\cap AB$. Khi đó $2$ điểm $J, E$ là $2$ điểm chung của mặt phẳng $(IJK), (ABCD)$ nên $JE = (ABCD) \\cap (IJK)$.
    \\item Trong mặt phẳng $(ABCD)$ gọi $P = BD \\cap JE$. Khi đó $2$ điểm $K, P$ là $2$ điểm chung của mặt phẳng $(IJK), (SBD)$ nên $KP = (SBD) \\cap (IJK)$.
    \\item Trong mặt phẳng $(ABCD)$ gọi $F = BC \\cap JE$. Khi đó $2$ điểm $K, F$ là $2$ điểm chung của mặt phẳng $(IJK), (SBC)$ nên $KF = (SBC) \\cap (IJK)$.
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

