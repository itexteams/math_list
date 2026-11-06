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


def bt_dang27_p2_b1_c4_ds10(self):
            # Khai báo biến
            dy = random.randint(-1, 1) # Biến thiên nhẹ về độ cao

            y_min = -2 + dy
            y_max = 5 + dy
            y_cuoi = 3 + dy
            y_tai_2 = 0 + dy

            # Nội dung câu hỏi
            noidungcauhoi = "Cho hàm số $y = f(x)$ có đồ thị như hình vẽ dưới đây."

            # Vẽ lại hình bằng TikZ trong LaTeX
            tikz_graph = r"""\begin{center}
            \begin{tikzpicture}[>=stealth, scale=0.5]
                \draw[->] (-5,0) -- (7.5,0) node[above] {$x$};
                \draw[->] (0,-3) -- (0,6.5) node[right] {$y$};
                \draw[thick] (-4,1) -- (-2,%s) -- (0,%s) -- (2,%s) -- (6,%s);
                \draw[dashed] (-4,0) node[below]{$-4$} -- (-4,1) -- (0,1);
                \draw[dashed] (-2,0) node[above]{$-2$} -- (-2,%s) -- (0,%s) node[right]{$%s$};
                \draw[dashed] (6,0) node[below]{$6$} -- (6,%s) -- (0,%s) node[left]{$%s$};
                \draw (0,0) node[below left]{$O$};
                \fill (2,0) circle (1.5pt) node[below right]{$2$};
            \end{tikzpicture}
            \end{center}""" % (y_min, y_max, y_tai_2, y_cuoi, y_min, y_min, y_min, y_cuoi, y_cuoi, y_cuoi)

            ########################################################################
            # a) Nhận biết: Giá trị tại x = 6
            val_a_d = '\\True Dựa vào đồ thị ta thấy $f(6)=%s$' % y_cuoi
            val_a_s = 'Dựa vào đồ thị ta thấy $f(6)=0$'
            list_nb = [val_a_d, val_a_s]
            nb_da = random.choice(list_nb)
            loigiai_nb = 'Dựa vào đồ thị ta thấy tại điểm có hoành độ $x=6$ thì tung độ tương ứng là $y=%s$. Vậy $f(6)=%s$.' % (y_cuoi, y_cuoi)

            ########################################################################
            # b) Thông hiểu: Tập giá trị
            val_b_d = '\\True Tập giá trị của hàm số trên đoạn $[-4;6]$ là $[%s;%s]$' % (y_min, y_max)
            val_b_s = 'Tập giá trị của hàm số trên đoạn $[-4;6]$ là $[0;%s]$' % y_max
            list_th = [val_b_d, val_b_s]
            th_da = random.choice(list_th)
            loigiai_th = 'Dựa vào đồ thị, giá trị thấp nhất của hàm số là $%s$ và giá trị cao nhất là $%s$. Do đó tập giá trị là $[%s;%s]$.' % (y_min, y_max, y_min, y_max)

            ########################################################################
            # c) Vận dụng: So sánh giá trị và biểu thức
            val_c_d = '\\True Ta có $f(4)-f(5)+2f(2) < %s$' % (2*y_tai_2 + 1)
            val_c_s = 'Ta có $f(4)-f(5)+2f(2) > 10$'
            list_vd = [val_c_d, val_c_s]
            vd_da = random.choice(list_vd)
            loigiai_vd = 'Dựa vào đồ thị, hàm số đồng biến trên khoảng $(2;6)$ nên với $4 < 5$ ta có $f(4) < f(5)$, suy ra $f(4) - f(5) < 0$. Mà $f(2) = %s$. Vậy $f(4) - f(5) + 2f(2) < %s$.' % (y_tai_2, 2*y_tai_2)

            ########################################################################
            # d) Vận dụng cao: Khoảng biến thiên
            val_d_d = '\\True Hàm số đồng biến trên khoảng $(-2;0)$ và nghịch biến trên khoảng $(0;2)$'
            val_d_s = 'Hàm số nghịch biến trên khoảng $(-2;0)$ và đồng biến trên khoảng $(0;2)$'
            list_vdc = [val_d_d, val_d_s]
            vdc_da = random.choice(list_vdc)
            loigiai_vdc = 'Quan sát đồ thị: Trên khoảng $(-2;0)$ đồ thị đi lên từ trái sang phải nên hàm số đồng biến. Trên khoảng $(0;2)$ đồ thị đi xuống nên hàm số nghịch biến.'

            # Xuất nội dung
            content = (
            '\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' +
            str(noidungcauhoi) + '\n' +
            str(tikz_graph) + '\n' +
            '\\choiceTFn \n'
            '{' + str(nb_da) + '}\n'
            '{' + str(th_da) + '}\n'
            '{' + str(vd_da) + '}\n'
            '{' + str(vdc_da) + '}\n'
            '\\loigiai{ \n'
            '\\begin{enumEX}[a)]{1} \n'
            '\\item ' + str(loigiai_nb) + '\n'
            '\\item ' + str(loigiai_th) + '\n'
            '\\item ' + str(loigiai_vd) + '\n'
            '\\item ' + str(loigiai_vdc) + '\n'
            '\\end{enumEX}} \n'
            '\\end{ex}\n \\end{minipage} \n\n')
            return content

