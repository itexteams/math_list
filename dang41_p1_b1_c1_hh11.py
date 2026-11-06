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


def bt_dang41_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Lấy ngẫu nhiên 9 điểm phân biệt cho các vị trí
        pool_points = ['A', 'B', 'C', 'D', 'S', 'M', 'N', 'P', 'Q', 'E', 'F', 'I', 'J', 'K', 'H']
        selected_points = random.sample(pool_points, 9)
        P1, P2, P3, P4, P0, M1, M2, I, K = selected_points

        # Mã TikZ vẽ hình theo phong cách mẫu
        tikz_code = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (P1) at (1.5,1.5);
    \\coordinate (P2) at (0,0);
    \\coordinate (P3) at (4,0);
    \\coordinate (P4) at (5.5,1.5);
    \\coordinate (P0) at (2,4);
    \\coordinate (M1) at ($(P1)!0.6!(P2)$);
    \\coordinate (M2) at ($(P0)!0.6!(P3)$);
    \\coordinate (I) at (intersection of P3--M1 and P2--P4);
    \\coordinate (K) at (intersection of M1--M2 and P0--I);
    \\draw[line width=1pt] (P0)--(P2) (P0)--(P3) (P0)--(P4) (P2)--(P3)--(P4);
    \\draw[line width=1pt, dashed] (P0)--(P1) (P1)--(P2) (P1)--(P4) (P2)--(P4) (P3)--(M1) (M1)--(M2) (P0)--(I);
    \\fill (P1) circle (1pt) node[above right] {$%s$};
    \\fill (P2) circle (1pt) node[left] {$%s$};
    \\fill (P3) circle (1pt) node[right] {$%s$};
    \\fill (P4) circle (1pt) node[right] {$%s$};
    \\fill (P0) circle (1pt) node[above] {$%s$};
    \\fill (M1) circle (1pt) node[left] {$%s$};
    \\fill (M2) circle (1pt) node[right] {$%s$};
    \\fill (I) circle (1pt) node[below] {$%s$};
    \\fill (K) circle (1pt) node[below right] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (P1, P2, P3, P4, P0, M1, M2, I, K))

        # Câu hỏi
        noidungcauhoi = ('Cho hình chóp $%s.%s%s%s%s$ có đáy là hình bình hành $%s%s%s%s$. Các điểm $%s, %s$ lần lượt thuộc các cạnh $%s%s, %s%s$ (không trùng với các đầu mút của các cạnh). Phát biểu nào sau đây đúng?'
                         % (P0, P1, P2, P3, P4, P1, P2, P3, P4, M1, M2, P1, P2, P0, P3))

        # Các đáp án
        da_d = ('\\True Giao điểm của $%s%s$ với $(%s%s%s)$ là giao điểm của $%s%s$ với $%s%s$, trong đó $%s$ là giao điểm của $%s%s$ với $%s%s$' % (M1, M2, P0, P2, P4, M1, M2, P0, I, I, P3, M1, P2, P4))
        das1 = ('Đường thẳng $%s%s$ không cắt mặt phẳng $(%s%s%s)$' % (M1, M2, P0, P2, P4))
        das2 = ('Giao điểm của $%s%s$ với $(%s%s%s)$ là $%s$' % (M1, M2, P0, P2, P4, M1))
        das3 = ('Giao điểm của $%s%s$ với $(%s%s%s)$ là giao điểm của $%s%s$ với $%s%s$' % (M1, M2, P0, P2, P4, M1, M2, P2, P4))

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, das1, das2, das3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('%s\n'
                   'Gọi $%s$ là giao điểm của $%s%s$ với $%s%s$, khi đó $%s%s$ và $%s%s$ cùng thuộc $(%s%s%s)$ nên cắt nhau tại $%s$.\\\\\n'
                   'Vì $%s \\in %s%s$ nên $%s \\in (%s%s%s)$. Vậy $%s$ là giao điểm của $%s%s$ với $(%s%s%s)$.'
                   % (tikz_code, 
                      I, P3, M1, P2, P4, P0, I, M1, M2, P0, P3, M1, K,
                      K, P0, I, K, P0, P2, P4, K, M1, M2, P0, P2, P4))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

