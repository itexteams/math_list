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


def bt_dang52_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Hoặc có thể random để ra các góc 30, 60. Tuy nhiên để bám sát hình ảnh, ta giữ góc 45.
            k = random.randint(1, 5)
            val_ab = 2 * k
            val_sa = latex(2 * k) + r'\sqrt{3}'
            # Tính toán các giá trị hiển thị
            ab_text = r'%sa' % (latex(val_ab)) if val_ab != 1 else r'a'
            sa_text = r'%sa' % (val_sa)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hình chóp $S.ABC$ có $SA \perp \left( ABC \right), SA = %s, AB = %s$, tam giác $ABC$ vuông cân tại $B$. Gọi $M$ là trung điểm của $SB$. Tính góc giữa đường thẳng $CM$ và mặt phẳng $\left( SAB \right)$.'''
                              % (sa_text, ab_text))

            # Các phương án
            da_d = r'\True $45^\circ$'
            s = [r'$30^\circ$', r'$60^\circ$', r'$90^\circ$']
            random.shuffle(s)
            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            # Đảm bảo giống 100% hình mẫu: nét đậm 1pt, đúng các đường nét đứt/liền
            hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[line width=1pt, scale=1]
                \coordinate (A) at (0,0);
                \coordinate (B) at (1.5,-1.5);
                \coordinate (C) at (4.5,-0.5);
                \coordinate (S) at (0,3.5);
                \coordinate (M) at ($(S)!0.5!(B)$);
                \draw[dashed]  (A)--(C);
                \draw (S)--(B)--(C)--cycle (S)--(C) (C)--(M) (S)--(A) (A)--(B);
                \foreach \p/\pos in {S/above, A/left, B/below, C/right, M/left}
                    \fill (\p) circle (0pt) node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}'''

            # Nội dung lời giải chi tiết
            loigiai = ('''Có $\\begin{cases} BC \\perp AB \\\\ BC \\perp SA \\end{cases} \\Rightarrow BC \\perp \\left( SAB \\right)$. \\\\
                         Có $BM$ là hình chiếu của $CM$ lên mặt phẳng $\\left( SAB \\right)$. Suy ra $\\left( CM; \\left( SAB \\right) \\right) = \\widehat{CMB}$. \\\\
                         Ta có $BC = AB = %s$. \\\\
                         Xét tam giác $SAB$ vuông tại $A$: $SB = \\sqrt{SA^2 + AB^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %sa$. \\\\
                         Vì $M$ là trung điểm $SB$ nên $MB = \\frac{SB}{2} = %sa$. \\\\
                         Xét tam giác $BCM$ vuông tại $B$ (do $BC \\perp \\left( SAB \\right) \\Rightarrow BC \\perp BM$): \\\\
                         $\\tan \\widehat{CMB} = \\frac{BC}{MB} = \\frac{%sa}{%sa} = 1$. \\\\
                         $\\Rightarrow \\widehat{CMB} = 45^\\circ$. \\\\
                         Vậy $\\left( CM; \\left( SAB \\right) \\right) = 45^\\circ$.'''
                         % (ab_text, sa_text, ab_text, latex(4*k), latex(2*k), latex(2*k), latex(2*k)))

            # Xuất nội dung theo mẫu (không dùng raw string r'' cho biến content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' 
                '\\loigiai{' +str(hinh_ve)+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

