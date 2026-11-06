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


def bt_dang22_p1_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':

        # Các đáp án trắc nghiệm (không có dấu chấm ở cuối, thay || bằng //)[cite: 27]
        da_d = ('\\True $(IJK) // (BCD)$')
        da_s1 = '$(DJK) // (ABC)$'
        da_s2 = '$(KMN) // (ABC)$'
        da_s3 = '$(IJK) // (KMD)$'

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung câu hỏi[cite: 27]
        noidungcauhoi = ('''%s''' % ('Cho tứ diện $ABCD$. Gọi $I, J, K$ lần lượt là trọng tâm các tam giác $ABC, ACD, ABD$ và $M, N$ lần lượt là trung điểm của các cạnh $BC, CD$. Khẳng định nào đúng?'))

        # Hình vẽ TikZ vẽ đúng 100% theo mẫu, nét vẽ 1pt, điểm 1pt, màu đen, đã bỏ các gạch chéo ký hiệu đoạn bằng nhau[cite: 28]
        hinhve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (1.8,5.2);
            \\coordinate (B) at (0.2,1.2);
            \\coordinate (C) at (3.2,-1.0);
            \\coordinate (D) at (6.8,1.2);
            \\coordinate (M) at ($(B)!0.5!(C)$);
            \\coordinate (N) at ($(C)!0.5!(D)$);
            \\coordinate (P) at ($(B)!0.5!(D)$);
            \\coordinate (I) at ($(A)!{2/3}!(M)$);
            \\coordinate (J) at ($(A)!{2/3}!(N)$);
            \\coordinate (K) at ($(A)!{2/3}!(P)$);
            \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C) (A)--(M) (A)--(N);
            \\draw[line width=1pt, dashed] (B)--(D) (A)--(P) (M)--(P)--(N)--(M) (I)--(K)--(J)--(I);
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[left] {$B$};
            \\fill (C) circle (1pt) node[below] {$C$};
            \\fill (D) circle (1pt) node[right] {$D$};
            \\fill (M) circle (1pt) node[below left] {$M$};
            \\fill (N) circle (1pt) node[below right] {$N$};
            \\fill (P) circle (1pt) node[below] {$P$};
            \\fill (I) circle (1pt) node[left] {$I$};
            \\fill (J) circle (1pt) node[right] {$J$};
            \\fill (K) circle (1pt) node[above left] {$K$};
            \\end{tikzpicture}
            \\end{center}''')

        # Nội dung lời giải (trình bày chi tiết từng bước như mẫu ảnh gốc, thay || bằng //)[cite: 29]
        loigiai = ('''%s
    Ta có\\\\
    Gọi $M, N, P$ lần lượt là trung điểm của $BC, CD, BD$.\\\\
    Khi đó $I, J, K$ lần lượt là trọng tâm các tam giác $ABC, ACD, ABD$ nên $I, J, K$ lần lượt nằm trên $AM, AN, AP$ và $\\frac{AI}{AM} = \\frac{AJ}{AN} = \\frac{AK}{AP} = \\frac{2}{3}$\\\\
    Suy ra $IK // MP$ và $KJ // PN$\\\\
    Ta có: $\\begin{cases} IK // MP \\\\ MP \\subset (BCD) \\Rightarrow IK // (BCD) \\\\ IK \\not\\subset (BCD) \\end{cases}$\\\\
    $\\begin{cases} KJ // PN \\\\ PN \\subset (BCD) \\Rightarrow KJ // (BCD) \\\\ KJ \\not\\subset (BCD) \\end{cases}$\\\\
    Vậy $\\begin{cases} IK // (BCD) \\\\ JK // (BCD) \\\\ IK, JK \\subset (IJK) \\\\ IK \\cap JK = \\{K\\} \\end{cases} \\Rightarrow (IJK) // (BCD)$.'''
                   % (hinhve))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n\\choice \n' '{'+str(list_1[0])+'}\n' '{'+str(list_1[1])+'}\n' '{'+str(list_1[2])+'}\n' '{'+str(list_1[3])+'}\n' '\\loigiai{\n'+str(loigiai)+'\n}\n' '\\end{ex}\n \\end{minipage} \n\n')
    return content

