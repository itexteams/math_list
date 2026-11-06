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


def bt_dang48_p1_b1_c1_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random các thông số cho điểm cực đại M(x1, y1) và cực tiểu N(x2, y2)
        x1 = random.randint(-4, -1)
        x2 = random.randint(1, 4)
        y1 = random.randint(1, 6)
        y2 = random.randint(-6, -1)

        # Tính giá trị biểu thức T = 2*x1 + x2 - y1*y2
        kq = 2 * x1 + x2 - y1 * y2

        # Đáp án đúng
        da = '$%s$' % (latex(kq))

        # Tạo danh sách các phương án sai (đảm bảo không trùng với đáp án đúng)
        s = set()
        while len(s) < 6:
            delta = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            sai = kq + delta
            if sai != kq:
                s.add('$%s$' % (latex(sai)))

        s_list = list(s)
        das1 = s_list[0]
        das2 = s_list[1]
        das3 = s_list[2]

        # Nội dung câu hỏi (chứa bảng biến thiên vẽ bằng TikZ đóng khung nét 1pt)
        noidungcauhoi = ('''Cho hàm số $y = f(x)$ xác định và liên tục trên $\\mathbb{R}$ có bảng biến thiên như hình bên dưới.
    \\\\
    \\begin{center}
    \\begin{tikzpicture}[xscale=1.2, yscale=0.75, line width=1pt, >=stealth]
      \\draw[black] (0,0) rectangle (7.5,3.6);
      \\draw[black] (0,2.6) -- (7.5,2.6);
      \\draw[black] (0,1.8) -- (7.5,1.8);
      \\draw[black] (1.2,0) -- (1.2,3.6);
      \\node at (0.6, 3.1) {$x$};
      \\node at (1.8, 3.1) {$-\\infty$};
      \\node at (3.5, 3.1) {$%s$};
      \\node at (5.2, 3.1) {$%s$};
      \\node at (6.9, 3.1) {$+\\infty$};
      \\node at (0.6, 2.2) {$f'(x)$};
      \\node at (2.65, 2.2) {$+$};
      \\node at (3.5, 2.2) {$0$};
      \\node at (4.35, 2.2) {$-$};
      \\node at (5.2, 2.2) {$0$};
      \\node at (6.05, 2.2) {$+$};
      \\node at (0.6, 0.9) {$f(x)$};
      \\node at (1.8, 0.2) {$-\\infty$};
      \\node at (3.5, 1.4) {$%s$};
      \\node at (5.2, 0.2) {$%s$};
      \\node at (6.9, 1.4) {$+\\infty$};
      \\draw[->, black] (2.1, 0.3) -- (3.2, 1.2);
      \\draw[->, black] (3.8, 1.2) -- (4.9, 0.3);
      \\draw[->, black] (5.5, 0.3) -- (6.6, 1.2);
    \\end{tikzpicture}
    \\end{center}
    Gọi $M(x_1; y_1)$ và $N(x_2; y_2)$ lần lượt là điểm cực đại và điểm cực tiểu của đồ thị hàm số $y = f(x)$. Giá trị của biểu thức $T = 2x_1 + x_2 - y_1 \\cdot y_2$ bằng'''
                        % (latex(x1), latex(x2), latex(y1), latex(y2))
                        )

        # Các phương án lựa chọn
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải chi tiết
        loigiai = ('''Căn cứ vào bảng biến thiên của hàm số $y = f(x)$:\\\\
    - Điểm cực đại của đồ thị hàm số là $M(x_1; y_1) = (%s; %s)$, do đó $x_1 = %s$ và $y_1 = %s$.\\\\
    - Điểm cực tiểu của đồ thị hàm số là $N(x_2; y_2) = (%s; %s)$, do đó $x_2 = %s$ và $y_2 = %s$.\\\\
    Thay các giá trị vào biểu thức $T = 2x_1 + x_2 - y_1 \\cdot y_2$, ta được:\\\\
    $T = 2 \\cdot (%s) + (%s) - (%s) \\cdot (%s) = %s$.'''
                   % (latex(x1), latex(y1), latex(x1), latex(y1),
                      latex(x2), latex(y2), latex(x2), latex(y2),
                      latex(x1), latex(x2), latex(y1), latex(y2), latex(kq))
                   )

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content 

