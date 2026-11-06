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


def bt_dang33_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Để random, ta có thể thay đổi giá trị cụ thể của c hoặc vị trí đỉnh.
            val_c = random.randint(-10, -1) # Giá trị c âm
            val_dinh_x = random.randint(1, 5) # Hoành độ đỉnh dương
            val_dinh_y = val_c + random.randint(2, 5) # Tung độ đỉnh phải cao hơn c vì đồ thị đi lên rồi đi xuống

            # B4: Tạo danh sách các tổ hợp dấu và loại trừ đáp án đúng
            all_cases = [
                ("a < 0, b > 0, c < 0", "True"),
                ("a < 0, b < 0, c > 0", "False"),
                ("a < 0, b > 0, c > 0", "False"),
                ("a > 0, b < 0, c < 0", "False"),
                ("a > 0, b > 0, c > 0", "False"),
                ("a < 0, b < 0, c < 0", "False")
            ]

            true_case = all_cases[0][0]
            false_cases = [c[0] for c in all_cases if c[1] == "False"]
            random.shuffle(false_cases)

            # Chọn 3 đáp án sai
            das1, das2, das3 = false_cases[:3]

            # Câu hỏi
            noidungcauhoi = r"""Cho hàm số $y = ax^2 + bx + c, (a \neq 0)$ có bảng biến thiên trên nửa khoảng $[0; +\infty)$ như hình vẽ dưới đây:
            \begin{center}
            \begin{tikzpicture}[>=stealth,scale=1]
                \def\xc{0} \def\xd{2} \def\xe{4}
                \def\yc{-2} \def\yd{0} \def\ye{-2}
                \draw (0,0) rectangle (6,2.5);
                \draw (0,1.5) -- (6,1.5);
                \draw (1.5,0) -- (1.5,2.5);
                \node at (0.75,2) {$x$}; \node at (1.8,2) {$0$}; \node at (3.75,2) {$-\frac{b}{2a}$}; \node at (5.5,2) {$+\infty$};
                \node at (0.75,0.75) {$y$};
                \node (A) at (1.8,0.3) {$%s$}; \node (B) at (3.75,1.2) {$-\frac{\Delta}{4a}$}; \node (C) at (5.5,0.3) {$-\infty$};
                \draw[->] (A) -- (B); \draw[->] (B) -- (C);
            \end{tikzpicture}
            \end{center}
            Dấu của $a, b, c$ là:""" % (val_c)

            # Các đáp án
            da_d = r'\True $' + true_case + '$'
            da_s1 = '$' + das1 + '$'
            da_s2 = '$' + das2 + '$'
            da_s3 = '$' + das3 + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải
            loigiai = r"""Dựa vào bảng biến thiên ta có: 
            \begin{itemize}
                \item Nhánh cuối cùng của bảng biến thiên đi xuống (hoặc đồ thị có điểm cực đại) nên parabol có bề lõm quay xuống dưới $\Rightarrow a < 0$.
                \item Hoành độ đỉnh $x_I = -\frac{b}{2a} > 0$. Vì $a < 0$ nên $-b < 0 \Rightarrow b > 0$.
                \item Tại $x=0$, ta thấy $y=%s$. Mà $y(0)=c$, do đó $c = %s < 0$.
            \end{itemize}
            Vậy $a < 0, b > 0, c < 0$.""" % (val_c, val_c)

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

