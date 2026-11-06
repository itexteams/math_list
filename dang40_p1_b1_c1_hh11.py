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


def bt_dang40_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random tên các điểm để tạo ra nhiều bài toán khác nhau
        pool = ['A', 'B', 'C', 'D', 'E', 'F', 'S', 'P', 'Q', 'R', 'K', 'H', 'M', 'N', 'I', 'J', 'G']
        selected_points = random.sample(pool, 8)
        v1, v2, v3, v4, m, n, g, h = selected_points

        # Mã TikZ vẽ hình theo phong cách yêu cầu
        tikz_code = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (V2) at (0,1);
    \\coordinate (V4) at (6,1);
    \\coordinate (V3) at (2,-1);
    \\coordinate (V1) at (3,4);
    \\coordinate (M) at ($(V1)!0.5!(V3)$);
    \\coordinate (N) at ($(V3)!0.5!(V4)$);
    \\coordinate (G) at (intersection of V1--N and V4--M);
    \\draw[line width=1pt] (V1)--(V2) (V1)--(V4) (V1)--(V3) (V2)--(V3)--(V4);
    \\draw[line width=1pt, dashed] (V2)--(V4);
    \\draw[line width=1pt] (V1)--(N) (V4)--(M) (V2)--(M);
    \\draw[line width=1pt, dashed] (V2)--(G) (V2)--(N);
    \\fill (V1) circle (1pt) node[above] {$%s$};
    \\fill (V2) circle (1pt) node[left] {$%s$};
    \\fill (V3) circle (1pt) node[below] {$%s$};
    \\fill (V4) circle (1pt) node[right] {$%s$};
    \\fill (M) circle (1pt) node[above left] {$%s$};
    \\fill (N) circle (1pt) node[below right] {$%s$};
    \\fill (G) circle (1pt) node[above right] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (v1, v2, v3, v4, m, n, g))

        # Câu hỏi
        noidungcauhoi = ('Cho tứ diện $%s%s%s%s$. Gọi $%s, %s$ lần lượt là trung điểm của $%s%s, %s%s$. Giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ là' 
                         % (v1, v2, v3, v4, m, n, v1, v3, v3, v4, m, v2, v4, v1, v2, n))

        # Các đáp án
        da_d = ('\\True đường thẳng $%s%s$ ($%s$ là trọng tâm tam giác $%s%s%s$)' % (v2, g, g, v1, v3, v4))
        das1 = ('đường thẳng $%s%s$' % (m, n))
        das2 = ('đường thẳng $%s%s$' % (v1, m))
        das3 = ('đường thẳng $%s%s$ ($%s$ là trực tâm tam giác $%s%s%s$)' % (v1, h, h, v1, v3, v4))

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, das1, das2, das3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''%s
        - $%s$ là điểm chung thứ nhất giữa hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$.
        - Vì $%s, %s$ lần lượt là trung điểm của $%s%s, %s%s$ nên suy ra $%s%s, %s%s$ là hai trung tuyến của tam giác $%s%s%s$. Gọi $%s = %s%s \\cap %s%s$
    $\\Rightarrow \\begin{cases} %s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\\\ %s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\end{cases} \\Rightarrow %s$ là điểm chung thứ hai giữa hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$.\\\\
    Vậy $(%s%s%s) \\cap (%s%s%s) = %s%s$.''' % 
    (tikz_code, 
    v2, m, v2, v4, v1, v2, n, 
    m, n, v1, v3, v3, v4, v1, n, v4, m, v1, v3, v4, g, v1, n, v4, m,
    g, v1, n, v1, v2, n, g, v1, v2, n, 
    g, v4, m, m, v2, v4, g, m, v2, v4, 
    g, m, v2, v4, v1, v2, n,
    v1, v2, n, m, v2, v4, v2, g))

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

