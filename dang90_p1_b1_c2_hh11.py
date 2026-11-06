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


def bt_dang90_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Ta chọn các góc phổ biến trong bài tập hình học
            angles = [30, 45, 60, 90]
            angle = random.choice(angles)
            angle_str = str(angle) + '^\\circ'

            # Tạo đáp án
            da_d = '\\True $' + angle_str + '$'
            distractors = [str(a) + '^\\circ' for a in angles if a != angle]
            da_s1 = '$' + distractors[0] + '$'
            da_s2 = '$' + distractors[1] + '$'
            da_s3 = '$' + distractors[2] + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # TikZ Figure - Vẽ hình minh họa
            tikz_fig = ('\\begin{tikzpicture}[scale=0.8, line width=1pt] \n'
                        '\\coordinate (S) at (1.5,3); \n'
                        '\\coordinate (A) at (0,0); \n'
                        '\\coordinate (B) at (4,0); \n'
                        '\\coordinate (C) at (2,-1); \n'
                        '\\coordinate (M) at ($(S)!0.5!(B)$); \n'
                        '\\coordinate (N) at ($(S)!0.5!(C)$); \n'
                        '\\draw (S) -- (A) -- cycle; \n'
                        '\\draw (S) -- (C) -- (B) -- cycle; \n'
                        '\\draw (A) -- (C); \n'
                        '\\draw (M) -- (N); \n'
                        '\\draw[dashed] (A) -- (B); \n'
                        '\\node[above] at (S) {$S$}; \n'
                        '\\node[left] at (A) {$A$}; \n'
                        '\\node[right] at (B) {$B$}; \n'
                        '\\node[below] at (C) {$C$}; \n'
                        '\\node[right] at (M) {$M$}; \n'
                        '\\node[left] at (N) {$N$}; \n'
                        '\\end{tikzpicture}')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác với $\\widehat{ABC} = %s$. Gọi các điểm $M, N$ lần lượt là trung điểm của $SB$ và $SC$. Khi đó góc giữa hai đường thẳng $MN$ và $AB$ bằng
            \\begin{center}
            %s
            \\end{center}''' % (angle_str, tikz_fig))

            # Nội dung lời giải
            loigiai = ('''Trong tam giác $SBC$, ta có $M$ là trung điểm của $SB$ và $N$ là trung điểm của $SC$. \\\\
            Suy ra $MN$ là đường trung bình của tam giác $SBC$, nên $MN // BC$. \\\\
            Khi đó, góc giữa hai đường thẳng $MN$ và $AB$ chính là góc giữa hai đường thẳng $BC$ và $AB$. \\\\
            Ta có $(MN, AB) = (BC, AB) = \\widehat{ABC} = %s$.''' % (angle_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+list_1[0]+'}\n'
                '{'+list_1[1]+'}\n'
                '{'+list_1[2]+'}\n'
                '{'+list_1[3]+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

