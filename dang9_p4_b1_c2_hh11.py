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


def bt_dang9_p4_b1_c2_hh11(self):
            # Khai báo biến
            # B2, B3, B4: Viết lại, suy nghĩ tìm cách random và điều chỉnh phương án
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Trường hợp 1: Vectơ BD và A'C'
                v1 = 'BD'
                v2 = "A'C'"
                v_parallel = 'AC'
                diag_square = 'ABCD'
            elif dang == '2':
                # Trường hợp 2: Vectơ AC và B'D'
                v1 = 'AC'
                v2 = "B'D'"
                v_parallel = 'BD'
                diag_square = 'ABCD'

            # Đáp án đúng luôn là 0 vì hai đường chéo này vuông góc
            da_dung = '0'

            # Các phương án sai
            s = ['1', '\\frac{1}{2}', '\\frac{\\sqrt{2}}{2}', '\\frac{\\sqrt{3}}{2}', '-1']
            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Câu hỏi
            noidungcauhoi = ('Cho hình lập phương $ABCD.A\'B\'C\'D\'$. Tính $\\cos \\left( \\vec{%s}, \\vec{%s} \\right)$.'
                             % (v1, v2))

            # Các đáp án
            da_d = ('\\True $\\cos \\left( \\vec{%s}, \\vec{%s} \\right) = %s$' % (v1, v2, da_dung))
            da_s1 = ('$\\cos \\left( \\vec{%s}, \\vec{%s} \\right) = %s$' % (v1, v2, das1))
            da_s2 = ('$\\cos \\left( \\vec{%s}, \\vec{%s} \\right) = %s$' % (v1, v2, das2))
            da_s3 = ('$\\cos \\left( \\vec{%s}, \\vec{%s} \\right) = %s$' % (v1, v2, das3))

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[scale=2, line join=round, line cap=round]
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (2,0);
                \\coordinate (D) at (2.8,0.8);
                \\coordinate (A) at (0.8,0.8);
                \\coordinate (B1) at (0,2);
                \\coordinate (C1) at (2,2);
                \\coordinate (D1) at (2.8,2.8);
                \\coordinate (A1) at (0.8,2.8);
                \\draw (B)--(C)--(C1)--(B1)--cycle;
                \\draw (C)--(D)--(D1)--(C1);
                \\draw (B1)--(A1)--(D1);
                \\draw[dashed] (B)--(A)--(D) (A)--(A1);
                \\draw[blue, thick, dashed] (B)--(D);
                \\draw[red, thick] (A1)--(C1);   
                \\node[left] at (B) {$B$};
                \\node[right] at (C) {$C$};
                \\node[right] at (D) {$D$};
                \\node[left] at (A) {$A$};
                \\node[left] at (B1) {$B'$};
                \\node[right] at (C1) {$C'$};
                \\node[right] at (D1) {$D'$};
                \\node[left] at (A1) {$A'$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung lời giải
            loigiai = (tikz_code + '''Ta có $%s \\perp %s$ (vì $%s$ là hình vuông nên hai đường chéo vuông góc với nhau). \\\\
            Mặt khác, trong hình lập phương $ABCD.A'B'C'D'$, ta có $%s \\parallel %s$. \\\\
            Từ đó suy ra $%s \\perp %s$. \\\\
            Do đó góc giữa hai vectơ $\\vec{%s}$ và $\\vec{%s}$ bằng $90^\\circ$. \\\\
            Vậy $\\cos \\left( \\vec{%s}, \\vec{%s} \\right) = \\cos 90^\\circ = 0$.''' 
                       % (v1, v_parallel, diag_square, v_parallel, v2, v1, v2, v1, v2, v1, v2))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

