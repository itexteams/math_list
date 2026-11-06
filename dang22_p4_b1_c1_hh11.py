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


def bt_dang22_p4_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ vẽ đúng 100% theo mẫu ảnh cung cấp
        # Nét vẽ 1pt, điểm 1pt, màu black
        hinh_ve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (1.5,1.5);
        \\coordinate (B) at (0.4,0.3);
        \\coordinate (C) at (4.5,0.4);
        \\coordinate (D) at (5.6,1.6);
        \\coordinate (S) at (1.9,4.8);
        \\coordinate (O) at (intersection of A--C and B--D);
        \\coordinate (I) at ($(B)!0.5!(C)$);
        \\coordinate (J) at ($(C)!0.5!(D)$);
        \\coordinate (K) at ($(S)!0.5!(A)$);
        \\coordinate (E) at (intersection of I--J and A--B);
        \\coordinate (F) at (intersection of I--J and A--D);
        \\coordinate (Q) at (intersection of K--E and S--B);
        \\coordinate (P) at (intersection of K--F and S--D);
        \\draw[line width=1pt] (S)--(B) (S)--(C) (E)--(I)--(C)--(J)--(F);
        \\draw[line width=1pt] (Q)--(I) (P)--(J) (Q)--(E) (P)--(F) (S)--(P);
        \\draw[line width=1pt, dashed] (S)--(A) (P)--(D) (S)--(O) (I)--(J);
        \\draw[line width=1pt, dashed] (A)--(E) (A)--(F) (A)--(C) (B)--(D);
        \\draw[line width=1pt, dashed] (B)--(C) (C)--(D);
        \\draw[line width=1pt, dashed] (K)--(Q) (K)--(P) (K)--(I) (K)--(J) (K)--(O) (K)--(P) (K)--(Q) (P)--(Q);
        \\fill (A) circle (1pt) node[above right] {$A$};
        \\fill (B) circle (1pt) node[below] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[above right] {$D$};
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (O) circle (1pt) node[below] {$O$};
        \\fill (I) circle (1pt) node[below] {$I$};
        \\fill (J) circle (1pt) node[below right] {$J$};
        \\fill (K) circle (1pt) node[above right] {$K$};
        \\fill (E) circle (1pt) node[left] {$E$};
        \\fill (F) circle (1pt) node[right] {$F$};
        \\fill (Q) circle (1pt) node[left] {$Q$};
        \\fill (P) circle (1pt) node[above right] {$P$};
    \\end{tikzpicture}
    \\end{center}"""

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$, có đáy $ABCD$ là hình bình hành. $I, J, K$ lần lượt là trung điểm của $BC, CD, SA$. Tìm giao tuyến của \\\\
    a) $(IJK)$ và $(SAB)$. \\\\
    b) $(IJK)$ và $(SAD)$. \\\\
    c) $(IJK)$ và $(SCB)$. \\\\
    d) $(IJK)$ và $(SDB)$.'''
                         % ()
                         )

        # Nội dung lời giải chi tiết giải hết các ý
        loigiai = ('''%s
    \\begin{enumEX}[a)]{1}
    \\item Trong mặt phẳng $(ABCD)$ gọi $E = AB \\cap IJ, F = AD \\cap IJ$. Khi đó $2$ điểm $K, E$ là $2$ điểm chung của mặt phẳng $(IJK), (SAB)$ nên $KE = (SAB) \\cap (IJK)$.
    \\item Tương tự, $KF = (SAD) \\cap (IJK)$.
    \\item Trong mặt phẳng $(SAB)$ gọi $Q = KE \\cap SB$. Khi đó $2$ điểm $Q, I$ là $2$ điểm chung của mặt phẳng $(IJK), (SCB)$ nên $QI = (SCB) \\cap (IJK)$.
    \\item Trong mặt phẳng $(SAD)$ gọi $P = SD \\cap KF$. Khi đó $2$ điểm $P, Q$ là $2$ điểm chung của mặt phẳng $(IJK), (SBD)$ nên $PQ = (SBD) \\cap (IJK)$.
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

