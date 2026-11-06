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


def bt_dang22_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến symbolic
            x = symbols('x')

            # Bước 1: Nội dung câu hỏi (sử dụng TikZ để vẽ hình)
            tikz_graph = r"""\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, >=stealth]
                \draw[fill=yellow!30, samples=100, domain=-1:1] plot (\x, {0.2*(\x+1)*(\x-1)*(4-\x)}) -- (1,0) -- (-1,0) -- cycle;
                \draw[fill=yellow!30, samples=100, domain=1:4] plot (\x, {0.2*(\x+1)*(\x-1)*(4-\x)}) -- (4,0) -- (1,0) -- cycle;
                \draw[thick, samples=100, domain=-1.5:4.5] plot (\x, {0.2*(\x+1)*(\x-1)*(4-\x)});
                \draw[->] (-2,0) -- (5,0) node[below] {$x$};
                \draw[->] (0,-2) -- (0,2) node[left] {$y$};
                \node at (-1.2,-0.2) {$-1$};
                \node at (0.2,-0.2) {$O$};
                \node at (1.2,0.2) {$1$};
                \node at (4.2,0.2) {$4$};
                \node at (3.5,1.5) {$y=f(x)$};
            \end{tikzpicture}
            \end{center}"""

            noidungcauhoi = r"Cho hàm số $y = f(x)$ liên tục trên $\mathbb{R}$ và có đồ thị là đường cong như hình vẽ bên dưới. Gọi $(H)$ là hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành và các đường thẳng $x = -1, x = 4$." + tikz_graph

            ########################################################################
            # Nhận biết: Công thức diện tích tổng quát
            ########################################################################
            nb_da_1_d = r'\True Diện tích $S$ của hình phẳng $(H)$ là $S = \int_{-1}^{4} |f(x)| \text{d}x$.'
            nb_da_1_s = r'Diện tích $S$ của hình phẳng $(H)$ là $S = \int_{-1}^{4} f(x) \text{d}x$.'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r"Theo công thức tính diện tích hình phẳng giới hạn bởi đồ thị $y=f(x)$, trục hoành và hai đường thẳng $x=a, x=b$, ta có $S = \int_{a}^{b} |f(x)| \text{d}x$."

            ########################################################################
            # Thông hiểu: Phá dấu trị tuyệt đối dựa vào hình vẽ
            ########################################################################
            th_da_1_d = r'\True Diện tích $S$ của hình phẳng $(H)$ là $S = \int_{-1}^{1} f(x) \text{d}x - \int_{1}^{4} f(x) \text{d}x$.'
            th_da_1_s = r'Diện tích $S$ của hình phẳng $(H)$ là $S = \int_{-1}^{1} f(x) \text{d}x + \int_{1}^{4} f(x) \text{d}x$.'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r"Dựa vào đồ thị, trên đoạn $[-1; 1]$ đồ thị nằm phía trên trục hoành ($f(x) \ge 0$), trên đoạn $[1; 4]$ đồ thị nằm phía dưới trục hoành ($f(x) \le 0$). Do đó: $S = \int_{-1}^{1} |f(x)| \text{d}x + \int_{1}^{4} |f(x)| \text{d}x = \int_{-1}^{1} f(x) \text{d}x - \int_{1}^{4} f(x) \text{d}x$."

            ########################################################################
            # Vận dụng: So sánh giá trị F(x)
            ########################################################################
            vd_da_1_d = r'\True Khẳng định đúng là $F(1) > F(-1) > F(4)$.'
            vd_da_1_s = r'Khẳng định đúng là $F(4) > F(1) > F(-1)$.'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r"""Gọi $S_1$ là diện tích phần phía trên trục hoành, $S_2$ là diện tích phần phía dưới trục hoành.\\
            Dựa vào hình vẽ ta thấy $S_2 > S_1$.\\
            Ta có: $S_1 = F(1) - F(-1) > 0 \Rightarrow F(1) > F(-1)$.\\
            $S_2 = -\int_{1}^{4} f(x) \text{d}x = F(1) - F(4)$.\\
            Vì $S_2 > S_1 \Rightarrow F(1) - F(4) > F(1) - F(-1) \Rightarrow -F(4) > -F(-1) \Rightarrow F(-1) > F(4)$.\\
            Vậy $F(1) > F(-1) > F(4)$."""

            ########################################################################
            # Vận dụng cao: Thể tích khối tròn xoay
            ########################################################################
            vdc_da_1_d = r'\True Thể tích vật thể tròn xoay khi quay $(H)$ quanh trục hoành là $V = \pi \int_{-1}^{4} [f(x)]^2 \text{d}x$.'
            vdc_da_1_s = r'Thể tích vật thể tròn xoay khi quay $(H)$ quanh trục hoành là $V = \int_{-1}^{4} [f(x)]^2 \text{d}x$.'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r"Công thức tính thể tích vật thể tròn xoay tạo thành khi quay hình phẳng giới hạn bởi đồ thị $y=f(x)$, trục hoành và hai đường thẳng $x=a, x=b$ quanh trục $Ox$ là $V = \pi \int_{a}^{b} [f(x)]^2 \text{d}x$."

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp để chọn bộ đáp án ngẫu nhiên thỏa mãn điều kiện 1-3 câu đúng
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo mẫu LaTeX
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + nb_da + '}\n'
                '{' + th_da + '}\n'
                '{' + vd_da + '}\n'
                '{' + vdc_da + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

