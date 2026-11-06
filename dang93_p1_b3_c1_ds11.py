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


def bt_dang93_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo tính ngẫu nhiên cho bài toán
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Hàm gốc của đề bài: y = \sqrt{2} cos(x + \pi/4)
                da_text = 'y = \\sqrt{2}\\cos \\left( x + \\frac{\\pi}{4} \\right)'
                das1 = 'y = \\sin \\left( x - \\frac{\\pi}{4} \\right)'
                das2 = 'y = \\cos \\left( x - \\frac{\\pi}{4} \\right)'
                das3 = 'y = \\sqrt{2}\\sin \\left( x + \\frac{\\pi}{4} \\right)'

                # Vẽ đồ thị bằng TikZ độ dày 1pt
                tikz_graph = '\\draw[line width=1pt,color=brown,smooth,samples=100,domain=-4.2:7.2] plot(\\x,{sqrt(2)*cos((\\x + 0.785398)*180/3.14159)});'

                noidungcauhoi = ('''Đường cong trong hình dưới đây là đồ thị của hàm số nào trong các hàm số sau đây?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.7, >=stealth]
                \\draw[->,line width=1pt,color=blue] (-4.5,0) -- (7.5,0) node[below] {$x$};
                \\draw[->,line width=1pt,color=blue] (0,-2.2) -- (0,2.5) node[right] {$y$};
                \\node[below left] at (0,0) {$O$};
                %s
                \\draw[dashed,line width=0.5pt,color=blue] (0,1.414) -- (2.356,1.414) -- (2.356,0);
                \\draw[dashed,line width=0.5pt,color=blue] (0,-1.414) -- (2.356,-1.414) -- (2.356,0);
                \\draw[dashed,line width=0.5pt,color=blue] (0,1) -- (6.283,1);
                \\draw[dashed,line width=0.5pt,color=blue] (5.497,0) -- (5.497,1.414) -- (0,1.414);
                \\node[left] at (0,1.414) {$\\sqrt{2}$};
                \\node[left] at (0,1) {$1$};
                \\node[left] at (0,-1.414) {$-\\sqrt{2}$};
                \\node[above] at (2.356,0) {$\\frac{3\\pi}{4}$};
                \\node[below] at (5.497,0) {$\\frac{7\\pi}{4}$};
                \\node[below] at (6.283,0) {$2\\pi$};
            \\end{tikzpicture}
            \\end{center}''' % (tikz_graph))

                loigiai = ('''Ta thấy hàm số có giá trị lớn nhất bằng $\\sqrt{2}$, giá trị nhỏ nhất bằng $-\\sqrt{2}$ nên loại các phương án không có hệ số $\\sqrt{2}$.\\\\
            Tại $x = \\frac{3\\pi}{4}$ thì $y = -\\sqrt{2}$. Thay $x = \\frac{3\\pi}{4}$ vào hai đáp án còn lại chỉ có $%s$ thỏa mãn.''' % (da_text))

            else:
                # Hàm số biến đổi ngẫu nhiên: y = \sqrt{2} sin(x + \pi/4)
                da_text = 'y = \\sqrt{2}\\sin \\left( x + \\frac{\\pi}{4} \\right)'
                das1 = 'y = \\sin \\left( x - \\frac{\\pi}{4} \\right)'
                das2 = 'y = \\cos \\left( x - \\frac{\\pi}{4} \\right)'
                das3 = 'y = \\sqrt{2}\\cos \\left( x + \\frac{\\pi}{4} \\right)'

                # Vẽ đồ thị bằng TikZ độ dày 1pt
                tikz_graph = '\\draw[line width=1pt,color=brown,smooth,samples=100,domain=-4.2:7.2] plot(\\x,{sqrt(2)*sin((\\x + 0.785398)*180/3.14159)});'

                noidungcauhoi = ('''Đường cong trong hình dưới đây là đồ thị của hàm số nào trong các hàm số sau đây?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.7, >=stealth]
                \\draw[->,line width=1pt,color=blue] (-4.5,0) -- (7.5,0) node[below] {$x$};
                \\draw[->,line width=1pt,color=blue] (0,-2.2) -- (0,2.5) node[right] {$y$};
                \\node[below left] at (0,0) {$O$};
                %s
                \\draw[dashed,line width=0.5pt,color=blue] (0,1.414) -- (0.785,1.414) -- (0.785,0);
                \\draw[dashed,line width=0.5pt,color=blue] (0,-1.414) -- (3.927,-1.414) -- (3.927,0);
                \\draw[dashed,line width=0.5pt,color=blue] (0,1) -- (2.356,1) -- (2.356,0);
                \\node[left] at (0,1.414) {$\\sqrt{2}$};
                \\node[left] at (0,1) {$1$};
                \\node[left] at (0,-1.414) {$-\\sqrt{2}$};
                \\node[below] at (0.785,0) {$\\frac{\\pi}{4}$};
                \\node[below] at (2.356,0) {$\\frac{3\\pi}{4}$};
                \\node[above] at (3.927,0) {$\\frac{5\\pi}{4}$};
            \\end{tikzpicture}
            \\end{center}''' % (tikz_graph))

                loigiai = ('''Ta thấy hàm số có giá trị lớn nhất bằng $\\sqrt{2}$, giá trị nhỏ nhất bằng $-\\sqrt{2}$ nên loại các phương án không có hệ số $\\sqrt{2}$.\\\\
            Tại $x = \\frac{\\pi}{4}$ thì $y = \\sqrt{2}$. Thay $x = \\frac{\\pi}{4}$ vào hai đáp án còn lại chỉ có $%s$ thỏa mãn.''' % (da_text))

            # Thiết lập đáp án đúng và đáp án sai (không chứa dấu chấm ở cuối phương án)
            da_d = ('\\True $' + str(da_text) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            # Trộn thứ tự ngẫu nhiên của các đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Định dạng xuất mã câu hỏi trắc nghiệm theo minipage mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

