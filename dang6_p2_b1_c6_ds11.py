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


def bt_dang6_p2_b1_c6_ds11(self):
            # Khai báo biến
            # Không gian mẫu n(Omega) = 36
            n_omega = 36

            # Định nghĩa nội dung bài toán (B1 & B2)
            noidungcauhoi = ("Gieo hai con xúc xắc cân đối và đồng chất. \\\\"
                             "Gọi $A$ là biến cố $\\text{“Tổng số chấm xuất hiện trên hai con xúc xắc bằng 5”}$.\\\\"
                             "$B$ là biến cố $\\text{“Tích số chấm xuất hiện trên hai con xúc xắc bằng 6”}$.\\\\ "
                             "$C$ là biến cố $\\text{“Có ít nhất một con xúc xắc xuất hiện mặt 1 chấm”}$. \\\\"
                             "$D$ là biến cố $\\text{“Số chấm trên hai con xúc xắc bằng nhau”}$.")

            ########################################################################
            # Câu (a): n(A U B)
            # A = {(1,4), (4,1), (2,3), (3,2)} -> n(A) = 4
            # B = {(1,6), (6,1), (2,3), (3,2)} -> n(B) = 4
            # A giao B = {(2,3), (3,2)} -> n(A giao B) = 2
            # n(A U B) = 4 + 4 - 2 = 6
            val_a_true = 6
            val_a_false = 9
            da_a_d = "\\True $n\\left(A \\cup B\\right) = %s$" % (val_a_true)
            da_a_s = "$n\\left(A \\cup B\\right) = %s$" % (val_a_false)
            list_da_a = [da_a_d, da_a_s]

            loigiai_a = ("Ta có $A = \\{(1;4), (4;1), (2;3), (3;2)\\} \\Rightarrow n(A)=4$. \\\\"
                         "$B = \\{(1;6), (6;1), (2;3), (3;2)\\} \\Rightarrow n(B)=4$. \\\\"
                         "$A \\cap B = \\{(2;3), (3;2)\\} \\Rightarrow n(A \\cap B)=2$. \\\\"
                         "Vậy $n(A \\cup B) = n(A) + n(B) - n(A \\cap B) = 4 + 4 - 2 = 6$.")

            ########################################################################
            # Câu (b): n(B U C)
            # C = {(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,1), (3,1), (4,1), (5,1), (6,1)} -> n(C) = 11
            # B giao C = {(1,6), (6,1)} -> n(B giao C) = 2
            # n(B U C) = 4 + 11 - 2 = 13
            val_b_true = 13
            val_b_false = 11
            da_b_d = "\\True $n\\left(B \\cup C\\right) = %s$" % (val_b_true)
            da_b_s = "$n\\left(B \\cup C\\right) = %s$" % (val_b_false)
            list_da_b = [da_b_d, da_b_s]

            loigiai_b = ("Ta có \\\\$C = \\{(1;1), (1;2), (1;3), (1;4), (1;5), (1;6), (2,1), (3,1), (4,1), (5,1), (6,1)\\} \\\\ \\Rightarrow n(C)=11$. \\\\"
                         "$B \\cap C = \\{(1;6), (6;1)\\} \\Rightarrow n(B \\cap C)=2$. \\\\"
                         "Vậy $n(B \\cup C) = n(B) + n(C) - n(B \\cap C) = 4 + 11 - 2 = 13$.")

            ########################################################################
            # Câu (c): n(not A U B)
            # n(not A) = 36 - 4 = 32. 
            # not A U B = n(not A) + n(B \ not A) = 32 + n(B giao A) = 32 + 2 = 34
            val_c_true = 34
            val_c_false = 32
            da_c_d = "\\True $n\\left(\\overline{A} \\cup B\\right) = %s$" % (val_c_true)
            da_c_s = "$n\\left(\\overline{A} \\cup B\\right) = %s$" % (val_c_false)
            list_da_c = [da_c_d, da_c_s]

            loigiai_c = ("Số phần tử của biến cố đối $\\overline{A}$ là $n(\\overline{A}) = 36 - 4 = 32$. \\\\"
                         "Biến cố $\\overline{A} \\cup B$ gồm các phần tử thuộc $\\overline{A}$ hoặc thuộc $B$. \\\\"
                         "Ta có $n(\\overline{A} \\cup B) = n(\\overline{A}) + n(B) - n(\\overline{A} \\cap B)$. \\\\"
                         "Trong đó $B \\cap \\overline{A} = B \\setminus (B \\cap A) = \\{(1;6), (6;1)\\} \\Rightarrow n(\\overline{A} \\cap B) = 2$. \\\\"
                         "Vậy $n(\\overline{A} \\cup B) = 32 + 4 - 2 = 34$.")

            ########################################################################
            # Câu (d): n(A U not D)
            # D = {(1,1), ..., (6,6)} -> n(D) = 6. n(not D) = 30.
            # A giao D = rong -> A con not D -> n(A U not D) = n(not D) = 30
            val_d_true = 30
            val_d_false = 32
            da_d_d = "\\True $n\\left(A \\cup \\overline{D}\\right) = %s$" % (val_d_true)
            da_d_s = "$n\\left(A \\cup \\overline{D}\\right) = %s$" % (val_d_false)
            list_da_d = [da_d_d, da_d_s]

            loigiai_d = ("Ta có $D = \\{(1;1), (2;2), (3;3), (4;4), (5;5), (6;6)\\} \\Rightarrow n(D)=6$. \\\\"
                         "Số phần tử của biến cố đối $\\overline{D}$ là $n(\\overline{D}) = 36 - 6 = 30$. \\\\"
                         "Vì $A \\cap D = \\varnothing$ nên $A \\subset \\overline{D}$, do đó $A \\cup \\overline{D} = \\overline{D}$. \\\\"
                         "Vậy $n(A \\cup \\overline{D}) = 30$.")

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp Random (B3)
            while True:
                da_a = random.choice(list_da_a)
                da_b = random.choice(list_da_b)
                da_c = random.choice(list_da_c)
                da_d = random.choice(list_da_d)

                answers = [da_a, da_b, da_c, da_d]
                true_count = count_true_answers(answers)

                # Đảm bảo có từ 1 đến 3 đáp án đúng
                if 1 <= true_count <= 3:
                    break

            # Xuất nội dung theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + 
                       str(noidungcauhoi) + '\n' +
                       '\\choiceTFn \n'
                       '{' + str(da_a) + '}\n'
                       '{' + str(da_b) + '}\n'
                       '{' + str(da_c) + '}\n'
                       '{' + str(da_d) + '}\n'
                       '\\loigiai{ \n'
                       '\\begin{enumEX}[a)]{1} \n'
                       '\\item ' + str(loigiai_a) + '\n'
                       '\\item ' + str(loigiai_b) + '\n'
                       '\\item ' + str(loigiai_c) + '\n'
                       '\\item ' + str(loigiai_d) + '\n'
                       '\\end{enumEX}} \n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

