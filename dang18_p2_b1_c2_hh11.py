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


def bt_dang18_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Khởi tạo các ký hiệu
            a_sym = symbols('a')

            # Bước 1: Random tham số
            # Ở bài này a là đơn vị độ dài, ta có thể giữ nguyên 'a' hoặc gán số cụ thể nếu muốn.
            # Ở đây mình chọn ngẫu nhiên một hệ số k cho cạnh a = k.
            k = random.randint(1, 5) 

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hình chóp $S.ABCD$ có đáy là hình vuông. Cạnh bên $SA$ vuông góc với $AB$ và $AD$. Gọi $K$ là hình chiếu vuông góc của $A$ lên $SB$.'''

            # Vẽ hình bằng TikZ (đưa vào phần lời giải hoặc đề bài)
            hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round]
            \coordinate (A) at (0,0);
            \coordinate (B) at (-1.5,-1.5);
            \coordinate (D) at (3,0);
            \coordinate (C) at ($(B)+(D)-(A)$);
            \coordinate (S) at (0,3);
            \coordinate (K) at ($(S)!0.6!(B)$);
            \draw[dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(K);
            \draw (S)--(B)--(C)--(D)--cycle (S)--(C);
            \tkzDrawPoints(S,A,B,C,D,K)
            \tkzLabelPoints[left](B,K)
            \tkzLabelPoints[right](D,C)
            \tkzLabelPoints[above](S)
            \tkzLabelPoints[above right](A)
            \tkzMarkRightAngle(S,A,B)
            \tkzMarkRightAngle(S,A,D)
            \tkzMarkRightAngle(A,K,S)
            \end{tikzpicture}
            \end{center}'''

            ########################################################################
            # Mệnh đề (a): SA vuông góc BC
            da_a_d = r'\True $SA \perp BC$'
            da_a_s = r'$SA$ không vuông góc với $BC$'
            list_a = [da_a_d, da_a_s]
            sel_a = random.choice(list_a)
            loigiai_a = r'Vì $SA \perp (ABCD)$ và $BC \subset (ABCD)$ nên $SA \perp BC$.'

            ########################################################################
            # Mệnh đề (b): SA vuông góc CD
            da_b_d = r'\True $SA \perp CD$'
            da_b_s = r'$SA$ không vuông góc với $CD$'
            list_b = [da_b_d, da_b_s]
            sel_b = random.choice(list_b)
            loigiai_b = r'Vì $SA \perp (ABCD)$ và $CD \subset (ABCD)$ nên $SA \perp CD$.'

            ########################################################################
            # Mệnh đề (c): BC vuông góc SB
            da_c_d = r'\True $BC \perp SB$'
            da_c_s = r'$BC$ không vuông góc với $SB$'
            list_c = [da_c_d, da_c_s]
            sel_c = random.choice(list_c)
            loigiai_c = r'Ta có $BC \perp AB$ (do $ABCD$ là hình vuông) và $BC \perp SA$ (do $SA \perp (ABCD)$). Suy ra $BC \perp (SAB)$. Mà $SB \subset (SAB)$ nên $BC \perp SB$.'

            ########################################################################
            # Mệnh đề (d): SC vuông góc AK
            da_d_d = r'\True $SC \perp AK$'
            da_d_s = r'$SC$ không vuông góc với $AK$'
            list_d = [da_d_d, da_d_s]
            sel_d = random.choice(list_d)
            loigiai_d = r'Theo chứng minh trên $BC \perp (SAB) \Rightarrow BC \perp AK$ (vì $AK \subset (SAB)$). Lại có $AK \perp SB$ (giả thiết). Từ đó suy ra $AK \perp (SBC)$. Vì $SC \subset (SBC)$ nên $AK \perp SC$.'

            def count_true(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)

                if 1 <= count_true([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n' +
                str(hinh_ve) + '\n' +
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

